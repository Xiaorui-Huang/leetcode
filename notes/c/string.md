# Strings in C

In C, processing a string involves manipulating arrays of characters. C strings
are represented as arrays of `char` and are null-terminated, meaning they end
with a special character `'\0'` to signify the end of the string. Below are
common operations to process strings in C:

Most interesting pattern is [tokenizing](#7-tokenizing-strings) strings using `strtok()`. 

## General `while` loop pattern

```c
int i = 0;
while (str[i] != '\0') {
    // Process str[i]
    i++;
}
```

This pattern is used to iterate over each character in a string until the
null terminator is reached.

### 1. **String Initialization**

Strings in C can be initialized in a few ways:

```c
char str1[] = "Hello, World!";
char str2[20] = "Hello, World!"; // Allows up to 19 characters + null terminator
char *str3 = "Hello, World!"; // Pointer to a string literal
```

### 2. **String Length**

You can determine the length of a string using `strlen()` from the `<string.h>` library:

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "Hello, World!";
    int length = strlen(str);
    printf("Length of string: %d\n", length);
    return 0;
}
```

### 3. **Copying Strings**

To copy one string to another, use `strcpy()` or `strncpy()`:

```c
#include <stdio.h>
#include <string.h>

int main() {
    char src[] = "Hello, World!";
    char dest[20];
    
    strcpy(dest, src); // Copies src to dest
    printf("Copied string: %s\n", dest);
    
    strncpy(dest, src, 5); // Copies first 5 characters of src to dest
    dest[5] = '\0'; // Manually add null terminator
    printf("Copied string: %s\n", dest);
    
    return 0;
}
```

### 4. **Concatenating Strings**

You can concatenate two strings using `strcat()` or `strncat()`:

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[20] = "Hello, ";
    char str2[] = "World!";
    
    strcat(str1, str2); // Appends str2 to str1
    printf("Concatenated string: %s\n", str1);
    
    strncat(str1, str2, 3); // Appends first 3 characters of str2 to str1
    printf("Concatenated string: %s\n", str1);
    
    return 0;
}
```

### 5. **Comparing Strings**

To compare two strings, use `strcmp()` or `strncmp()`:

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "Hello";
    char str2[] = "World";
    
    if (strcmp(str1, str2) == 0) {
        printf("Strings are equal\n");
    } else {
        printf("Strings are not equal\n");
    }
    
    if (strncmp(str1, str2, 3) == 0) {
        printf("First 3 characters are equal\n");
    } else {
        printf("First 3 characters are not equal\n");
    }

    
    return 0;
}
```

### 6. **Finding Substrings**

You can find a substring within a string using `strstr()`:

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "Hello, World!";
    char *sub = strstr(str, "World");
    
    if (sub) {
        printf("Substring found: %s\n", sub);
    } else {
        printf("Substring not found\n");
    }
    
    return 0;
}
```

### 7. **Tokenizing Strings**

You can split a string into tokens using `strtok()`:

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "Hello, World! This is a test.";
    char *token = strtok(str, " ");
    
    while (token != NULL) {
        printf("Token: %s\n", token);
        token = strtok(NULL, " ");
    }
    
    return 0;
}
```

### 8. **Modifying Characters in a String**

You can modify characters in a string directly, as long as it’s not a string literal:

```c
#include <stdio.h>

int main() {
    char str[] = "Hello, World!";
    
    str[7] = 'w'; // Change 'W' to 'w'
    printf("Modified string: %s\n", str);
    
    return 0;
}
```

### 9. **Reversing a String**

Reversing a string can be done by swapping characters from the start and end:

```c
#include <stdio.h>
#include <string.h>

void reverse(char str[]) {
    int n = strlen(str);
    for (int i = 0; i < n / 2; i++) {
        char temp = str[i];
        str[i] = str[n - i - 1];
        str[n - i - 1] = temp;
    }
}

int main() {
    char str[] = "Hello, World!";
    
    reverse(str);
    printf("Reversed string: %s\n", str);
    
    return 0;
}
```

### Summary

- Strings in C are arrays of `char` with a null terminator.
- String operations such as copying, concatenation, and comparison are facilitated by standard library functions.
- Manual manipulation of strings, like reversing or tokenizing, requires understanding of array indexing and loops.

These basic operations cover most string processing tasks in C.
