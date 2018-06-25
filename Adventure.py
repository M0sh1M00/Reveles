import random
import time



# GENERATION STUFF
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = [1, 2, 3, 4, 5]

### STORY STUFF
sp = " "

norm1 = ["Icy" , "Fiery" , "Angelic", "Soul", "Quick", "Explosive", "Sandy", "Demonic", "Poisonious", "Windy", "Bloody", "Flaming", "Snowy", "Frozen", "Lightning", "Deadly", "Venomous", "Valiant", "Zealous"]
norm2 = ["Strike", "Jab", "Spin", "Thrust", "Summon", "Barrage", "Offensive", "Onslaught", "Violation", "Assualt", "Enroachment", "Smash", "Devasation", "Tormentation", "Paralysis", "Demolition"]

norm = []
var8 = 0
var9 = 1 - 2
for var6 in norm1:

    for var7 in norm2:
        var9 = var9 + 1
        x = (norm1[var8] +sp+ norm2[var9])
        norm.append(x)

    var8 = var8 + 1
    var9 = 1 - 2
#x = 0
#for i in norm:
#    print(norm[x])
#    x = x + 1





### NAMES

namepre = ["the Courageous", "the Charismatic", "the Intelligent", "the Elder", "the Wise", "the Wealthy", "the Normal"]


### UP TO VAR10


biomes = ["snow", "desert", "hell", "heaven", "random"]


### ICE
icestarter = ["Through the blizzard you see movement. It comes closer. You can see clearly now. Its",
"Through the arachaic snow you see a wooden shack, as you enter you see a lifeless body slumped on the floor with blood oozing out of it. Next to the body is"]


iceenemy = ["penguin", "snow elemental", "polar bear", "Eskimo", "husky", "fox", "ice elemental"]


### desert
desstarter = ["The sun beats down on you as you trudge through the endless miles of course sand. In the distance you see an object approaching. After wiping the sand out of your eyes it becomes apparent. Its",
"As you take shelter in a pyramid, ecscaping the blazing sun you look behind you. Oh No. Its",
"As you approach an oasis surrounded by an ineffable amount of desolate terrain you, look into the deep and clear blue water, getting ready to quench your thrist. Thats when you see something unbelivable. Its"]


desenemy = ["vulture", "sand worm", "mummy", "armadillo", "kangaroo", "scorpion", "scarab beetle", "desert elemental"]

### hell

helstarter = ["The chaotic screams and magma bubbling below you fill your ears as you traverse through the crimson caves, littered with skulls. As you turn the corner of the cave you become startled. Its",]


helenemy = ["medusa", ", severed head", "reaper", "hellhound", "tortured soul", "gremlin"]
### HEAVEN

heastarter = ["random"]

heaenemy = ["lost soul", "arch angel", "knight", "disciple"]


end = ["", "", "", "", "A shiver goes down your spine", "It lurches forward", "It jerks forward", "A cold wind brushes against your face"]
item = ["a cloak", "a gown", "armour", "silk woven fabrics", "a deadly aura", "a jewel encrusted attire", "a garb" ]
adjective = ["a glowing", "a black", "a white", "a bloodthirsty", "an undead", "a rouge", "a starved", "a staggering", "a fear inducing", "a nimble"]
joining = ["enshrined in", "wearing", "smothered in", "bearing", "covered top to bottom in"]
weapon = ["axe", "sword", "katana", "knife", "dagger", "wand", "scythe"]
modify = ["enchanted", "mysterious", "dangerous", "sharp", "cursed", "glowing"]
body = ["inside the carcass of", "within the body of", "entrenched in the stomach of", "in a bag near", "deep inside", "close to"]
adj2 = ["crushing", "stunning", "epic", "awesome", "incredible", "legendary", "awe inspiring", "fabulous", "tremendous", "unbelievable"]

### SHOP STUFF

shopobject = ["Orb", "Potion", "Ring", "Keys", "Shard", "Tablet"]
shopadjlife = ["of Healing", "of Life", "of Essence"]
lifeshop = []
lifeshop.append(random.choice(shopobject))
lifeshop.append(random.choice(shopadjlife))
shoplife = (lifeshop[0] + sp + lifeshop[1])
shoplifeg = 0
while shoplifeg <= 19:
    shoplifeg = random.choice(number)*random.choice(number)+random.choice(number)

boughtsapphire = 0



###COLLECTION

collection = []
collectionfull = ["Sapphire", "Emerald", "Ruby", "Diamond", "Topaz"]
hasgem = 0




gold = 0
goldN = 0
num = 0
fite = 2
var2 = 1
### CHECKER VARIABLES


weapon = ["axe", "sword", "katana", "knife"]
modify = ["enchanted", "mysterious", "dangerous", "sharp"]
curweap1 = []
curweap2 = []
stat1 = ""
stat2 = ""
stat3 = ""
stat4 = ""
stat5 = ""
stat6 = 0
stat7 = 0
stat8 = 0
stat9 = 0
stat10 = 0
life = 5
hpcap = 100
hp = 100
ehp = 0
emove = []
enemystat = []




