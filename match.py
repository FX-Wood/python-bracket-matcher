from stack import Stack

def match(sample):
    # make a stack
    stack = Stack()

    # make a dictionary of delimiters
    delimiters = {
        '[':']',
        '{':'}',
        '(':')'
    }
    # iterate over sample string
    for char in sample:
    # if open is encountered, put on stack
        if char in delimiters.keys():
            stack.push(char)
    # if close is encountered, check to see if the last add was a matching delimiter
        elif char in delimiters.values():
            try:
                last = stack.pop()
            except IndexError:
                return False
            if not delimiters[last] == char:
                return False
    # once the loop is closed, if there are chars on the stack, fail
    try:
        stack.pop()
        return False
    # if the pop fails, everything is great!
    except IndexError:
        return True
