#include<iostream>
#include<string>

using namespace std;

void computeLPS(string pat, int * lps){
	int i = 0, j = 1;
	lps[0] = 0;
 	for(int p = 1; p < pat.size(); ){
 		if(pat[i] == pat[p]){
 			i++;
 			lps[p] = i;
 			p++;
 		}else{
 			if(i != 0){
 				i = lps[i-1];
 			}else{
 				lps[p] = 0;
 				p++;
 			}
 		}
 	}

}

void search(string text, string pat){
	int lps [pat.size()];
	computeLPS(pat, lps);
	int i = 0; // index for text
    int j = 0; // index for pat


    while (i < text.size()) { 

        if (pat[j] == text[i]) { 
            j++; 
            i++; 
        } 
  
        if (j == pat.size()) { 
            printf("Found pattern at index %d ", i - j); 
            j = lps[j - 1]; 
        } 
        else if (i < text.size() && pat[j] != text[i]) { 
            if (j != 0) 
                j = lps[j - 1]; 
            else
                i = i + 1; 
        } 
    } 
}


int main(){

	string text = "ABABABCABABABCABABACC";
	string pat = "ABABAC";
	search(text,pat);

	return 0;
}