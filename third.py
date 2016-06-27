# Write unittests for this function:

import unittest

def count_letter_in_string(string, letter):
  if type(string) != str:
    return 0
  count = 0
  for current_letter in string:
    if current_letter == letter:
      count += 1
  return count

#print(count_letter_in_string('hello', 'l'))

class MyTest(unittest.TestCase):
    def test_string_input_was_given(self):
        self.assertEqual(count_letter_in_string('hello', 'l'), 2)

    def test_int_input_was_given(self):
        self.assertEqual(count_letter_in_string(4, 'l'), 0)

    def test_list_input_was_given(self):
        self.assertEqual(count_letter_in_string([4, 5], 'l'), 0)

    def test_letter_input_not_in_string(self):
        self.assertEqual(count_letter_in_string('hi', 'l'), 0)



if __name__ == '__main__':
    unittest.main()
