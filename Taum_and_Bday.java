import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a = 0; a < t; a++){
            long b = in.nextLong();
            long w = in.nextLong();
            long x = in.nextLong();
            long y = in.nextLong();
            long z = in.nextLong();
            x = x>y? ((x-y>z)? y+z : x) : x;
            y = y>x? ((y-x>z)? x+z : y) : y;
            System.out.println(b*x+w*y);
        }  
    }
}
