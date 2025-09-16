#include <iostream>
#include <fstream>
#include <utility>
#include <vector>

int GRIDSIZE = 71;
int BYTESFALLEN = 1024;
using Position = std::pair<int, int>;

std::vector<std::vector<int>> grid(GRIDSIZE, std::vector<int>(GRIDSIZE, 0));
std::vector<Position> vec;
std::vector<Position> direction = {{0,1}, {0,-1}, {-1,0}, {1,0}};

int floodfill() {

    std::vector<Position> newvec;
    int count = 0;

    while (vec.size() > 0) {
        for (Position p : vec) {
            if (p.first == GRIDSIZE - 1 && p.second == GRIDSIZE - 1) {
                std::cout << "break" << std::endl;
                return count;
            }
            for (Position dir : direction) {
                int newx = p.first + dir.first;
                int newy = p.second + dir.second;
                if (newx < grid.size() && newx >= 0 && newy < grid.size() && newy >= 0 && grid[newy][newx] != -1) {
                    grid[newy][newx] = -1;
                    newvec.push_back(std::make_pair(newx, newy));
                }
            }
        }
        vec = std::move(newvec);
        newvec.clear();
        count++;
    }
    return -1;
}

int main(void) {
    std::vector<Position> corruptedbytes;
    std::fstream inputstream("day18.in");
    int x, y;
    char comma;

    while (inputstream >> x >> comma >> y) {
        corruptedbytes.push_back(std::make_pair(x, y));
    }

    for (int i = 0; i < BYTESFALLEN; i++) {
        Position p = corruptedbytes[i];
        grid[p.second][p.first] = -1;
    }

    vec.push_back(std::make_pair(0, 0));
    int part1ans = floodfill();
    std::cout << part1ans << std::endl;

    int min = 0;
    int max = corruptedbytes.size();
    while (min < max) {
        for (auto &row : grid) {
            row = std::vector<int>(GRIDSIZE, 0);
        }
        int mid = (min + max) / 2;
        for (int i = 0; i < mid; i++) {
            Position p = corruptedbytes[i];
            grid[p.second][p.first] = -1;
        }
        vec.clear();
        vec.push_back(std::make_pair(0, 0));
        int ff = floodfill();
        if (ff == -1) {
            max = mid - 1;
        } else {
            min = mid + 1;
        }
        std::cout << min << " " <<max << std::endl;
    }
    std::cout << min << std::endl;
    std::cout << corruptedbytes[min].first << " " << corruptedbytes[min].second << std::endl;
}
