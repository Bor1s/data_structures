# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

def check(text):
    opening_brackets_stack = []
    opening_brackets_stack_indexes = []
    fail_position = -1

    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            opening_brackets_stack_indexes.append(i+1)

        if next == ')' or next == ']' or next == '}':
            if not opening_brackets_stack:
                fail_position = i+1
                break

            # Process closing bracket, write your code here
            opening_brackets_stack_element = opening_brackets_stack.pop()
            opening_brackets_stack_indexes.pop()
            bracket_matcher = Bracket(opening_brackets_stack_element, i)
            if not bracket_matcher.Match(next):
                fail_position = i+1
                break

    # Printing answer, write your code here

    if fail_position > -1:
        return fail_position

    if opening_brackets_stack:
        return opening_brackets_stack_indexes[0]
    else:
        return 'Success'


if __name__ == "__main__":
    text = sys.stdin.read()
    length = len(text)
    if length >= 1: #and length <= 10**5:
        print(check(text))
