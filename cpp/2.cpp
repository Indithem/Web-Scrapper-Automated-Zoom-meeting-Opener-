#include <ctime>
// for istringstream
#include <sstream>
// for get_time
#include <iomanip>
// convert string iso format to ctime object
time_t get_timeOBJ_from_str(const std::string& inp){
	// a bundle that contains data on day,year,mins,hrs etc
	// direct object, not a pointer
	struct std::tm tm;
	// stream derived from given input, works in C++11
	std::istringstream stringstream(inp);

									//2021-07-22 17:00:00
	stringstream >> std::get_time(&tm,"%Y-%m-%d %H:%M:%S");	// CHANGE HERE TO CHANGE FORMAT

	return mktime(&tm);
}

#include<iostream>
#include<string>

#define print(X) std::cout<<X<<std::endl;

int main(int numberofargssent,char ** argv){

    // while (true){
    // std::getline(std::cin,str);
    // std::cout<<str<<std::endl;

    std::string str = std::string(argv[1])+" "+std::string(argv[2]);
    time_t t=get_timeOBJ_from_str(str);
    time_t now;time(&now);

    if (now>t){std::cout<<"it is in past\n";}
    else{std::cout<<"it is in future\n";}

    struct tm* gm;


/*    gm = gmtime(&t); //this converts the t`as in my time` to GMT
    print(gm->tm_hour);
*/


    struct tm* lm = localtime(&t);
    print(lm->tm_wday);

    // ctime::g

        // std::cout<<"Day is "<< t.GetDayoftheWeek();
    // }

    system("g++");
}