//Link d Questão: https://www.beecrowd.com.br/judge/pt/problems/view/2238

#include <iostream>
#include <string>

using namespace std;

int numb[4] = {0,0,0,0};

void split(string str)
{
	string number = "";
	
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < str.size(); j++)
		{
			if (str[j] == ' ')
			{
				cout << number << endl;
				number = "";
			}
			else
			{
				number = number + str[j];
			}
		}	
		
	}
	
}


int main()
{
	//A -> Divisor de N
	//B -> Não Divisor N
	//C -> Multiplo N
	//D -> Não Multiplo N
	
	string input;
	getline(cin,input);
	split(input);
	
	
}
