from typing import List

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  res = 0
  t = 1
  while t < N:
    if t in S:
      res -= (K)
      print(t, res)
      t += (1 + K)
    else:
      res += 1
      print(t, res)
      t += K
  return (int(res))


N = 10
K = 1
M = 2
S = [2, 4]

print(getMaxAdditionalDinersCount(10, 1, 2, [2,6]))
print(getMaxAdditionalDinersCount(15, 2, 3, [11,6,14]))