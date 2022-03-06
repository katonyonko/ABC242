import io
import sys

_INPUT = """\
6
4
2
1000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353
  N=int(input())
  dp=[[0]*9 for _ in range(N)]
  dp[0]=[1]*9
  for i in range(N-1):
    for j in range(9):
      if j==0:
        dp[i+1][j]=(dp[i][j]+dp[i][j+1])%mod
      elif j==8:
        dp[i+1][j]=(dp[i][j]+dp[i][j-1])%mod
      else:
        dp[i+1][j]=(dp[i][j]+dp[i][j+1]+dp[i][j-1])%mod
  print(sum(dp[-1])%mod)