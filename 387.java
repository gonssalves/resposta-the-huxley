import java.io.*;
import java.util.*;

public class HuxleyCode {
  public static void main(String args[]) {
    Scanner in = new Scanner(System.in); 
	int a = in.nextInt();
	int b = in.nextInt();
	int c = in.nextInt();
	int d = in.nextInt();
	int e = in.nextInt();
	
	if(a > b && b > c && c > d && d > e){
	    System.out.print("D");
	    
	}else if(a < b && b < c && c < d && d < e){
	    System.out.print("C");
	}else{
	    System.out.print("N");
	}
  }
}
