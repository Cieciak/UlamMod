#include <math.h>
#include <stdio.h>

int prime(int x){
    if (x < 6){
        return (x >= 2) && (x != 4);
    } else {
        for (int n = 2; n < x; n++){
            if (x % n == 0){return 0;}
        }
    }
    return 1;
}