// all the modules that are required for main to work as a script


#include <string>
#include <fstream>
// Check if a file exists
bool isfile(const std::string& file_name){
  std::ifstream file(file_name);
  if (file.fail()) return false;
  return true;
}


#include <sys/time.h>
#include <math.h>
// Get time in the needed format
std::string time_format(){
  char buffer[26];
    int millisec;
    time_t time_holder;
    time_holder = time(NULL);
    struct tm* tm_info;
    struct timeval tv;

    gettimeofday(&tv, NULL);

    millisec = lrint(tv.tv_usec/1000.0); // Round to nearest millisec
    if (millisec>=1000) { // Allow for rounding up to nearest second
        millisec -=1000;
        tv.tv_sec++;
    }

    tm_info = localtime(&time_holder);

    strftime(buffer, 26, "%Y-%m-%d %H:%M:%S", tm_info);
 
    return std::string(buffer)+","+std::to_string(millisec);   
}


#include <ctime>	// for istringstream
#include <sstream>	// for get_time
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


#include "jsoncpp.cpp"
#include <fstream>
// Open json file and send it to var
void load_json_to_var(Json::Value& root){
    std::ifstream json_file("data.json",std::fstream::binary);
    json_file >> root;
}

/*
    to get the last element of list:
    json.size()-1   `will be the index`
    `so`    json[json.size()-1]
*/

/*
    time_t objects can be compared normally, as in mathematical notation
*/

/*
    to get weekday:
        struct tm* lm = localtime(&t);      //make a tm* from time_t
        lm->tm_wday         //int
        `SUNDAY=0
         MONDAY=1
         ...
         SATURDAY=6`
*/

/*
    to execute a command
        system(`command`);

    no need to import anything
*/


#include <fstream>
enum LOGLEVEL{
    INFO = 0,
    WARN = 5,
    ERROR=10    
};
// custom output to file
void log(std::string inp,LOGLEVEL lvl = INFO){
    std::string msg;
    msg += "[" + time_format()+ "] main.cpp ";

    switch (lvl)
    {
    case INFO:
        msg+= "INFO ";
        break;
    case WARN:
        msg+= "WARN ";
        break;
    case ERROR:
        msg+= "ERROR ";
        break;
    default:
        break;
    }

    msg += inp;

    // msg is prepared, should be appended to file
    std::ofstream log_file("log.log",std::fstream::app);

    log_file << msg << std::endl;
}


// popup a message box with msg

// sleep till time, better version, that suited hibernation too!

// recreate no_escape.py