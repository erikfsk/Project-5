#include <cmath>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include <random>
#include <armadillo>
#include <string>
#include <mpi.h>
#include <boost/timer.hpp>
using namespace  std;
using namespace arma;
// output file
ofstream ofile;


void Assignment_A(int N, int MCcycles, double saving, vec& agents);
void Assignment_D(int N, int MCcycles, double saving, vec& agents, double alpha);
void Assignment_E(int N, int MCcycles, double saving, vec& agents, double alpha, double gamma);
void WriteResultstoFile(vec intervales, int length);
void Progress_bar(int my_rank,int simulations,int i, int& progress);
void Progress_bar_done(int my_rank);



int main(int argc, char* argv[])
{
  string filename;
  int Nagents = 1000;
  int MCcycles = int(pow(10,7));
  int simulations = 1000;
  double mu,intial_money;



  // Check if enough arguments are provided 
  if (argc <= 2) {
    cout << "Bad Usage: " << argv[0] << 
      " read mu and output file" << endl;
    exit(1);
  }

  if (argc > 1) {
    filename=argv[2]; 
    mu = atof(argv[1]);
  }
  intial_money = 1;


  // parallelization - START
  int my_rank, numprocs;
  MPI_Init (&argc, &argv);
  MPI_Comm_size (MPI_COMM_WORLD, &numprocs);
  MPI_Comm_rank (MPI_COMM_WORLD, &my_rank);
  

  int progress = 1;
  mat Agents = ones<mat>(Nagents,simulations)*intial_money;
  
  for(int i = 0; i < simulations; i++){

    
    // Progress bar
    Progress_bar(my_rank,simulations,i,progress);
    
    // 
    // pick assignment
    // 

    vec Simualation_Agents = ones<vec>(Nagents)*intial_money;
    
    // Assignment_A(Nagents, MCcycles, mu + 0.30*my_rank, Simualation_Agents);
    // Assignment_D(Nagents, MCcycles, mu, Simualation_Agents, 0.5 + my_rank*0.5);
    Assignment_E(Nagents, MCcycles, mu, Simualation_Agents, 1,1 + 1*my_rank);

    // Fill matrix with data for a simulation
    for(int nr = 0; nr < Nagents; nr++){
      Agents(nr,i) = Simualation_Agents(nr);
    }

  }


  // Make a histogram data to write to file 
  int length = 1000;
  vec intervales = zeros(length);
  for(int i = 0; i < Nagents; i++){
    for(int j = 0; j < simulations; j++){
      int index = (int)(Agents(i,j)*100)%length;
      intervales(index) += 1;
    }
  }
  
  // write to file
  string fileout = filename+"_"+to_string(1 + my_rank)+".txt";
  ofile.open(fileout);
  ofile << "X" << setw(15) << "Y" << endl;
  WriteResultstoFile(intervales,length);
  

  Progress_bar_done(my_rank);
  MPI_Finalize();
  // parallelization - END
  
  return 0;
}



void Assignment_A(int Nagents, int MCcycles, double saving, vec& agents)
{
  // initializing random generator
  std::random_device rd;
  std::mt19937_64 gen(rd());
  std::uniform_real_distribution<double> rand(0.0,1.0);

  int j = 0;
  while(j < MCcycles){

    //  Pick two random agents
    int k = (int)(Nagents*rand(gen));
    int l = (int)(Nagents*rand(gen));
    if(k == l){continue;}

    // Transaction
    double eps = rand(gen);
    double dm = (1-saving)*(eps*agents(l)-(1-eps)*agents(k));
    agents(k) += dm;
    agents(l) -= dm;
    j++;
  }
}

void Assignment_D(int Nagents, int MCcycles, double saving, vec& agents, double alpha)
{
  // initializing random generator
  std::random_device rd;
  std::mt19937_64 gen(rd());
  std::uniform_real_distribution<double> rand(0.0,1.0);

  int j = 0;
  while(j < MCcycles){

    // Pick two random agents
    int k = (int)(Nagents*rand(gen));
    int l = (int)(Nagents*rand(gen));
    if(k == l){continue;}
    if(rand(gen) < pow(fabs(agents(k)-agents(l)),-alpha)){

      // Transaction
      double eps = rand(gen);
      double dm = (1-saving)*(eps*agents(l)-(1-eps)*agents(k));
      agents(k) += dm;
      agents(l) -= dm;
    }
    j++;
  }
}

