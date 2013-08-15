# Enter your answrs for chapter 6 here
# Name: Amaka Atoyebi


# Ex. 6.6
def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1: -1]

def is_palindrome(word):
	if (first(word) == last(word)):
		print first(word)
		print middle(word)
		print last(word)
		return True
		
	else:
		return False


is_palindrome('redivider')

# Ex 6.8
def gcd(a, b):
	r = a%b
	
	if (b==0):
	 	return a

	if (r==0):
		return b

	if (a<b):
		return gcd(b, a)

	else:	
	 	print r
	 	return gcd(b, r)

gcd(120, 900)	 	