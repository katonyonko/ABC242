import io
import sys

_INPUT = """\
6
30 500 20 103
50 500 100 1
1 2 1 1000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  A,B,C,X=map(int,input().split())
  if X<=A:
    print(1)
  elif X<=B:
    print(C/(B-A))
  else:
    print(0)