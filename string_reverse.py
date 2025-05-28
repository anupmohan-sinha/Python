def reverse_string(s):
    return s[::-1]

print(reverse_string("Anup Mohan"))

def slice_alt(s):
    return s[26:0:-1]

print(slice_alt('abcdefghijklmnopqrstuvwxyz'))


''' 
Question:- Reverse a String
    Write a function reverse_string(s) that takes a string s and returns the string reversed.

In Python, the expression s[::-1] is using slice notation to create a reversed copy of the sequence s.

s[start:stop:step]

s - sequence
start - start is the index where slice begins (inclusive)
stop - stop is the index where the slice ends (exclusive)
step - step is how many items to move forward (or backward) between each element


When you write s[::-1], you’re omitting both start and stop, and specifying a step of -1. The defaults and effect are:

Default start: When step is negative, the default start becomes the last element.

Default stop: When step is negative, the default stop becomes before the first element.

step = -1: Move one position backward each time.

s[::-1]
means:

Start at the end of s.

Move backwards one element at a time.

Stop when you’ve passed the beginning.

That gives you a new sequence that is s in reverse order.
'''