name = input("What is your name young adventurer? ")
name = list(name)
name[0] = name[0].upper()
name = "".join(name)

name = name + sp + random.choice(namepre)





time.sleep(1)
print ("Biomes in the current build are:")
time.sleep(1)
print ("Snow")
time.sleep(1)
print ("Desert")
time.sleep(1)
print ("Hell")
time.sleep(1)
print ("Heaven")
time.sleep(1)
print ("Random")
print(" ")
time.sleep(1)
biome = input("Which biome will you adventure in? ")
while True:
    if biome in biomes:
        break
    else:
        print("That biome was invalid")
        biome = input("Which biome will you adventure in? ")
if biome == "random":
    while biome == "random":
        biome = random.choice(biomes)
time.sleep(2)
print("   ")
print ("Type 'help' if you dont know what to type!")
print("   ")
time.sleep(2)
print("As you enter the "+ biome+ ", you see a weapon lying by a tree!")
time.sleep(3)
while True:
    curweap1.append(random.choice(modify))
    curweap1.append(random.choice(weapon))
    main = random.choice(number) + random.choice(number)
    while main >= 11:
        main = 0
        main = random.choice(number) + random.choice(number)

    while 3 >= main:
        main = 0
        main = random.choice(number) + random.choice(number)
        while main >= 11:
            main = 0
            main = random.choice(number) + random.choice(number)





    y = random.choice(number)
    sec1 = y
    while sec1 >= main:
        sec1 = 0
        y = random.choice(number)
        sec1 = y

    number.remove(y)
    sec2 = random.choice(number)
    while sec2 >= main:
        sec2 = 0
        sec2 = random.choice(number)

    if sec1 > sec2:
        r = 1
    else:
        r = 2
    if sec1 <= 2:
        sec1 = sec1 + 1
    if sec2 <= 2:
        sec2 = sec1 + 1
    if sec1 == main:
        main = main + 1
    if sec2 == main:
        main = main + 1


    ### I SPENT LIKE 30 MINUTES ADDING IN THE LINE BELOW,IT WAS A THICC BUG
    number.append(y)
    ### XD

    oth1 = random.choice(number)
    oth2 = random.choice(number)
    if r == 1:
        while oth1 >= sec2:
            oth1 = random.choice(number) - 1

        while oth2 >= sec2:
            oth2 = random.choice(number) - 1


    elif r == 2:
        while oth1 >= sec1:
            oth1 = random.choice(number) - 1

        while oth2 >= sec1:
            oth2 = random.choice(number) - 1

    main = str(main)
    sec1 = str(sec1)
    sec2 = str(sec2)
    oth1 = str(oth1)
    oth2 = str(oth2)
    mainA = random.choice(norm)
    norm.remove (mainA)
    sec1A = random.choice(norm)
    norm.remove (sec1A)
    sec2A = random.choice(norm)
    norm.remove (sec2A)
    oth1A = random.choice(norm)
    norm.remove (oth1A)
    oth2A = random.choice(norm)
    norm.remove (oth2A)

    curweap2.append(curweap1[0])
    curweap2.append(curweap1[1])
    print("Upon further inspection, it seems to be a " + curweap2[0] +sp+ curweap2[1]+"!")
    time.sleep(2)
    print(mainA + " is a primary move with " + main + " levels!")
    time.sleep(2)
    print(sec1A + " is a secondary move with " + sec1 + " levels!")
    time.sleep(2)
    print(sec2A + " is a secondary move with " + sec2 + " levels!")
    time.sleep(2)
    print(oth1A + " is a normal move with " + oth1 + " levels!")
    time.sleep(2)
    print(oth2A + " is a normal move with " + oth2 + " levels!")


    norm.append (mainA)
    norm.append (sec1A)
    norm.append (sec2A)
    norm.append (oth1A)
    norm.append (oth2A)

    stat1 = mainA
    stat2 = sec1A
    stat3 = sec2A
    stat4 = oth1A
    stat5 = oth2A
    stat6 = main
    stat7 = sec1
    stat8 = sec2
    stat9 = oth1
    stat10 = oth2

    stats = {


    stat1: stat6,

    stat2: stat7,

    stat3: stat8,

    stat4: stat9,

    stat5: stat10

    }



    ### Battle Fluff

    fluff5 = ["The enemy tries to hide its writhing pain from your attack but to no avail. The enemy is critically damaged",

    "The enemy becomes temporary stunned from your ineffable " + curweap2[0] + sp + curweap2[1]+"!",

    "The enemy can barely stand after your " + random.choice(adj2) + " attack!"

    "Your " + random.choice(adj2) " moves have left the enemy dumbfounded on what to do next!"

    "The " random.choice(adj2) " "

    ]





    fluff4 = []
    fluff3 = []
    fluff2 = []
    fluff1 = []


    efluff1 = [""]
    efluff2 = []
    efluff3 = []
    efluff4 = []
    efluff5 = []




    break



