#include <fstream>
#include<iostream>
#include<string>
#include <vector>
#include <algorithm>

using namespace std;

void isReflexive(char * data, vector<char> data2, int);
void isSymetric(char*, int, vector<char>);
void isTransitive(char*, int);

bool nadaCumple = true;

int main(){
	cout << "Dame el nombre del archivo: \n";
	string nombreArchivo;
	cin >> nombreArchivo;
	cout << endl;
	ifstream file(nombreArchivo);
	string str;
	getline(file, str);
	int numFilas = atoi(str.c_str());
	vector<char> data1;
	vector<char> data2;
	char * data;
	data = (char *) alloca(sizeof(char) * numFilas*2);
	
	for (int i = 0; i < numFilas*2; ++i){
		file >> data[i];
		data1.push_back(data[i]);
	}

	data2 = data1;

	cout << "El conjunto S es: { ";

	sort(data2.begin(), data2.end());
	data2.erase(unique(data2.begin(), data2.end()), data2.end());


	for (vector<char>::iterator it = data2.begin(); it != data2.end(); ++it){
		if (it == data2.end() - 1)
			cout << *it << " } \n";
		else
			cout << *it << ", ";
	}
	
	cout << "La relacion es: \n";
	isReflexive(data, data2, numFilas);
	//isSymetric(data, numFilas);
	//cout << data2.size();
	if (nadaCumple){
		cout << "NO CUMPLE NINGUNA\n";
	}


	char fin;
	system("pause");
	return 0;
}



void isReflexive(char * data, vector<char> data2, int numFilas){
	vector<char> ayuda;
	int size = data2.size();
	for (vector<char>::iterator it = data2.begin(); it != data2.end(); ++it){
		for (int i = 0; i < numFilas * 2; i=i+2){
			if (*it == data[i]){
				if (data[i] == data[i + 1]){
					ayuda.push_back(data[i]);
				}
			}
		}
	}
	ayuda.erase(unique(ayuda.begin(), ayuda.end()), ayuda.end());

	if (ayuda.size() == size){
		cout << "Reflexiva\n";
		nadaCumple = false;
	}
	if (ayuda.size() == 0){
		cout << "Irreflexiva\n";
		nadaCumple = false;
	}

	isSymetric(data, numFilas, ayuda);
}

void isSymetric(char* data, int numFilas, vector<char> numRef){
	int aux, aux1;
	int contadorRelaciones=0;
	for (int i = 0; i < numFilas * 2; i = i + 2){
		if (data[i] != data[i + 1]){
			aux = data[i];
			aux1 = data[i+1];
			for (int j = i+2; j < numFilas * 2; j = j + 2){
				if (j != i){
					if (data[j] == aux1 && data[j + 1] == aux){
						contadorRelaciones +=2;
					}
					if (data[j] == aux && data[j + 1] == aux1){
						contadorRelaciones--;
					}
				}
			}
		}
	}
	int totalLineas = numRef.size() + contadorRelaciones;
	//cout << totalLineas << endl;
	if (numFilas == totalLineas){
		cout<< "Simetrica\n";
		nadaCumple = false;
	}
	if (totalLineas == 0){
		cout << "Asimetrica\n";
		nadaCumple = false;
	}
	isTransitive(data, numFilas);
}


void isTransitive(char* data, int numFilas){
	bool transitive = false;
	////////////////////////////////
	int prueba;
	for (int i = 0; i < numFilas * 2; i = i + 2){
		prueba = data[i+1];
		for (int j = 0; j < numFilas * 2; j = j + 2){
			if (i != j && data[j] == prueba){
				transitive = true;
				break;
			}
		}
	}
	////////////////////////////////
	int aux[2], aux1[2];
	for (int i = 0; i < numFilas * 2; i=i+2){
		if (data[i] != data[i + 1]){
			aux[0] = data[i];
			aux[1] = data[i + 1];
			for (int j = 0; j < numFilas * 2; j = j + 2){
				if (i != j){
					if (aux[1] == data[j] && data[j]!=data[j+1] /*&& data[j+1] != aux[0]*/){
						transitive = false;
						aux1[0] = data[j];
						aux1[1] = data[j + 1];
						for (int k = 0; k < numFilas * 2; k = k + 2){
							if (k != i && k != j){
								if (data[k] == aux[0] && data[k + 1] == aux1[1]){
									transitive = true;
								}
							}
						}
					}
				}
			}
			if (transitive == false){
				break;
			}
		}
	}
	if (transitive == true){
		cout << "Transitiva \n";
		nadaCumple = false;
	}
}