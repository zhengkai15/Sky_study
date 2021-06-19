#while True:
#    try:
#        print("hello")
#    except EOFerror:
#        break
while True:
    try:
        print(input()[::-1])
    except EOFError:
        break
