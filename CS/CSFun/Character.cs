using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSFun
{
    
    internal class Character
    {
        public static int Count = 0;

        public string Name { get; protected set; }
        public string Race { get; protected set; }
        
        public Character (string  name, string race)
        {
            Name = name;
            Race = race;
            Count++;    
        }

        public virtual void Introduce()
        {
            Console.WriteLine($"I am {Name}, a {Race}.");
        }

        public static void CountCharacters()
        {

            Console.WriteLine($"There are {Count} characters.");
        }
    }
}
