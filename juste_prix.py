import random as rd
import os 

try_number=7
mini=1
maxi=100
assert mini<maxi
def gen_nombre(borne_inf,borne_sup):
    r=rd.randint(mini,maxi)
    return r
tries=0
loss=0
win=0
txt='Input a number between ',mini,'and',maxi,
game_starter='Input p to play, q to quit or r to reset '
txt_entry_error='Invalid number, please enter a number between',mini,'and',maxi
ingame=True
while ingame==True:


    nbr=gen_nombre(mini,maxi)
    u=str(input(game_starter))
    tries=0
    while tries!=try_number:
        tries+=1
        if u=='q':
            break
        if u=='r':
            os.system("attrib -h jp\juste_prix_stat.txt")
            stat=open("jp\juste_prix_stat.txt",'w')
            stat.close()
            os.system("attrib +h jp\juste_prix_stat.txt")
            break
        else:
            n=int(input(txt))
            if n>maxi or n<mini:
                n=int(input(txt_entry_error))

        if n==nbr:
            print("You won in ",tries," tries")
            stat_jp=open("jp\juste_prix_stat.txt",'a')
            stat_jp.write("Won in "+str(tries)+"tries")
            stat_jp.write("\n")
            stat_jp.close()
            os.system("attrib +h jp\juste_prix_stat.txt") #+h to hide and -h to show + path of the file
            win+=1
            break
        if n>nbr:
            print("It is smaller")
        else:
            print("It is bigger")
        if tries==try_number:
            loss+=1
    print("Currently: computer:",loss," you:",win," Do you want to play again?")
    replay=str(input("Type y if you want and n if you do not "))
    assert replay=="y" or "n"
    if replay=="n":
        ingame=False
os.system("attrib -h jp\match_history.txt")
match_history=open("jp\match_history.txt","a")
match_history.write("Computer:"+str(loss)+" You:"+str(win))
match_history.write("\n")
match_history.close()
os.system("attrib +h jp\match_history.txt")



