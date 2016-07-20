#include <fstream>
#include<iostream>
#include<string>
#include <vector>
#include <algorithm>

using namespace std;

void funcionRecursiva(vector<string>, vector<string>, int);
vector<string> actualizaNivelAbajo(vector<string>, vector<string>, int);


vector<string> nivelAbajo;
vector<string> nivelAuxiliar;

int main(){

	int numCasosBase;
	cout << "Dame el numero de casos base que deseas introducir: ";
	cin >> numCasosBase;
	vector<string> casosBase;

	for (int i = 0; i < numCasosBase; i++){
		string aux;
		cout << "\nDame el caso base # " << i+1 << " : ";
		cin >> aux;
		if (aux == "*"){
			casosBase.push_back(" ");
		}
		else{
			casosBase.push_back(aux);
		}
	}
	
	int numCasosRecursivos;
	cout << "\nAhora Dame el numero de casos del paso recursivo: ";
	cin >> numCasosRecursivos;
	//numCasosRecursivos = numCasosRecursivos+1;
	vector<string> casosRecursivo;

	for (int i = 0; i < numCasosRecursivos; i++){
		string aux;
		cout << "\nDame el caso recursivo # " <<  i+1 << " : ";
		cin >> aux;
		casosRecursivo.push_back(aux);
	}


	int numRepiteFuncion;
	cout << "\nDame el numero de veces que deseas que se repita la funcion: ";
	cin >> numRepiteFuncion;
	numRepiteFuncion = numRepiteFuncion + 1;
	vector<string> res;

	funcionRecursiva(casosRecursivo, casosBase, numRepiteFuncion);
	cout << "\n";
	system("pause");
	return 0;
}



void funcionRecursiva(vector<string> casosRecursivo, vector<string> casosBase, int numRep){
	if (numRep == 1){
		cout << "Iteracion # " << numRep -1 << ": ";
		if (casosBase.size() == 0){
			nivelAbajo.push_back(".");
			cout << "String Nulo,";
		}
		for (vector<string>::iterator it = casosBase.begin(); it != casosBase.end(); ++it){
			nivelAbajo.push_back(*it);
			if (*it == " "){
				cout << "String Nulo, ";
			}
			else{
				cout << *it << " ,";
			}
		}
	}
	else{
		funcionRecursiva(casosRecursivo, casosBase, numRep - 1);
		cout << "\nIteracion # " << numRep -1 << " :";
		nivelAbajo = actualizaNivelAbajo(casosRecursivo, casosBase, numRep);
		for (vector<string>::iterator it = nivelAbajo.begin(); it != nivelAbajo.end(); ++it){
			if (*it != " "){
				cout << *it << ",";
			}
		}
	}
}


