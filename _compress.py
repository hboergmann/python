from random import randrange

def randomFile(name, n):
    c = 0
    with open(name,"wb") as outfile:
        while c < n:
            x = randrange(255)
            outfile.write(x.to_bytes(1, "little"))
            c += 1
            
            
randomFile("RANDOM", 6500000)
