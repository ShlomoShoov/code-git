using System;
using System.Runtime.CompilerServices;



public class Track
{
    public int Id { get; set;}
    public double Speed;
    private double _heading;

    public double Heading
    {
        get { return _heading; }
        set
        {
            if (value < 0 || value > 359) _heading = 0;
            else _heading = value;
        }
    }

    public Track(int id, double speed)
    {
        Id = id;
        Speed = speed;
        Console.WriteLine("cons run 1");
        Console.WriteLine($"Inside constructor -> Property Id: {this.Id}, Field Speed: {this.Speed}");
    }

    public Track() : this(7,83)
    {
        Console.WriteLine($"hello from cons 2");
        
    }
}

class Projram
{
    static void Main()
    {
        Track a = new Track();
        Track b = new Track();
        Console.WriteLine($"{a.Id}:{a.Speed}");
        a.Id = 5;
        
        a.Heading = 200;
        Console.WriteLine($"{a.Id}:{a.Speed}:{a.Heading}");

    }
}