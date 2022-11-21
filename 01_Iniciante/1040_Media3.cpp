//https://www.beecrowd.com.br/judge/pt/problems/view/1040
#include <iostream>

using namespace std;

float n1,n2,n3,n4,n5 = 0.0;

int main()
{

    cin >> n1 >> n2 >> n3 >> n4;

    float soma_total = (n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1);
    float soma_peso = (2 + 3 + 4 + 1);
    float media =  soma_total / soma_peso;
    cout << fixed ;
    cout.precision(1);
    cout << "Media: " << media << endl;

    if (media >= 7.0) {
        cout << "Aluno aprovado." << endl;
    }
    else if (media < 5.0) {
        cout << "Aluno reprovado." << endl;
    }else {
        cout << "Aluno em exame." << endl;
        cin >> n5;

        cout << "Nota do exame: " << n5 << endl;

        media = (media + n5)/2;

        if (media >= 5.0)
        {
            cout << "Aluno aprovado." << endl;
            cout << "Media final: " << media << endl;
        }
        else{
            cout << "Aluno reprovado" << endl;
            cout << "Media final: " << media << endl;
        }
    }

    return 0;
}
