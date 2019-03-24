#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

int main()
{
	ifstream infile; 
	infile.open("outc.txt",ios::in);
	
	string line;
	int stepmax = 0;

	while(getline(infile,line)) {
    
    	//string line;
		int i = 0;


		
		unsigned long long int N = stoi(line);
		unsigned long long int n = N;

		while (1) {
			unsigned long long int result = 1;

			while (N != 0) {
				unsigned long long int digit = N % 10;
				N = N / 10;
				result = result * digit;
			}
			//cout << result << endl;
			i++;

			if (result < 10) {
				break;
			}

			N = result;
	}
		//cout << "TOTAL STEPS: " << i << endl;

		

		if(i > stepmax){

			stepmax = i;
			cout << "New record: " << i << " with number: " << n << endl;

		}


	}

	infile.close();

	return 0;
}
