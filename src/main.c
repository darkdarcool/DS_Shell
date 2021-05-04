#include <stdio.h>
#include <string.h>
int main()
{
    char str1[100];
    char input[10][10]; 
    int i,j,ctr; 
    printf("$) ");
    fgets(str1, sizeof str1, stdin);	
 
    j=0; ctr=0;
    for(i=0;i<=(strlen(str1));i++)
    {
        // if space or NULL found, assign NULL into newString[ctr]
        if(str1[i]==' '||str1[i]=='\0')
        {
            input[ctr][j]='\0';
            ctr++;  //for next word
            j=0;    //for next word, init index to 0
        }
        else
        {
            input[ctr][j]=str1[i];
            j++;
        }
    }
		

    printf(input);
    return 0;
}