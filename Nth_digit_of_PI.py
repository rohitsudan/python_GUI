from decimal import *
getcontext().prec = 25 # sets the precision to 25 digits after the decimal

def factorial(n):
	if n<1:
		return 1
	else:
		return (n*factorial(n-1))

def baileyborwein(n):
	pi = Decimal(0)
	k=0
	while(k<n):
		pi=pi+(Decimal(1)/(16**k))*((Decimal(4)/(8*k+1))-(Decimal(2)/(8*k+4))-(Decimal(1)/(8*k+5))-(Decimal(1)/(8*k+6)))
		k=k+1
	#pi = pi * 1/(2**6)
	return pi

print(baileyborwein(30))

