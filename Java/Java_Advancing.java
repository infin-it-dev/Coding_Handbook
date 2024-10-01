package Java;
import java.util.Scanner;


public class Java_Advancing {

public static void main (String [] args) {
    System.out.println("Lets try a Scanner!");

    System.out.println("What is your name?");



    Scanner name = new Scanner (System.in);


    String nameString = name.nextLine();


    System.out.println("Your name is " + nameString + "!");


}

}


