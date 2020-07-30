//10828 스택구현
/*
명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

 */
#include <iostream>
#include <stack>
#include <cstdio>
#include <string>

using namespace std;

int main() {
	int n;
	cin >> n;
	
	string str;
	stack<int> s;

	for (int i = 0; i < n; i++) {
		cin >> str;
		if (str == "push") {
			int num;
			cin >> num;
			s.push(num);
		}
		else if (str == "pop") {
			if (s.empty()) {
				cout << "-1\n";
			}
			else {
				cout << s.top() << endl;
				s.pop();
			}
		}
		else if (str == "size") {
			cout << s.size() << endl;
		}
		else if (str == "empty") {
			if (s.empty()) {
				cout << "1\n";
			}
			else cout << "0\n";
		}
		else if (str == "top") {
			if (s.empty()) {
				cout << "-1\n";
			}
			else cout << s.top() << endl;
		}
	}
}