#Besides numbers, Python can also manipulate strings, which can be expressed in several ways. They can be enclosed in single quotes ('...') or double quotes ("...") with the same result [2]. \ can be used to escape quotes:

'spam eggs'  # single quotes
'doesn\'t'  # use \' to escape the single quote...
"doesn't"  # ...or use double quotes instead
'"Yes," they said.'
"\"Yes,\" they said."
'"Isn\'t," they said.'

#In the interactive interpreter, the output string is enclosed in quotes and special characters are escaped with backslashes. While this might sometimes look different from the input (the enclosing quotes could change), the two strings are equivalent. The string is enclosed in double quotes if the string contains a single quote and no double quotes, otherwise it is enclosed in single quotes. The print() function produces a more readable output, by omitting the enclosing quotes and by printing escaped and special characters:

'"Isn\'t," they said.'
print('"Isn\'t," they said.')
s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), \n is included in the output
print(s)  # with print(), \n produces a new line

#If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:

print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

#String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''. End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line. The following example:

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium'

#Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.

'Py' 'thon'

#This feature is particularly useful when you want to break long strings:

text = ('Put several strings within parentheses '
...         'to have them joined together.')
text

word = 'Python'
In addition to indexing, slicing is also supported. While indexing is used to obtain individual characters, slicing allows you to obtain substring:

word[:2] + word[2:]
'Python'
ord[-2:]  # characters from the second-last (included) to the end
One way to remember how slices work is to think of the indices as pointing between characters, with the left edge of the first character numbered 0. Then the right edge of the last character of a string of n characters has index n, for example:

The first row of numbers gives the position of the indices 0…6 in the string; the second row gives the corresponding negative indices. The slice from i to j consists of all characters between the edges labeled i and j, respectively.

For non-negative indices, the length of a slice is the difference of the indices, if both are within bounds. For example, the length of word[1:3] is 2.

Attempting to use an index that is too large will result in an error:
word[4:42]
word[42:]
word[0] = 'J'
word[2:] = 'py'
'J' + word[1:]
word[:2] + 'py'
s = 'supercalifragilisticexpialidocious'
len(s)
