#include <stdio.h>

int main() {
  float input;
  float soma = 0;
  float media = 0;
  float i=0;

  printf("");
  scanf("%f", &input);

    if(input < 0){
        printf("%.2f\n", soma);
        printf("%.2f", media);
    }else{
    while(input >= 0) {
    soma += input;
    i++;
    printf("");
    scanf("%f", &input);
  }
    }
  
    
    media = soma/i;
    
    if(soma>0){
        printf("%.2f\n", soma);
        printf("%.2f", media);
    }
    
      return 0;
  

 
}
