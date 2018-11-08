// For loop using a list collection as the range to generate values for the variable 'a'

// How to run:
// Compile using :> scalac [sourcefile].scala
// Run using :> scala [compiled file without extension]

object ForListDemo {
  def main(args: Array[String]) {
    var a = 0;
    val numList = List(-1,0,1,2,3,4,5,6);

    for( a <- numList ){
      println( "Value of a: " + a );
    }
  }
}
