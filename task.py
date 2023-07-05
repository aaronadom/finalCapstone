# Little sister's vocab task

# Add a prefix to a word
# the function that takes word as a parameter and returns a new prefixed word
def add_prefix_un(word):
    return input("Enter a prefix: ") + word

word1 = input("Please enter a word: ")
result1 = add_prefix_un(word1)
print(result1)

word2 = input("Please enter an another word: ")
result2 = add_prefix_un(word2)
print(result2)

# Remove a suffix from a word
# The function that takes in a word str, and returns the root word without the ness suffix.
# If If the root word originally ended in a consonant followed by a 'y', then the 'y' was changed to 'i'. 
# Removing 'ness' needs to restore the 'y' in those root words.

def remove_suffix_ness(word):
    if word.endswith("ness"):
        root_word = word[:-4]  # Remove the "ness" suffix

        # checking if originally ended in a consonant followed by "y"
        if root_word[-1] == "i" and root_word[-2].isalpha() and isconsonant(root_word[-2]):
            root_word = root_word[:-1] + "y"  # Restore the "y" in the root word

        return root_word
    else:
        return word

# checking if a character is a consonant
def isconsonant(char):
    return char.lower() not in "aeiou"

word3 = input("Please enter a word that ends in ness: ")
result1 = remove_suffix_ness(word3)
print(result1)  

word4 = input("Please enter another word that ends in ness: ")
result2 = remove_suffix_ness(word4)
print(result2)