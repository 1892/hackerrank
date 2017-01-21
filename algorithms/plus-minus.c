#include <stdio.h>

int main(){
    int p_c = 0, m_c = 0, z_c = 0, n, temp;
    scanf("%d", &n);

    for(int i = 0; i < n; i++){
        scanf("%d", &temp);
        if ( temp > 0 ){
            p_c += 1;
        }else if(temp < 0){
            m_c += 1;
        }else{
            z_c += 1;
        } 
    }
    float p, m, z;
    p = (double)p_c / n;
    m = (double)m_c / n;
    z = (double)z_c / n;
    printf("%f\n%f\n%f\n", p, m, z);
}