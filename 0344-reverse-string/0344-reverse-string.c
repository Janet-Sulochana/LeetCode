void reverseString(char* s, int sSize) {
   char temp[sSize];
   for(int i=0;i<sSize;i++){
        temp[i]=s[i];
   }
   for(int i=0;i<sSize;i++){
        s[i]=temp[sSize-1-i];
   }
}