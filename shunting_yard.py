'''
A module that implements the famous shunting-yard algorithm to
convert mathematical expressions in infix notation into equivalent
expressions in postfix notation, which is easier for a computer
program to evaluate.

To use, call `infixToPostfix` with a string that contains a valid
mathematical expression in infix notation. This will return the
expression in postfix notation.

The module also contains a number of helper functions that could
be useful in implementing other, similar algorithms.
'''


def appendToOutput(outString, token):
    '''
    Accept an output string and a token and return a new output
    string with the token appended to it with spaces inserted
    appropriately such that numbers and operators are separated
    with a single space.
    '''
    if outString == '':
        return token
    return outString + ' ' + token


def comparePrecedence(leftOp, rightOp):
    '''
    Accept two operators as strings and compare their precedence.
    Return -1 if `leftOp` has lower precedence then `rightOp`,
    0 if the two have equal precdence, and 1 if `leftOp` has
    higher precedence than `rightOp`.
    '''
    lowOps = ['+', '-']

    if leftOp in lowOps:
        if rightOp in lowOps:
            return 0
        else:
            return -1

    if rightOp in lowOps:
        return 1
    else:
        return 0


def infixToPostfix(inString):
    '''
    Accept a mathematical expression in infix notation and
    return an equivalent expression in postfix notation.

    The following operators are supported:
      * + (addition)
      * - (subtraction)
      * * (multiplication)
      * / (division)

    Parentheses are also supported for grouping.
    '''
    operatorStack = []
    outString = ''

    for token in tokenize(inString):
        if isNumber(token):
            outString = appendToOutput(outString, token)
        if isOperator(token):
            while True:
                if stackIsEmpty(operatorStack):
                    break
                operator = peekAtStack(operatorStack)
                if comparePrecedence(token, operator) > 0:
                    break
                if isLeftBracket(operator):
                    break
                popFromStack(operatorStack)  # Consume the operator
                outString = appendToOutput(outString, operator)
            pushToStack(operatorStack, token)
        if isLeftBracket(token):
            pushToStack(operatorStack, token)
        if isRightBracket(token):
            while not isLeftBracket(peekAtStack(operatorStack)):
                operator = popFromStack(operatorStack)
                outString = appendToOutput(outString, operator)
            popFromStack(operatorStack)  # Get rid of the left bracket

    # Append all remaining operators to the output
    while not stackIsEmpty(operatorStack):
        operator = popFromStack(operatorStack)
        outString = appendToOutput(outString, operator)

    return outString


def isDigit(character):
    '''
    Accept a single character as a string and return `True` if
    it is a valid digit and `False` otherwise.
    '''
    return character in '0123456789'


def isLeftBracket(token):
    '''
    Accept a string token such as those produced by the `tokenize`
    function and return `True` if it is a valid left bracket
    character and `False` otherwise.
    '''
    return token in '[('


def isNumber(token):
    '''
    Accept a string token such as those produced by the `tokenize`
    function and return `True` if it is a valid number and `False`
    otherwise.
    '''
    for character in token:
        if not isDigit(character):
            return False
    return True


def isOperator(token):
    '''
    Accept a string token such as those produced by the `tokenize`
    function and return `True` if it is a valid operator and
    `False` otherwise. Valid operators are symbols like "+", "-",
    and so on.
    '''
    return token in '+-*/'


def isRightBracket(token):
    '''
    Accept a string token such as those produced by the `tokenize`
    function and return `True` if it is a valid right bracket
    character and `False` otherwise.
    '''
    return token in '])'


def peekAtStack(stack):
    '''
    Accept a list, which is treated as a stack that grows "up" or
    to the left (depending on how you visualize these things), and
    return the top-most item without removing it from the stack.

    The list will not be mutated.
    '''
    return stack[0]


def popFromStack(stack):
    '''
    Accept a list, which is treated as a stack that grows "up" or
    to the left (depending on how you visualize these things), and
    remove and return the top-most item.

    The list will be mutated to remove the first item.
    '''
    item = stack.pop(0)
    return item


def pushToStack(stack, item):
    '''
    Accept a list, which is treated as a stack that grows "up" or
    to the left (depending on how you visualize these things), and
    push the given item onto its top.

    The list will be mutated to prepend the new item.
    '''
    stack.insert(0, item)


def stackIsEmpty(stack):
    '''
    Accept a list, which is treated as a stack and return `True`
    if the stack is empty (contains zero items) and `False`
    otherwise.
    '''
    return len(stack) == 0


def tokenize(inString):
    '''
    Accept a mathematical expression as a string presumed to be
    in infix notation and produce an iterator of tokens to be
    consumed by the shunting-yard algorithm.
    '''
    nextToken = ''
    for character in inString:
        isBracket = isLeftBracket(character) or isRightBracket(character)
        if isDigit(character):
            nextToken = nextToken + character
        elif isOperator(character) or isBracket:
            # This only works if all operators are single characters
            if nextToken != '':
                yield nextToken
                nextToken = ''
            yield character
        else:
            if nextToken != '':
                yield nextToken
                nextToken = ''
    if nextToken != '':
        yield nextToken


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser(
        description='Convert a string from infix to postfix.')
    parser.add_argument(
        'infix',
        metavar='I',
        help='a mathematical expression in infix notation')
    args = parser.parse_args()

    infix = args.infix
    postfix = infixToPostfix(infix)
    print(postfix)
