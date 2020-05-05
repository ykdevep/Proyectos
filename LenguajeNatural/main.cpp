#include <fstream>
#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    fstream archivo("estud.txt");
    int numero, nota1, nota2, notaFinal, opcion;

    do
    {
        cout << "Entre un nuevo registro\n Entre cero para salir.";
        cin >> opcion;
        cin.ignore();
        
            if (!archivo.is_open())
            {
                archivo.open("estud.txt", ios::out);
            }
            cout << "Entre núm. De estudiante: ";
            getline(cin, numero);
            cout << "Entre nota de examen 1: ";
            getline(cin, nota1);
            cout << "Entre nota de examen 2: ";
            getline(cin, nota2);
            cout << "Entre nota de examen final: ";
            getline(cin, notaFinal);

            archivo << "Número de estudiante: " << numero << endl;
            archivo << "Nota examen 1: " << nota1 << endl;
            archivo << "Nota examen 2: " << nota2 << endl;
            archivo << "Nota final: " << notaFinal << endl;

            system("cls");
            cout << "Registro guardado.\n";
            system("pause");
            system("cls");
 
        archivo.close();

    } while (opcion != 0);

    char leer[128];
    archivo.open("estud.txt", ios::out);
    while (!archivo.eof())
    {
        archivo >> leer;
        cout << leer << endl;
    }
    archivo.close();
    system("pause");
    return 0;   

}