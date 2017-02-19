#include "employees.h"
#include <cstring>
#include <stdint.h>
#include <iostream>
#include <string>
#include <fstream>

Employee::~Employee(){
	delete [] _name;
}
Employee::Employee(){
	_name = NULL;
	_base_salary = 0;
	}


std::ostream& operator<<(std::ostream& os, Employee& o){
	o.write(os);
	return os;
}

std::istream& operator>>(std::istream& os, Employee& o){
	o.read(os);
	return os;
}

std::ofstream& operator<<(std::ofstream& os, Employee& o){
	o.fwrite(os);
	return os;
}

std::ifstream& operator>>(std::ifstream& os, Employee& o){
	o.fread(os);
	return os;
}

//Developer

Developer::Developer():Employee(){
	_has_bonus = false;
}
Developer::~Developer(){
}

void Developer::write(std::ostream& os){
	std::string s;
	s = _name;
	os << "Developer\n" << "Name: " << s << "\n" << "Base Salary: " << _base_salary<< "\n" << "Has bonus: ";
	if (_has_bonus)
		os << '+';
	else 
		os << '-';
}

std::ostream& operator<<(std::ostream& os, Developer& o){
	o.write(os);
	return os;
}

void Developer::fwrite(std::ofstream& os){
	int32_t type = 1;
	std::string s = _name; 
	os.write((char*)&type, sizeof(type));
	os.write(s.c_str(), s.size()+1);
	os.write((char*)&_base_salary, sizeof(_base_salary));
	os.write((char*)&_has_bonus, sizeof(_has_bonus));
}

std::ofstream& operator<<(std::ofstream& os, Developer& o){
	o.fwrite(os);
	return os;
}

void Developer::read(std::istream& os){
	std::string s;
	os >> s >> _base_salary >> _has_bonus;
	_name = new char [s.size()+1];
	strcpy(_name, s.c_str());
}

std::istream& operator>>(std::istream& os, Developer& o){
	o.read(os);
	return os;
}

void Developer::fread(std::ifstream& os){
	std::string s;
	char c;
	os.read(&c, sizeof(char));
	while(c != '\0'){
	s.push_back(c);
	os.read(&c, sizeof(char));
	}
	_name = new char [s.size()+1];
	strcpy(_name, s.c_str());
	os.read((char*)&_base_salary, sizeof(_base_salary));
	os.read((char*)&_has_bonus, sizeof(_has_bonus));
}

std::ifstream& operator>>(std::ifstream& os, Developer& o){
	o.fread(os);
	return os;
}

// SalesManager



SalesManager::SalesManager():Employee(){
	_sold_nm = 0;
	_price = 0;
}

SalesManager::~SalesManager(){
}

void SalesManager::write(std::ostream& os){
	os << "Sales Manager\n" << "Name: " << _name << "\n" << "Base Salary: " << _base_salary<< "\n" << "Sold items: " << _sold_nm << '\n' << "Item price: " << _price;
}

std::ostream& operator<<(std::ostream& os, SalesManager& o){
	o.write(os);
	return os;
}

void SalesManager::fwrite(std::ofstream& os){
	int32_t type = 2;
	std::string s = _name;
	os.write((char*)&type, sizeof(type));
	os.write(s.c_str(), s.size()+1);
	os.write((char*)&_base_salary, sizeof(_base_salary));
	os.write((char*)&_sold_nm, sizeof(_sold_nm));
	os.write((char*)&_price, sizeof(_price));
}

std::ofstream& operator<<(std::ofstream& os, SalesManager& o){
	o.fwrite(os);
	return os;
}
void SalesManager::read(std::istream& os){
	std::string s;
	os >> s >> _base_salary >> _sold_nm >> _price;
	_name = new char [s.size()+1];
	strcpy(_name, s.c_str());
}

std::istream& operator>>(std::istream& os, SalesManager& o){
	o.read(os);
	return os;
}
void SalesManager::fread(std::ifstream& os){
	std::string s;
	char c;
	os.read(&c, sizeof(char));
	while(c != '\0'){
	s.push_back(c);
	os.read(&c, sizeof(char));
	}
	_name = new char [s.size()+1];
	strcpy(_name, s.c_str());
	os.read((char*)&_base_salary, sizeof(_base_salary));
	os.read((char*)&_sold_nm, sizeof(_sold_nm));
	os.read((char*)&_price, sizeof(_price));
}

std::ifstream& operator>>(std::ifstream& os, SalesManager& o){
	o.fread(os);
	return os;
	}
//EmployeesArray
EmployeesArray::EmployeesArray(){
	_employees = new Employee*[10];
	cap = 10;
	size = 0;
}
	
EmployeesArray::~EmployeesArray(){
	for (int i = 0; i < size; i++){
		delete _employees[i];
		}
	delete [] _employees;
}

int EmployeesArray::total_salary() const{
	int s = 0;
	for (int i = 0; i < size; i++)
		s +=  (_employees[i])->salary();
	return s;
}

void EmployeesArray::add(Employee *e){
	if (size + 1 >= cap){
		Employee** tmp = new Employee*[cap*2];
		memcpy(_employees,tmp,cap*sizeof(tmp[0]));
		cap*=2;
		std::swap(tmp, _employees);
		}
	_employees[size++] = e;
}

std::ostream& operator<<(std::ostream& os, EmployeesArray& o){
	for (int i = 0; i < o.size; i++){
		os << i+1 <<'.';
		os << (*o._employees[i]);
		os << '\n';
	}
	os<< "== Total salary: " << o.total_salary() << "\n";
	return os;
}

std::istream& operator>>(std::istream& os, EmployeesArray& o){
	int type;
	os >> type;
	if (type == 1){
		Developer* d = new Developer();
		os >> (*d);
		o.add(d);
	}
	else{
		SalesManager* s = new SalesManager();
		os >> (*s);
		o.add(s);
	}
	return os;
}

std::ofstream& operator<<(std::ofstream& os, EmployeesArray& o){
	os.write((char *)&o.size, sizeof(int));
	for(int i = 0; i < o.size; i++){
		os << (*o._employees[i]);
	}
	return os;
}

std::ifstream& operator>>(std::ifstream& os, EmployeesArray& o){
	int _size;
	os.read((char *)&_size, sizeof(_size));
	for(int i = 0; i < _size; i++){
		int32_t type;
		os.read((char*)&type,sizeof(type));
		if (type == 1){
			Developer* d = new Developer();
			os >> (*d);
			o.add(d);
		}
		else{
			SalesManager* s = new SalesManager();
			os >> *(s);
			o.add(s);
		}
	}
	return os;
}
