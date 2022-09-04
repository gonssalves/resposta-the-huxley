#include <stdio.h>

int main()
{
    char input[100], c1, c2;
    int i, length;

    printf ("");
    gets(input);
    length=strlen(input);
    
    printf ("");
    scanf ("%c", &c1);
    
    printf ("");
    scanf (" %c", &c2);
    
    for(i=0;i<length;i++){
        if (input[i]==c1){
            input[i]=c2;
        }
    }
    
    printf ("%s", input);
    
    return 0;
}
