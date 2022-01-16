import unittest

# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

def checkPermuationByDictionary(string1, string2):
  #  string1 being a permuation of string2 means that if we rearrange the letters in string2 we can form string1 and vice versa.
  dict1 = {}
  dict2 = {}
  if(len(string1) != len(string2)):
    return False
  else:
    for letter in string1: # for every letter in string1: 
      if letter not in dict1: # if the letter is not in dict then add to dictionary
        dict1[letter] = 1
      else: # else add +1 to the dictionary for that key
        dict1[letter] += 1
    
    for letter in string2: # for every letter in string2: 
      if letter not in dict2: # if the letter is not in dict2 then add to dict2
        dict2[letter] = 1
      else: # else add +1 to the dictionary for that key
        dict2[letter] += 1
  
  return dict1 == dict2

def checkPermuationBySort(string1, string2):
  return "".join(sorted(string1)) == "".join(sorted(string2))


class Test(unittest.TestCase):
    # str1, str2, is_permutation
    test_cases = (
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    )

    testable_functions = [checkPermuationByDictionary, checkPermuationBySort]

    def test_cp(self):
        # true check
        for check_permutation in self.testable_functions:
            for str1, str2, expected in self.test_cases:
                assert check_permutation(str1, str2) == expected


if __name__ == "__main__":
    unittest.main()