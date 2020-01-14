"""
@author: Anirudh Sharma
"""

def isPalindrome(s):
    
    def toChars(s):
        s = s.lower()
        ans = ''
        for char in s:
            if char in 'abcdefghijklmnopqrstuvwxyz':
                ans += char
        return ans
    
    def check(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and check(s[1:-1])
    
    return check(toChars(s))

s = input("Enter a string: ")        
print("Is", s, "palindrome:", isPalindrome(s))