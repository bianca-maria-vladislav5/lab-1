'''
Returneaza true daca n este prim si false daca nu.
'''
from math import sqrt

def is_prime(n):
	for num in range(2, int(sqrt(n))):
		if n%num==0:
			return False
	return True	


def is_prime_1(n):
	ii_prim = True
	for num in range(2, int(sqrt(n))):
		if n%num==0:
			ii_prim = False
	return ii_prim

  
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
	p = 1
	for num in lst:
		p=p*num
	return p	
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
	r = x % y
	while r > 0:
		x = y
		y = r
		r = x % y
	return y
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
		while x != y:
			if x > y:
				x -= y
			else:
				y -= x
		return y
  
def main():
  # interfata de tip consola aici
	pass

if __name__ == '__main__':
  main()
