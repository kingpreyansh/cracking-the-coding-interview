import unittest

# Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. 

# Input: Name, True Length

def replaceSpaces(string, trueLen):
  # the join will join the array with '%20' as wanted
  # the .strip() will get rid of trailing and leading spaces
  # the .split(" ") will return an array of items based on the spaces

  # NOTE TO SELF: The trueLen is there for a reason so make sure you use it
  return "%20".join(string[:trueLen].split(" "))


class Test(unittest.TestCase):
    """Test Cases"""
    test_cases = {
        ("much ado about nothing      ", 22, "much%20ado%20about%20nothing"),
        ("Mr John Smith       ", 13, "Mr%20John%20Smith"),
        (" a b    ", 4, "%20a%20b"),
        (" a b       ", 5, "%20a%20b%20")
    }
    testable_functions = [replaceSpaces]

    def test_urlify(self):
        for urlify in self.testable_functions:
            for input1, input2, expected in self.test_cases:
                assert urlify(input1, input2) == expected

if __name__ == '__main__':
  unittest.main()

