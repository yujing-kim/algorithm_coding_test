#include <deque>
#include <iostream>
#include <string>

using namespace std;

int main(){
    int N;
    cin >> N;
    deque<int> dq;
    string str;
    int n;
    for(int i = 0 ; i < N ;i++){
        cin >> str;
        if(str == "push_back"){
            cin >> n;
            dq.push_back(n);
        }else if(str == "push_front"){
            cin >> n;
            dq.push_front(n);
        }else if(str == "pop_front"){
            if(dq.empty()){
                cout << -1 << '\n';
            }else{
                cout << dq.front() << "\n";
                dq.pop_front();
            }
        }else if(str == "pop_back"){
            if(dq.empty()){
                cout << -1 << '\n';
            }else{
                cout << dq.back() << "\n";
                dq.pop_back();
            }
        }else if(str == "size"){
            cout << dq.size() << '\n';
        }else if(str == "empty"){
            cout << dq.empty() << '\n';
        }else if(str == "front"){
            if(dq.empty()){
                cout << -1 << '\n';
            }else{
                cout << dq.front() << '\n';
            }
            
        }else {
            if(dq.empty()){
                cout << -1 << '\n';
            }else{
                cout << dq.back() << '\n';
            }
        }
    }
    return 0;
}