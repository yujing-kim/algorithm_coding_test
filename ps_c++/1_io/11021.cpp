#include <iostream>
#include <cstdio>

using namespace std;

int t ; //test case
int a,b;
int main(){
    scanf("%d", &t);
    
    for(int i = 0 ; i < t ; i++){
        scanf("%d %d", &a, &b);
        printf("Case #%d: ", i+1);
        printf("%d\n", a+b);
    }
    return 0;
}