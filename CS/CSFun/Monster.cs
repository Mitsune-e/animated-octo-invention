using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace CSFun
{
    internal class Monster : Character
    {
        public Monster(string name) : base(name, "Monster") { }


        public override void Introduce()
        {

            Console.WriteLine($" I am a fearful Monster {Name}");
        }
    }
}
