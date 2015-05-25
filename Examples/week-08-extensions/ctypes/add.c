#include <stdio.h>

int add(int x, int y) {
    return x+y;
}
int main(void) {
    int w = 3;
    int q = 2;
    printf("%d + %d = %d\n\n", w, q, add(w,q));
}
