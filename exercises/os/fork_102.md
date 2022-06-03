## Fork 101

Answer the questions given the following program (without running it):

```
#include<stdio.h>
#include <unistd.h> 

int main()
{
  fork();
  fork();
  printf("\nyay\n");
  return 0;
}
```

1. How many times the word "yay" will be printed?
2. How many processes will be created?
