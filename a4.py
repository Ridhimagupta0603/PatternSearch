

from ast import mod
import random
import math

#To generate random prime less than N
def randPrime(N):
	primes = []
	for q in range(2,N+1):
		if(isPrime(q)):
			primes.append(q)
	return primes[random.randint(0,len(primes)-1)]

# To check if a number is prime

def isPrime(q):
	if(q > 1):
		for i in range(2, int(math.sqrt(q)) + 1):
			if (q % i == 0):
				return False
		return True
	else:
		return False

#pattern matching
#since q is less than N and N is O(log(m/ε)) bits so wherever we are encountering q we can write the space and time complexity to be  O(log(m/ε)) bits in place of O(logq) bits
def randPatternMatch(eps,p,x): #run in time O(m + n) log (m/ε) and use O(k + log n +log(m/ε)) working spacesince O(log (m/ε))+O(m + n) log (q) -->O(m + n) log (m/ε) time 
	N = findN(eps,len(p)) #O(log (m/ε)) time and space
	q = randPrime(N)
	return modPatternMatch(q,p,x)#O(m + n) log (q)  time, use O(k + log n+ log q) working memory

#pattern matching with wildcard
def randPatternMatchWildcard(eps,p,x):#) runs in time O(m + n) log m/ε uses O(k + log n +log(m/ε)) working space
	N = findN(eps,len(p)) #O(log (m/ε)) time and space
	q = randPrime(N)
	return modPatternMatchWildcard(q,p,x) #O(m + n) log (q)  time ,use O(k + log n+ log q) working memory

# return appropriate N that satisfies the error bounds
"""
let p denote pattern and x denote substring
p!=x,   f(p)modq=f(x)modq --> diff=f(p)-f(q) mod q ==0;
diff is atmost 26**m so since The number of prime factors of diff is at most log2 26**m=mlog2 26 or atmost mlog2 32 or 5m-->let it be a
now the total number of primes less than N are π(N) ≥N/2 log2 N
probability eps==a/π(N)N--> 5m* log2 N/N <=eps 
if we chose N =⌈5(m/eps) lg(m/eps)⌉ then the Pr(fp=fq) but p(pattern)!=x(substring) is eps
as 5m*log2 N/⌈5(m/eps) lg(m/eps)⌉<=eps .Thus We take, N =⌈5(m/eps) lg(m/eps)⌉--> ceil function to take the higher integer value.

"""
def findN(eps,m):
	#print(math.ceil(5*m*(math.log2(m//eps))//eps))
	return math.ceil(2*5*m*(math.log2(5*m//eps))//eps)

def ordi(s):
	if s=='?':
		return 0
	else:
		return(ord(s)-65)
def pow26(power,q):
	return (26**(power))%q

# Return sorted list of starting indices where p matches x

def modPatternMatch(q,p,x):# run in time O(m +n) log q and use O(k + log n+ log q) working memory
	occur=[]
	m=len(p)
	n=len(x)
	fp=0
	fq=0
	pow26m=pow26(m-1,q)
	
	for i in range(m):#runs in O(mlogq)time , log q for arithmetic operations. takes O(loq+logn) working memory
		
		fp = (26*fp + ordi(p[i])) % q
		fq = (26*fq + ordi(x[i])) % q
	
	i=0
	while i < n-m+1:#O(nlogq) time logq for arithmetic operations
		if fq==fp:#if the hash value is same we append that index O(1) time
			occur.append(i)
		if i+m<n:#update the hash value by subtracting the ith ord value and adding the i+m th ord value #takes O(logq+logn) working memory 
			
			fq= (26*(fq-ordi(x[i])*(pow26m)) + ordi(x[i+m])) % q
		i+=1
	#print(occur)#O(k) working memory
	return occur #O(k) working memory
def modPatternMatchWildcard(q,p,x):# run in time O(m +n) log q and use O(k + log n+ log q) working memory
	occur=[]
	m=len(p)
	n=len(x)
	fp=0
	fq=0
	
	pow26m=pow26(m-1,q) #O(logq) bits and time
	for i in range(m):#runs in O(mlogq)time , log q for arithmetic operations. takes O(loq+logn) working memory
		if p[i]=='?':
			j=i
			
		fp = (26*fp + ordi(p[i])) % q
		fq = (26*fq + ordi(x[i])) % q
	pow26j=pow26(m-1-j,q) #O(logq) bits and time
	fp=(fp+(26**(m-1-j))*(ordi(x[j])))%q # takes O(logq) time and O(logq) space
	i=0
	while i < n-m+1:#O(nlogq) time logq for arithmetic operations
		if fq==fp:#if the hash value is same we append that index O(1) time
			occur.append(i)
		if i+m<n and i+j+1<n:#update the hash value by subtracting the ith ord value and adding the i+m th ord value 
			#takes O(logq+logn) working memory
			#also update the pattern hash value  
			
			fp=(fp+(pow26j)*(ordi(x[i+j+1])-ordi(x[i+j])))%q #O(logq ) space and O(logq time)
			
			fq= (26*(fq-ordi(x[i])*(pow26m)) + ordi(x[i+m])) % q  #O(logq ) space and O(logq time)

			
		i+=1
	#print(occur)#O(k) working memory
	return occur #O(k) working memory 
