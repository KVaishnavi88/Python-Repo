import java.util.Scanner;
public class share
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int x=sc.nextInt();
        int y=sc.nextInt();
        int total=((x*1)+(y*2));
        if(total%2!=0){
            System.out.println("NO");
        }
        else{
           int hv=total/2;
           if(hv<=total && hv%2<=x)
           {
              System.out.println("YES");
           }
           else{
            System.out.println("NO");
           }
        }
    }
}