#include "employees.h"
#include <cstring>
#include <string>
#include <stdint.h>
#include <iostream>
#include <fstream>

int main(){
	std::string s;
	std::cin >> s;
	std::ifstream in;
	std::ofstream out;
	EmployeesArray ea;
	while(true){
		if (s == "load"){
			std::string file_name;
			std::cin >> file_name;
			//std::fstream read(file_name, std::ios::binary|std::ios::in);
			in.open(file_name.c_str(), std::ios::binary);
			in >> ea;
			in.close();
		}
		if (s == "list")
			std::cout << ea;
		if (s == "add")
			std::cin >> ea;
		if (s == "save"){
			std::string file_name;
			std::cin >> file_name;
			out.open(file_name.c_str(), std::ios::binary);
			//std::fstream write(file_name, std::ios::binary|std::ios::out);
			out << ea;
			out.close();
		}
		if (s == "exit")
			return 0;
		std::cin >> s;
	}
	return 0;
}
