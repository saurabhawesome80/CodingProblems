// Given an array,find the maximum j – i such that arr[j] > arr[i] 

#include<iostream>
using namespace std;

void printArray(int * arr, int n){
    for(int i = 0; i < n; i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}

int maxIndexDiff(int * arr, int n){
    int Lmin[n], Rmax[n];
    Lmin[0] = arr[0];
    for(int i = 1; i < n; i++){
        Lmin[i] = (arr[i] < Lmin[i - 1]) ? arr[i] : Lmin[i - 1];
    }
    Rmax[n - 1] = arr[n - 1];
    for(int i = n - 2; i >= 0; i--){
        Rmax[i] = (arr[i] > Rmax[i + 1]) ? arr[i] : Rmax[i + 1];
    }
    int i = 0, j = 0, max_diff = 0;
    while(j < n && i < n){
        if(Lmin[i] < Rmax[j]){
            max_diff = ((j - i) > max_diff) ? (j - i) : max_diff;
            j++;
        }
        else i++;
    }
    return max_diff;
}

int main(){
    int arr[] = {18,8,4,3,6,7,6,10,4};
    cout<<"max j-i such that arr[j] > arr[i] : "<<maxIndexDiff(arr, 9);
    return 0;
}