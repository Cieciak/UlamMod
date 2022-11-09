#include <stdio.h>


int sqrt(int x){
    if (x < 2){return x;}
    float guess = x / 2;
    for (int i = 0; i < 10; i++){
        guess = .5 * (guess + x / guess);
    }
    return (int)guess;
}

int is_prime(int x){
    if (x < 2){return 0;}
    for (int i = 2; i <= sqrt(x); i++){
        if (x % i == 0){return 0;}

    }
    return 1;
}