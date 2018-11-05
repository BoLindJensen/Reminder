using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

/* 
 * Write a program that prints the numbers from 1 to 100. 
 * But for multiples of three print "Fizz" instead of the number and 
 * for the multiples of five print "Buzz". 
 * For numbers which are multiples of both three and five print "FizzBuzz".

 Solution by Bo Lind Jensen for fun. 

 */

namespace FizzBuzz
{
    class Program
    {
        static void Main(string[] args)
        {
            //  Take 1 (with and wihtout numbers)
 /*            for (int index = 1; index <= 100; index++)
            {
//                if ((index % 5 == 0 && index % 3 == 0)) { Console.WriteLine(index + " FizzBuzz"); continue; }
//                if ((index % 5 == 0)) { Console.WriteLine(index + " Buzz"); continue; }
//                if ((index % 3 == 0)) { Console.WriteLine(index + " Fizz"); continue; }

                if ((index % 5 == 0 && index % 3 == 0)) { Console.WriteLine("FizzBuzz"); continue; }
                if ((index % 5 == 0)) { Console.WriteLine("Buzz"); continue; }
                if ((index % 3 == 0)) { Console.WriteLine("Fizz"); continue; }

                else
                {
                    Console.WriteLine(index);
                }
            }
 */
            // Take 2 (without number but with the multiplier used for the result.)
            for (int i = 1; i < 101; i++) {
                if (i % 15 == 0) { Console.WriteLine("FizzBuzz (15)"); }
                else if (i % 3 == 0) { Console.WriteLine("Fizz (3)"); }
                else if (i % 5 == 0) { Console.WriteLine("Buzz (5)"); }
                else {
                    Console.WriteLine(i);
                }
            }

        // Pause the console window
            Console.ReadLine();
        }
    }
}