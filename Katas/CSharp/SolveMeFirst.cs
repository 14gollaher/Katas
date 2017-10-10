// https://www.hackerrank.com/challenges/solve-me-first

using System;
public class SolveMeFirst
{
    public static void Execute()
    {
        int val1 = Convert.ToInt32(Console.ReadLine());
        int val2 = Convert.ToInt32(Console.ReadLine());
        int sum = FindSum(val1, val2);
        Console.WriteLine(sum);
    }
    private static int FindSum(int a, int b)
    {
        return a + b;

    }
}
