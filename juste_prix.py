import random as rd

mini=1
maxi=100
assert mini<maxi
def gen_nombre(borne_inf,borne_sup):
    r=rd.randint(mini,maxi)
    return r
tries=0
txt='Input a number between ',mini,'and',maxi

ingame=True
while ingame==True:
    nbr=gen_nombre(mini,maxi)
    while tries!=20:
        u=int(input(txt))
        if u==nbr:
            print("You won in ",tries," tries")
            stat_jp=open('juste_prix_stat.txt','a')
            stat_jp.write("Won in ",tries,"tries")
            stat_jp.write("\n")
            stat_jp.close()
            break
        if u>nbr:
            print("It is smaller")
        else:
            print("It is bigger")
        tries+=1
    print("Do you want to play again?")
    replay=str(input("Type y if you want and n if you do not"))
    assert replay=="y" or "n"
    if replay=="n":
        ingame=False



