#include <bits/stdc++.h>
using namespace std;
//It's stupid but it works :D
string line;

int main() {
    
    ifstream MyFile("input.txt");
    getline(MyFile, line);
    MyFile.close();
    int xMin;
    int xMax;
    int yMin;
    int yMax;
    vector<int> values;
    string temp;
    const regex r("(-?\\d+)");  
    smatch sm;

    string::const_iterator searchStart( line.cbegin() );
    while ( regex_search( searchStart, line.cend(), sm, r ) )
    {
        values.push_back(stoi(sm[0]));  
        searchStart = sm.suffix().first;
    } 
    xMin = values[0];
    xMax = values[1];
    yMin = values[2];
    yMax = values[3];
    int globalYMax;
    int count=0;
    for (int initX=-1000; initX < 1010; initX++) {
        for (int initY=-1000; initY < 10000; initY++) {
            int x=0;
            int y=0;
            int xS=initX;
            int yS=initY;
            int currentYMax=0;
            for(int step=0; step<1000; step++) {
                x += xS;
                y += yS;
                xS += xS>0 ? -1 : xS<0 ? +1 : 0;
                yS += -1;
                currentYMax = max(currentYMax, y);
                if (x<=xMax && x>=xMin && y<=yMax && y>=yMin) {
                    globalYMax = max(globalYMax, currentYMax);
                    count++;
                    break;
                }
            }
        }
    }
    

    cout << "part1: " << globalYMax << endl;
    cout << "part2: " << count << endl;
    return 0;
}