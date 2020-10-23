// 홀수

#include <iostream>
#include <vector>
#define MIN(a,b) ((a<b) ? a : b)

using namespace std;
int total = 0, m = 100;

int main(){
    int n = 0;
    for(int i  = 0 ; i < 7 ; i++){
        cin >> n;
        if(n%2 == 1){ //홀수
            total+=n;
            m = MIN(n,m);
        }
        
    }
    if(total>0){
        cout << total << '\n' << m << '\n';
    }
    else{
        cout << -1 << '\n';
    }
    
}