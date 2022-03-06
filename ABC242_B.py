import io
import sys

_INPUT = """\
6
aba
zzzz
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=list(input())
  S.sort()
  print(*S,sep='')