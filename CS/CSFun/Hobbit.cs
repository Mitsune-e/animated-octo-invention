using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace CSFun
{
    internal class Hobbit : Character
    {
        public Hobbit(string name) : base (name, "Hobbit")
        { }

        public void SneakAround ()
            {
            Console.WriteLine($"`{Name} is sneaking around");
            }
           
        public void ChangeName(string newName)
        {
            Name = newName;

        }
        
    }
}
