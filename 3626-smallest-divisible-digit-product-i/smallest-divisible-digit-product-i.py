class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        q,r=divmod(n,10)
        re=t// gcd(max(q,1),t)
        n=((r+re-1)//re)*re
        x=n-(n-10)*(n//10)
        return q*10+x
        