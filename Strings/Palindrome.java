package com.jdsa.strings;

public class Palindrome {

	public static boolean checkPalindrome(String str) {
		int start = 0;
		int end = str.length() - 1;
		while (start < end) {
			if (str.charAt(start) != str.charAt(end))
				return false;
			start++;
			end--;
		}
		return true;
	}

	public static void main(String[] args) {
		String str = "abcdcba";
		System.out.println(checkPalindrome(str));
	}

}
