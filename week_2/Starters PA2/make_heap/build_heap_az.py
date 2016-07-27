# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    assert (n >= 1) and (n <= 100000)
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def LeftChild(self,i):
    return 2*i

  def RightChild(self,i):
    return 2*i + 1

  def swap(self,idx1, idx2):
    self._data[idx1], self._data[idx2] = self._data[idx2], self._data[idx1]

  def SiftDown(self, index):
    max_index = index
    array_length = len(self._data) - 1
    # NOTE function count for numbers 1..n.
    # And we have 0-based index and need to explicitly add +1
    # to keep indces consistent.
    l = self.LeftChild(index) + 1 
    if (l <= array_length) and (self._data[l] < self._data[max_index]):
      max_index = l

    # NOTE function count for numbers 1..n.
    # And we have 0-based index and need to explicitly add +1
    # to keep indces consistent.
    r = self.RightChild(index) + 1
    if (r <= array_length) and (self._data[r] < self._data[max_index]):
      max_index = r

    if index != max_index:
      self._swaps.append([index, max_index])
      self.swap(index, max_index)
      self.SiftDown(max_index)

  def GenerateSwaps(self):
    size = len(self._data) // 2
    for i in range(size,0,-1):
      # i - 1 since python generates
      # [3,2,1], not [2,1,0] indexes when
      # going backwards
      self.SiftDown(i-1)

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
