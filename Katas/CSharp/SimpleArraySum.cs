// https://www.hackerrank.com/challenges/simple-array-sum

using System;
public static class SimpleArraySum
{
    private static int FindArraySum(int n, int[] ar)
    {
        int sum = 0;
        foreach (var item in ar)
        {
            sum += item;
        }
        return sum;
    }

    public static void Execute()
    {
        int n = Convert.ToInt32(Console.ReadLine());
        string[] ar_temp = Console.ReadLine().Split(' ');
        int[] ar = Array.ConvertAll(ar_temp, Int32.Parse);
        int result = FindArraySum(n, ar);
        Console.WriteLine(result);
    }
}
