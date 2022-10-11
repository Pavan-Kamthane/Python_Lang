package com.practice.strings;

public class ReverseString {

	public static String reverse(String str) {
		int n = str.length();

		char[] charArr = str.toCharArray();
		for (int i = 0; i < n / 2; i++) {
			char temp = charArr[i];
			charArr[i] = charArr[n - 1 - i];
			charArr[n - 1 - i] = temp;
		}
		return String.valueOf(charArr);
	}

	public static void main(String[] args) {
		String str = "Hello World";
		String reverseStr = reverse(str);
		System.out.println("Reverse of Str: " + reverseStr);
	}

}
