#include "jsoncpp.cpp"
#include <fstream>
// Open json file and send it to var
void load_json_to_var(Json::Value& root){
    std::ifstream json_file("data.json",std::fstream::binary);
    json_file >> root;
}

#include <iostream>
int main(){
    Json::Value file;
    load_json_to_var(file);

    std::cout<<file[file.size()-1];

}