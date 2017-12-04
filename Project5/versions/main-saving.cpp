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


void Assignment_A(int N, int MCcycles, double saving, vec& agents);

int main(int argc, char* argv[])
{
  string filename;
  int Nagents = 500;
  int MCcycles = int(pow(10,7));
  int simulations = 96;
  double mu,intial_money;

  if (argc <= 3) {
    cout << "Bad Usage: " << argv[0] << 
      " read mu, intial_money and output file" << endl;
    exit(1);
  }

  if (argc > 1) {
    filename=argv[3]; 
    mu = atof(argv[1]);
    intial_money = atof(argv[2]);
  }

  int my_rank, numprocs;
  MPI_Init (&argc, &argv);
  MPI_Comm_size (MPI_COMM_WORLD, &numprocs);
  MPI_Comm_rank (MPI_COMM_WORLD, &my_rank);
  

  mat Agents = ones<mat>(Nagents,simulations/numprocs)*intial_money;
  for(int i = 0; i < simulations/numprocs; i++){

    vec Simualation_Agents = ones<vec>(Nagents)*intial_money;
    Assignment_A(Nagents, MCcycles, mu, Simualation_Agents);

    for(int nr = 0; nr < Nagents; nr++){
      Agents(nr,i) = Simualation_Agents(nr);
    }


  }
  cout << accu(Agents)/((simulations/numprocs)*500.) << endl;
  Agents.save(filename+"_"+to_string(my_rank)+".txt",csv_ascii);
  MPI_Finalize();
  
  return 0;
}



// The Monte Carlo part with the Metropolis algo with sweeps over the lattice
void Assignment_A(int N, int MCcycles, double saving, vec& agents)
{
  std::random_device rd;
  std::mt19937_64 gen(rd());
  std::uniform_real_distribution<double> rand(0.0,1.0);

  int j = 0;
  while(j < MCcycles){
    int k = (int)(N*rand(gen));
    int l = (int)(N*rand(gen));
    if(k == l){continue;}
    double eps = rand(gen);
    double dm = (1-saving)*(eps*agents(l)-(1-eps)*agents(k));
    agents(k) += dm;
    agents(l) -= dm;
    j++;
  }
}
