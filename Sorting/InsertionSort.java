/* About-: This is an in-place comparison-based sorting algorithm. Here, a sub-list is maintained which is always
  sorted. For example, the lower part of an array is maintained to be sorted. An element which is to be 'insert'ed 
 in this sorted sub-list, has to find its appropriate place and then it has to be inserted there. Hence the name, 
 insertion sort */

package Sorting;

import java.util.Arrays;

public class InsertionSort {
    public static void main(String[] args) {
        int[] arr = { 5, 3, 4, 1, 2 };
        insertion(arr);
        System.out.println(Arrays.toString(arr));
    }

    static void insertion(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = i + 1; j > 0; j--) {
                if (arr[j] < arr[j - 1]) {
                    swap(arr, j, j - 1);
                } else {
                    break;
                }
            }
        }
    }

    static void swap(int[] arr, int first, int second) {
        int temp = arr[first];
        arr[first] = arr[second];
        arr[second] = temp;
    }
}