vector<string> actualizaNivelAbajo(vector<string> casosRecursivo, vector<string> casosBase, int numRep){
	//vector<string> aux;
	vector<string> aux;
	vector<string> auxUltimo;
	vector<string> auxProvisional;
	vector<string> auxProvisional2;
	string prov;
	string prov2;
	vector<char> complicado;
	bool cambio = false;

	for (vector<string>::iterator it = casosRecursivo.begin(); it != casosRecursivo.end(); ++it){
		for (int i = 0; i < it->length(); i++){
			if ((*it)[i] == 'u' || (*it)[i] == 'v' || (*it)[i] == 'w' || (*it)[i] == 'x' || (*it)[i] == 'y' || (*it)[i] == 'z'){
				complicado.push_back((*it)[i]);
			}
		}
	}


	complicado.erase(unique(complicado.begin(), complicado.end()), complicado.end());

	for (vector<char>::iterator it = complicado.begin(); it != complicado.end(); ++it){
		//	cout << *it;
	}
	
	//if (complicado.size()>1){
		string ayudaCambio;
		string ayudaCambio2;
		//auxProvisional = casosRecursivo;
		for (vector<string>::iterator it = casosRecursivo.begin(); it != casosRecursivo.end(); ++it){
			ayudaCambio = *it;
			for (vector<string>::iterator it2 = nivelAbajo.begin(); it2 != nivelAbajo.end(); ++it2){
				for (int i = 0; i < ayudaCambio.length(); i++){
					if (ayudaCambio[i] == 'u'){
						ayudaCambio.replace(ayudaCambio.find("u"), 1, *it2);
						cambio = true;
					}
				}
				if (cambio){
					aux.push_back(ayudaCambio);
					ayudaCambio = *it;
					cambio = false;
				}
			}

			for (vector<string>::iterator it2 = nivelAbajo.begin(); it2 != nivelAbajo.end(); ++it2){
				for (int i = 0; i < ayudaCambio.length(); i++){
					if (ayudaCambio[i] == 'v'){
						ayudaCambio.replace(ayudaCambio.find("v"), 1, *it2);
						cambio = true;
					}
				}
				if (cambio){
					aux.push_back(ayudaCambio);
					ayudaCambio = *it;
					cambio = false;
				}
			}

			for (vector<string>::iterator it2 = nivelAbajo.begin(); it2 != nivelAbajo.end(); ++it2){
				for (int i = 0; i < ayudaCambio.length(); i++){
					if (ayudaCambio[i] == 'w'){
						ayudaCambio.replace(ayudaCambio.find("w"), 1, *it2);
						cambio = true;
					}
				}
				if (cambio){
					aux.push_back(ayudaCambio);
					ayudaCambio = *it;
					cambio = false;
				}
			}

			for (vector<string>::iterator it2 = nivelAbajo.begin(); it2 != nivelAbajo.end(); ++it2){
				for (int i = 0; i < ayudaCambio.length(); i++){
					if (ayudaCambio[i] == 'x'){
						ayudaCambio.replace(ayudaCambio.find("x"), 1, *it2);
						cambio = true;
					}
				}
				if (cambio){
					aux.push_back(ayudaCambio);
					ayudaCambio = *it;
					cambio = false;
				}
			}

			for (vector<string>::iterator it2 = nivelAbajo.begin(); it2 != nivelAbajo.end(); ++it2){
				for (int i = 0; i < ayudaCambio.length(); i++){
					if (ayudaCambio[i] == 'y'){
						ayudaCambio.replace(ayudaCambio.find("y"), 1, *it2);
						cambio = true;
					}
				}
				if (cambio){
					aux.push_back(ayudaCambio);
					ayudaCambio = *it;
					cambio = false;
				}
			}

			for (vector<string>::iterator it2 = nivelAbajo.begin(); it2 != nivelAbajo.end(); ++it2){
				for (int i = 0; i < ayudaCambio.length(); i++){
					if (ayudaCambio[i] == 'z'){
						ayudaCambio.replace(ayudaCambio.find("z"), 1, *it2);
						cambio = true;
					}
				}
				if (cambio){
					aux.push_back(ayudaCambio);
					ayudaCambio = *it;
					cambio = false;
				}
			}

		}

		for (vector<string>::iterator it = aux.begin(); it != aux.end(); ++it){
			(*it).erase(remove((*it).begin(), (*it).end(), '.'), (*it).end());
		}


		bool quedanExp = false;
		for (vector<string>::iterator it = aux.begin(); it != aux.end(); ++it){
			for (int i = 0; i < (*it).size(); i++){
				if ((*it)[i] == 'u' || (*it)[i] == 'v' || (*it)[i] == 'w' || (*it)[i] == 'x' || (*it)[i] == 'y' || (*it)[i] == 'z'){
					quedanExp = true;
					break;
				}
			}
		}


		while (quedanExp){
			for (vector<string>::iterator it = aux.begin(); it != aux.end(); ++it){
				string ayuda2 = (*it);
				/////////////////////////////////////////////////////
				bool paseDirecto = false;
				for (int i = 0; i < ayuda2.size(); i++){
					if (ayuda2[i] == 'u' || ayuda2[i] == 'v' || ayuda2[i] == 'w' || ayuda2[i] == 'x' || ayuda2[i] == 'y' || ayuda2[i] == 'u'){
						paseDirecto = true;
					}
				}
				if (!paseDirecto){
					auxProvisional.push_back(ayuda2);
				}
				////////////////////////////////////////////////////
				cambio = false;
				for (vector<string>::iterator it2 = nivelAbajo.begin(); it2 != nivelAbajo.end(); ++it2){
					for (int i = 0; i < ayuda2.size(); ++i){
						if (ayuda2[i] == 'u'){
							ayuda2.replace(ayuda2.find("u"), 1, *it2);
							cambio = true;
						}
					}
					if (cambio){
						auxProvisional.push_back(ayuda2);
						ayuda2 = *it;
						cambio = false;
					}
				}

				for (vector<string>::iterator it2 = nivelAbajo.begin(); it2 != nivelAbajo.end(); ++it2){
					for (int i = 0; i < ayuda2.size(); ++i){
						if (ayuda2[i] == 'v'){
							ayuda2.replace(ayuda2.find("v"), 1, *it2);
							cambio = true;
						}
					}
					if (cambio){
						auxProvisional.push_back(ayuda2);
						ayuda2 = *it;
						cambio = false;
					}
				}

				for (vector<string>::iterator it2 = nivelAbajo.begin(); it2 != nivelAbajo.end(); ++it2){
					for (int i = 0; i < ayuda2.size(); ++i){
						if (ayuda2[i] == 'w'){
							ayuda2.replace(ayuda2.find("w"), 1, *it2);
							cambio = true;
						}
					}
					if (cambio){
						auxProvisional.push_back(ayuda2);
						ayuda2 = *it;
						cambio = false;
					}
				}

				for (vector<string>::iterator it2 = nivelAbajo.begin(); it2 != nivelAbajo.end(); ++it2){
					for (int i = 0; i < ayuda2.size(); ++i){
						if (ayuda2[i] == 'x'){
							ayuda2.replace(ayuda2.find("x"), 1, *it2);
							cambio = true;
						}
					}
					if (cambio){
						auxProvisional.push_back(ayuda2);
						ayuda2 = *it;
						cambio = false;
					}
				}

				for (vector<string>::iterator it2 = nivelAbajo.begin(); it2 != nivelAbajo.end(); ++it2){
					for (int i = 0; i < ayuda2.size(); ++i){
						if (ayuda2[i] == 'y'){
							ayuda2.replace(ayuda2.find("y"), 1, *it2);
							cambio = true;
						}
					}
					if (cambio){
						auxProvisional.push_back(ayuda2);
						ayuda2 = *it;
						cambio = false;
					}
				}

				for (vector<string>::iterator it2 = nivelAbajo.begin(); it2 != nivelAbajo.end(); ++it2){
					for (int i = 0; i < ayuda2.size(); ++i){
						if (ayuda2[i] == 'z'){
							ayuda2.replace(ayuda2.find("z"), 1, *it2);
							cambio = true;
						}
					}
					if (cambio){
						auxProvisional.push_back(ayuda2);
						ayuda2 = *it;
						cambio = false;
					}
				}
			}
			aux = auxProvisional;
			auxProvisional.clear();

			////////////////////////////
			bool quedanExp2 = false;
			for (vector<string>::iterator it = aux.begin(); it != aux.end(); ++it){
				for (int i = 0; i < (*it).size(); i++){
					if ((*it)[i] == 'u' || (*it)[i] == 'v' || (*it)[i] == 'w' || (*it)[i] == 'x' || (*it)[i] == 'y' || (*it)[i] == 'z'){
						quedanExp2 = true;
						break;
					}
				}
			}
			if (!quedanExp2){
				quedanExp = false;
			}
		}

		for (vector<string>::iterator it = aux.begin(); it != aux.end(); ++it){
			(*it).erase(remove((*it).begin(), (*it).end(), '.'), (*it).end());
		}

		for (vector<string>::iterator it = aux.begin(); it != aux.end(); ++it){
			(*it).erase(remove((*it).begin(), (*it).end(), ' '), (*it).end());
		}

		sort(aux.begin(), aux.end());
		aux.erase(unique(aux.begin(), aux.end()), aux.end());

		for (vector<string>::iterator it = casosBase.begin(); it != casosBase.end(); ++it){
			if (*it == " "){
				aux.push_back(" ");
			}
		}



		if (numRep > 2){

			int borrado = 0;
			vector<int> seBorran;
			int minimo=1000;
			for (vector<string>::iterator it2 = nivelAbajo.begin(); it2 != nivelAbajo.end(); ++it2){
				if ((*it2).length() < minimo){
					minimo = (*it2).length();
				}
			}

			for (vector<string>::iterator it = aux.begin(); it != aux.end(); ++it){
				//for (vector<string>::iterator it2 = nivelAbajo.begin(); it2 != nivelAbajo.end(); ++it2){
					if ((*it).length() <= minimo){
						seBorran.push_back(borrado);
					}
				//}
				borrado++;
			}



			sort(seBorran.begin(), seBorran.end());
			seBorran.erase(unique(seBorran.begin(), seBorran.end()), seBorran.end());
			int restale=0;
			for (vector<int>::iterator it = seBorran.begin(); it != seBorran.end(); ++it){
				aux.erase(aux.begin() + ((*it)-restale));
				restale++;
			}
		}


		//aux.erase(aux.begin());

		return aux;
}