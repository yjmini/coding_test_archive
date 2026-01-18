#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main()
{
	string str = "The_headline_is_the_text_indicating_the_nature_of_the_article_below_it.";
	for (int i = 0; i < str.size(); i++) {
		str[i] = toupper(str[i]);
	}
	
	cout << str;

	return 0;
}