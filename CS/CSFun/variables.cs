using System;

Console.WriteLine("Hello, Middle Earth!");

// _, letters, numbers
int age = 23;
string name = "Frodo";

bool isHero = true;
double height = 1.4536; 
float weight = 25.6f;


Console.WriteLine($"{name} is {age} years old.\nisHero:{isHero} weight:{weight} height:{height}");

isHero = false;

Console.WriteLine($"{isHero}");

const int SPEED = 3;

Console.WriteLine($"{SPEED}");