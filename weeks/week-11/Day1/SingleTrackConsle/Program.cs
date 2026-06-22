using System;
using System.ComponentModel.Design;

namespace Project
{
    class SingleTrack
    {
        static void Main()
        {
            // define basic varibles  needed
            string errorTitle = "===== error ====\n";
            bool hasValid = false;
            int singleID = 0;
            int speed = 0;
            int degrees = 0;
            string status = "";


            // take id
            while (hasValid == false)
            {
                Console.WriteLine("enter Track ID");
                string userInput = Console.ReadLine();
                bool valid = int.TryParse(userInput, out singleID);
                if (valid)
                {
                    hasValid = true;
                } 
                else
                {
                    Console.WriteLine($"{errorTitle}you must enter id as int but got {userInput}");

                }
            

            }
            // take speed
            hasValid = false;
            while (hasValid == false)
            {
                Console.WriteLine("enter Speed per hour");
                string userInput = Console.ReadLine();
                bool valid = int.TryParse(userInput, out speed);
                if (valid)
                {
                    hasValid = true;
                }
                else
                {
                    Console.WriteLine($"{errorTitle}you must enter speed as int but got {userInput}");
                }
            }
            // take degreees
            hasValid = false;
            while (hasValid == false)
            {
                Console.WriteLine("enter Heading as degrees (0-359)");
                string userInput = Console.ReadLine();
                bool valid = int.TryParse(userInput, out degrees);
                if (valid)
                {
                    if (degrees > 359 || degrees < 0) 
                    {
                        Console.WriteLine($"{errorTitle}degrees must be betweeen 0-359, but got {degrees}");
                    }
                    else
                    {
                        hasValid = true;
                    }
                }
                else
                {
                    Console.WriteLine($"{errorTitle}you must enter speed as int but got {userInput}");
                }
                

            }
            // take status
            hasValid = false;
            string[] validStatus = { "cruising", "turning", "stopped", "accelerating" };
            while (!hasValid)
            {
                Console.WriteLine($"enter your status ({string.Join(",", validStatus)})");
                string userInput = Console.ReadLine();
                foreach (string s in validStatus)
                {
                    if (s == userInput.ToLower())
                    {
                        hasValid = true;
                        status = s;
                        break;
                    }
                  
                        
                }
                if (!hasValid)
                {
                    Console.WriteLine($"{errorTitle}status must be in {string.Join(",", validStatus)} but got {userInput}");
                }
                 
            }
            // calaulation

            // speed category
            string speedCategory;
            if (speed >= 300)
            {
                speedCategory = "fast";
            }
            else if (speed >= 100)
            {
                speedCategory = "medioum";
            }
            else
            {
                speedCategory = "slow";
            }
            // demo 2
            int intDemo2 = degrees/60;
            double dubleDemo2 = (double) speed / 60;

            // show the report 
            string report = $"=== Track Report === \r\n" +
                $"Track ID: {singleID} \r\n" +
                $"Speed: {speed} km/h ({speedCategory}) \r\n" +
                $"Heading: {degrees} degrees \r\n" +
                $"Status: {status} \r\n" +
                $"Division Demo 1: {degrees}/30 = {degrees/30} (int) | {(double)degrees/30} (double) \r\n" +
                $"Division Demo 2: {speed}/60 = {speed/60} (int) | {dubleDemo2} (double) \r\n";
            Console.WriteLine(report);










        }
        


    }
}