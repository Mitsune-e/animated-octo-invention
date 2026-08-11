using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSFun
{
    internal class Rock
    {
        private string name;
        private int weight;


        public Rock(string name, int weight)
        {
            this.name = name;
            this.weight = weight;
        }

        public override string ToString()
        {
            return $"Name: {this.name}, Weight: {this.weight}";
        }
    }
}
