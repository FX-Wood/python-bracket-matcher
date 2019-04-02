from stack import Stack

def match(sample):
    # make a stack
    stack = Stack()

    # make a list of the open chars
    open = ['(', '{', '[']
    
    # make a list of the close chars
    close = [')', '}', '[']


    # iterate over sample string
    for char in sample:
    # if open is encountered, put on stack
        if char in open:
            stack.push(char)
    # if close is encountered, check to see if the last add was a match
        elif char in close:
            last = stack.pop()
            if not open.index(last) == close.index(char):
                return False
    return True


    # at end, remove from
