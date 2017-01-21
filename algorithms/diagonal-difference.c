#include <stdio.h>
#include <stdlib.h>

int main(){
    int n, r_d = 0, l_d = 0;
    scanf("%d", &n);

    int matrix[n][n];
    for(int i = 0 ; i < n; i++){
        for(int j =0 ; j < n; j++){
            scanf("%d", &matrix[j][i]);
        }
    }

    for(int i = 0, j = n - 1 ; i < n ; i++, j--){
        l_d += matrix[i][i];
        r_d += matrix[i][j];
    }

    printf("%d \n", abs(l_d - r_d));
    
}