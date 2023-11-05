#include <stdio.h>
#include <string.h>

int main () {
   char str1[15];
   char str2[15];
   int str3=10;
   strcpy(str1, "tutorialspoint");
   strcpy(str2, "compileonline");

   puts(str1);
   puts(str2);
   //printf("%c", str1);
  
   char str4[2];
   (char)(str3);
   
   printf("%s", str4);

   puts(str4);
   printf("%s", str1);
   return(0);
}
