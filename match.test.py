from match import match

tests = [
    ['abc(123)', True],
    # returns false -- missing closing bracket

    ['abc(123', False],
    #returns true

    ['a[bc(123)]', True],
    #returns false -- inproperly nested

    ['a[bc(12]3)', False],
    #returns true

    ['a{b}{c(1[2]3)}', True],
    #returns false -- inproperly nested

    ['a{b}{c(1}[2]3)', False],
    #returns true

    ['()', True],
    #returns false - no opening bracket to correspond with last character

    ['[]]', False]
    #returns true -- no brackets = correctly matched
]
i = 0
for case in tests:
    result = match(case[0])
    print(f"test {i}, sample: {case[0]}")
    print(f"expected result: {case[1]}")
    print(f"actual result: {result}")
    assert result == case[1]
    i += 1