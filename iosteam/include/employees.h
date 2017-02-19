#ifndef __LAB11_EMPLOYEES_H_INCLUDED
#define __LAB11_EMPLOYEES_H_INCLUDED

#include <stdint.h>
#include <iostream>
#include <fstream>

class Employee{
protected:
	char *_name;
	int32_t _base_salary;
	Employee();
public:
	virtual void read(std::istream& os) = 0;
	virtual void fread(std::ifstream& os) = 0;
	virtual void write(std::ostream& os) = 0;
	virtual void fwrite(std::ofstream& os) = 0;
	virtual int salary() const = 0;
	virtual ~Employee();
	friend std::ostream& operator<<(std::ostream& os, Employee& o);
	friend std::istream& operator>>(std::istream& os, Employee& o);
	friend std::ofstream& operator<<(std::ofstream& os, Employee& o);
	friend std::ifstream& operator>>(std::ifstream& os, Employee& o);
};


class Developer: public Employee {
public:
	Developer();
	~Developer();
	int salary() const {
		int salary = _base_salary;
		if (_has_bonus) { salary += 1000; }
		return salary;
}	
	friend std::ostream& operator<<(std::ostream& os, Developer& o);
	friend std::istream& operator>>(std::istream& os, Developer& o);
	friend std::ofstream& operator<<(std::ofstream& os, Developer& o);
	friend std::ifstream& operator>>(std::ifstream& os, Developer& o);

	virtual void read(std::istream& os);
	virtual void fread(std::ifstream& os);
	virtual void write(std::ostream& os);
	virtual void fwrite(std::ofstream& os);
private:
	bool _has_bonus;
	Developer(Developer& d);
	Developer& operator=(Developer& d); 
};


class SalesManager:public Employee {
public:
	~SalesManager();
	SalesManager();
	int salary() const {
		return _base_salary + _sold_nm * _price * 0.01;
	}
	friend std::ostream& operator<<(std::ostream& os, SalesManager& o);
	friend std::istream& operator>>(std::istream& os, SalesManager& o);
	friend std::ofstream& operator<<(std::ofstream& os, SalesManager& o);
	friend std::ifstream& operator>>(std::ifstream& os, SalesManager& o);
	virtual void read(std::istream& os);
	virtual void fread(std::ifstream& os);
	virtual void write(std::ostream& os);
	virtual void fwrite(std::ofstream& os);
private:
	int32_t _sold_nm, _price;
	SalesManager(SalesManager& s);
	SalesManager& operator=(SalesManager& s); 
	
};


class EmployeesArray {
public:
	EmployeesArray();
	~EmployeesArray();
	void add(Employee *e);
	int total_salary() const;
	friend std::ostream& operator<<(std::ostream& os, EmployeesArray& o);
	friend std::istream& operator>>(std::istream& os, EmployeesArray& o);
	friend std::ofstream& operator<<(std::ofstream& os, EmployeesArray& o);
	friend std::ifstream& operator>>(std::ifstream& os, EmployeesArray& o);
private:
	Employee **_employees;
	int32_t cap;
	int32_t size;
};

#endif
