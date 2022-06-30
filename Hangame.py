import random as rad
import os
import time
os.system('cls')
def intro(): 
    print("Welcome to the Hangman")
    print("We have some rules: you can try a guess only \033[32m 6 times\33[m. Letters which aren't present in the word and also letters already tapped counts as incorrect answer")
    print('----')
list=["eevee", "girafarig",  "alomomola","suitcase", "proportion", "stimulation", "theft" ,"paint" ,"measure", "pollution ","shareholder","copy"]
targetword=list[rad.randint(0,len(list)-1)] #draw a word to be figured out by the player
back=[]
chances=6
conts=0
repeatlist=[]
for i in range(len(targetword)):
        back.append("_ ") #create a list with the blanks to fill

new_back=(" ".join(back)) # transform the list to chr in order eliminate the brackets 
while chances!=0:
    intro()
    print('You have',chances,'tries \n')
    print(new_back)
    guess=input("try to guess a letter mate, mate:")
    if (targetword.find(guess)!=-1 and guess not in repeatlist ): #verify if the word hasn't alredy been used and it's present in the word 
        repeatlist.append(guess) 
        for i in range(len(targetword)): #verify if there are more than one repeated letter in the word 
            if(targetword[i].find(guess)==0):
                back[i]=targetword[i]
                new_back=(" ".join(back))
                conts+=1
        os.system('cls')

    else:
        if(targetword.find(guess)==-1):
            chances-=1
            print("Ops, there's no \033[31m{}\033[m in the word, you only have: {} chances".format(guess, chances))
            time.sleep(2)
            os.system('cls')
        elif(guess in repeatlist):
            print("hey bro, you have already tapped \033[31m{}\033[m it counts as a \033[31m wrong answer\033[m".format(guess))
            chances-=1
            time.sleep(1)
            os.system('cls')
    if(conts==len(targetword)):
        intro()
        print(new_back)
        print('you win')
        time.sleep(1)
        break
    if chances == 0:
        print('you lose')
