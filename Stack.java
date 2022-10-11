import java.io.*;
import java.util.*;
import java.util.Collections;

class Nightwemet
{
    public static void main(String args[])throws IOException
    {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int i;
        while(a > 0)
        {
            int N = sc.nextInt();
            int arr[] = new int[N];
            for(i = 0; i < N; i++)
                arr[i] = sc.nextInt();
            Solution ob = new Solution();
            int ans = ob.minSubset(arr,N);
            System.out.println(ans);
            a--;
        }
    }
}
class Solution { 

    int minSubset(int[] Arr,int N) 

    { 

     long sum=0;

     for(int i=0;i<Arr.length;i++)

     sum+=Arr[i];

     

     Arrays.sort(Arr);

     long curr=0;

     int cnt=0;

     for(int j=Arr.length-1;j>=0;j--)

     {

         curr+=Arr[j];

         if(curr>(sum-curr))

         break;

         cnt++;

     }

     return cnt+1;

     

    }

}