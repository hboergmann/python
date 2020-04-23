# Rekursion
def move(f, t):
    print("Move disk from {} to {} ".format(f, t))
    
def movevia(f, v, t):
    move(f, v)
    move(v,t)

# def foo(x)
 #   foo(x)  

def hanoi(n, f, h, t):  # n = number; f=from; h=helper; t=target
    if n == 0:
        pass
    else:
        hanoi(n-1,f,t,h)
        move(f,t)
        hanoi(n-1,h,f,t)

print(move("A", "C"))
print(movevia("A", "B", "C"))
print(hanoi(4,"A", "B", "C"))
