#include <iostream>
#include "jsoncpp.cpp"
#include <fstream>
#include <string>


int main(){

    std::ifstream json_file("data.json",std::fstream::binary);
    Json::Value root;

    json_file >> root;

    std::cout<< root[0] <<std::endl;

}