import io
import sys

_INPUT = """\
6
ABC
4
0 1
1 1
1 3
1 6
CBBAACCCCC
5
57530144230160008 659279164847814847
29622990657296329 861239705300265164
509705228051901259 994708708957785197
176678501072691541 655134104344481648
827291290937314275 407121144297426665
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  Q=int(input())
  X={'A':0, 'B':1, 'C':2}
  Y={0:'A', 1:'B', 2:'C'}
  def solve(t,k):
    if t>60:
      if k==0:
        return (X[S[0]]+t)%3
      else:
        if k%2==0:
          return (solve(t-1,k//2)+1)%3
        else:
          return (solve(t-1,k//2)+2)%3
    elif t>0:
      if k%2==0:
        return (solve(t-1,k//2)+1)%3
      else:
        return (solve(t-1,k//2)+2)%3
    else:
      return X[S[k]]
  for i in range(Q):
    t,k=map(int,input().split())
    k-=1
    print(Y[solve(t,k)])