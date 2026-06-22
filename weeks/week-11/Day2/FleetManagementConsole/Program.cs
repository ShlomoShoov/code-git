using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.Design;

class FleetManagement
/*
 * This class manage the Fleet flowing system
 * using the Console, the user able to add data
 * get data, filter search and ger statistics.
 */
{

    const int IndexID = 0;
    const int IndexSpeed = 1;
    const int IndexHeading = 2;

    static void Menu(List<int[]> tracks)
    {
        bool isRunning = true;
        while (isRunning)
        {
            int userChoice = GetChoice();
            switch (userChoice) {
                case 0:
                    Console.WriteLine("good bye!");
                    isRunning = false;
                    break;
                case 1:
                    Display(tracks);
                    break;
                case 2:
                    int id = GetNumber("Enter your id");
                    Display(tracks, id);
                    break;

                case 3:
                    int speed = GetNumber("Enter the speed:");
                    FilterBySpeed(tracks, speed);
                    break;
                case 4:
                    int heading = GetNumber("Enter the heading (0-359)", 0, 359);
                    FilterByHeading(tracks, heading);
                    break;
                case 5:
                    GetSummary(tracks);
                    break;
            }
        }
    }
    static int GetChoice()
    {
        string menu = "===== welcome =====\n" +
            "1. Show all\n" +
            "2. Show by id\n" +
            "3. Filter by speed\n" +
            "4. Filter by heading\n" +
            "5. Get report\n" +
            "0. Exit";
        Console.WriteLine(menu);
        int userInput = GetNumber("Enter your choice...", 0, 5);
        return userInput;
    }
    
    static void Display(List<int[]> tracks)
    {
        if (tracks.Count == 0) Console.WriteLine("There is no Tracks!");
        for (int i = 0; i<tracks.Count; i++)
        {
            DisplayTrcak(tracks, i);
        }
    }
    static void Display(List<int[]> tracks, int id)
    {
        int index = GetIndex(tracks, id);
        if (index >= 0) DisplayTrcak(tracks, index);
        else Console.WriteLine($"{id} Not exists");

    }

    static void FilterBySpeed(List<int[]> tracks, int speed)
    {
        List<int> filteredIndexes = [];
        for (int i = 0; i<tracks.Count; i++)
        {
            if (tracks[i][IndexSpeed] == speed) filteredIndexes.Add(i);
        }
        DispalyTracksByIndex(tracks, filteredIndexes);
    }

    static void FilterByHeading(List<int[]> tracks , int heading)
    {
        List<int> indexes = [];
        for (int i=0; i<tracks.Count; i++)
        {
            if (tracks[i][IndexHeading] == heading) indexes.Add(i);
        }
        DispalyTracksByIndex(tracks, indexes);
    }

    static void GetSummary(List<int[]> tracks)
    {
        Console.WriteLine($"Average speed: {GetAvg(tracks)}\n" +
            $"Maximum speed is of id: {GetFaster(tracks)}\n" +
            $"Count of all of tracks {tracks.Count}");
    }

    static float GetAvg(List<int[]> tracks)
    {
        int sum = 0;
        if (tracks.Count == 0) return 0.0f;
        for (int i = 0; i<tracks.Count; i++)
        {
            sum += tracks[i][IndexSpeed];
        }
        return (float)sum / tracks.Count;
    }
    static int? GetFaster(List<int[]> tracks)
    {
        int maxSpeed = 0;
        int? maxIndex = null;
        for (int i= 0; i<tracks.Count; i++)
        {
            if (tracks[i][IndexSpeed] > maxSpeed)
            {
                maxSpeed = tracks[i][IndexSpeed];
                maxIndex = tracks[i][IndexID];
            }
            
        }
        return maxIndex;

    }
    static void DispalyTracksByIndex(List<int[]> tracks, List<int> indexes)
    {
        foreach (int i in indexes)
        {
            DisplayTrcak(tracks, i);
        }
    }

    static int GetIndex(List<int[]> tracks, int id)
    {
        for (int i=0; i<tracks.Count; i++)
        {
            if (tracks[i][IndexID] == id) return i;
            
        }
        return -1;
    }

    static void DisplayTrcak(List<int[]> tracks, int i)
    {
        Console.WriteLine($"ID: {tracks[i][IndexID]}|Speed:{tracks[i][IndexSpeed]}|Heading:{tracks[i][IndexHeading]}");
    }

    static int GetNumber(string msg)
    {
        bool gotValid = false;
        int userNumber = 0;
        while (!gotValid)
        {
            Console.WriteLine(msg);
            bool valid = int.TryParse(Console.ReadLine(), out userNumber);
            if (valid) gotValid = true;
            else Console.WriteLine("=====Error====\n must got int");
        }
        return userNumber;
    }
    static int GetNumber(string msg, int minVal, int maxVal)
    {
        bool isValid = false;
        int userNumber = 0;
        while (!isValid)
        {
            userNumber = GetNumber(msg);
            if (userNumber >= minVal && userNumber <= maxVal) isValid = true;
            else Console.WriteLine($"===Error===\nNumber must be between {minVal} to {maxVal}");
        }
        return userNumber;
    }
    static void Main()
    {

        List<int[]> tracks = [];
        int[] track = { 1, 150, 90 };
        int[] track2 = { 2, 185, 90 };

        tracks.Add(track);
        tracks.Add(track2);
        Menu(tracks);

    }
}