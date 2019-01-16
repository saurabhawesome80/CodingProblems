#include<iostream>

using namespace std;

int getMoney(){
	return 1;
}

int getMoney(int some){
	return 3;
}

int main(int argc , char * argv[]){
	cout<<getMoney();
	cout<<endl<<getMoney(4);
	return 0;
}