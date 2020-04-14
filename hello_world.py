from random import shuffle
liste = "amazing excited gorgeous blazing stunning biggest \
    tremendous greatest best fantastic phenomenal delightful \
    ambitious exciting  staggering outstanding fantastic smart \
    gorgeous best massive incredible spectacular cool magical \
    revolutionary intuitive beautiful".upper().split()
shuffle(liste)

for strophe in range(5):
    for n in range(2):
        for i in range(4):
            print ("spam ", end=' ')
        print()
    #shuffle(liste)
    #print(liste[0] + " SPAM, " +liste[1]+" SPAM")
    #print(liste.pop() + " SPAM, " + liste.pop() + " SPAM")
    #print("{} SPAM, {} SPAM".format(liste.pop(), liste.pop()))  # {} sind platzhalter
    # besser ist
    el1 = liste.pop()
    el2 = liste.pop()
    print("{} SPAM, {} SPAM".format(el1, el2))  # {} sind platzhalter
    print()
print()
#ende



