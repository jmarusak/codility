object Solution {
  def solution(n: Int): Int = {
    val binary = n.toBinaryString
    val gaps = binary.substring(0, binary.lastIndexOf("1"))
      .split("1")
      .map(_.length)
    if (gaps.isEmpty) 0 else gaps.max