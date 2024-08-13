import random 
import words 
import stages 

lives=6
word=random.choice(words.word_list)
print(word)
res=[]
for i in range(len(word)):
    res+='_'
print(res)

game_over=False
while not game_over:
    guess=input("Guess a letter: ")
    for pos in range(len(word)):
        letter=word[pos]
        if(letter==guess):
            res[pos]=guess
    print(res)
    if(guess not in word):
        lives-=1
        if(lives==0):
            game_over=True
            print("You Lose!!")
    if("_" not in res):
        game_over=True
        print("You Win!!")
    print(stages.stages[lives])