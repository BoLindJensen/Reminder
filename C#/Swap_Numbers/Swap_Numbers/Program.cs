using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Swap_Numbers
{
    class Program
    {
        static void Main(string[] args)
        {
            TempVarSwap swaps = new TempVarSwap();

            swaps.SwapIntsUsingSelfe(5,10);
            Console.WriteLine("");
            swaps.SwapIntsUsingBufferVariable(5,10);

            
            //Pause Console
            Console.ReadKey();

        }
    }
}
