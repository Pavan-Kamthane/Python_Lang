public class OddEven {
        public static void main(String[] args) {
         int n = 68;
            System.out.println(isOdd(n));
        }

        //Using bitwise Operator any number AND with 1 gives that number only
        //if there is one it means its a odd otherwise its a even
        //output true == odd number
        //output false == even number
    private static boolean isOdd(int n) {
            return (n & 1) == 1;
    }
}
