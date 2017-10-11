import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for (int i=0; i<t; i++){
            int n = scanner.nextInt();
            int[] a = new int[n];
            for (int j=0; j<n; j++){
                a[j]=scanner.nextInt();
            }
            bubleSort(a,n);
            System.out.println(a[n-2]<a[n-1]?"YES":"NO");
        }
    }
    
    public static void bubleSort(int[] array, int n){
        for (int i=0; i<n-2; i++){
            for (int j=n-2-1; j>=i; j--){
                while (array[j]>array[j+1]||array[j]>array[j+2]) {
                    rotate(array,j);
                }
            }
        }
    }
    
    public static void rotate(int[] arr, int a){
        int temp = arr[a];
        arr[a] = arr[a+1];
        arr[a+1] = arr[a+2];
        arr[a+2] = temp;
    }
}
