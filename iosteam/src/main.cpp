#include "employees.h"
#include <cstring>
#include <string>
#include <stdint.h>
#include <iostream>
#include <fstream>

int main(){
	//std::ofstream ofile;
    //std::ifstream ifile;
    ////char *c = new char[10];
    
    //std::string d;
    //std::cin >> d;
    //d = d + '\0';
    //ofile.open("foobar.bin", std::ios::binary|std::ios::out);
    //ofile.write(d.c_str(), d.size()+1);
    //ofile.close();
   //// std::cout<<c;
    //ifile.open("foobar.bin", std::ios::binary|std::ios::in);
    //std::string s;
    ////char *t = new char[10];
    //char p;
    //ifile.read(&p, sizeof(char));
    //while(p != '\0'){
	//s.push_back(p);
	//ifile.read(&p, sizeof(char));
	//}
    //ifile.close();
    //std::cout << s;
	//Developer d;
	//Developer p;
	//std::cin >> d;
	//std::cout << d;
	//std::cin >> s;
	//out.open(s.c_str(), std::ios::binary|std::ios::out);
	//char p;
    //std::string b; 
    //in.read(&p, sizeof(char));
    //while(p != '\0'){
	//b.push_back(p);
	//in.read(&p, sizeof(char));
	//}
    //std::cout << b;
	//out << d;
	//out.close();
	//in.open(s.c_str(), std::ios::binary|std::ios::in);
	//in >> p;
	//std::cout << p; 
	EmployeesArray ea;
	 std::string s;
	std::ifstream in;
	std::ofstream out;
	std::cin >> s;
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
