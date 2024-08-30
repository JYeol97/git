# import sys
#
# sys.stdin = open("input (7).txt")

def check(N, stack):
    for i in range(len(N)):
        if len(N) == 1 and N[i] == '.':
            return
        if N[i] == '(':
            stack.append(N[i])

        elif N[i] == '[':
            stack.append(N[i])

        elif N[i] == ')':
            if len(stack) >= 1:
                if stack[-1] == '(':
                    stack.pop(-1)

                else:
                    return 'no'

            else:
                return 'no'

        elif N[i] == ']':
            if len(stack) >= 1:
                if stack[-1] == '[':
                    stack.pop(-1)

                else:
                    return 'no'

            else:
                return 'no'

    if len(stack) >= 1:
        return 'no'

    else:
        return 'yes'


while True:
    N = list(map(str, input()))
    stack = []
    if N == ['.']:
        break

    else:
        print(check(N, stack))
