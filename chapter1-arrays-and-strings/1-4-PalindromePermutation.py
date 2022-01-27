# Palindrome Permutation: Given a string, write a function to check if it is a permuation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. You can ignore casing and non-letter characters.

# can you rearrange it to be a palindrome

# ababa

# CTCI Algorithm  to solve this problem: use a hashmap to count the number of occurences of each letter and only 1 letter is allowed to have an odd number of occurrences

def isArrangedPalindrome(word):
  wordDict = {}
  for letter in word:
    if(letter not in wordDict):
      wordDict[letter] = 1
    else:
      wordDict[letter] += 1
  return passesCheck(wordDict)

def passesCheck(dict):
  numOfOdds = 0
  for key in dict:
    if(dict[key]%2 == 1):
      numOfOdds+=1
  return numOfOdds < 2

if __name__ == '__main__':
  print(isArrangedPalindrome("ababa"))