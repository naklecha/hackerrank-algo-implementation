#include <iostream>
#include <algorithm>
int main() {
    int k;
    std::cin>>k;
    for(int i=0;i<k;i++) {
        std::string input;
        std::cin>>input;
        if(std::next_permutation(input.begin(),input.end()))
            std::cout<<input<<std::endl;
        else
            std::cout<<"No Answer"<<std::endl;
    }
    return 0;
}
