import re

def is_palindrome(s):
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    print(cleaned)
    print(cleaned[::-1])
    return cleaned == cleaned[::-1]

print(is_palindrome('mad$&^.@@@@am'))


'''
Question:- Check for Palindrome

    Write a function is_palindrome(s) that returns True if the string s is a palindrome 
    (reads the same forwards and backwards, case-insensitive, ignore non-alphanumeric), otherwise False.

 re.sub(pattern, repl, s)
    pattern: a regular expression to match.
    repl: the replacement string.
    s: the input string.
    It returns a new string where every substring matching pattern is replaced by repl.
'''