package knappPreparationArrays;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sid = new Scanner(System.in);
		
		System.out.print("What are you trying to find: ");
		int findItem = sid.nextInt();
		
		int[] arrayOne = {11, 1, 2, 12, 64, 67, 34256, 34567, 345, 2345, 45678 ,3456, 234, 111, 2904};
		
		System.out.println("");
		
		for (int i = 0; i < arrayOne.length; i++) {
			if (arrayOne[i] == findItem) {
				System.out.println("Itam found! = " + arrayOne[i] + ", at position = " + i);
				break;
			}
			else if (arrayOne[i] != findItem) {
				System.out.println(i + " Searching...");
				if (i == arrayOne.length - 1) {
					System.out.println("Cannot be found..");	
				}
			}
		}
	}
}
