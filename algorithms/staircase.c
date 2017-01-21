#include <stdio.h>

int main(){
    int n, temp;
    scanf("%d", &n);


    for(int i = 1; i <= n; i++){
        
        for(int j = 0; j < i; j++){
            printf("%*s", n, " ");
            printf("#");
        }
        printf("\n");
    }

    // printf("%3s\n", "#");
    // printf("%3s\n", "##");
    // printf("%3s\n", "###");
}