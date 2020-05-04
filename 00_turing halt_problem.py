# turing halt problem
def holds(fun, arg):
    pass

def wierd(fun):
    if holds(fun, fun):
        while True:
            pass
        else:
            return

wierdstr = """
def wierd(fun):
    if holds(fun, fun):
        while true:
            pass
        else:
            return
"""

wierd(wierdstr)
