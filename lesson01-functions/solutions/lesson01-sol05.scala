// ------------- Lesson 01 Functions - Exercise 5 -------------
object Lesson01Sol05 {

  // 1. Write a function called factorial that takes an integer n and returns the factorial of n.
  // If n is less than 1, return 1.

  def factorial(n: Int): Int = {
    if (n <= 1) 1
    else n * factorial(n - 1)
  }

  // 2. Write a function called listSum that takes a list of integers and returns the sum of all the elements in the list.

  def listSum(list: List[Int]): Int = {
    list match {
      case Nil => 0
        case head :: tail => head + listSum(tail)
    }
  }

  // 3. Write a function called listMax that takes a list of integers and returns the maximum element in the list.
  // If the list is empty, throw an error using the following code: throw new IllegalArgumentException("Empty list")

  def listMax(list: List[Int]): Int = {
    list match {
      case Nil => throw new IllegalArgumentException("Empty list")
      case head :: Nil => head
      case head :: head2 :: tail => if (head > head2) listMax(head::tail) else listMax(head2::tail) 
    }
  }

  // 4. Write a function called evensInList that takes a list of integers and returns a new list containing only the even numbers from the original list.

  def evensInList(list: List[Int]): List[Int] = {
    list match {
      case Nil => Nil
        case head :: tail =>
        if (head % 2 == 0) head :: evensInList(tail)
        else evensInList(tail)
    }
  }

  // -------- Tests --------
  def main(args: Array[String]): Unit = {
    // Test factorial
    assert(factorial(0) == 1)
      assert(factorial(1) == 1)
      assert(factorial(5) == 120)
      assert(factorial(10) == 3628800)
      assert(factorial(-1) == 1)


      // Test listSum
      assert(listSum(List(1, 2, 3, 4, 5)) == 15)
      assert(listSum(List(-1, -2, -3, -4, -5)) == -15)
      assert(listSum(List(0, 0, 0)) == 0)
      assert(listSum(List()) == 0)

      // Test listMax
      assert(listMax(List(1, 2, 3, 4, 5)) == 5)
      assert(listMax(List(-1, -2, -3, -4, -5)) == -1)
      assert(listMax(List(0, 0, 0)) == 0)
      try {
        listMax(List())
      } catch {
        case e: IllegalArgumentException => assert(e.getMessage == "Empty list")
      }

    // Test evensInList
    assert(evensInList(List(1, 2, 3, 4, 5)) == List(2, 4))
      assert(evensInList(List(-1, -2, -3, -4, -5)) == List(-2, -4))
      assert(evensInList(List(0, 0, 0)) == List(0, 0, 0))

      println("All tests passed!")
  }
}
