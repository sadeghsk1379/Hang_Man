
print("Player 1 please Enter a word for player 2:")
word2=input()

print("Player 2 please Enter a word for player 1:")
word1=input()

Word1 = list(word1)
Word2 = list(word2)

Word1_now=['_'] * len(Word1)
Word2_now=['_'] * len(Word2)



lives1= (len(Word1)/3) *2
lives2= (len(Word2)/3) *2
lives1=int(lives1)
lives2=int(lives2)

while lives1 !=0 and lives2!=0:
    print("Player 1 please Enter your guess:")
    guess1=input()

    print("Player 2 please Enter your guess:")
    guess2=input()

    if guess1 in Word1:
        print("good jab player1")
        index1= Word1.index(guess1)
        Word1_now[index1]=guess1
    else:
        lives1 = lives1 -1
        print("The word {} was wrong player 1".format(guess1))

    if guess2 in Word2:
        print("good jab player2")
        index2= Word2.index(guess2)
        Word2_now[index2]=guess2
    else:
        lives2 = lives2 -1
        print("The word {} was wrong player 2".format(guess2))

    print ("----------------------------------")
     
    print("player 1")
    print(Word1_now)
    print(lives1,"\n")

    print("player2")
    print(Word2_now)
    print(lives2,"")

    print ("----------------------------------")

    if '_'not in Word1_now:
        print("player1 Won")
        break;
    if '_'not in Word2_now:
        print("player2 Won")
        break;
    

if lives1 ==0 :
     print("player 2 won")
if lives2==0:
    print("player 1 won")
