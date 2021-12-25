#include <bits/stdc++.h>

using namespace std;

int main(){
    string line;
    vector<vector<char>> m;
    int w,h=0;
    while (getline(cin, line)){
        vector<char> v(line.begin(), line.end());
        m.push_back(v);
        h++;
        w = v.size();
    }

    bool moved = true;
    int step = 0;
    while (moved) {
        moved = false;
        // right
        for (int y=0; y<h; y++){
            bool zeroMoved = false;
            for (int x=0; x<w; x++) {
                if (m[y][x]=='>' && m[y][(x+1)%w]=='.' && (x!=w-1 || !zeroMoved)) {
                    m[y][(x+1)%w] = '>';
                    m[y][x] = '.';
                    moved = true;
                    if (x==0) zeroMoved = true;
                    x++;
                }
            }
        }
        // left
        for (int x=0; x<w; x++){
            bool zeroMoved = false;
            for (int y=0; y<h; y++) {
                if (m[y][x]=='v' && m[(y+1)%h][x]=='.' && (y!=h-1 || !zeroMoved)) {
                    m[(y+1)%h][x] = 'v';
                    m[y][x] = '.';
                    moved = true;
                    if (y==0) zeroMoved = true;
                    y++;
                }
            }
        }
        step++;
    }

    cout << "part1: " << step << endl;
    

}
