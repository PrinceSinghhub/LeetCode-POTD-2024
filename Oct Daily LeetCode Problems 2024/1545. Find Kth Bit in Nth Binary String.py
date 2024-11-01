class Solution:
	def invert(self, s):
		res=""
		for i in s:
			if i=='0':
				res+='1'
			else:
				res+='0'
		return res[::-1]

	def findbits(self, n):
		if n==0:
			return '0'
		si1=self.findbits(n-1)
		si1r=self.invert(si1)
		si=si1+'1'+si1r
		return si

	def findKthBit(self, n: int, k: int):
		s=self.findbits(n)
		return s[k-1]