using System;

namespace Examples
{
    class Examples
    {
        enum Level
        {
            Low,
            Medium
        }
       static void Main()

        {
            Level myVar = Level.Medium;
            Console.WriteLine(myVar);
            int n  = 0;
            Try(out n);
            Console.WriteLine(n);
            int? nn = null;
            Console.WriteLine(nn ?? 7);
            //int* r = &n;
            }
        
        static void Try(out int num)
        {
            num = 4;
        }

    }
}

