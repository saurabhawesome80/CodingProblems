/*
Given a list of numbers, return whether any two sums to k.
For example, given [10, 15, 3, 7] and k of 17, 
return true since 10 + 7 is 17.

input : first line ( n and k)
        n space seperated ints

output : True or False
*/

#include<iostream>
#include <map>
using namespace std;

bool findPair(int * arr, int n, int k){
    map<int, bool> hash;
    for(int i = 0; i < n; i++){
        hash.insert(pair<int, int>(arr[i], true));
    }
    for(int i = 0; i < n; i++){
        if(hash.find(k - arr[i]) != hash.end()){
            return true;
        }
    }
    return false;
}

int main(){
    int n,k;
    cin>>n>>k;
    int arr[n];
    for(int i = 0; i < n; i++){
        cin>>arr[i];
    }
    bool found = findPair(arr, n, k);
    cout<<"pair found : "<<found;
    return 0;
}