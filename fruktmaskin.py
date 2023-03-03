import random
#vi ska återanvända kod

#array
frukter = ("Apelsin", "Banan","melon", "Kiwi", "Citron")
looping = True

#Definerar funktion
def print_fruit(userinput):
    fnr = int(userinput)
    print("\n" + frukter[fnr-1] + " Kommer här!\n")
#Huvudprogram

print("\n-:FruktMaskin:-")


while looping:

    i = 1
    for frukt in frukter:
        print(str(i) + ": " + frukt)
        i += 1
   
    fruktnr = input("\nMata in nr på border tuck du vill ha")
    print_fruit(fruktnr)
    go = input("\nVill du ha en frukt till?")

    if(go == "n"):
        break

    print("-----------------------------------------------------------------------------")
    
    print("Föresten, du får en frukt till för du är snäll och en anka\n")
    slumpfrukt  = random.randint(1, 5)
    print_fruit(slumpfrukt)