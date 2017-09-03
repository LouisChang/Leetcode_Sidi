#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

int firstUniqChar(string s) {
        unordered_map <char,int> myMap;
        for (char c:s){
	    cout << c << ' ' << &c << endl;
            myMap[c]++;   
        }
        for (int i = 0; i < s.length();i++){
            if (myMap[s[i]] == 1) return i;   
        }
        return -1;
}

int main()
{
	string s;
	cin >> s;
	cout << firstUniqChar(s) << endl;
        return 0;

}



