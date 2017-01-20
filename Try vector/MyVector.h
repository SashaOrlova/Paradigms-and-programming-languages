#pragma once
#include <string>
//using namespace std;
class MyVector {
    protected:
		int* _data;
		size_t size;
		size_t cp;
		static int counter;
	public:
		MyVector();
		MyVector(size_t sz);
		~MyVector();
		void pushBack(int val);
		bool isEmpty();
		int popBack();
		virtual std::string getName();
		void setValue(size_t i, int val);
		int getValue(size_t i);
		size_t getSize();
		int getCounter();
	};
		
