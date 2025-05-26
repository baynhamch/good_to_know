#Bubble Sort Algorithm

## Python
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

## Java
``` java
public class Sorting {

    public static int[] bubblesort(int[] A) {

        int arr_length = A.length; 

        for (int i = 0; i < arr_length - 1; i++) {

            for (int j = 0; j < arr_length - i - 1; j++) {

                if (A[j] > A[j + 1]) {

                    int temp = A[j];

                    A[j] = A[j +1];
                    A[j + 1] = temp;



                }
                    
            }
        }
        return A;
    }
        public static void main(String[] args) {
    // Sorting sorting = new Sorting();
    int[] myArray = {2, 45, 37, 21, 31, 50, 29, 22, 67, 88, 56};
    System.out.println(myArray);

     int[] bubSort = Sorting.bubblesort(myArray);
     System.out.println(java.util.Arrays.toString(bubSort));

    return;
  }
}

```
