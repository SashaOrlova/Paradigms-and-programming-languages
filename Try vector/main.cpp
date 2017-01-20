#include "MyVector.h"
#include <cstdlib>
#include <iostream>

using namespace std;

int main(){
	MyVector vec;
	MyVector vec1(3);
	vec.pushBack(1);
	cout << vec.getValue(0) << '\n';
	vec.setValue(0, 3); 
	vec1.pushBack(2);
	cout << vec.getName()<< ' ' << vec1.getSize()<< '\n';
	cout << vec.popBack()<< ' ' << vec1.popBack() << '\n';
	cout << vec.getCounter();
	return 0;
}
