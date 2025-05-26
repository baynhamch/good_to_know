

```Python
def bubblesort(A):
    for i in range(len(A) - 1):
        for j in range(len(A) - i - 1):
            if (A[j] > A[j + 1]):
                A[j], A[j+1] = A[j +1], A[j]



A = list(range(1000))
shuffle(A)
bubblesort(A)
print(A)
```

``` java
```
