// A for loop which loops over multiple ranges

// How to run:
// Compile using :> scalac [sourcefile].scala
// Run using :> scala [compiled file without extension]


object MultiRangeDemo {
  def main(args: Array[String]) {
    var a = 0;
    var b = 0;

    // for ( Variable generator Range; Variable generator Range) {do stuff}
    for( a <- 1 to 3; b <- 1 to 3){
      println( "a: " + a );
      println( "b: " + b );
    }
  }
}
