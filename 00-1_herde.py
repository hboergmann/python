# Ali Baba hat testamentarisch verfügt, dass seine Herde unter seinen sieben Kinder aufgeteilt wird
# jedes Kind bekommt den Bruchteil der Schafe, die seinem Alter entsprechen.
# Die Kinder sind alle unter 20 Jahre alt
# z.B. ein 10-jähriger bekommt ein Zehntel
# Die einzige Tochter erhält 24 Schafe
lauf = True
for a in range(2,14):
    for b in range(3,15):
        for c in range(4,16):
            for d in range(5,17):
                for e in range(6,18):
                    for f in range(7,19):
                        for g in range(8,20):
                            if(a==b or a==c or a==d or a==e or a==f or a==g or b==c or b==d or b==e or b==f or b==g or c==d or c==e or c==f or c==g or d==e or d==f or d==g or e==f or e==g or f==g):
                                pass
                            else:
                                x=1/a+1/b+1/c+1/d+1/e+1/f+1/g
                                if (x==1 and lauf==True):
                                    print(str(a)+"->"+str(b)+"->"+str(c)+"->"+str(d)+"->"+str(e)+"->"+str(f)+"->"+str(g))
                                    lauf = False
                                    x = 300
                                    y = 1
                                    while y > 0:
                                        x = x + 1
                                        y = (x % a) + (x % b) + (x % c) + (x % d) + (x % e) + (x % f) + (x % g)
                                    print(x, y)
