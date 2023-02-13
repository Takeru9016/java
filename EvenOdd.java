class EvenOdd
{
public static void main(String args[])
{
int n[]=new int [args.length];
for(int i=0;i<args.length;i++)
{
n[i]=Integer.parseInt(args[i]);
}
int even=0;
int odd=0;
for(int i=0;i<args.length;i++)
if(n[i]%2 ==0)
{
even++;
}
else 
{
odd++;
}
System.out.println("Even number is ="+even);
System.out.println("Odd number is ="+odd);
}
}