#include<iostream>
#include<string>
#include <vector>
#include <algorithm>

using namespace std;


int main(){


	string arr[6][2];

	arr[0][0] = "q1";
	arr[0][1] = "q2";
	arr[1][0] = "q0";
	arr[1][1] = "q3";
	arr[2][0] = "q3";
	arr[2][1] = "q0";
	arr[3][0] = "q4";
	arr[3][1] = "q5";
	arr[4][0] = "q0";
	arr[4][1] = "q3";
	arr[5][0] = "q3";
	arr[5][1] = "q0";

	string entrada;
	cin >> entrada;
	string actual="q0";

	for (int i = 0; i < entrada.length(); i++){
		if (entrada[i] == '0'){
			if (actual == "q0"){}
			else if (actual == "q1"){}
			else if (actual == "q2"){}
			else if (actual == "q3"){}
			else if (actual == "q4"){}
			else if (actual == "q5"){}
		}
		else if (entrada[i] == '1'){
			if (actual == "q0"){}
			else if (actual == "q1"){}
			else if (actual == "q2"){}
			else if (actual == "q3"){}
			else if (actual == "q4"){}
			else if (actual == "q5"){}
		}
	}



	system("pause");
	return 0;
}