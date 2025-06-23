char* removeDuplicates(char* s) {
   int len = strlen(s);
    if (len <= 1) return s;  

    int write_pos = 0;  

    for (int read_pos = 0; read_pos < len; read_pos++) {
        if (write_pos > 0 && s[write_pos - 1] == s[read_pos]) {
            write_pos--;  
        } else {
            s[write_pos++] = s[read_pos];  
        }
    }

    s[write_pos] = '\0'; 
    return s;
}
