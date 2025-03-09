def is_balanced(expression: str) -> bool:
    open_parens = 0
    open_brackets = 0
    open_braces = 0
    close_parens = 0
    close_brackets = 0
    close_braces = 0
    
    for char in expression:
        if char == '(':
            open_parens += 1
        elif char == ')':
            close_parens += 1
        elif char == '[':
            open_brackets += 1
        elif char == ']':
            close_brackets += 1
        elif char == '{':
            open_braces += 1
        elif char == '}':
            close_braces += 1

    return open_parens == close_parens and open_brackets == close_brackets and open_braces == close_braces

expression1 = "(a + b) * [c + {d + e}]"
expression2 = "(a + b) * [c + {d + e})"
expression3 = "((())[])"
expression4 = "[{(a + b)}]"

print(is_balanced(expression1))
print(is_balanced(expression2))
print(is_balanced(expression3))
print(is_balanced(expression4))
