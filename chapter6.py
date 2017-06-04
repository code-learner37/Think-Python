# 4 - 6 - 2017
# Chapter 6

# 6-1
''' The program prints 9 90 8100
    it sums the values of all arugments in function c and then times it by 10,
    and finally return the sqaure of it.
'''

# 6-2 Ackermann function

def ack(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ack(m - 1, 1)
    if m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))

# 6-3

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(s):
    
    if len(s) <= 1: # didn't think of this! I thought of modifying the middle function to accept odd number digits
        return True

    if first(s) == last(s):
        return is_palindrome(middle(s)) 
    else:                                 
        return False
    
'''
    Q1: They all return empty string '' when the middle function is called with
    a string with 2 letters, 1 letter, or an empty string.

'''

# 6-4

def is_power(a, b):
    if a == b:
        return True
    if a % b == 0:
        return is_power(a/b, b) # once again, I forgot to add "return" at the front
    else:
        return False
    
# 6-5

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)
