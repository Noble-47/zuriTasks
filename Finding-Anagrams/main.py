# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True



def find_anagram(word, anagram):
    from collections import Counter
    # anagram matching is case insensitive
    word_count = Counter(word.lower())
    anagram_count = Counter(anagram.lower())
    return True if word_count == anagram_count else False

# Test
# print(find_anagram("Game", "Mage"))
# print(find_anagram("below", "elbow"))
# print(find_anagram("hello", "check"))
