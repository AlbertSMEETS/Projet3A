import random

def reset():
    file = open(".score.txt", "w")
    file.write(str(0))
    print("Votre score a ete reinitialise")
    file.close()
    
    file = open(".nbParties.txt", "w")
    file.write(str(0))
    print("Votre nombre de parties a ete reinitialise")
    file.close()
    return 0
    
def main():
    mini = 0
    maxi = 100
    play = True
    maxTries = 100

    file = open(".score.txt", "r")
    data = file.readlines()
    score = int(data[0].strip("\n"))
    file.close()
            
    file = open(".nbParties.txt", "r")
    data = file.readlines()
    nb = int(data[0].strip("\n")) 
    file.close()        

    print("Votre score est " + str(score))
    print("Vous avez joue " + str(nb) + " fois") 


    choice = int(input("Voulez vous jouer seul, contre un robot, reinitialiser les stats ou quitter (1/2/3/4) ?\n"))
    if (choice == 1 ): 
        while play:
            n = random.randint(mini, maxi)
            guess = -1
            tries = 0
            while guess != n and tries <= maxTries:
                tries += 1
                guess = int(input("choisir un nombre entre " + str(mini) + " et " + str(maxi) + "\n"))
                if (guess < n) :
                    print("plus grand")
                if (tries > maxTries):
                        print("perdu, vous avez ateint le nombre maximum de tentatives")
                elif (guess > n) :
                        print("plus petit")
                        if (tries > maxTries):
                                print("perdu, vous avez ateint le nombre maximum de tentatives")
                else :
                        print("trouve en " + str(tries) + " essais")
        
                file = open(".score.txt", "r")
                data = file.readlines()
                score = int(data[0].strip("\n")) + tries
                file.close()
                
                file = open(".score.txt", "w")
                file.write(str(score))
                print("Votre score est " + str(score))
                file.close()
                
                file = open(".nbParties.txt", "r")
                data = file.readlines()
                nb = int(data[0].strip("\n")) + 1
                file.close()
                
                file = open(".nbParties.txt", "w")
                file.write(str(nb))
                print("Vous avez joue " + str(nb) + " fois") 
                file.close()
                answer = int(input("voulez vous rejouer, reinitialiser les stats ou quitter ? (1/2/3)\n"))
                if(answer == 2 ):
                    reset()
                elif(answer == 3):
                    play = False                    

    elif(choice == 2):
        while(play):
                mini=0
                maxi = 100
                guess = -1
                tries = 0
                n = int(input("choisir un nombre entre " + str(mini) + " et " + str(maxi) + " pour le robot\n"))
                while (guess != n and tries <= maxTries):
                        tries += 1
                        guess = int(mini + ((maxi-mini)/2))
                        randomPourcent=random.randint(int(guess*(0.9)),int(guess*(1.1)))
                        guess+= randomPourcent
                        print("Le robot a choisi " + str(guess))
                        if (guess < n) :                         
                                mini = guess + 1
                                if (tries > maxTries):
                                        print("le robot a atteint le nombre maximum de tentatives")
                        elif (guess > n) :
                                maxi = guess - 1
                                if (tries > maxTries):
                                        print("le robot a atteint le nombre maximum de tentatives")
                        else :
                                print("le robot a trouve en " + str(tries) + " essais")
                        
                
                answer = int(input("voulez vous rejouer, reinitialiser les stats ou quitter ? (1/2/3)\n"))
                if(answer == 2 ):
                    reset()
                elif(answer == 3):
                    play = False
                    
    elif(choice == 3 ):
        reset()
        
    else:
        print("Le jeu est ferme")
main()

  
