using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Swap_Numbers
{
    class TempVarSwap
    {

        public void SwapIntsUsingBufferVariable(int a, int b) { 
//            int a = 5;
//            int b = 10;
            int c = 0;

            Console.WriteLine("Perform Swap of A & B using C variable: ");

            Console.WriteLine("A: " + a);
            Console.WriteLine("B: " + b);
            Console.WriteLine("C: " + c);
            Console.WriteLine("Swapping");

            c = b;  // Temp save
            b = a;  // B becomes A
            a = c;  // A becomes B via C
            c = 0;

            Console.WriteLine("A: " + a);
            Console.WriteLine("B: " + b);
            Console.WriteLine("C: " + c);
        }


        public void SwapIntsUsingSelfe(int a, int b){
            //            int a = 15;
            //            int b = 5;
            Console.WriteLine("Perform Swap of A & B using only A & B variables");
            Console.WriteLine("A: " + a);
            Console.WriteLine("B: " + b);
            Console.WriteLine("Swapping");

            a = a + b;
            b = a - b;
            a = a - b;

            Console.WriteLine("A: " + a);
            Console.WriteLine("B: " + b);
        }


    }
    
}
