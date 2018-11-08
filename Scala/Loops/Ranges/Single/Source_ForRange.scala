// A For loop with a given Range
// for loop execution using different ranges

// How to run
// Compile using :> scalac [sourcefile].scala
// Run using :> scala [compiledfile]


object ForRangeDemo {
  def main(args: Array[String]) {
    var a = 0;
    var b = 0;

    // for ( Variable generate[or symbol ] Range [to, until]){do stuff}
    for( a <- 1 to 5){
      println( "1 To 5 value of a: " + a );
    }

    for( b <- 1 until 5){
      println( "1 Until 5 value of b: " + b);
    }
  }
}
