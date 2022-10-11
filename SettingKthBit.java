//we have to set the kth bit of a number n as 1 and then display the obtained number.
public class SettingKthBit {
    public static void main(String args[]) {
        int n = 10, k = 3;
        int c = ((k - 1) << 1) | n; // we are doing left shift on 1,(k-1) times, and then taking 'OR' with n.
                                    // This wil perform the given task correctly

        System.out.print("The required output is: ");
        System.out.println(c);

    }
}
