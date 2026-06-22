Console.Write("Enter speed: ");
string raw = Console.ReadLine();
Console.WriteLine(raw);
double speed;
double.TryParse(raw,out speed); // convert the text to a number
Console.WriteLine($"Speed doubled is {speed * 2}");