if 1 ==1:





    while True:
        time.sleep(2)
        print(" ")
        start = input("What do you want to do now " + name + "? ")
        print(" ")
        time.sleep(2)
        if start == "fight":
            time.sleep(3)

            ### Biome
            locitem = random.choice(item)
            if biome == "snow":
                locenemy = random.choice(iceenemy)
                print (random.choice(icestarter) + sp + random.choice(adjective) + sp + locenemy + sp + random.choice(joining) + sp + locitem + "." + sp + random.choice(end))
            if biome == "desert":
                locenemy = random.choice(desenemy)
                print (random.choice(desstarter) + sp + random.choice(adjective) + sp + locenemy + sp + random.choice(joining) + sp + locitem + "." + sp + random.choice(end))

            if biome == "hell":
                locenemy = random.choice(helenemy)
                print (random.choice(helstarter) + sp + random.choice(adjective) + sp + locenemy + sp + random.choice(joining) + sp + locitem + "." + sp + random.choice(end))


            if biome == "heaven":
                locenemy = random.choice(heaenemy)
                print (random.choice(heastarter) + sp + random.choice(adjective) + sp + locenemy + sp + random.choice(joining) + sp + locitem + "." + sp + random.choice(end))



            time.sleep(3)
            var10 = 0
            while var10 != 5:
                emove.append(random.choice(norm))
                var10 = var10 + 1



            if True:
                emove1s = random.choice(numbers)
                numbers.remove(emove1s)
                emove2s = random.choice(numbers)
                numbers.remove(emove2s)
                emove3s = random.choice(numbers)
                numbers.remove(emove3s)
                emove4s = random.choice(numbers)
                numbers.remove(emove4s)
                emove5s = random.choice(numbers)
                numbers.append(emove1s)
                numbers.append(emove2s)
                numbers.append(emove3s)
                numbers.append(emove4s)
                strength1 = random.choice(numbers)
                numbers.remove(strength1)
                strength2 = random.choice(numbers)
                numbers.remove(strength2)
                strength3 = random.choice(numbers)
                numbers.remove(strength3)
                strength4 = random.choice(numbers)
                numbers.remove(strength4)
                strength5 = random.choice(numbers)
                numbers.append(strength1)
                numbers.append(strength2)
                numbers.append(strength3)
                numbers.append(strength4)
                numbers.append(strength5)


            var4 = 0
            while var4 != 1:
                curweap1.append(random.choice(modify))
                curweap1.append(random.choice(weapon))
                main = random.choice(number) + random.choice(number)
                while main >= 11:
                    main = 0
                    main = random.choice(number) + random.choice(number)

                while 3 >= main:
                    main = 0
                    main = random.choice(number) + random.choice(number)
                    while main >= 11:
                        main = 0
                        main = random.choice(number) + random.choice(number)
                y = random.choice(number)
                sec1 = y
                while sec1 >= main:
                    sec1 = 0
                    y = random.choice(number)
                    sec1 = y

                number.remove(y)
                sec2 = random.choice(number)
                while sec2 >= main:
                    sec2 = 0
                    sec2 = random.choice(number)

                if sec1 > sec2:
                    r = 1
                else:
                    r = 2
                if sec1 <= 2:
                    sec1 = sec1 + 1
                if sec2 <= 2:
                    sec2 = sec1 + 1
                if sec1 == main:
                    main = main + 1
                if sec2 == main:
                    main = main + 1


                ### I SPENT LIKE 30 MINUTES ADDING IN THE LINE BELOW,IT WAS A THICC BUG
                number.append(y)
                ### XD

                oth1 = random.choice(number)
                oth2 = random.choice(number)
                if r == 1:
                    while oth1 >= sec2:
                        oth1 = random.choice(number) - 1

                    while oth2 >= sec2:
                        oth2 = random.choice(number) - 1


                elif r == 2:
                    while oth1 >= sec1:
                        oth1 = random.choice(number) - 1

                    while oth2 >= sec1:
                        oth2 = random.choice(number) - 1


                enemystat.append(main)
                enemystat.append(sec1)
                enemystat.append(sec2)
                enemystat.append(oth1)
                enemystat.append(oth2)
                var4 = 1

            ehp = random.choice(number)*10 + random.choice(number)
            print("The "+locenemy + " has " + str(ehp) + " hp!")
            ### NOT IN USE VAR var2 = 0
            print("Type 'moves' to see your moves during battle!")


            ### FIGHT SEQUENCE
            while True:
                if ehp <= 0:
                    break
                elif hp <= 0:
                    break
                time.sleep(3)
                move = input("What move will you do? (number) ")
                if move == "moves":



                    time.sleep(1)
                    print("Your " + curweap2[0] + sp + curweap2[1] + " has the following stats:")
                    time.sleep(2)
                    print(stat1 + ": " +str(stats[stat1]))
                    time.sleep(1)
                    print(stat2 + ": " +str(stats[stat2]))
                    time.sleep(1)
                    print(stat3 + ": " +str(stats[stat3]))
                    time.sleep(1)
                    print(stat4 + ": " +str(stats[stat4]))
                    time.sleep(1)
                    print(stat5 + ": " +str(stats[stat5]))
                    time.sleep(1)
                    move = input("What move will you do? (number) ")
                if move == "1":
                    if strength1 == 1:
                        print("The move "+ stat1+ " from your "+ curweap2[1]+" was ineffective against the "+ locenemy+"!")
                    elif strength1 == 2:
                        print("The move "+ stat1+ " from your "+ curweap2[1]+" was slightly effective against the "+ locenemy+"!")
                        locstat = stats[stat1]
                        locstat = int(locstat)
                        locstat = locstat/2
                        locstat = int(locstat)
                        ehp = ehp - locstat
                    elif strength1 == 3:
                        print("The move "+ stat1+ " from your "+ curweap2[1]+" was effective against the "+ locenemy+"!")
                        locstat = stats[stat1]
                        locstat = int(locstat)
                        ehp = ehp - locstat
                    elif strength1 == 4:
                        print("The move "+ stat1+ " from your "+ curweap2[1]+" was very effective against the "+ locenemy+"!")
                        locstat = stats[stat1]
                        locstat = int(locstat)
                        locstat = locstat+locstat
                        ehp = ehp - locstat
                    elif strength1 == 5:
                        print("The move "+ stat1+ " from your "+ curweap2[1]+" was extremely effective against the "+ locenemy+"!")
                        locstat = stats[stat1]
                        locstat = int(locstat)
                        locstat = locstat+locstat+locstat
                        ehp = ehp - locstat
                elif move == "2":
                    if strength2 == 1:
                        print("The move "+ stat2+ " from your "+ curweap2[1]+" was ineffective against the "+ locenemy+"!")
                    elif strength2 == 2:
                        print("The move "+ stat2+ " from your "+ curweap2[1]+" was slightly effective against the "+ locenemy+"!")
                        locstat = stats[stat2]
                        locstat = int(locstat)
                        locstat = locstat/2
                        locstat = int(locstat)
                        ehp = ehp - locstat
                    elif strength2 == 3:
                        print("The move "+ stat2+ " from your "+ curweap2[1]+" was effective against the "+ locenemy+"!")
                        locstat = stats[stat2]
                        locstat = int(locstat)
                        ehp = ehp - locstat
                    elif strength2 == 4:
                        print("The move "+ stat2+ " from your "+ curweap2[1]+" was very effective against the "+ locenemy+"!")
                        locstat = stats[stat2]
                        locstat = int(locstat)
                        locstat = locstat+locstat
                        ehp = ehp - locstat
                    elif strength2 == 5:
                        print("The move "+ stat2+ " from your "+ curweap2[1]+" was extremely effective against the "+ locenemy+"!")
                        locstat = stats[stat2]
                        locstat = int(locstat)
                        locstat = locstat+locstat+locstat
                        ehp = ehp - locstat
                elif move == "3":
                    if strength3 == 1:
                        print("The move "+ stat3+ " from your "+ curweap2[1]+" was ineffective against the "+ locenemy+"!")
                    elif strength3 == 2:
                        print("The move "+ stat3+ " from your "+ curweap2[1]+" was slightly effective against the "+ locenemy+"!")
                        locstat = stats[stat3]
                        locstat = int(locstat)
                        locstat = locstat/2
                        locstat = int(locstat)
                        ehp = ehp - locstat
                    elif strength3 == 3:
                        print("The move "+ stat3+ " from your "+ curweap2[1]+" was effective against the "+ locenemy+"!")
                        locstat = stats[stat3]
                        locstat = int(locstat)
                        ehp = ehp - locstat
                    elif strength3 == 4:
                        print("The move "+ stat3+ " from your "+ curweap2[1]+" was very effective against the "+ locenemy+"!")
                        locstat = stats[stat3]
                        locstat = int(locstat)
                        locstat = locstat+locstat
                        ehp = ehp - locstat
                    elif strength3 == 5:
                        print("The move "+ stat3+ " from your "+ curweap2[1]+" was extremely effective against the "+ locenemy+"!")
                        locstat = stats[stat3]
                        locstat = int(locstat)
                        locstat = locstat+locstat+locstat
                        ehp = ehp - locstat
                elif move == "4":
                    if strength4 == 1:
                        print("The move "+ stat4+ " from your "+ curweap2[1]+" was ineffective against the "+ locenemy+"!")
                    elif strength4 == 2:
                        print("The move "+ stat4+ " from your "+ curweap2[1]+" was slightly effective against the "+ locenemy+"!")
                        locstat = stats[stat4]
                        locstat = int(locstat)
                        locstat = locstat/2
                        locstat = int(locstat)
                        ehp = ehp - locstat
                    elif strength4 == 3:
                        print("The move "+ stat4+ " from your "+ curweap2[1]+" was effective against the "+ locenemy+"!")
                        locstat = stats[stat4]
                        locstat = int(locstat)
                        ehp = ehp - locstat
                    elif strength4 == 4:
                        print("The move "+ stat4+ " from your "+ curweap2[1]+" was very effective against the "+ locenemy+"!")
                        locstat = stats[stat4]
                        locstat = int(locstat)
                        locstat = locstat+locstat
                        ehp = ehp - locstat
                    elif strength4 == 5:
                        print("The move "+ stat4+ " from your "+ curweap2[1]+" was extremely effective against the "+ locenemy+"!")
                        locstat = stats[stat4]
                        locstat = int(locstat)
                        locstat = locstat+locstat+locstat
                        ehp = ehp - locstat
                elif move == "5":
                    if strength5 == 1:
                        print("The move "+ stat5+ " from your "+ curweap2[1]+" was ineffective against the "+ locenemy+"!")
                    elif strength5 == 2:
                        print("The move "+ stat5+ " from your "+ curweap2[1]+" was slightly effective against the "+ locenemy+"!")
                        locstat = stats[stat5]
                        locstat = int(locstat)
                        locstat = locstat/2
                        locstat = int(locstat)
                        ehp = ehp - locstat
                    elif strength5 == 3:
                        print("The move "+ stat5+ " from your "+ curweap2[1]+" was effective against the "+ locenemy+"!")
                        locstat = stats[stat5]
                        locstat = int(locstat)
                        ehp = ehp - locstat
                    elif strength5 == 4:
                        print("The move "+ stat5+ " from your "+ curweap2[1]+" was very effective against the "+ locenemy+"!")
                        locstat = stats[stat5]
                        locstat = int(locstat)
                        locstat = locstat+locstat
                        ehp = ehp - locstat
                    elif strength5 == 5:
                        print("The move "+ stat5+ " from your "+ curweap2[1]+" was extremely effective against the "+ locenemy+"!")
                        locstat = stats[stat5]
                        locstat = int(locstat)
                        locstat = locstat+locstat+locstat
                        ehp = ehp - locstat

                time.sleep(3)
                if ehp <= 0:
                    break
                elif hp <= 0:
                    break
                if random.choice(number) == 1:
                    time.sleep(3)
                    print("The enemy seems to have reformed itself!")
                    emove1s = random.choice(numbers)
                    numbers.remove(emove1s)
                    emove2s = random.choice(numbers)
                    numbers.remove(emove2s)
                    emove3s = random.choice(numbers)
                    numbers.remove(emove3s)
                    emove4s = random.choice(numbers)
                    numbers.remove(emove4s)
                    emove5s = random.choice(numbers)
                    numbers.append(emove1s)
                    numbers.append(emove2s)
                    numbers.append(emove3s)
                    numbers.append(emove4s)
                    strength1 = random.choice(numbers)
                    numbers.remove(strength1)
                    strength2 = random.choice(numbers)
                    numbers.remove(strength2)
                    strength3 = random.choice(numbers)
                    numbers.remove(strength3)
                    strength4 = random.choice(numbers)
                    numbers.remove(strength4)
                    strength5 = random.choice(numbers)
                    numbers.append(strength1)
                    numbers.append(strength2)
                    numbers.append(strength3)
                    numbers.append(strength4)
                    numbers.append(strength5)


                enemymove = random.choice(emove)
                print("The "+locenemy + " has " + str(ehp) + " hp remaining!")
                time.sleep(3)
                if enemymove == emove[0]:
                    if emove1s == 1:
                        print("The enemies move "+ emove[0]+ " was ineffective against you!")
                    elif emove1s == 2:
                        print("The enemies move "+ emove[0]+ " was slightly effective against you!")
                        locstat = enemystat[0]
                        locstat = int(locstat)
                        locstat = locstat/2
                        locstat = int(locstat)
                        hp = hp - locstat
                    elif emove1s == 3:
                        print("The enemies move "+ emove[0]+ " was effective against you!")
                        locstat = enemystat[0]
                        locstat = int(locstat)
                        hp = hp - locstat
                    elif emove1s == 4:
                        print("The move "+ emove[0]+ " was very effective against you!")
                        locstat = enemystat[0]
                        locstat = int(locstat)
                        locstat = locstat+locstat
                        hp = hp - locstat
                    elif emove1s == 5:
                        print("The move "+ emove[0]+ " was extremely effective against you!")
                        locstat = enemystat[0]
                        locstat = int(locstat)
                        locstat = locstat+locstat+locstat
                        hp = hp - locstat
                elif enemymove == emove[1]:
                    if emove2s == 1:
                        print("The enemies move "+ emove[1]+ " was ineffective against you!")
                    elif emove2s == 2:
                        print("The enemies move "+ emove[1]+ " was slightly effective against you!")
                        locstat = enemystat[1]
                        locstat = int(locstat)
                        locstat = locstat/2
                        locstat = int(locstat)
                        hp = hp - locstat
                    elif emove2s == 3:
                        print("The enemies move "+ emove[1]+ " was effective against you!")
                        locstat = enemystat[1]
                        locstat = int(locstat)
                        hp = hp - locstat
                    elif emove2s == 4:
                        print("The move "+ emove[1]+ " was very effective against you!")
                        locstat = enemystat[1]
                        locstat = int(locstat)
                        locstat = locstat+locstat
                        hp = hp - locstat
                    elif emove2s == 5:
                        print("The move "+ emove[1]+ " was extremely effective against you!")
                        locstat = enemystat[1]
                        locstat = int(locstat)
                        locstat = locstat+locstat+locstat
                        hp = hp - locstat
                elif enemymove == emove[2]:
                    if emove3s == 1:
                        print("The enemies move "+ emove[2]+ " was ineffective against you!")
                    elif emove3s == 2:
                        print("The enemies move "+ emove[2]+ " was slightly effective against you!")
                        locstat = enemystat[2]
                        locstat = int(locstat)
                        locstat = locstat/2
                        locstat = int(locstat)
                        hp = hp - locstat
                    elif emove3s == 3:
                        print("The enemies move "+ emove[2]+ " was effective against you!")
                        locstat = enemystat[2]
                        locstat = int(locstat)
                        hp = hp - locstat
                    elif emove3s == 4:
                        print("The move "+ emove[2]+ " was very effective against you!")
                        locstat = enemystat[2]
                        locstat = int(locstat)
                        locstat = locstat+locstat
                        hp = hp - locstat
                    elif emove3s == 5:
                        print("The move "+ emove[2]+ " was extremely effective against you!")
                        locstat = enemystat[2]
                        locstat = int(locstat)
                        locstat = locstat+locstat+locstat
                        hp = hp - locstat
                elif enemymove == emove[3]:
                    if emove4s == 1:
                        print("The enemies move "+ emove[3]+ " was ineffective against you!")
                    elif emove4s == 2:
                        print("The enemies move "+ emove[3]+ " was slightly effective against you!")
                        locstat = enemystat[3]
                        locstat = int(locstat)
                        locstat = locstat/2
                        locstat = int(locstat)
                        hp = hp - locstat
                    elif emove4s == 3:
                        print("The enemies move "+ emove[3]+ " was effective against you!")
                        locstat = enemystat[3]
                        locstat = int(locstat)
                        hp = hp - locstat
                    elif emove4s == 4:
                        print("The move "+ emove[3]+ " was very effective against you!")
                        locstat = enemystat[3]
                        locstat = int(locstat)
                        locstat = locstat+locstat
                        hp = hp - locstat
                    elif emove4s == 5:
                        print("The move "+ emove[3]+ " was extremely effective against you!")
                        locstat = enemystat[3]
                        locstat = int(locstat)
                        locstat = locstat+locstat+locstat
                        hp = hp - locstat
                elif enemymove == emove[4]:
                    if emove5s == 1:
                        print("The enemies move "+ emove[4]+ " was ineffective against you!")
                    elif emove5s == 2:
                        print("The enemies move "+ emove[4]+ " was slightly effective against you!")
                        locstat = enemystat[4]
                        locstat = int(locstat)
                        locstat = locstat/2
                        locstat = int(locstat)
                        hp = hp - locstat
                    elif emove5s == 3:
                        print("The enemies move "+ emove[4]+ " was effective against you!")
                        locstat = enemystat[4]
                        locstat = int(locstat)
                        hp = hp - locstat
                    elif emove5s == 4:
                        print("The move "+ emove[4]+ " was very effective against you!")
                        locstat = enemystat[4]
                        locstat = int(locstat)
                        locstat = locstat+locstat
                        hp = hp - locstat
                    elif emove5s == 5:
                        print("The move "+ emove[4]+ " was extremely effective against you!")
                        locstat = enemystat[4]
                        locstat = int(locstat)
                        locstat = locstat+locstat+locstat
                        hp = hp - locstat
                time.sleep(3)
                if ehp <= 0:
                    break
                elif hp <= 0:
                    vbreak
                print("You have " + str(hp) + " hp out of "+ str(hpcap)+" hp left!")
                hp = int(hp)
                print("  ")
            ### VERY IMPORTANT!


            time.sleep(3)
            enemystat.remove(main)
            enemystat.remove(sec1)
            enemystat.remove(sec2)
            enemystat.remove(oth1)
            enemystat.remove(oth2)
            if ehp <= 0:
                print ("You won!")
                time.sleep(3)

                ###Gen
                num = random.choice(number)
                goldN = random.choice(number)

                ###Enemy drop
                if num >= 8: #8
                    ### Weapon
                    curweap1.append(random.choice(modify))
                    curweap1.append(random.choice(weapon))

                    print("The enemy dropped a " + curweap1[0] + sp + curweap1[1] + ". You also find " +str(goldN) + " gold coins " + random.choice(body) + " the monster")
                    gold = gold + int(goldN)
                    while hasgem == 0:
                        if random.choice(number) >= 5:
                            if locitem == "a jewel encrusted attire":
                                print("Within the jewel encrusted attire you have found an Emerald! It has been added to you collection")
                                collection.append(collectionfull[1])
                                hasgem = 1



                    ### STAT GENERATION
                    main = random.choice(number) + random.choice(number)
                    while main >= 11:
                        main = 0
                        main = random.choice(number) + random.choice(number)

                    while 3 >= main:
                        main = 0
                        main = random.choice(number) + random.choice(number)
                        while main >= 11:
                            main = 0
                            main = random.choice(number) + random.choice(number)





                    y = random.choice(number)
                    sec1 = y
                    while sec1 >= main:
                        sec1 = 0
                        y = random.choice(number)
                        sec1 = y

                    number.remove(y)
                    sec2 = random.choice(number)
                    while sec2 >= main:
                        sec2 = 0
                        sec2 = random.choice(number)

                    if sec1 > sec2:
                        r = 1
                    else:
                        r = 2
                    if sec1 <= 2:
                        sec1 = sec1 + 1
                    if sec2 <= 2:
                        sec2 = sec1 + 1
                    if sec1 == main:
                        main = main + 1
                    if sec2 == main:
                        main = main + 1


                    ### I SPENT LIKE 30 MINUTES ADDING IN THE LINE BELOW, IT WAS A THICC BUG
                    number.append(y)
                    ### XD

                    oth1 = random.choice(number)
                    oth2 = random.choice(number)
                    if r == 1:
                        while oth1 >= sec2:
                            oth1 = random.choice(number) - 1

                        while oth2 >= sec2:
                            oth2 = random.choice(number) - 1


                    elif r == 2:
                        while oth1 >= sec1:
                            oth1 = random.choice(number) - 1

                        while oth2 >= sec1:
                            oth2 = random.choice(number) - 1





                    main = str(main)
                    sec1 = str(sec1)
                    sec2 = str(sec2)
                    oth1 = str(oth1)
                    oth2 = str(oth2)
                    mainA = random.choice(norm)
                    norm.remove (mainA)
                    sec1A = random.choice(norm)
                    norm.remove (sec1A)
                    sec2A = random.choice(norm)
                    norm.remove (sec2A)
                    oth1A = random.choice(norm)
                    norm.remove (oth1A)
                    oth2A = random.choice(norm)
                    norm.remove (oth2A)
                    print(mainA + " is a primary move with " + main + " levels!")
                    print(sec1A + " is a secondary move with " + sec1 + " levels!")
                    print(sec2A + " is a secondary move with " + sec2 + " levels!")
                    print(oth1A + " is a normal move with " + oth1 + " levels!")
                    print(oth2A + " is a normal move with " + oth2 + " levels!")

                    norm.append (mainA)
                    norm.append (sec1A)
                    norm.append (sec2A)
                    norm.append (oth1A)
                    norm.append (oth2A)
                    keep = input("Do you want to keep this weapon? (y/n) ")
                    if keep == "y":
                        curweap2.append(curweap1[0])
                        curweap2.append(curweap1[1])
                        stat1 = mainA
                        stat2 = sec1A
                        stat3 = sec2A
                        stat4 = oth1A
                        stat5 = oth2A
                        stat6 = main
                        stat7 = sec1
                        stat8 = sec2
                        stat9 = oth1
                        stat10 = oth2


                    stats = {


                    stat1: stat6,

                    stat2: stat7,

                    stat3: stat8,

                    stat4: stat9,

                    stat5: stat10

                    }

                elif num >= 2:

                    print("You found " + str(goldN) + " gold " + random.choice(body) + " of the monster")

                    gold = gold + int(goldN)
                else:
                    print("Sadly nothing was dropped")
            else:
                print ("you died and lost 1 life!")
                life = life - 1
                if life == 0:
                    print("You have 0 lives left. The game is over")
                    quit()
                elif life <= 3:
                    print("Watch out! You only have " + str(life) + " lives left!")
                    life = int(life)
        elif start == "help":
            print("The following commands are available in the current build:")
            print("fight")
            print("stats")
            print("game_end")
            print("upgrade")
            print("shop")
            print("changelog")
            print("collection")
            print("The following commands will be added in the next patch:")
            print("biome")
        elif start == "stats":
            print("What stats do you wish to see?")
            print("Weapon")
            print("Life")
            print("Gold")
            stats2 = input("   ")
            if stats2 == "weapon":
                time.sleep(1)
                print("Your " + curweap2[0] + sp + curweap2[1] + " has the following stats:")
                time.sleep(2)
                print(stat1 + ": " +str(stats[stat1]))
                time.sleep(1)
                print(stat2 + ": " +str(stats[stat2]))
                time.sleep(1)
                print(stat3 + ": " +str(stats[stat3]))
                time.sleep(1)
                print(stat4 + ": " +str(stats[stat4]))
                time.sleep(1)
                print(stat5 + ": " +str(stats[stat5]))
                time.sleep(1)
            elif stats2 == "gold":
                time.sleep(1)
                print("You have " + str(gold) + " gold.")
                gold = int(gold)
            elif stats2 == "life":
                print("You have "+str(life)+" lives left!")
                life = int(life)
        elif start == "upgrade":
            time.sleep(1)
            if gold >= 10:
                upgrade = input("which move do you want to upgrade (number)")
                if upgrade == "1":
                    stats[stat1] = stats[stat1] + 1
                    gold = gold - 10
                if upgrade == "2":
                    stats[stat2] = stats[stat2] + 1
                    gold = gold - 10
                if upgrade == "3":
                    stats[stat3] = stats[stat3] + 1
                    gold = gold - 10
                if upgrade == "4":
                    stats[stat4] = stats[stat4] + 1
                    gold = gold - 10
                if upgrade == "5":
                    stats[stat5] = stats[stat5] + 1
                    gold = gold - 10
                time.sleep(2)
                print("You have "+ str(gold) + " left")
                gold = int(gold)
            else:
                goldN = 10 - gold
                print("You need " + str(goldN)+ " more gold to upgrade moves")
        elif start == "game_end":
            print("You have quit the game. These are your final stats:")
            time.sleep(2)
            print("Gold: "+ str(gold))
            time.sleep(2)
            print("HP: " +str(hp))
            time.sleep(2)
            print("Lives: "+ str(life))
            time.sleep(2)
            print("Stats: " )
            time.sleep(1)
            print(stat1 + ": " +str(stats[stat1]))
            time.sleep(1)
            print(stat2 + ": " +str(stats[stat2]))
            time.sleep(1)
            print(stat3 + ": " +str(stats[stat3]))
            time.sleep(1)
            print(stat4 + ": " +str(stats[stat4]))
            time.sleep(1)
            print(stat5 + ": " +str(stats[stat5]))
            time.sleep(2)
            print("Weapon: " + curweap2[0] + sp + curweap2[1])
            time.sleep(2)
            print("Thanks for playing!")
            time.sleep(2)
            quit()
        elif start == "shop":
            time.sleep(2)
            print("Type 'help (item)' to learn more about any item in the shop!")
            time.sleep(2)
            print("Type '(item)' to buy any item in the shop! (In this patch this is case sensitive)")
            time.sleep(2)
            print(" ")
            print("SHOP")
            print(" ")
            print(shoplife + ": " + str(shoplifeg)+ " gold")

            if boughtsapphire == 0:
                print(" ")
                print("Sapphire: 50 gold")

            print(" ")



            time.sleep(3)
            buy = "a"
            while True:
                print(" ")
                buy = input("What item do you wish to buy? Type back to go 'back' to menu ")
                time.sleep(2)


                if buy == shoplife:
                    if shoplifeg > gold:
                        print("You do not have enough gold to purchase this item")
                        time.sleep(2)
                    else:
                        gold = gold - shoplifeg
                        life = life + 1
                        print("You have bought 1 "+ shoplife + "!")
                        time.sleep(2)
                elif buy == ("help "+shoplife):
                    print("For a price of only "+str(shoplifeg)+" gold, the " +shoplife+ " will give you an extra life!")
                elif buy == "Sapphire":
                    if boughtsapphire == 0:
                        if 50 > gold:
                            print("You do not have enough gold to purchase this item")
                            time.sleep(2)
                        else:
                            collection.append(collectionfull[0])
                            boughtsapphire = 1
                            print("You have bought the Sapphire!")
                            time.sleep(2)
                    else:
                        print("That item has been sold out")
                        time.sleep(2)
                elif buy == "help Sapphire":
                    print("It has a sparkle like the ocean blue, when bought you can check it out in your collection!")


                elif buy == "back":
                    break
                else:
                    print("That was not a valid item!")
        elif start == "changelog":
            update = input("Update? (for e.g 0.3)")
            if update == "0.3":
                print("0.3:")
                print("Desert biome")
                print("Name generator")
                print("Made stats names much more expansive")
                print("Enemies and you can change strengths and weaknesses during fights")
                print("Altered drop chance")
                print("Created shop")
                print("Created changelog")
                print("Created game_end")
                print("Fixed 2 bugs that occured when fighting (attacks didnt work and enemies attack equaled your attack)")
                print("Added more to snow biome")
                print("Ability to check moves during battle")
                print("Created changelog")
            if update == "0.4":
                print("Added Heaven and Hell biomes")
                print("Created the collection, an area where you keep precious minerals that you find")
                print("Added more flavour lines during fights")
                print("Created a mulititude of new lines in many lists")
                print ("Added hidden minerals in the game to collect")
        elif start == "collection":

            if len(collection) == 0:
                print("You have not yet collected any minerals!")
            else:
                print("You have collected the following minerals:")
                for i in collection:

                    print(i)
            i = len(collectionfull) - len(collection)
            print("You have " +str(i)+" minerals left to collect")
        else:
            print("That was not a valid command. Type 'help' for more information!")
