#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
int main()
{
    char str1[100];
    char input[10][10]; 
    int i,j,ctr; 
    while (1) {

    
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
    
    for(i=0;i < ctr;i++) {
      int f = i + 1;
      
      if (strcmp(input[i], "read") == 0) {
        char ee[] = "cat ";
        strcat(ee, input[f]);
        system(ee);
        break;
      }
      
      

    }
  }
  return 0;
}
