import io
import sys

_INPUT = """\
6
5
3
AXA
6
ABCZAZ
30
QWERTYUIOPASDFGHJKLZXCVBNMQWER
28
JVIISNEOXHSNEAAENSHXOENSIIVJ
31
KVOHEEMSOZZASHENDIGOJRTJVMVSDWW
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import deque
  mod=998244353
  z=[pow(26,i,mod) for i in range(10**6)]
  T=int(input())
  for _ in range(T):
    N=int(input())
    S=input()
    l=len(S)%2
    if l==0:
      i,j=len(S)//2-1,len(S)//2
    else:
      i,j=len(S)//2-1,len(S)//2+1
    while i>=0 and S[i]==S[j]:
      l+=2
      i-=1
      j+=1
    ans=0
    S=deque(S)
    while len(S)>1:
      x=S.popleft()
      y=S.pop()
      ans=(ans+(ord(x)-ord('A'))*z[(len(S)+1)//2])%mod
      if ord(x)>ord(y) and len(S)<=l:
        ans=(ans-1)%mod
    if len(S)==0:
      ans=(ans+1)%mod
    elif len(S)==1:
      ans=(ans+ord(S[0])-ord('A')+1)%mod
    print(ans)