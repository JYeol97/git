# if 조건문 : 
#       수행할_문장1
#       수행할_문장2
#          ... 
# else : 
#       수행할_문장A
#       수행할_문장B
#          ...

# A,B = map(int, input().split())
# if A>B:
#     print(A)
# if A<B:
#     print(B)
# elif A==B:
#     print("==")

# A,B = map(int, input().split())
# if A>B:
#     print(A)
# elif A<B:
#     print(B)
# else A==B:
#     print("==")

# A,B = map(int, input().split())
# if A>B:
#     print(A)
# elif A<B:
#     print(B)
# else:
#     print("==")


A,B = map(int, input().split())
if A>B:
    print(">")
elif A<B:
    print("<")
else:
    print("==")