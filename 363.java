import java.io.*;
import java.util.*;

public class HuxleyCode {
  public static void main(String args[]) {
    Scanner myObj = new Scanner(System.in);
    char c;
    
    System.out.print("");

    int i1 = myObj.nextInt();
    
    System.out.print("");
    
    int i2 = myObj.nextInt();
    
    c = myObj.next().charAt(0);
    
    int i3 = myObj.nextInt();

    
    if(c == '+'){
        int total = i2 + i3;
         if(total > i1){
            System.out.print("OVERFLOW\n");
        }else{
            System.out.print("OK");
        
        } 
        
    
     
    }else{
        int total = i2 * i3;
         if(total > i1){
            System.out.print("OVERFLOW\n");
        }else{
            System.out.print("OK");
        } 
        
    }
  }
}
