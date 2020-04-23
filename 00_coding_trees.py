# coding trees in python
# 3 * y + x     or    3 * (y + x)
# as atree  
#                   *                               +
#                  /  \                            /  \
#                3     +                         +     3
#                     /  \                      /  \
#                    y    x                    3     y   

class Expr:
    pass

class Times(Expr):
    def __init__(self, l, r):       # left and right
        self.l = l
        self.r = r

    def __str__(self):
        return "(" + str(self.l) + "*" + str(self.r) + ")"

    def eval(self, env):
        return self.l.eval(env) * self.r.eval(env)

class Plus(Expr):
        def __init__(self, l, r):
            self.l = l
            self.r = r
        
        def __str__(self):
            return "(" + str(self.l) + "+" + str(self.r) + ")"
            
        def eval(self, env):
            return self.l.eval(env) + self.r.eval(env)

class Const(Expr):
        def __init__(self, val):
            self.val = val
        
        def __str__(self):
            return str(self.val)

        def eval(self,env):
            return self.val

class Var(Expr):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def eval(self, env):
        return env[self.name]


e1 = Times(Const(3), Plus(Var("y"), Var("x")))  # 3 * y + x
e2 = Plus(Var("x"), Times(Const(3),Var("y")))  # 3 * (y + x)

print(e1)
print(e2)

env =  { "x": 2, "y" :4}    # environment in a dictionary - asign values to numbers

print(env["x"])
print(env["y"])
print(e1.eval(env))
print(e2.eval(env))


