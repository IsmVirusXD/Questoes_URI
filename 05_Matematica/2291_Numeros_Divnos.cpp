// link da Questão: https://www.beecrowd.com.br/judge/pt/problems/view/2291

#include <iostream>

using namespace std;

int divisores(int n);
int num_perfeito(int n);

int main()
{
    int entrada = 0;

    do
    {

        cin >> entrada;
        cout << num_perfeito(entrada);

    } while (entrada != 0);

    return 0;
}

int divisores(int n)
{
    int soma = 0;

    for (int i = 0; i <= n; i++)
    {
        if (n % i == 0)
        {
            soma += i;
        }
    }

    return soma;
}

int num_perfeito(int n)
{
    int i = 1;
    int result = 0;
    do
    {
        result += divisores(i);

    } while (i <= n);

    return result;
}