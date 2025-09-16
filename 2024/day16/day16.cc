#include <iostream>
#include <queue>
#include <vector>
#include <fstream>
#include <string>
#include <deque>

using Position = std::pair<int, int>;
std::priority_queue<std::tuple<Position, int, int>> pq; //tuple(position, direction, cost)


void pathfinder(std::vector<std::string> &map){
    while(true) {
        std::tuple<Position, int, int> t = pq.pop();
        Position pos = t<0>;
    }
}

int main(void) {
    std::fstream inputstream("test.in");
    std::vector<std::string> map;
    std::string line;
    Position start, end;
    int rowcount = 0;

    while(inputstream >> line) {
        if (line.find('S') != std::string::npos){
            start = std::make_pair(rowcount, line.find('S'));
            std::cout << rowcount << " " << line.find('S') <<std::endl;
        }
        if (line.find('E') != std::string::npos) {
            end = std::make_pair(rowcount, line.find('E'));
            std::cout << rowcount << " " << line.find('E') << std::endl;
        }
        rowcount++;
    }

    pathfinder(map);

    std::cout << map[end.first][end.second] << std::endl;
}
