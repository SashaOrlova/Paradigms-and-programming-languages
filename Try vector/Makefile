all: vector 

vector: main.o MyVector.o 
	g++ main.o MyVector.o -o vector

main.o: main.cpp MyVector.h
	g++ -c main.cpp

MyVector.o: MyVector.cpp MyVector.h
	g++ -c MyVector.cpp

clean:
	rm -rf *.o vector
