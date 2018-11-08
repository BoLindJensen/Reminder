// A For loop used in conjunction with 'yield [loop variable]' to assign return values to another variable,

object ForListConditionYieldDemo {
  def main(args: Array[String]) {
    var a = 0;
    var numList = List(-1,0,1,2,3,4,5,6,7,8);


    var yieldResults = for{ a <- numList if a != -1 ; if a != 3 ; if a <= 5 }yield a
    // returned values from the for loop contains 0,1,2,4,5

    // Now print returned values using another loop.
    for( a <- yieldResults){
      println( "Value of a: " + a );
    }

  }
}
