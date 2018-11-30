import random
import time

# GENERATION STUFF
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = [1, 2, 3, 4, 5]

### DEFINITIONS

#sound = Sound()
#sound.read('sound.wav')
#sound.play()


### STORY STUFF
sp = " "

norm1 = ["Icy" , "Fiery" , "Angelic", "Soul", "Quick", "Explosive", "Sandy", "Demonic", "Poisonious", "Windy", "Bloody", "Flaming", "Snowy", "Frozen", "Lightning", "Deadly", "Venomous", "Disabling", "Riptide",
"Flying", "Whirling","Acidic","Slimy"]
norm2 = ["Strike", "Jab", "Spin", "Thrust", "Summon", "Barrage", "Offensive", "Onslaught", "Violation", "Assualt", "Enroachment", "Smash", "Devasation", "Tormentation", "Paralysis", "Demolition", "Blaze"]

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


### USE THIS CODE TO SHOW OF HOW MANY POSSIBLE NAMES FOR WEAPONS THERE ARE!
#x = 0
#for i in norm:
#    print(norm[x])
#    x = x + 1



### NAMES

namepre = ["the Courageous", "the Charismatic", "the Intelligent", "the Elder", "the Wise", "the Wealthy", "the Normal", "the Charming", "the Kind", "the Selfless", "the Young"]


### UP TO VAR10


biomes = ["polar", "desert", "underworld", "niravana", "mountain", "random"]
norbiome = ["polar", "desert", "mountain"]
norbiomefull = ["polar", "desert", "mountain"]
divbiome = ["underworld", "niravana"]
#undbiome = [] Not going to be added in foreseable future


### ICE
icestarter = ["Through the blizzard you see movement. It comes closer. You can see clearly now. Its",
"Through the arachaic snow you see a wooden shack, as you enter you see a lifeless body slumped on the floor with blood oozing out of it. Next to the body is"]


iceenemy = ["penguin", "snow elemental", "polar bear", "Eskimo", "husky", "fox", "ice elemental", "ermine"]


### desert
desstarter = ["The sun beats down on you as you trudge through the endless miles of course sand. In the distance you see an object approaching. After wiping the sand out of your eyes it becomes apparent. Its",
"As you take shelter in a pyramid, ecscaping the blazing sun you look behind you. Oh No. Its",
"As you approach an oasis surrounded by an ineffable amount of desolate terrain you, look into the deep and clear blue water, getting ready to quench your thrist. Thats when you see something unbelivable. Its"]


desenemy = ["vulture", "sand worm", "mummy", "armadillo", "kangaroo", "scorpion", "scarab beetle", "desert elemental", "viper", "jerboa", "camel"]

###mountain

moustarter = ["*BANG* You here the thundering sound of what you assume to be a boulder crashing down the mountain path. As you look up to examine the size of the boulder the realization comes. Its not a boulder. Its",
"Up above, standing on a narrow ledge of the mountain shrowded in darkness from the night sky, you see something strange. It seems to be"]

mouenemy = ["rock elemental", "alpaca", "llama", "mountain goat", "moutain leopard", "tahr", "chiru", "kiang", "gazelle", "yak"]
### hell

helstarter = ["The chaotic screams and magma bubbling below you fill your ears as you traverse through the crimson caves, littered with skulls. As you turn the corner of the cave you become startled. Its",
"As you ignore the endless shrieks, you sail through the rough magma rapids on your bone boat looking for enough food to make it to the next day. All of a sudden, emerging from the red rapids below you is",]


helenemy = ["medusa", "severed head", "reaper", "hellhound", "tortured soul", "gremlin"]
### HEAVEN

heastarter = ["Your ears are filled with the gorgeous melody of harps in unison as you frolick over the vast clouds. The tranquility will never end-- Your thoughts are cut off by a most grotesque being appearing. Its",
"Tender, pure or perhaps luscious are just a handful of words that hardly do the duty of describing the luxurious place that you are in, and nothing could ever take away from that beauty. That is what you think until you encounter the unthinkable. Its",

]

heaenemy = ["lost soul", "arch angel", "seraph", "disciple", "fairy", "cherub"]


end = ["", "", "", "", "A shiver goes down your spine", "It lurches forward", "It jerks forward", "A cold wind brushes against your face"]

item = ["a jewel encrusted attire", "a cloak", "a gown", "armour", "silk woven fabrics", "a deadly aura", "a garb" ]

adjective = ["a glowing", "a black", "a white", "a bloodthirsty", "an undead", "a rouge", "a starved", "a staggering", "a fear inducing", "a nimble"]

joining = ["enshrined in", "wearing", "smothered in", "bearing", "covered top to bottom in"]

body = ["inside the carcass of", "within the body of", "entrenched in the stomach of", "in a bag near", "deep inside", "close to"]

adj2 = ["crushing", "stunning", "epic", "awesome", "incredible", "legendary", "awe inspiring", "fabulous", "tremendous", "unbelievable"]

adj3 = ["battered", "exhuasted", "wounded", "bruised", "injured", "disfigured", "disheartened"]
### SHOP STUFF

shopobject = ["Orb", "Potion", "Ring", "Keys", "Shard", "Tablet"]
shopadjlife = ["of Healing", "of Life", "of Essence"]
lifeshop = []
lifeshop.append(random.choice(shopobject))
lifeshop.append(random.choice(shopadjlife))

shopobject.remove(lifeshop[0])
shopadjlife.remove(lifeshop[1])



shoplife = (lifeshop[0] + sp + lifeshop[1])
shoplifeg = 0
while shoplifeg <= 14:
    shoplifeg = random.choice(number)*random.choice(number)-random.choice(number)

boughtsapphire = 0

shophp = (random.choice(shopobject) + sp + random.choice(shopadjlife))
shophpg = 0
while shophpg <= 14:
    shophpg = random.choice(number)*random.choice(number)-random.choice(number)

###COLLECTION

collection = []
collectionfull = ["Sapphire", "Emerald", "Ruby", "Topaz"]#, "Topaz"]
hasgem = 0
hastopaz = 0


hasboughtaruby = 0
gold = 0
goldN = 0
num = 0
### CHECKER VARIABLES


weapon = ["axe", "broad-sword", "katana", "knife", "dagger", "wand", "scythe", "club", "mace", "long-bow", "pike", "lance", "flail", "long-sword", "short-sword", "hallberd", "cross-bow", "glaive", "falchion",
"morning-star", "hatchet", "trident", "javelin", "spear", "saber", "rapier"]

