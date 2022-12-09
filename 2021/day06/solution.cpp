#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

string line;
vector<string> lines;

long long solve(int n) {
    long long fishes[9] = {0,0,0,0,0,0,0,0,0};
    for (char c : lines[0]) {
        if (c != ',') {
            fishes[(int) c-'0'] += 1; 
        }
    }
    for (int i=0; i < n; i++) {
        long long day0 = fishes[0];
        for (int j = 1; j < 9; j++) {
            fishes[j-1] = fishes[j];
        }
        fishes[6] += day0;
        fishes[8] = day0;
    }
    long long result = 0;
    for (int i=0; i<9; i++) {
        result += fishes[i];
    }
    return result;
}

int main() {
    
    ifstream MyFile("input.txt");
    while(getline(MyFile, line)) {
        lines.push_back(line);
    }
    MyFile.close();
    cout << "part1: " << solve(80) << endl;
    cout << "part2: " << solve(256) << endl;
    return 0;
}