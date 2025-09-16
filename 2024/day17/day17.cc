#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int A,B,C,PC = 0;
std::vector<int> program;

int getcoperand() {
    int val = program[PC + 1];
    if (val == 4) return A;
    if (val == 5) return B;
    if (val == 6) return C;
    return val;
}

std::vector<int> simulate(){
    std::vector<int> answervec;
    int opcode, operand;

    std::cout << "A:" << A << "B:" << B << "C:" << C << std::endl;
    while (PC < program.size()) {
        opcode = program[PC];
        std::cout << PC <<std::endl;

        switch(opcode){
            double f;
            case 0: //adv
                operand = getcoperand();
                f = A;
                f = f / std::pow(2, operand);
                A = std::floor(f);
                break;
            case 1: //bxl
                operand = program[PC + 1];
                B = B ^ operand;
                break;
            case 2: //bst
                operand = getcoperand();
                B = operand % 8;
                break;
            case 3: //jnz
                operand = program[PC + 1];
                if (A != 0) {
                    PC = operand;
                    PC-=2;
                }
                break;
            case 4: //bxc
                B = B ^ C;
                break;
            case 5: //out
                operand = getcoperand();
                answervec.push_back(operand % 8);
                break;
            case 6: //bdv
                operand = getcoperand();
                f = A;
                f /= std::pow(2, operand);
                B = std::floor(f);
                break;
            case 7: //cdv
                operand = getcoperand();
                f = A;
                f /= std::pow(2, operand);
                C = std::floor(f);
                break;
            default:
                break;
        }
        std::cout << "A:" << A << "B:" << B << "C:" << C << std::endl;
        PC+=2;
    }
    return answervec;
}

int main(void) {
    std::fstream inputstream("test2.in");
    std::string str;
    int num;

    //parse input
    getline(inputstream, str, ':');
    inputstream >> A;
    getline(inputstream, str, ':');
    inputstream >> B;
    getline(inputstream, str, ':');
    inputstream >> C;
    getline(inputstream, str, ':');
    while (inputstream >> num) {
        program.push_back(num);
        getline(inputstream, str, ',');
    }

    std::vector<int> answervec = simulate();
    for (int ans : answervec) {
        std::cout << ans << ",";
    }
    std::cout << std::endl;
}
