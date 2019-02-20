#include <iostream>
#include <string>
using namespace std;

void computeLPS(string pat, int * lps){ //example - abcab
    int i = 0, j = 1; 
    lps[0] = 0;
    while(j < pat.size()){
        if(pat[i] == pat[j]){
            i++;
            lps[j] = i;
            j++;
        }else{
            if(i != 0){
                i = lps[i-1];
            }else{
                lps[j] = 0;
                j++;
            }
        }
    }
}

int KMPSearch(string str, string pat){
    int lps [pat.size()];
    computeLPS(pat, lps);
    int i = 0, j = 0;
    while(i < str.size()){
        if(str[i] == pat[j]){
            i++;
            j++;
        }
        if(j == pat.size()){
            return i - pat.size();
        }
        if(i < str.size() && str[i] != pat[j]){
            if(j != 0){
                j = lps[j-1];
            }else{
                i++;
            }
        }
    }
    return -1;
}

int main(){
    string str = "abcdabfgabcabdeab";
    string pat = "abcab";
    int index = KMPSearch(str, pat);
    if(index == -1) cout<<"Pattern Not Found";
    else cout<<"Found at : "<<index;
    return 0;
}