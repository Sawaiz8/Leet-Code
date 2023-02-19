def isNotPrime(element, primes):
  for i in range(1, len(primes)):
      if element % primes[i] == 0:
          return True
  return False

def noOfElementsDivisibleByElementExclusively(primes, x, end):
  if x == 0:
      return 0
  if x == 1 or x == 2:
      return 1
  #if denominator > numerator
  if primes[end - 1] >= x: #Check tree: we don't need to do a lot of unnessacary iterations, when we know there is only element that exists
      return 1
  total = x - x // primes[0]
  for i in range(1, end):
      total -= noOfElementsDivisibleByElementExclusively(primes, x//primes[i], i)
  return total

def countPrimes(n):
  if n<=2 : return 0
  odd = True if n % 2 != 0 else False
  n = n - 1 #Remove 1 as prime
  total = n // 2 if odd else n//2 + 1 
  primes = list()
  primes.append(2)
  
  for element in range(3,n//2,2):
      if element > 7 and isNotPrime(element, primes):
          continue
      noOfElementsDivisibleByElement = n//element
      remover = noOfElementsDivisibleByElementExclusively(primes, noOfElementsDivisibleByElement, len(primes))
      if remover == 1:#If remover is one then that means that prime doesn't act as a factor in another number till n
          break
      total = total - (remover - 1) #-1 from remover since we have to exclude the prime we just found from that list
      primes.append(element)
  print(len(primes))
  return total   
x = 5000000000
print(countPrimes(x))

#Better Solution from leetcode
'''
def countPrimes(n):
  n -= 1
  if n < 2:
      return 0
  r = int(n ** 0.5)
  V = [n//d for d in range(1, r + 1)]
  V += list(range(V[-1] - 1, 0, -1))
      
  S = {v: v - 1 for v in V}
  for p in range(2, r + 1):
      if S[p] == S[p - 1]:
          continue
      p2 = p * p
      sp_1 = S[p - 1]
      for v in V:
          if v < p2:
              break
          S[v] -= S[v//p] - sp_1
  return S[n]

x = 5000000000
print(countPrimes(x))
'''
