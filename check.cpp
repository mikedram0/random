#include "pch.h"
#include <iostream>


using namespace std;

int main()
{
	int i = 0;
	unsigned long long int N = 999999;
	while (1) {
		unsigned long long result = 1;

		while (N != 0) {
			unsigned long long digit = N % 10;
			N = N / 10;
			result = result * digit;
		}
		cout << result << endl;
		i++;

		if (result < 10) {
			break;
		}

		N = result;
}
	cout << "TOTAL STEPS: " << i;

	return 0;
}