modify = ["enchanted", "mysterious", "dangerous", "sharp", "cursed", "glowing", "blunt", "ghastly", "jagged", "murderous"]

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
life = 3
hpcap = 100
hp = 100
ehp = 0
emove = []
enemystat = []
cantravel = False

#devmode = (joshua please do not play the game with this on! if you must please do it after youve played it normally a couple of time. to turn it on replace this message with '1')



### CHANGING THE TIMES CAN RUIN THE GAMES ATMOSPHERE
timer1 = 0.4

timer2 = 1

timer3 = 1.3


buildings = ["a tannery","a tradepost","a blacksmith","a church","a library","a townhall","a hut","a hut","a hut","a smokehouse","a barracks","an armoury"]

builditems = ["a chair","a carpet","a bookshelf","an armour stand","a chest","the furnace","a table","the stairs","a stash of weapons"]

buildnear = ["near","under","close to","next to","adjacent to"]

searching = ["exploring","searching","looking in","examining","inspecting"]

travar = ["You see a small hamlet in the distance",
"The wind russles your wagon",
"You notice a pile of " +random.choice(shopobject)+"s sharing the wagon with you",
"Your stomach rumbles, are we there yet?",
"A sea of trees dance outside the wagon window",
"Your ears are filled with the near endless 'neighs' of the horses",
"*BUMP* you hit a rock",
"You tap your fingers on the bottom of the wagon to both aleviate the boredom and to create a rythm. Tap. Tap Tap. Tap Tap Tap Tap. T-Tap.",
"You are jolted from your sleep after the wagon bumped something underneath",
"In the corner you see a "+ random.choice(weapon) + ". I wonder if its better than yours",
"You spot a cloud that looks like a duck, and one that looks like a horse and one that resembles a Panzerkampfwagen IV with an enlargened StuG III gun",
"Your fingers brush against the coarse wooden walls",
"Zzz Zzz Zzz",
"You ponder lifes deepest questions",
"You reminisce on the " + random.choice(adj2) + " fights you have been in"]



### BEGIN ACTUAL GAME!!!


name = input("What is your name young adventurer? ")
#while name:
#    time.sleep(timer2)
#    print("That is not a valid name")
#    time.sleep(timer1)
#    name = input("What is your name young adventurer? ")
while name == "":
    time.sleep(timer2)
    print("That was not a valid name!")
    time.sleep(timer2)
    print(" ")
    name = input("What is your name young adventurer? ")

name = list(name)
name[0] = name[0].upper()
name = "".join(name)
name = name + sp + random.choice(namepre)






time.sleep(timer1)
biome = input("Which biome will you adventure in? (Type help for a list) ").lower()
while True:
    if biome in biomes:
        break
    elif biome == "help":
        time.sleep(timer1)
        print ("Biomes in the current build are:")
        time.sleep(timer1)
        print ("Polar")
        time.sleep(timer1)
        print ("Desert")
        time.sleep(timer1)
        print("Mountain")
        time.sleep(timer1)
        print ("Underworld")
        time.sleep(timer1)
        print ("Niravana")
        time.sleep(timer1)
        print ("Random")
        print(" ")
        time.sleep(timer2)
        biome = input("Which biome will you adventure in? ").lower()

    else:
        time.sleep(timer1)
        print("That biome was invalid, type help for a list of biomes in this build!")
        time.sleep(timer2)
        print(" ")
        biome = input("Which biome will you adventure in? ").lower()
if biome == "random":
    while biome == "random":
        biome = random.choice(biomes)
time.sleep(timer2)
print("   ")
time.sleep(timer2)
print("As you enter a "+ biome+ " biome, you see a weapon lying by a tree!")
time.sleep(timer3)
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
    print("It seems to be a " + curweap2[0] +sp+ curweap2[1]+"!")
    time.sleep(timer2)
    print("After experimenting with the " + curweap2[1]+(" you find that it has several special abilites!"))
    time.sleep(timer2)
    print(mainA + " is a primary move with " + main + " levels!")
    time.sleep(timer2)
    print(sec1A + " is a secondary move with " + sec1 + " levels!")
    time.sleep(timer2)
    print(sec2A + " is a secondary move with " + sec2 + " levels!")
    time.sleep(timer2)
    print(oth1A + " is a normal move with " + oth1 + " levels!")
    time.sleep(timer2)
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




    break