void Assignment_E(int Nagents, int MCcycles, double saving, vec& agents, double alpha, double gamma)
{
  // initializing random generator
  std::random_device rd;
  std::mt19937_64 gen(rd());
  std::uniform_real_distribution<double> rand(0.0,1.0);


  mat interactions = ones<mat>(Nagents,Nagents);
  vec max_interactions = ones<vec>(Nagents);
  
  int j = 0;
  while(j < MCcycles){

    // Pick two random agents
    int k = (int)(Nagents*rand(gen));
    int l = (int)(Nagents*rand(gen));
    if(k == l){continue;}
    if (fabs(agents(k)-agents(l)) < 1){
      if (rand(gen) < pow((interactions(k,l))/((max_interactions(k)+max_interactions(l))/2.),gamma)){

        // Transaction
        interactions(k,l) += 1;
        interactions(l,k) += 1;
        if (interactions(k,l) > max_interactions(k)){
          max_interactions(k) += 1;
        } 
        if (interactions(k,l) > max_interactions(l)){
          max_interactions(l) += 1;
        } 

        double eps = rand(gen);
        double dm = (1-saving)*(eps*agents(l)-(1-eps)*agents(k));
        agents(k) += dm;
        agents(l) -= dm;
      }
    }
    else if (rand(gen) < pow(fabs(agents(k)-agents(l)),-alpha)*pow((interactions(k,l))/((max_interactions(k)+max_interactions(l))/2.),gamma)){
      
      // Transaction
      interactions(k,l) += 1;
      interactions(l,k) += 1;
      if (interactions(k,l) > max_interactions(k)){
        max_interactions(k) += 1;
      } 
      if (interactions(k,l) > max_interactions(l)){
        max_interactions(l) += 1;
      } 
      double eps = rand(gen);
      double dm = (1-saving)*(eps*agents(l)-(1-eps)*agents(k));
      agents(k) += dm;
      agents(l) -= dm;
    }
    j++;
  }
}

void WriteResultstoFile(vec intervales, int length)
{
  double normed = accu(intervales);
  ofile << setiosflags(ios::showpoint | ios::uppercase);
  for(int i = 0; i < length; i++){
    ofile << setprecision(8) << i/100.;
    ofile << setw(15) << setprecision(8) << intervales(i)/normed << endl;
  }
} // end output function



void Progress_bar(int my_rank,int simulations,int i, int& progress)
{
  // PROGRESSBAR
  int length = 10;
  if(my_rank >= 0){
    if ((i) % (simulations/length) == 0){
      string output = "";
      for(int line = 0; line < my_rank+1; line++){
        output += "\n";
      }
      if(progress > 1){
        output += "Thread: "+to_string(my_rank+1)+"   0%";
        for(int nr = 0; nr < progress; nr++){
          output += "#";
        }
        for(int nr = 0; nr < length-progress; nr++){
          output += "-";
        }
        output += "100%";
      }
      
      for(int line = 0; line < my_rank +1; line++){
        output += "\n\x1b[A\x1b[A";
      }
      if(progress == 1){
        if(my_rank != 0){
          cout << "\x1b[A\x1b[A";
        } else {
          cout << "\x1b[A";
        }        
      }
      cout << output;
      progress++;
    }
  }
}

void Progress_bar_done(int my_rank)
{
  // PROGRESSBAR - DONE
  string output = "";
  for(int line = 0; line < my_rank+1; line++){
    output += "\n";
  }
  output += "Thread: "+to_string(my_rank+1)+"   ------DONE------";
  for(int line = 0; line < my_rank +1; line++){
    output += "\n\x1b[A\x1b[A";
  }
  cout << output;
}


