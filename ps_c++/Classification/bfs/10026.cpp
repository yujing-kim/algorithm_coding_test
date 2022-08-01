//10026 _ 적록색약
/*
 * 입력을 받을때 두개의 맵을 한번에 입력받는다.
 * bfs의 인자로 맵을 주어서 계산한다
 * 방문배열을 초기화 시켜야한다
 */
#include <iostream>
#include<vector>
#include <queue>
#include<string.h>

using namespace std;

int N;
vector<int> v[100]; // 정상의 맵
vector<int> vrg[100]; //적녹색약의 맵
int visit[100][100]; //방문배열
char c; //RGB 받음
int dx[] ={0,0,1,-1};
int dy[] ={1,-1,0,0};
int answer;//답(정상인 사람)

void bfs(int x, int y, vector<int> c[]){
    /*
     *  1. queue 생성 , 첫번째 원소 넣기, 방문배열체크
     *  2. while 돌리기
     */
    queue<pair<int, int> > q;
    q.push(make_pair(x,y));
    visit[x][y] = 1; //들어와서 처음을 표시(시작점)

    int color = c[x][y]; //시작점의 색
    answer++;

    while(!q.empty()){  //시작점 부터 같은 영역들을 탐색
        x = q.front().first;
        y = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(nx >= 0 && ny >= 0 && nx < N && ny < N){
                if (c[nx][ny] == color && visit[nx][ny] == 0) {
                    visit[nx][ny] = 1; //방문
                    q.push(make_pair(nx, ny));
                }
            }
        }
    }
}


int input(){
    cin >> N;

    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++) {
            cin >> c;
            v[i].push_back(c);

            if(v[i][j] == 82 || v[i][j] == 71){
                vrg[i].push_back(82);
            }
            else{
                vrg[i].push_back(c);
            }
        }
    }
    return 0;
}


int p(){
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++) {
            cout << v[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++) {
            cout << vrg[i][j] << " ";
        }
        cout << endl;
    }

}

int main() {
    input();
    // R : 82 ,G:71
//    p();
    for(int n = 0 ; n < 2 ; n++) {
        memset(visit, 0, sizeof(visit));
        answer = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (visit[i][j] == 0) {
                    if(n == 0){
                        bfs(i, j, v);
                    }
                    else {
                        bfs(i, j, vrg);
                    }
                }
            }
        }
        cout << answer << " ";
    }
    cout << '\n';

    return 0;
}

