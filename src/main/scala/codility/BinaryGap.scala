object Solution {
  def solution(n: Int): Int = {
    val binary = n.toBinaryString
    val gaps = binary.substring(0, binary.lastIndexOf("1"))
      .split("1")
      .map(s => s.length)
    if (gaps.isEmpty) 0 else gaps.max
  }

  def main(args: Array[String]): Unit = {
    println(solution(32))
  }
}
