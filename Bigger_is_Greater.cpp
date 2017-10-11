#include <iostream>
#include <algorithm>
int main() {
    int t;
    std::cin>>t;
    for(int i=0;i<t;i++) {
        std::string input;
        std::cin>>input;
        if(std::next_permutation(input.begin(),input.end()))
            std::cout<<input<<std::endl;
        else
            std::cout<<"no answer"<<std::endl;
    }
    return 0;
}
