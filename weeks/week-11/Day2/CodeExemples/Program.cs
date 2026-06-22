using System;

class Example {
    static List<int> speeds = new();
    static void Main()
    {
        int[] ids = new int[3];
        
        Console.WriteLine(string.Join(",",new int[3]));
        Console.Write(ids.Length);
        Console.Write(string.Join("," ,ids));

        List<double> speeds  = new List<double>();
        speeds.Add(7);
        Console.WriteLine($"count of sppeed: {speeds.Count}");
        speeds.Remove(1);

        Console.WriteLine($"count of sppeed: {speeds.Count}");

        Console.WriteLine($"speed in the firest index= {speeds[0]}");

        Console.WriteLine( myFirstFunction(7));

    }
    
    static int myFirstFunction(int num)
    {

        Proccess("hello",3,5);
        return 7;
    }

    static void Proccess(string s, params int[] nums)
    {
        Console.WriteLine($"{string.Join(",", nums)},{s}");
        foreach (int str in nums) Console.WriteLine(str);
        for (int i = 0; i < nums.Length+1; i+=1)
            Console.WriteLine(nums[i]);
        
          
        
    }

}


