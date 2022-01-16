# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def isUnique(string):
  # for example take the string 'abcdef'
  # I want to make sure that string[a] != any of the other characters
  string = list(string)
  for index, letter in enumerate(string):
    # I could remove the letter and see if it still exists
    string.pop(index)
    if(letter in string):
      return False
  return True


if __name__ == '__main__':
   print(isUnique("abcdefghhi"))