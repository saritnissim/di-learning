def is_balanced(input_str):
    stack = []
    opening = ['(', '{', '[']
    closing = [')', '}', ']']

    for char in input_str:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return False # There is no opening bracket
            top = stack.pop()
            if opening.index(top) != closing.index(char):
                return False
    #If stack is empty, then return True
    if not stack:
        return True
            
