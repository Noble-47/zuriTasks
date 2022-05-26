# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


# illegal_patterns : all non word character including spaces and underscores

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, 'r') as f:
        text = f.read()
    return text
    
def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    from collections import Counter
    import re
    pattern = re.compile(r'[''\W_]+')
    textlines = pattern.sub(' ',text)
    counts = Counter(textlines.strip().split(" "))
    return dict(counts)
    

# read_file_content('story.txt')
print(count_words())