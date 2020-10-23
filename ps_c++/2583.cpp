//영역 구하기
#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

int M, N, K;
// 방향벡터 시 변수
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};

//영역의 크기를 넣을 벡터와 크기를 셀 변수
vector<int> s;
int cnt = 0;

//방문배열, map, row
vector< vector<int> > ch;
vector< vector<int> > mapp;
vector<int> row;

void input(){
    cin >> M >> N >> K;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            row.push_back(0);
        }
        mapp.push_back(row);
        row.clear();
    }

    for(int i = 0 ; i < K ; i++){
        int x1,y1,x2,y2;
        cin >> x1 >> y1 >> x2 >> y2;
        for(int xx = x1 ; xx < x2 ; xx++){
            for(int yy = y1 ; yy < y2 ; yy++){
                mapp[yy][xx]++;
            }
        }
    }
}

void dfs(int x, int y){
    //방문 체크
    ch[x][y] = 1;
    cnt++; //크기 +1

    //네 방향을 검사
    for(int i = 0 ; i < 4 ; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(nx >= 0 && nx < M && ny >= 0 && ny < N){ //범위에 맞고
            if(ch[nx][ny] == 0 && mapp[nx][ny] == 0){ //1이고, 방문 안했으면
                dfs(nx, ny);
            }
        }
    }

}

void makeCH(int x, int y){
    for(int i = 0 ; i < x ; i++){
        for(int j = 0 ; j < y ; j++){
            row.push_back(0);
        }
        ch.push_back(row);
        row.clear();
    }
}

void printCH(int x, int y){
    for(int i = 0 ; i < x ; i++){
        for(int j = 0 ; j < y ; j++){
            cout << mapp[i][j] << ' ';
        }
        cout << '\n';
        
    }
}

int main(){
    input();
    makeCH(M, N);

    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            if(ch[i][j] == 0 && mapp[i][j] == 0){
                cnt = 0;
                dfs(i,j);
                s.push_back(cnt);
            }
        }
    }
    
    // printCH(M,N);

    cout << s.size() << '\n';

    //정렬
    sort(s.begin(), s.end());

    for(int i = 0 ; i < s.size() ;i++) cout<<s[i] << ' ';
    cout << '\n';
    return 0;
}