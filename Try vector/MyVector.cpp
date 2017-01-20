#include "MyVector.h"
#include <cstdlib>

using namespace std;

int MyVector::counter = 0;

MyVector::MyVector():size(0), cp(0), _data(NULL){ counter++; }

MyVector::MyVector(size_t sz):size(0), cp(sz) {
	_data = new int [sz];
	counter++;
}

MyVector::~MyVector(){
	if (_data) delete [] _data;
}

void MyVector::pushBack(int v){
	if (cp > size) {
		_data[size++] = v;
	}
	else {
		int *tmp = new int [cp*2];
		for (int i = 0; i < size; i++)
			tmp[i] = _data[i];
		cp *= 2;
		swap(tmp,_data);
		delete [] tmp;
		_data[size++] = v;
	}
}
bool MyVector::isEmpty(){
	return size;
}

int MyVector::popBack(){
	if (size){
		return _data[--size];
	}
	return 0;
}
string MyVector::getName(){
	return "vector";
} 
// ->     *(fdf). 
void MyVector::setValue(size_t i, int val){
	if (i < size)
		_data[i] = val;
}
int MyVector::getValue(size_t i){
	if (i < size)
		return _data[i];
	else return 0;
}
size_t MyVector::getSize(){
	return size;
}

int MyVector::getCounter(){
		return counter;
	}
