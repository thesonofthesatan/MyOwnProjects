import java.util.*;
public class dailyProduction {
   public static void main(String[] args) {
      Scanner scn = new Scanner(System.in); //scn = scanner
      
      //Asking for input
      System.out.print("Enter Cycle time in Seconds: ");
      float cycTim = scn.nextFloat();
      System.out.print("Enter percentage to be accounted: ");
      float perc = scn.nextFloat(); // perc = percent
      
      //Generating formula
      float num1 = (cycTim / 60); // converting seconds to minutes
      float num2 = (60 / num1); //converting minuts to hour
      float num3 = (num2 * perc / 100); //with 90 percentage
      
      //Printing results out
      System.out.println("");
      System.out.println("Production per hour: " + num3);
      System.out.println("Production per shift: " + (num3 * 10.5));
   }
}
