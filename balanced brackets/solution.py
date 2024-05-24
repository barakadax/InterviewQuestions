from collections import deque

class balanced_brackets:
    def __init__(self) -> None:
        self.__brackets = { '(': ')', '[': ']', '{': '}' }

    
    def validate_balance(self, expression: str) -> bool:
        opening_brackets_stack = deque()

        for character in expression:
            if character not in self.__brackets and character not in self.__brackets.values():
                return False
            elif character in self.__brackets:
                opening_brackets_stack.append(character)
            else:
                if not opening_brackets_stack:
                    return False
                
                current_bracket = opening_brackets_stack.pop()
                if self.__brackets[current_bracket] != character:
                    return False

        return True if not opening_brackets_stack else False


if __name__ == '__main__':
    expression = '{()[{}[]]}[]'
    balanced_validator = balanced_brackets()
    print('Balanced' if balanced_validator.validate_balance(expression) else 'Not balanced')