generatetravelnumber = True
if 1 ==1:
    time.sleep(timer2)
    print("    ")
    print("If you want to learn how to play type tutorial")
    time.sleep(timer2)
    print("If you already know how to play type skip")
    time.sleep(timer2)
    print("   ")
    while True:
        tutorial = input("Do you want to do tutorial or skip? ")
        time.sleep(timer2)
        if tutorial == "tutorial":
            whatlevel = input("Do you want this tutorial to go fully in depth about the features of this game or leave some to be explored? (depth/shallow) ")
            time.sleep(timer2)
            while True:
                if whatlevel == "depth":
                    break
                elif whatlevel == "shallow":
                    break
                else:
                    print("   ")
                    print("That was not a valid answer!")
                    time.sleep(timer2)
                    print("   ")
                    whatlevel = input("Do you want this tutorial to go fully in depth about the features of this game or leave some to be explored? (depth/shallow) ")
            time.sleep(timer2)

            print("There will be a wall of text so be prepared, please read it all thorougly to understand Reveles... ")
            time.sleep(timer3)

            print("    ")
            print("You will see a question soon after this tutorial asking as to what you want to do. Firstly keep in mind that the entire idea of this game is randomization meaning that each biome, enemy, weapon, building will be generated based on chance. Some of these randomized words and things to do you will only find in certain biomes or places.")
            time.sleep(timer3)
            time.sleep(timer3)
            time.sleep(timer3)
            time.sleep(timer3)
            time.sleep(timer3)
            time.sleep(timer3)
            time.sleep(timer3)
            time.sleep(timer3)
            time.sleep(timer3)
            time.sleep(timer3)
            print("     ")
            if whatlevel == "depth":
                print("The main feature of Reveles is the 'explore' command which gives the player the following chances:")
                time.sleep(timer3)
                time.sleep(timer2)
                print("2 in 5 chance of fighting an enemy")
                time.sleep(timer3)
                time.sleep(timer2)
                print("2 in 5 chance of finding a village/ruins/other and looting it")
                time.sleep(timer3)
                time.sleep(timer2)
                print("1 in 10 chance of getting stuck in a trap and loosing some hp")
                time.sleep(timer3)
                time.sleep(timer2)
                print("1 in 10 chance of transending dimensions (if your in a normal biome(e.g polar) you go to a special biome(e.g underworld) and vice versa)")
                time.sleep(timer3)
                time.sleep(timer3)
                time.sleep(timer3)
                print("     ")
            else:
                print("The explore command is the main feature of Reveles which has a variety of chances for different things to happen!")
            time.sleep(timer3)
            time.sleep(timer2)
            print("In terms of fighting it works as follows:")
            time.sleep(timer3)
            time.sleep(timer2)
            print("As seen from the weapon you just picked up, every weapon in Reveles has 5 randomly generated moves, each with a different value")
            time.sleep(timer3)
            time.sleep(timer3)
            time.sleep(timer2)
            print("For your specific weapon, the main move is: "+stat1 + " that has " +str(stats[stat1])+" attack damage")
            time.sleep(timer3)
            time.sleep(timer3)
            time.sleep(timer2)
            print("When fighting you will type '1','2','3','4' or '5' corresponding to the move number. For example the main move mentioned prior would be '1'. If you are ever confused what your moves are you can always type 'moves' during battle!")
            time.sleep(timer3)
            time.sleep(timer3)
            time.sleep(timer3)
            time.sleep(timer2)
            print("    ")
            print("There is also a collection system in Reveles in which you collect a variety of different minerals")
            time.sleep(timer3)
            time.sleep(timer2)
            time.sleep(timer3)
            if whatlevel == "depth":
                print("If you find at least one mineral and are in a normal biome then you will have the option to travel to other normal biomes for a price")
            else:
                print("If you find one be sure to keep it as something might happen if you're in the right place")
            time.sleep(timer3)
            time.sleep(timer2)
            time.sleep(timer3)
            print("To beat the game you must collect all 4 minerals. Though this is more of an achievment than a actual goal as there is no current reward")
            time.sleep(timer3)
            time.sleep(timer3)
            time.sleep(timer2)
            time.sleep(timer3)
            print("    ")
            print("Finally a shop exists where you can trade the gold you have for items that heal you or give you life")
            time.sleep(timer3)
            time.sleep(timer2)
            time.sleep(timer2)
            time.sleep(timer3)
            print("The rest can be figured out by playing the game...")
            time.sleep(timer3)
            time.sleep(timer2)

            print("So lets get right into it!")
            time.sleep(timer3)
            print("    ")



            break
        elif tutorial == "skip":
            time.sleep(timer2)
            print("Your adventure begins...")
            time.sleep(timer2)

            break
        else:
            time.sleep(timer2)
            print("That was not a valid response!")
            time.sleep(timer2)
    print ("Type 'help' if you dont know what to type!")
    print("   ")
    while True:

        ### THIS LINE DECIDES CRITEA OF TRAVELING!
        if len(collection) >= 1:
            if cantravel == False:
                if biome in norbiome:
                    time.sleep(timer2)
                    print("   ")
                    print("Wealthy traders have started coming to this region. They bear maps and information about lands far and wide in places unknown to you!")
                    time.sleep(timer2)
                    print("You have unlocked the 'travel' section of the menu!")
                    norbiome.remove(biome)
                    norranbiome = random.choice(norbiome)
                    norranbiomeg = 0
                    if generatetravelnumber == True:
                        while norranbiomeg <= 70:
                            norranbiomeg = random.choice(number)*random.choice(number)+random.choice(number)
                    generatetravelnumber = False
                    cantravel = True



        time.sleep(timer2)
        print(" ")
        start = input("What do you want to do now " + name + "? ").lower()
        print(" ")
        time.sleep(timer2)
        if start == "explore":
            time.sleep(timer3)
            rannum = random.choice(numbers)
            numbers = [1, 2, 3, 4, 5]
            if rannum >= 4:
                ### Biome
                locitem = random.choice(item)
                if biome == "polar":
                    locenemy = random.choice(iceenemy)
                    print (random.choice(icestarter) + sp + random.choice(adjective) + sp + locenemy + sp + random.choice(joining) + sp + locitem + "." + sp + random.choice(end))
                if biome == "desert":
                    locenemy = random.choice(desenemy)
                    print (random.choice(desstarter) + sp + random.choice(adjective) + sp + locenemy + sp + random.choice(joining) + sp + locitem + "." + sp + random.choice(end))
                if biome == "underworld":
                    locenemy = random.choice(helenemy)
                    print (random.choice(helstarter) + sp + random.choice(adjective) + sp + locenemy + sp + random.choice(joining) + sp + locitem + "." + sp + random.choice(end))
                if biome == "niravana":
                    locenemy = random.choice(heaenemy)
                    print (random.choice(heastarter) + sp + random.choice(adjective) + sp + locenemy + sp + random.choice(joining) + sp + locitem + "." + sp + random.choice(end))
                if biome == "mountain":
                    locenemy = random.choice(mouenemy)
                    print (random.choice(moustarter) + sp + random.choice(adjective) + sp + locenemy + sp + random.choice(joining) + sp + locitem + "." + sp + random.choice(end))

                time.sleep(timer3)
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
                    numbers.remove(emove5s)

                    numbers.append(emove1s)
                    numbers.append(emove2s)
                    numbers.append(emove3s)
                    numbers.append(emove4s)
                    numbers.append(emove5s)
                    strength1 = random.choice(numbers)
                    numbers.remove(strength1)
                    strength2 = random.choice(numbers)
                    numbers.remove(strength2)
                    strength3 = random.choice(numbers)
                    numbers.remove(strength3)
                    strength4 = random.choice(numbers)
                    numbers.remove(strength4)
                    strength5 = random.choice(numbers)
                    numbers.remove(strength5)
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
                print("Type 'moves' to see your moves during battle!")
                ### FIGHT SEQUENCE
                while True:
                    if ehp <= 0:
                        break
                    elif hp <= 0:
                        break
                    time.sleep(timer3)
                    while True:
                        move = input("What move will you do? (number) ").lower()
                        if move == "moves":



                            time.sleep(timer1)
                            print("Your " + curweap2[0] + sp + curweap2[1] + " has the following stats:")
                            time.sleep(timer2)
                            print(stat1 + ": " +str(stats[stat1]))
                            time.sleep(timer1)
                            print(stat2 + ": " +str(stats[stat2]))
                            time.sleep(timer1)
                            print(stat3 + ": " +str(stats[stat3]))
                            time.sleep(timer1)
                            print(stat4 + ": " +str(stats[stat4]))
                            time.sleep(timer1)
                            print(stat5 + ": " +str(stats[stat5]))
                            time.sleep(timer1)
                            move = input("What move will you do? (number) ").lower()
                        Strength = 0
                        if move == "1":
                            statnum = stat1
                            Strength = strength1
                            break
                        elif move == "2":
                            statnum = stat2
                            Strength = strength2
                            break
                        elif move == "3":
                            statnum = stat3
                            Strength = strength3
                            break
                        elif move == "4":
                            statnum = stat4
                            Strength = strength4
                            break
                        elif move == "5":
                            statnum = stat5
                            Strength = strength5
                            break
                        else:
                            time.sleep(2)
                            print("That was not a valid move")
                            time.sleep(1)
                            move = input("What move will you do? (number) ").lower()


                    fluff5 = ["The "+ locenemy +" tries to hide its writhing pain from your attack but to no avail. The enemy is critically damaged",

                    "The "+ locenemy +" becomes temporarily stunned from your ineffable " + curweap2[0] + sp + curweap2[1]+"!",

                    "Your " + random.choice(adj2)+ " moves have left the "+locenemy+" dumbfounded on what to do next!",

                    "The wind russles past the " + random.choice(adj3) + " floor bound body of the " + locenemy +"!",

                    "Your "+ curweap2[1] + " plunges deep into the " + locenemy + ", causing a sever shriek to be heard from them!"

                    ]

                    fluff4 = ["The enemy looks severly " + random.choice(adj3) + " after your "+ random.choice(adj2) + " move!",

                    "It might have been luck. It might have been chance. It might have been skill. But whatever it was it is undeniable that the "+locenemy+" has been battered beyond repair!",

                    "Like flowing water, your " + statnum + " smoothly crushes the " + locenemy + "!"

                    ]


                    fluff3 = [random.choice(adj2)+". Your attack was right on target!",

                    "The "+locenemy + " watches a thick stream of crimson ecscapes their body due to your "+ curweap2[1]+"!",

                    "The enemy can barely stand after your " + random.choice(adj2) + " attack!",

                    ]


                    fluff2 = ["Despite your planned strike, due to the " + locenemy + "'s evasive talents, it falls completely flat, dealing minimal damage",

                    "As you attacked you felt an overwhelming sense of fatigue overcome you, slowing down your attack and allowing the enemy to dodge!"]

                    fluff1 = ["Your attack falls flat as you fail to strike the " + locenemy + " despite your continual onslaught!",

                    "Villagers all around echo the name '" + name + "' as " + random.choice(adj2) + ". Monsters for miles in any direction fear your "+ curweap2[1]+ ". All this and you still can't land a single strike on the "+ locenemy + "!"

                    ]


                    efluff1 = ["Your " + random.choice(adj2) + " body deflects all of the "+ locenemy + "'s attacks!"]
                    efluff2 = ["Using your "+random.choice(adj2)+ " strategy you have sustained minimal damage!"]
                    efluff3 = ["Unfortunently your quick dodge was not quick enough! Although you did avoid sustaining any serious damage you did take some "+random.choice(adj2)+" blows!" ]
                    efluff4 = ["As the attack smashes your head against the ground you smell a nautious mix of dirt and blood.",
                    "Your seemingly useless "+ curweap2[1]+ " could barely even block the simplest of attacks, leading to the "+locenemy+" to grin at your pitiful being"]

                    efluff5 = ["Your once feared reputation has almost been sullied beyond repair after the "+ locenemy+ " completely anihilates you!"]


                    if True:
                        if Strength == 1:
                            print("The move "+ statnum+ " from your "+ curweap2[1]+" was ineffective against the "+ locenemy+"!")
                            if random.choice(number) >= 5:
                                time.sleep(timer2)
                                print(random.choice(fluff1))
                        elif Strength == 2:
                            print("The move "+ statnum+ " from your "+ curweap2[1]+" was slightly effective against the "+ locenemy+"!")
                            locstat = stats[statnum]
                            locstat = int(locstat)
                            locstat = locstat/2
                            locstat = int(locstat)
                            ehp = ehp - locstat
                            if random.choice(number) >= 5:
                                time.sleep(timer2)
                                print(random.choice(fluff2))
                        elif Strength == 3:
                            print("The move "+ statnum+ " from your "+ curweap2[1]+" was effective against the "+ locenemy+"!")
                            locstat = stats[statnum]
                            locstat = int(locstat)
                            ehp = ehp - locstat
                            if random.choice(number) >= 5:
                                time.sleep(timer2)
                                print(random.choice(fluff3))
                        elif Strength == 4:
                            print("The move "+ statnum+ " from your "+ curweap2[1]+" was very effective against the "+ locenemy+"!")
                            locstat = stats[statnum]
                            locstat = int(locstat)
                            locstat = locstat+locstat
                            ehp = ehp - locstat
                            if random.choice(number) >= 5:
                                time.sleep(timer2)
                                print(random.choice(fluff4))
                        elif Strength == 5:
                            print("The move "+ statnum+ " from your "+ curweap2[1]+" was extremely effective against the "+ locenemy+"!")
                            locstat = stats[statnum]
                            locstat = int(locstat)
                            locstat = locstat+locstat+locstat
                            ehp = ehp - locstat
                            if random.choice(number) >= 5:
                                time.sleep(timer2)
                                print(random.choice(fluff5))


                    time.sleep(timer3)
                    if ehp <= 0:
                        break
                    elif hp <= 0:
                        break
                    if random.choice(number) == 1:
                        time.sleep(timer3)
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
                        numbers.remove(emove5s)

                        numbers.append(emove1s)
                        numbers.append(emove2s)
                        numbers.append(emove3s)
                        numbers.append(emove4s)
                        numbers.append(emove5s)
                        strength1 = random.choice(numbers)
                        numbers.remove(strength1)
                        strength2 = random.choice(numbers)
                        numbers.remove(strength2)
                        strength3 = random.choice(numbers)
                        numbers.remove(strength3)
                        strength4 = random.choice(numbers)
                        numbers.remove(strength4)
                        strength5 = random.choice(numbers)
                        numbers.remove(strength5)

                        numbers.append(strength1)
                        numbers.append(strength2)
                        numbers.append(strength3)
                        numbers.append(strength4)
                        numbers.append(strength5)
                    enemymove = random.choice(emove)
                    print("The "+locenemy + " has " + str(ehp) + " hp remaining!")
                    time.sleep(timer3)


                    if enemymove == emove[0]:
                        x = 0
                        Strength = emove1s
                    elif  enemymove == emove[1]:
                        x = 1
                        Strength = emove2s
                    elif  enemymove == emove[2]:
                        x = 2
                        Strength = emove3s
                    elif  enemymove == emove[3]:
                        x = 3
                        Strength = emove4s
                    elif  enemymove == emove[4]:
                        x = 4
                        Strength = emove5s
                    if True:
                        if Strength == 1:
                            print("The enemies move "+ emove[x]+ " was ineffective against you!")
                            if random.choice(number) >= 5:
                                time.sleep(timer2)
                                print(random.choice(efluff1))
                        elif Strength == 2:
                            print("The enemies move "+ emove[x]+ " was slightly effective against you!")
                            locstat = enemystat[x]
                            locstat = int(locstat)
                            locstat = locstat/2
                            locstat = int(locstat)
                            hp = hp - locstat
                            if random.choice(number) >= 5:
                                time.sleep(timer2)
                                print(random.choice(efluff2))
                        elif Strength == 3:
                            print("The enemies move "+ emove[x]+ " was effective against you!")
                            locstat = enemystat[x]
                            locstat = int(locstat)
                            hp = hp - locstat
                            if random.choice(number) >= 5:
                                time.sleep(timer2)
                                print(random.choice(efluff3))
                        elif Strength == 4:
                            print("The move "+ emove[x]+ " was very effective against you!")
                            locstat = enemystat[x]
                            locstat = int(locstat)
                            locstat = locstat+locstat
                            hp = hp - locstat
                            if random.choice(number) >= 5:
                                time.sleep(timer2)
                                print(random.choice(efluff4))
                        elif Strength == 5:
                            print("The move "+ emove[x]+ " was extremely effective against you!")
                            locstat = enemystat[x]
                            locstat = int(locstat)
                            locstat = locstat+locstat+locstat
                            hp = hp - locstat
                            if random.choice(number) >= 5:
                                time.sleep(timer2)
                                print(random.choice(efluff5))
                    time.sleep(timer3)
                    if ehp <= 0:
                        break
                    elif hp <= 0:
                        break
                    print("You have " + str(hp) + " hp out of "+ str(hpcap)+" hp left!")
                    hp = int(hp)
                    print("  ")
                ### VERY IMPORTANT!
                time.sleep(timer3)
                enemystat.remove(main)
                enemystat.remove(sec1)
                enemystat.remove(sec2)
                enemystat.remove(oth1)
                enemystat.remove(oth2)
                if ehp <= 0:
                    print ("You won!")
                    time.sleep(timer3)

                    ###Gen
                    num = random.choice(number)
                    goldN = random.choice(number)+random.choice(number)

                    ###Enemy drop
                    if num >= 8: #8
                        ### Weapon
                        curweap3 = []
                        curweap3.append(random.choice(modify))
                        curweap3.append(random.choice(weapon))

                        print("The enemy dropped a " + curweap3[0] + sp + curweap3[1] + ". You also find " +str(goldN) + " gold coins " + random.choice(body) + " the monster")
                        gold = gold + int(goldN)
                        if hasgem == 0:
                            if locitem == "a jewel encrusted attire":
                                time.sleep(timer2)
                                print(" ")
                                print("Within the jewel encrusted attire you have found an Emerald! It has been added to you collection")
                                print(" ")
                                collection.append(collectionfull[1])
                                hasgem = 1

                        elif hasgem == 1:
                            print("You find an Emerald within the attire, however it is left behind as it does not even come close to matching the beauty of the first you found")



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
                        print("After experimenting with the "+ curweap1[1]+ ", you find it has some intresting abilites!")
                        time.sleep(timer2)
                        print(mainA + " is a primary move with " + main + " levels!")
                        time.sleep(timer1)
                        print(sec1A + " is a secondary move with " + sec1 + " levels!")
                        time.sleep(timer1)
                        print(sec2A + " is a secondary move with " + sec2 + " levels!")
                        time.sleep(timer1)
                        print(oth1A + " is a normal move with " + oth1 + " levels!")
                        time.sleep(timer1)
                        print(oth2A + " is a normal move with " + oth2 + " levels!")
                        time.sleep(timer1)

                        norm.append (mainA)
                        norm.append (sec1A)
                        norm.append (sec2A)
                        norm.append (oth1A)
                        norm.append (oth2A)
                        answertokeepquestion = 0
                        while answertokeepquestion == 0:
                            keep = input("Do you want to keep this weapon? (yes/no) (note that keeping will result in the discarding of current weapon)").lower()
                            if keep == "yes":
                                print("You have equipped the " + curweap3[0]+ sp+ curweap3[1]+"!")
                                curweap2 = []
                                curweap2.append(curweap3[0])
                                curweap2.append(curweap3[1])
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
                                answertokeepquestion = 1
                            if keep == "no":
                                print("Its probably weaker than your current weapon anyway!")
                                answertokeepquestion = 1


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

                        if hasgem == 0:
                            if locitem == "a jewel encrusted attire":
                                time.sleep(timer2)
                                print(" ")
                                print("Within the jewel encrusted attire you have found an Emerald! It has been added to you collection")
                                print(" ")
                                collection.append(collectionfull[1])
                                hasgem = 1
                    else:
                        print("Sadly nothing was dropped")
                else:
                    print ("you died and lost 1 life!")
                    life = life - 1
                    hp = 100
                    if life == 0:
                        print("You have 0 lives left. The game is over")
                        quit()
                    elif life <= 2:
                        print("Watch out! You only have " + str(life) + " lives left!")
                        life = int(life)
            elif rannum <= 2:
                villagewords = [

                "village",
                "hamlet",
                "walled town",
                "town",
                "borough"

                ]

                dvillagewords = [

                "ruins",
                "cavern",
                ]

                ruinwords = [

                "some battered",
                "some broken",
                "some shattered",
                "some destroyed",
                "some intact"
                ]

                cavernwords = [
                "a grimy",
                "a twilight",
                "an expansive",
                "a mysterious",
                "an unexplored",
                "an odd"
                ]
                if biome in norbiome:
                    village = random.choice(villagewords)
                    explorevillage = input("You come across an abandoned "+village+", standing out in the otherwise desolate terrain. Do you wish to explore inside? (yes/no) ").lower()
                    if explorevillage == "yes":
                        while True:
                            villagenumber = random.choice(numbers)
                            if villagenumber == 1:
                                print("Unfortunently the "+village+" seems to have already been looted. Nothing remains")
                                break
                            while villagenumber != 1:
                                rangold = random.choice(number)
                                time.sleep(timer3)
                                time.sleep(timer2)
                                print(" ")
                                print("While "+random.choice(searching)+" " + random.choice(buildings) + " in the "+village+", you find " +str(rangold) +" gold "+ random.choice(buildnear) +sp + random.choice(builditems)+"!")
                                gold += rangold
                                if hastopaz == 0:
                                    if int(random.choice(number))+int(random.choice(number)) == 20:
                                        hastopaz = 1
                                        collection.append(collectionfull[3])
                                        time.sleep(timer2)
                                        print(" ")
                                        print("Whilst "+random.choice(searching)+" the well in the off chance something is there you look into the bucket, hanging from the rope. Inside you find a Topaz! it has been added to your collection!")
                                villagenumber = random.choice(numbers)
                            print(" ")
                            time.sleep(timer2)
                            print("You search in several more buildings but to no avail. This "+ village + " is empty!")
                            break



                if biome in divbiome:
                    while True:
                        village = random.choice(dvillagewords)
                        if village == "ruins":
                            explorevillage = input("You come across "+ random.choice(ruinwords)+" ruins, do you explore them? (yes/no) ").lower()
                        elif village == "cavern":
                            explorevillage = input("You come across "+ random.choice(cavernwords)+" cavern, do you descend down? (yes/no) ").lower()
                        time.sleep(timer2)


                        ###INCLUDE BREAK AT BOTTOM OF CHAIN!!!!
                        cavernsize = [
                        "an ineffably big",
                        "an enormous",
                        "a large",
                        "an ant sized",
                        "a tiny",
                        ]
                        caverntype = [
                        "chasm",
                        "underground waterfall",
                        "underground lavafall",
                        "ravine"
                        ]

                        ruintype1 = [
                        "battered",
                        "broken",
                        "shattered",
                        "destroyed",
                        "eroded",
                        "wrecked",
                        "deserted",
                        "forgotten",
                        "neglected",
                        "empty"
                        ]

                        ruintype2 = [
                        "shrine",
                        "hut",
                        "chapel",
                        "cathedral",
                        "mosque",
                        "treasure room",
                        "dungeon",
                        "tomb",
                        "cemetry"
                        ]

                        ruintype3 = []
                        x = 0
                        i = 1 - 2
                        for variable1 in ruintype1:

                            for variable2 in ruintype2:
                                i = i + 1
                                thething = (ruintype1[x] +sp+ ruintype2[i])
                                ruintype3.append(thething)
                            x = x + 1
                            i = 1 - 2
                        if explorevillage == "yes":
                            localvar = 1
                            while localvar == 1:
                                villagenumber = random.choice(numbers)
                                if villagenumber == 1:
                                    if village == "ruins":
                                        print("Unfortunently the "+village+" seem to have already been explored and looted. Nothing remains")
                                    elif village == "cavern":
                                        print("Unfortunently the "+village+" seems to have already been explored and looted. Nothing remains")
                                    break
                                while villagenumber != 1:
                                    rangold = random.choice(number)
                                    time.sleep(timer3)
                                    time.sleep(timer2)
                                    print(" ")
                                    #print("While "+random.choice(searching)+" " + random.choice(buildings) + " in the "+village+", you find " +str(rangold) +" gold "+ random.choice(buildnear) +sp + random.choice(builditems)+"!")
                                    if village == "cavern":
                                        print("While "+ random.choice(searching )+ " in "+ random.choice(cavernsize) + sp + random.choice(caverntype) +" within the cavern, you find "+str(rangold)+" gold!")
                                    elif village == "ruins":
                                        print("While "+ random.choice(searching )+ " in the "+ random.choice(ruintype3)+" of the ruins, you find "+str(rangold)+" gold!")
                                    gold += rangold
                                    #if hastopaz == 0:
                                    #    if int(random.choice(number))+int(random.choice(number)) == 20:
                                    #        hastopaz = 1
                                    #        collection.append(collectionfull[3])
                                    #        time.sleep(timer2)
                                    #        print(" ")
                                    #        print("Whilst "+random.choice(searching)+" the well in the off chance something is there you look into the bucket, hanging from the rope. Inside you find a Topaz! it has been added to your collection!")
                                    villagenumber = random.choice(numbers)
                                print(" ")
                                time.sleep(timer2)
                                if village == "cavern":
                                    print("You search in several more twisting and turning tunnels within the cavern but to no avail. This "+ village + " is empty!")
                                elif village == "ruins":
                                    print("You search in several more broken structures within the ruins but to no avail. These "+ village + " are empty!")

                                localvar = 0
                            break
                        elif explorevillage == "no":
                            print("There was probably nothing valuable in the "+village+" anyway!")
                            break
                        else:
                            print("That was not a valid response. Please type yes or no. ")
            elif rannum == 3:
                rannum = random.choice(number)
                if rannum >= 6:
                    possiblehurt = ["You explore the lands surrounding you for miles in each direction, mapping a whole new world. All of a sudden you are jolted by a fall. As you look down you see your leg coated in crimson.",
                    "As you explore you feel a sting on your arm. As you look as to what it is you notice an enormous gash bleeding out!"

                    ]
                    time.sleep(timer2)
                    ranum = int(random.choice(number)) + int(random.choice(number))
                    print(random.choice(possiblehurt))
                    print("You lost " +str(rannum)+" hp!")
                    time.sleep(timer2)
                    if hp <= 0:
                        print ("You died and lost 1 life!")
                        hp = 100
                        time.sleep(timer2)
                        life = life - 1
                        if life == 0:
                            print("You have 0 lives left. The game is over")
                            time.sleep(timer2)
                            quit()
                        elif life <= 2:
                            print("Watch out! You only have " + str(life) + " lives left!")
                            time.sleep(timer2)
                            life = int(life)



                    ### LOSE RANDOM AMOUNT OF HP
                elif rannum <= 5:
                    ### TELEPORT TO DIFFERENT BIOME
                    if biome in norbiome:
                        print("You scout the land but to no avail, that is until you find a cavern darker than a thousand nights. You enter with your blazing torch to guide you.")
                        time.sleep(timer3)
                        intersection = input("You come up to an intersection, do you wish to go left or right? (left/right) ").lower()
                        time.sleep(timer2)

                        if random.choice(number) >= 6:
                            rangold = random.choice(numbers)
                            print("You find "+str(rangold)+" gold scattered across the floor")
                            time.sleep(timer2)
                        else:
                            rannum = int(random.choice(numbers))+int(random.choice(number))
                            print("You fall to the ground writhing in pain after getting hit by a dart trap. You lose "+str(rannum)+ " hp!")
                            time.sleep(timer2)
                            if hp <= 0:
                                print ("You died and lost 1 life!")
                                hp = 100
                                time.sleep(timer2)
                                life = life - 1
                                if life == 0:
                                    print("You have 0 lives left. The game is over")
                                    time.sleep(timer2)
                                    quit()
                                elif life <= 2:
                                    print("Watch out! You only have " + str(life) + " lives left!")
                                    time.sleep(timer2)

                                    life = int(life)

                        print("While wandering deeper into the seemingly endless labyrinth of chasms and tunnels you come across a blindngly bright multicolored portal")
                        enterportal = input("Do you enter it? (yes/no) ")
                        if enterportal == "yes":
                            biome = random.choice(divbiome)
                            print("As you enter you find youself in a crazy, forign place. You are in "+biome+"!")

                    if biome in divbiome:
                        if biome == "underworld":
                            print("You notice a dark, gloomy chasm below you, filled to the brim with endless shrieks. You descend down towards it")
                            time.sleep(timer2)

                        elif biome == "niravana":
                            print("Through the angelic tunes in the distance you see an opening in the clouds. ")
                            time.sleep(timer2)
                        if random.choice(number) >= 6:
                            rangold = random.choice(numbers)
                            print("You find "+str(rangold)+" gold scattered across the floor")
                            time.sleep(timer2)
                        else:
                            rannum = int(random.choice(numbers))+int(random.choice(number))
                            print("You fall to the ground writhing in pain after getting hit by a dart trap. You lose "+str(rannum)+ " hp!")
                            time.sleep(timer2)
                            ###HPSTUFF
                            if hp <= 0:
                                print ("You died and lost 1 life!")
                                hp = 100
                                time.sleep(timer2)
                                life = life - 1
                                if life == 0:
                                    print("You have 0 lives left. The game is over")
                                    time.sleep(timer2)
                                    quit()
                                elif life <= 2:
                                    print("Watch out! You only have " + str(life) + " lives left!")
                                    time.sleep(timer2)
                                    life = int(life)

                        print("While wandering deeper into the seemingly endless labyrinth of chasms and tunnels you come across a blindngly bright multicolored portal")
                        enterportal = input("Do you enter it? (yes/no) ")
                        if enterportal == "yes":
                            biome = random.choice(norbiome)
                            print("As you enter you find youself in a crazy, forign place. You are in "+biome+"!")


                    else:
                        print("please report this line to oscar, it means the game is broken!")
        elif start == "help":
            print("The following commands are available in the current build:")
            time.sleep(timer1)
            print("explore")
            time.sleep(timer1)
            print("stats")
            time.sleep(timer1)
            print("end")
            time.sleep(timer1)
            print("upgrade")
            time.sleep(timer1)
            print("shop")
            time.sleep(timer1)
            print("changelog")
            time.sleep(timer1)
            print("collection")
            if cantravel == True:
                time.sleep(timer1)
                print("travel")

            #print("The following commands will be added in the next patch:")
        #print("Note: Cheats are currently enabled")
    #    time.sleep(timer2)
        elif start == "stats":
            print("The following stats are avaible for viewing:")
            time.sleep(timer1)
            print("Weapon")
            time.sleep(timer1)
            print("Life")
            time.sleep(timer1)
            print("Gold")
            time.sleep(timer1)
            stats2 = input("What stats do you wish to see? ").lower()
            if stats2 == "weapon":
                time.sleep(timer1)
                print("Your " + curweap2[0] + sp + curweap2[1] + " has the following stats:")
                time.sleep(timer2)
                print(stat1 + ": " +str(stats[stat1]))
                time.sleep(timer1)
                print(stat2 + ": " +str(stats[stat2]))
                time.sleep(timer1)
                print(stat3 + ": " +str(stats[stat3]))
                time.sleep(timer1)
                print(stat4 + ": " +str(stats[stat4]))
                time.sleep(timer1)
                print(stat5 + ": " +str(stats[stat5]))
                time.sleep(timer1)
            elif stats2 == "gold":
                time.sleep(timer1)
                print("You have " + str(gold) + " gold.")
                gold = int(gold)
            elif stats2 == "life":
                print("You have "+str(life)+" lives left!")
                life = int(life)
        elif start == "upgrade":
            time.sleep(timer1)
            if gold >= 10:
                upgrade = input("Which move do you want to upgrade? (number) ").lower()
                time.sleep(timer2)
                x = 0



                if upgrade == "1":
                    stats[stat1] = int(stats[stat1]) + 1
                    x += 1
                if upgrade == "2":
                    stats[stat2] = int(stats[stat2]) + 1
                    x += 1
                if upgrade == "3":
                    stats[stat3] = int(stats[stat3]) + 1
                    x += 1
                if upgrade == "4":
                    stats[stat4] = int(stats[stat4]) + 1
                    x += 1
                if upgrade == "5":
                    stats[stat5] = int(stats[stat5]) + 1
                    x += 1
                if x != 0:
                    gold = gold - 10
                time.sleep(timer2)
                print("You have "+ str(gold) + " gold left")
                gold = int(gold)
            else:
                goldN = 10 - gold
                print("You need " + str(goldN)+ " more gold to upgrade moves")
        elif start == "end":
            print("You have quit Reveles. These are your final stats:")
            time.sleep(timer2)
            print("Gold: "+ str(gold))
            time.sleep(timer2)
            print("HP: " +str(hp))
            time.sleep(timer2)
            print("Lives: "+ str(life))
            time.sleep(timer2)
            print("Stats: " )
            time.sleep(timer1)
            print(stat1 + ": " +str(stats[stat1]))
            time.sleep(timer1)
            print(stat2 + ": " +str(stats[stat2]))
            time.sleep(timer1)
            print(stat3 + ": " +str(stats[stat3]))
            time.sleep(timer1)
            print(stat4 + ": " +str(stats[stat4]))
            time.sleep(timer1)
            print(stat5 + ": " +str(stats[stat5]))
            time.sleep(timer2)
            print("Weapon: " + curweap2[0] + sp + curweap2[1])
            time.sleep(timer2)
            if len(collection) != 0:
                print("You have collected the following minerals:")
                time.sleep(timer2)
                for i in collection:
                    print(i)
                    time.sleep(timer1)
            print("Thanks for playing!")
            time.sleep(timer2)
            quit()
        elif start == "shop":
            time.sleep(timer2)
            print("Type 'help (item)' to learn more about any item in the shop!")
            time.sleep(timer2)
            print("Type '(item)' to buy any item in the shop! (In this patch this is case sensitive)")
            time.sleep(timer2)
            print(" ")
            print("SHOP")
            time.sleep(timer1)
            print(" ")
            print(shoplife + ": " + str(shoplifeg)+ " gold")
            time.sleep(timer1)
            if boughtsapphire == 0:
                print(" ")
                print("Sapphire: 40 gold")
                time.sleep(timer1)

            print(" ")
            print(shophp + ": " + str(shophpg)+ " gold")



            time.sleep(timer3)
            buy = "a"
            while True:
                print(" ")
                buy = input("What item do you wish to buy? Type back to go 'back' to menu ")
                time.sleep(timer2)


                if buy == shoplife:
                    if shoplifeg > gold:
                        print("You do not have enough gold to purchase this item")
                        time.sleep(timer2)
                    else:
                        gold = gold - shoplifeg
                        life = life + 1
                        print("You have bought 1 "+ shoplife + "!")
                        time.sleep(timer2)
                elif buy == ("help "+shoplife):
                    print("For a price of only "+str(shoplifeg)+" gold, the " +shoplife+ " will give you an extra life!")
                elif buy == "Sapphire":
                    if boughtsapphire == 0:
                        if 40 > gold:
                            print("You do not have enough gold to purchase this item")
                            time.sleep(timer2)
                        else:
                            collection.append(collectionfull[0])
                            boughtsapphire = 1
                            print("You have bought the Sapphire!")
                            gold = gold - 50
                            time.sleep(timer2)
                    else:
                        print("That item has been sold out")
                        time.sleep(timer2)
                elif buy == "help Sapphire":
                    print("It has a sparkle like the ocean blue, when bought you can check it out in your collection!")
                elif buy == shophp:
                    if shophpg > gold:
                        print("You do not have enough gold to purchase this item")
                        time.sleep(timer2)
                    else:
                        gold = gold - shophpg
                        while hp != 100:
                            hp = hp + 1
                        print("You have bought 1 "+ shophp + "!")
                        time.sleep(2)


                elif buy == ("help "+ shophp):
                    print("Are you low on hp? well if you have " + str(shophpg) + " gold to spare then you can afford one "+ shophp + "! This item will heal all lost hp!")

                elif buy == "back":
                    break
                else:
                    print("That was not a valid item!")
        elif start == "changelog":
            update = input("Update? (for e.g 0.3)").lower()
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
                print("Added Purgatory and Niravana biomes")
                print("Created the collection, an area where you keep precious minerals that you find")
                print("Added more flavour lines during fights")
                print("Created a mulititude of new lines in many lists")
                print ("Added hidden minerals in the game to collect (there are 3 so far)")
                print("Compacted the code by removing several hundred lines")
                print("Added a new item to the shop (Renewing HP!)")
                print("Made the upgrade place actually work")
                print("Fixed some bugs")
                print("Added some bugs (probably)")
                print("Added the ability to travel (between normal biomes) once a mineral is found")
                print("Commands are not case sensitive (other than in the shop)")
            if update == "0.5":
                print("Changed 'fight' to 'explore' which adds new options!")
                print("One of the aforementioned options is a portal between special and normal biomes")
                print("Another of the aforementioned options is to find and loot cities")
                print("Pugatory is now called underworld")
                print("Created mountain biome")
                print("Added words to lots of randomized lists")
                print("Added some new minerals")
                print("Added a tutorial")
                print("Smashed a bug that made certain chances more weighted than they were supposed to be")
                print("Adjusted the time text takes to come out")
                #make things more random in fight!
        elif start == "collection":

            if len(collection) == 0:
                print("You have not yet collected any minerals!")
            else:
                print("You have collected the following minerals:")
                for i in collection:

                    print(i)
            i = len(collectionfull) - len(collection)
            print("You have " +str(i)+" minerals left to collect")

                ### TRAVEL VARIABLES
        elif start == "travel":
            if cantravel == True:
                if biome in norbiomefull:
                    print("Traders are currently willing to take you to " + norranbiome + ". Obviously for a price! ")
                    time.sleep(timer2)
                    print("After searching far and wide for the cheapest option you find a trader willing to take you for " + str(norranbiomeg)+" gold")
                    print("   ")
                    accept = input("Do you accept? (yes/no) ").lower()
                    if accept == "yes":
                        if gold >= norranbiomeg:
                            biome = norranbiome
                            rannum = 0
                            beenshopping = 0
                            while rannum != 1:
                                print("   ")
                                print(random.choice(travar))
                                time.sleep(timer3)
                                if random.choice(number) >= 9:
                                    if beenshopping == 0:
                                        if hasboughtaruby == 0:
                                            beenshopping = 1
                                            while True:
                                                print("The wagon stops to resupply for its journey ahead.")
                                                goingtoshop = input("Whilst the wagon resupplies there seems to be a shop outside. Do you want to take a look? (yes/no) ")
                                                if goingtoshop == "no":
                                                    print("Its probably nothing anyway, you think")
                                                    break
                                                if goingtoshop == "yes":
                                                    costforruby = random.choice(number)+random.choice(numbers)
                                                    buyruby = input("A shopkeeper has a large stash of rubies for sale at a cheap price! Do you want to buy one for "+str(costforruby)+" gold? (yes/no) ")
                                                    if buyruby == "yes":
                                                        if gold >= costforruby:
                                                            print("You have bought a Ruby!")
                                                            collection.append(collectionfull[2])
                                                            gold = gold - costforruby
                                                            hasboughtaruby = 1
                                                            time.sleep(timer2)
                                                            print("The journey continues!")
                                                            break
                                                        else:
                                                            print("You try to barter and to get it at a cheaper price but to no avail, maybe next time!")
                                                            break
                                                    elif buyruby == "no":
                                                        print("Who needs such useless and trivial things anyway?")
                                                        break
                                                    else:
                                                        print("That was not a valid answer!")
                                                else:
                                                    print("That was not a valid answer!")

                                rannum = random.choice(number)

                            print("You have arrived in the "+biome+"!")
                            print("The traders bid you good luck in the "+biome+"!")
                            norranbiome = random.choice(norbiome)
                        else:
                            print("You walk to board the wagon. As you step up the wagon dealer asks for the money. You are unable to scrounge together any funds")
                            time.sleep(timer2)
                            print("You are shooed of the wagon, they tell you to come back once you have the gold to pay!")
            else:
                print("That was not a valid command. Type 'help' for more information!")


        else:
            print("That was not a valid command. Type 'help' for more information!")
