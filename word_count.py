import re
import sys

text = sys.argv[1] 

# create list of words
pattern = re.compile(r"[\W _]+") 
words = pattern.split(text)

print(f'word list : {words}\nnumber of words = {len(words)}')

