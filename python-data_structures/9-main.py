#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

# Additional tests
print(multiple_returns(""))  # Empty string
print(multiple_returns("Hello"))  # Single word
print(multiple_returns("Python is awesome!"))  # Multiple words
