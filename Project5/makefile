#c++ mpicxx
compile= mpicxx
LIB=  -L/usr/local/lib -larmadillo
FLAGS= -O3
INCLUDEPATH= -I/usr/local/include


main.exe	:	main.cpp
	${compile} -o main.exe main.cpp ${INCLUDEPATH} ${LIB} ${FLAGS}


#solsys.exe	:	planet.o  main.o solarsystem.o
#	${compile} -o solsys.exe planet.o main.o solarsystem.o 


#planet.o	:	planet.cpp
#	${compile} -c  planet.cpp


#main.o	:	main.cpp
#	${compile} ${LIB} -c  main.cpp


#solarsystem.o	:	solarsystem.cpp
#	${compile} ${LIB} -c  solarsystem.cpp


