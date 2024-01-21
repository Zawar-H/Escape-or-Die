import time, random, sys


def UserIntro():
    print('Hello, "guest"')
    print(
        'My name is, Zawar Haider, and I am the creator of the adventure game, "Escape or Die"'
    )
    print('Would you like to play(y or n)?')
    play = input()
    if play == ('y'):
        print('Great')
    if play != ('y'):
        print('That\'s fine, goodbye')
        exit()


def PreIntro():
    print(
        'Use simple instructions(i.e. "walk east," "pick up object," or "open door") to function throughout the game'
    )
    print()
    time.sleep(2)
    print('Let\'s begin!')
    print()
    time.sleep(3)
    print('You are invited to a dinner party hosted by your new neighbour')
    print()
    time.sleep(2)
    print('Since he is new to the neighbourhood and owns a massive manor,')
    print(
        'he decides to invite every single person living in your neighbourhood to a dinner'
    )
    print()
    time.sleep(2)
    print(
        'While at the party, the lights suddenly go out and one of the guests is killed'
    )
    print()
    time.sleep(2)
    print('A little while later, another guest is killed')
    print()
    time.sleep(2)
    print('Its just a matter of time before you are the next victim')
    print()
    time.sleep(2)
    print(
        'The objective of this game is to escape the killer by maneuvering your way out of the manor, or you get killed by the killer'
    )
    time.sleep(3)
    print()
    print()
    print()


PlayAgain = True
while PlayAgain == True:
    UserIntro()
    PreIntro()

    print(
        '           ███████╗███████╗ ██████╗ █████╗ ██████╗ ███████╗     ██████╗ ██████╗     ██████╗ ██╗███████╗'
    )
    print(
        '           ██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝    ██╔═══██╗██╔══██╗    ██╔══██╗██║██╔════╝'
    )
    print(
        '           █████╗  ███████╗██║     ███████║██████╔╝█████╗      ██║   ██║██████╔╝    ██║  ██║██║█████╗  '
    )
    print(
        '           ██╔══╝  ╚════██║██║     ██╔══██║██╔═══╝ ██╔══╝      ██║   ██║██╔══██╗    ██║  ██║██║██╔══╝  '
    )
    print(
        '           ███████╗███████║╚██████╗██║  ██║██║     ███████╗    ╚██████╔╝██║  ██║    ██████╔╝██║███████╗'
    )
    print(
        '           ╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚══════╝     ╚═════╝ ╚═╝  ╚═╝    ╚═════╝ ╚═╝╚══════╝'
    )
    print(
        '                                                                                            '
    )
    print(
        '                                              ▄▄▄·▄▄▌   ▄▄▄·  ▄· ▄▌')
    print(
        '                                             ▐█ ▄███•  ▐█ ▀█ ▐█▪██▌')
    print(
        '                                              ██▀·██▪  ▄█▀▀█ ▐█▌▐█▪')
    print(
        '                                             ▐█▪·•▐█▌▐▌▐█ ▪▐▌ ▐█▀·.')
    print(
        '                                             .▀   .▀▀▀  ▀  ▀   ▀ • ')
    print('')
    print('                                             .▄▄▄  ▄• ▄▌▪  ▄▄▄▄▄')
    print('                                             ▐▀•▀█ █▪██▌██ •██  ')
    print('                                             █▌·.█▌█▌▐█▌▐█· ▐█.▪')
    print('                                             ▐█▪▄█·▐█▄█▌▐█▌ ▐█▌·')
    print('                                             ·▀▀█.  ▀▀▀ ▀▀▀ ▀▀▀ ')

    play2 = input()
    if play2 != ('play'):
        print('Until next time...')
        exit()
    if play2 == ('play'):
        time.sleep(2)
        FirstCutscene = ('''October 14, 1987:
The neighbourhood is putting up their decorations to get ready for halloween,
children are making their costumes, and parents are buying candy.
The new neighbour, James Miller, of three weeks is also oddly giddy and preparing for halloween. He looks very wealthy since
he lives in a very large manor, he even asked some of our neighbours for help because of how big his house is.'''
                         + "\n")
        print(' ')
        for character in FirstCutscene:
            sys.stdout.write(character)
            time.sleep(0.05)
        time.sleep(2)
        print('Everything is peaceful')
        time.sleep(3)
        print('At least that\'s what it seems...')
        time.sleep(3)
        #possible picture
        SecondCutscene = ('''October 20, 1987:
        You receive a letter in the mail. It turns out to be an invitation
        to a dinner from your new neighbour.''' + "\n")
        print(' ')
        for character in SecondCutscene:
            sys.stdout.write(character)
            time.sleep(0.05)
        time.sleep(2)
        Extra1 = ('''The letter reads:
"Hello Mr. Wilson,
You are  formally invited to a dinner I am hosting at my place.
Please reach my manor at 8 p.m. sharp.
Sincerely,
James Miller"''' + "\n")
        print(' ')
        for character in Extra1:
            sys.stdout.write(character)
            time.sleep(0.07)
        time.sleep(2)
        Extra2 = ('''Even though a dinner party being hosted close to halloween
seems a bit odd, you still decide to go...''' + "\n")
        print()
        for character in Extra2:
            sys.stdout.write(character)
            time.sleep(0.09)
        #Movements begin
        time.sleep(3)
        print('"You open the front door and enter"')
        Move1 = True
        while Move1 == True:
            print('You are now able to walk')
            Move1 = input()
            if Move1 == ('walk') or Move1 == ('walk up') or Move1 == (
                    'walk north') or Move1 == ('go') or Move1 == ('go up'):
                print('You reach the front foyer')
                break
            else:
                print('You are not able to do that')
                Move1 = True

        time.sleep(2)
        print('There is a ceiling fan hanging above you')
        print()
        time.sleep(2)
        print('There is a small hallway in front of you')
        Move3 = True
        while Move3 == True:
            print('What\'s next?')
            time.sleep(2)
            print('*Keep walking?*')
            print('*Look around?*')
            Move3 = input()
            if Move3 == ('walk') or Move3 == ('keep walking') or Move3 == (
                    'walk north') or Move3 == ('go') or Move3 == ('go up'):
                print('You reach the main living room')
                break
            if Move3 == ('look around'):
                print('You only see walls at your sides')
                Move3 = True
            else:
                print('You are not able to do that. You have to keep going')
                Move3 = True
        print()
        time.sleep(2)
        print('A very large chandelier hangs above your head')
        print()
        time.sleep(2)
        print('Lots of other guests are present, too')
        print()
        time.sleep(2)
        print(
            'You recognize most of the guests because you have been living in the neighbourhood'
        )
        print('for a long time and have become familiar with the people here')
        time.sleep(2)
        EXTRA = (
            '''They are walking around, talking to others, sipping from their
wine glasses, or just sitting down on the multiple couches
in the living room''' + "\n")
        print()
        for character in EXTRA:
            sys.stdout.write(character)
            time.sleep(0.1)
        time.sleep(2)
        Move4 = True
        while Move4 == True:
            print('What\'s your next move?')
            time.sleep(2)
            print('*Sit down?*')
            print('*Take a drink?*')
            Move4 = input()
            if Move4 == ('sit') or Move4 == ('sit down'):
                time.sleep(2)
                print(
                    'You take a seat on the couch closest to you, and one of the guests start talking to you'
                )
                break
            if Move4 == ('get drink') or Move4 == ('take drink') or Move4 == (
                    'get a drink') or Move4 == ('take a drink'):
                print(
                    'You take a glass of fine whiskey from the trays of one of the waiters walking around'
                )
                print('and start sipping')
                print()
                time.sleep(2)
                print(
                    'As you are drinking away, one of the guests approach you with a smile'
                )
                print()
                time.sleep(1)
                print(
                    'It is Julia Elise, you call her "Mrs. Elise" out of respect, and she starts talking with you right away'
                )
                print()
                time.sleep(1)
                print(
                    'She is the town librarian, so she always has fun stories')
                Move4 = True
            else:
                print('You are not able to do that')
                Move4 = True
        print()
        time.sleep(2)
        print(
            'You recognize this guest because he runs the dry cleaner store down the street'
        )
        print()
        time.sleep(2)
        print('You call him "Mr. Timmons"')
        print()
        time.sleep(1)
        print(
            'After greeting each other, he talks to you about work and how business has been lately'
        )
        print()
        time.sleep(3)
        print('DING DING DING!!!')
        print()
        time.sleep(2)
        print(
            'It\'s James Miller hitting a metal spoon on the side of his wine glass'
        )
        print()
        time.sleep(2)
        ThirdCutscene = (
            '''"Good evening, everyone. I am so glad everybody made it in time for my dinner.
Now, if everyone could promptly make their way to the dining room on the second floor,
that would be fantatstic, thank you."''' + "\n")
        print()
        for character in ThirdCutscene:
            sys.stdout.write(character)
            time.sleep(0.05)
        time.sleep(3)
        Extra3 = ('''Dining room on the second floor?
Everyone gives each other puzzled looks as they start to move''' + "\n")
        print()
        for character in Extra3:
            sys.stdout.write(character)
            time.sleep(0.05)
        Extra4 = (
            '''It gets very crowded as the guests make their way up to the
second floor. It gets difficult to see your surroundings, but you just
follow everyone else. After 15, very strange minutes, everyone is seated
at the huge dining table in the dining room''' + "\n")
        print()
        time.sleep(3)
        for character in Extra4:
            sys.stdout.write(character)
            time.sleep(0.1)
        print(' ')
        time.sleep(3)
        print('Before you know it, everyone is eating their food')
        print()
        time.sleep(2)
        print(
            '''In front of you, there is a plate with a cut of steak, mashed potatotes with
gravy, and a glass of red wine''')
        time.sleep(3)
        Move5 = True
        while Move5 == True:
            print('What will you do next?')
            time.sleep(2)
            print('*Eat the steak?*')
            time.sleep(1)
            print('*Eat the mashed potatoes?*')
            time.sleep(1)
            print('*Take a sip of the red wine?*')
            time.sleep(1)
            print('*Look around?*')
            Move5 = input()
            if Move5 == ('eat steak') or Move5 == ('take steak'):
                print(
                    'You cut off a piece from the cut of steak and put it in your mouth'
                )
                print()
                time.sleep(2)
                print(
                    'The seasoning and the way it is cooked makes it perfect,')
                print('and soon enough, you finish the entire cut')
                Move5 = True
            if Move5 == ('take sip') or Move5 == ('drink wine') or Move5 == (
                    'take wine'):
                print('The wine tastes exceptionally good, maybe it\'s fresh,')
                print()
                print('and with the steak, it is even better')
                Move5 = True
            if Move5 == ('eat mashed potatoes'):
                print(
                    'The mashed potatoes aren\'t so good, but the gravy masks its taste'
                )
                Move5 = True
            if Move5 == ('look around'):
                print('You see everyone focused on eating their food')
                break
            else:
                print('You are not able to do that at this time')
                Move5 = True
        time.sleep(2)
        FourthCutscene = (
            '''From the corner of your eye, you notice James Miller giving
you an angry stare while taking a sip of his wine and that\'s when it happens...'''
            + "\n")
        print()
        for character in FourthCutscene:
            sys.stdout.write(character)
            time.sleep(0.05)
        print(' ')
        print('CLICK')
        print(' ')
        time.sleep(3)
        FifthCutscene = (
            '''The lights suddenly go out and you hear two gushing sounds,
one after the other''' + "\n")
        print()
        for character in FifthCutscene:
            sys.stdout.write(character)
            time.sleep(0.05)
        print()
        time.sleep(3)
        SixthCutscene = (
            '''As the lights come back on, two of the guests in the room have blood just pouring
out of stab wounds in their stomachs''' + "\n")
        print()
        for character in SixthCutscene:
            sys.stdout.write(character)
            time.sleep(0.05)
        time.sleep(2)
        SeventhCutscene = (
            '''As soon as everyone sees this scene, screams and yells start erupting
in the dining room, everyone starts panicking, and people start rushing through the door. However,
James Miller is nowhere in sight!''' + "\n")
        print()
        for character in SeventhCutscene:
            sys.stdout.write(character)
            time.sleep(0.05)
        print(' ')
        Move6 = True
        while Move6 == True:
            print('Whats your next move?')
            print()
            time.sleep(1)
            print('*Stay seated?*')
            print()
            print('*Run?')
            Move6 = input()
            if Move6 == ('stay seated'):
                print(
                    'You remain in your seat a little longer, but eventually you have to move in order to escape the killer...'
                )
                Move6 = True
            if Move6 == ('run'):
                print('You sprint out of the room in an instant')
                break
            else:
                print('You are not able to do that at this moment')
                Move13 = True
        #possible second corridor
        print('DAMN IT!')
        print()
        time.sleep(0.5)
        print(
            'Since it got very crowded coming up here, you do not remember the surroundings'
        )
        print()
        time.sleep(3)
        Extra5 = (
            'Now you have to maneuver your way out of the house to avoid the killer and escape...'
            + "\n")
        print()
        for character in Extra5:
            sys.stdout.write(character)
            time.sleep(0.05)
        Extra6 = ('OR DIE!!!' "\n")
        print()
        for character in Extra6:
            sys.stdout.write(character)
            time.sleep(0.4)
        time.sleep(2)
        print(
            'You see one large corridor in front of you and 2 doors on each side'
        )
        print()
        time.sleep(2)
        print('OH NOO!!')
        time.sleep(1)
        Extra7 = (
            'The lights go out, you hear two other screams, and footsteps below you!!!'
            + "\n")
        print()
        for character in Extra7:
            sys.stdout.write(character)
            time.sleep(0.06)
        time.sleep(0.5)
        Move7 = True
        while Move7 == True:
            print('What do you do next?')
            print()
            time.sleep(2)
            print('*Do you open door 1, 2, 3, or 4?*')
            Move7 = input()
            if Move7 == ('1') or Move7 == ('2'):
                print('This room looks like a family room')
                print()
                time.sleep(0.5)
                print(
                    'There are family pictures on the wall, a bed, and a closet with clothes inside'
                )
                Move7 = True
            if Move7 == ('4'):
                print('You see what looks like an elevator hatch')
                print()
                time.sleep(0.5)
                print(
                    'Since the power keeps going out, you don\'t trust using the elevator'
                )
                Move7 = True
            if Move7 == ('3'):
                time.sleep(0.5)
                print(
                    'Finally! You find the stairs and start making your way down'
                )
                break
            else:
                print('You are not able to do that at this moment')
                Move13 = True
        print()
        time.sleep(1)
        print('CLICK')
        print()
        time.sleep(1)
        print(
            'The lights go out again and shortly after you hear another scream'
        )
        print()
        time.sleep(1)
        print('You still keep going')
        print()
        Extra8 = (
            '''As you come out of the staircase, you see yet another corridor
with 2 doors on one side and another door on the other side, the corridor
also takes a right turn at the end''' + "\n")
        print()
        for character in Extra8:
            sys.stdout.write(character)
            time.sleep(0.06)
        time.sleep(2)
        print('You should examine the rooms just in case you need to hide')
        print()
        time.sleep(1)
        Move8 = True
        while Move8 == True:
            print('What room do you go into?')
            print()
            time.sleep(0.5)
            print('*Room 1*')
            print()
            print('*Room 2*')
            print()
            print('*Room 3*')
            Move8 = input()
            if Move8 == ('1') or Move8 == ('room 1'):
                print('This room looks like a television room')
                time.sleep(0.5)
                print('The room is small with very little furniture')
                print()
                print('making it a bad room to hide in')
                Move8 = True
            if Move8 == ('2') or Move8 == ('room 2'):
                print('This room is a small washroom, which is bad for hiding')
                print()
                Move8 = True
            if Move8 == ('3') or Move8 == ('room 3'):
                print('This room looks like a storage room')
                print()
                time.sleep(0.5)
                print('It\'s got lots of equipment and is large room')
                print()
                time.sleep(0.5)
                print('making it a perfect room for hiding')
                break
            else:
                print('You are not able to do that at this moment')
                Move13 = True

        time.sleep(2)
        EighthCutscene = ('''CREEAKK... The stairs door suddenly opens...
You see James Miller with a huge knife in his hands
IT\'S THE KILLER!!!
YOU HAVE TO RUNN!
Luckily, the lights go out again, giving you a chance to hide''' + "\n")
        print()
        for character in EighthCutscene:
            sys.stdout.write(character)
            time.sleep(0.06)
        Move9 = True
        while Move9 == True:
            print('What room do you run into to hide from the killer?')
            Move9 = input()
            if Move9 == ('1') or Move9 == ('room 1') or Move9 == (
                    '1') or Move9 == ('room 1'):
                print(
                    'This would not be a good room for hiding as the killer may be too familiar with it'
                )
                print()
                time.sleep(0.5)
                print('Go to another room, QUICK')
                Move9 = True
            if Move9 == ('2') or Move9 == ('room 2') or Move9 == (
                    '2') or Move9 == ('room 2'):
                print(
                    'This would not be a good room for hiding as the killer may be too familiar with it'
                )
                print()
                time.sleep(0.5)
                print('Go to another room, QUICK')
                Move9 = True
            if Move9 == ('3') or Move9 == ('room 3') or Move9 == (
                    '3') or Move9 == ('room 3'):
                print('Great!')
                print()
                print('The storage room is the perfect place to hide')
                break
            else:
                print('You are not able to do that at this moment')
                Move9 = True
        time.sleep(2)
        NinthCutscene = ('''You decide to hide behind a small cabinet
The killer opens the door and looks around but does not turn on the lights
That was very fortunate'''
                         "\n")
        print()
        for character in NinthCutscene:
            sys.stdout.write(character)
            time.sleep(0.06)
        TenthCutscene = ('''You hear his footsteps fading away so you decide
it\'s time to get up and keep moving through the house''' + "\n")
        print()
        time.sleep(2)
        for character in TenthCutscene:
            sys.stdout.write(character)
            time.sleep(0.06)
        time.sleep(1)
        print(
            'You move through the corridor, take the right turn, and end up in an open space'
        )
        print()
        time.sleep(1)
        print('This area has very limited furniture, so it is very spacious')
        print()
        time.sleep(1)
        print('There are two corridors that start from this area')
        print()
        time.sleep(0.5)
        print('There is one to your right and one to your left')
        print()
        time.sleep(0.5)
        Move10 = True
        while Move10 == True:
            print('Which corridor will you take?')
            print()
            print('*The right one or the left one?*')
            Move10 = input()
            if Move10 == ('right') or Move10 == ('right one') or Move10 == (
                    'right corridor') or Move10 == ('the right one'):
                print(
                    'As you walk through this corridor and take its left turn, you see two doors and a dead end'
                )
                print()
                time.sleep(1)
                print('THUD THUD')
                print()
                time.sleep(1)
                print('IT\'S THE KILLER AGAIN!')
                print()
                time.sleep(1)
                print('Quick! You have no time to think')
                Move11 = True
                while Move11 == True:
                    print('What door do you open?')
                    print()
                    print('*1 or 2?*')
                    Move11 = input()
                    Move11 = int(Move11)
                    DeathDoor = random.randint(1, 2)
                    if Move11 == DeathDoor:
                        print('You open the door and enter')
                        print()
                        time.sleep(2)
                        print('It\'s an empty room')

                        EleventhCutscene = (
                            '''As soon as you go further into the room, James Miller walks in holding
his knife. When you see him, you stumble backwards and fall down.''' + "\n")
                        print()
                        time.sleep(2)
                        for character in EleventhCutscene:
                            sys.stdout.write(character)
                            time.sleep(0.06)
                        TwelfthCutscene = (
                            '''"Well, well, well. If it isn\'t the neighbour, Mr.Wilson. Leaving so soon?
I thought we could have a nice dinner. You know, ever since I moved into this neighbourhood, I\'ve had a
special type of hatred for you. Since you are here, now is a good time as any is to get rid of this hatred"'''
                            + "\n")
                        print()
                        time.sleep(2)
                        for character in TwelfthCutscene:
                            sys.stdout.write(character)
                            time.sleep(0.08)
                        time.sleep(1)
                        print('THUD THUD THUD')
                        print()
                        time.sleep(1)
                        print(
                            'He starts running towards you with a menacing look on his face...'
                        )
                        print()
                        time.sleep(2.5)
                        print('SHHHING...')
                        TirteenthCutscene = (
                            '''Miller is standing right above you with a smile on his face. As you look down
at your chest, you can see a massive blade going through you. Before you can respond, Miller pulls the knife
out in a quick motion and runs out of the room''' + "\n")
                        print()
                        time.sleep(2.5)
                        for character in TirteenthCutscene:
                            sys.stdout.write(character)
                            time.sleep(0.04)
                        FinalCutscene = (
                            '''You lay there with blood pouring out of your chest. Everything hurts as you
are trying to process everything in your head. Why did James have such hatred for you? Why did he host
a dinner close to halloween? Why did he kill his guests?''' + "\n")
                        print()
                        time.sleep(2.5)
                        for character in FinalCutscene:
                            sys.stdout.write(character)
                            time.sleep(0.1)
                        ExtraFinal = (
                            '''As you are trying to answer these questions, you can feel your body not being able
to breathe anymore. Everything is fading to black. With that, you accept your fate and close your eyes...'''
                            + "\n")
                        print()
                        time.sleep(2.5)
                        for character in ExtraFinal:
                            sys.stdout.write(character)
                            time.sleep(0.13)
                            break
                        time.sleep(1.5)
                        #YOU DIED ART
                        print(' ')
                        print('Play Again?')
                        PlayAgain = input()
                        if PlayAgain == ('yes') or PlayAgain == ('y'):
                            PlayAgain = True
                        if PlayAgain != ('yes') or PlayAgain != ('y'):
                            print('Okay')
                            print()
                            print('Goodbye')
                            exit()
                    if Move11 != DeathDoor:
                        print(
                            'As you enter the room, you see a window showing the outside...'
                        )
                        FinalCutsceneTwo = (
                            '''Without hesitation, you bust open the window and jump through it to freedom.
This portion of the property faces the back of the neighbourhood, so you take off towards the side of the manor'''
                        )
                        for character in FinalCutsceneTwo:
                            sys.stdout.write(character)
                            time.sleep(0.1)

                        FinalCUTsceneTwo = (
                            '''As you look back, you can see James Miller looking at you through the window.
He does not bother chasing after you and that\'s how you know you are truly free'''
                        )
                        time.sleep(1)
                        print()
                        for character in FinalCUTsceneTwo:
                            sys.stdout.write(character)
                            time.sleep(0.1)
                        print()
                        print('Play Again?')
                        PlayAgain2 = input()
                        if PlayAgain2 == ('yes') or PlayAgain2 == ('y'):
                            PlayAgain = True
                        if PlayAgain2 != ('yes') or PlayAgain2 != ('y'):
                            print('Okay')
                            print()
                            print('Goodbye')
                            exit()
            if Move10 == ('left') or Move10 == ('left one') or Move10 == (
                    'left corridor') or Move10 == ('the left one'):
                print(
                    'As you walk through this corridor and take its right turn, you see two doors and a dead end'
                )
                print()
                print('THUD THUD THUD')
                print()
                print('IT\'S THE KILLER, JAMES MILLER!')
                print()
                print('Quick! You have no time to think')
                Move12 = True
                while Move12 == True:
                    print('What door do you open?')
                    print()
                    print('*1 or 2?*')
                    Move12 = input()
                    if Move12 == ('1') or Move12 == ('room 1'):  #deathdoor2
                        print(
                            'As you rush into this room, all you see is emptiness'
                        )
                        print()
                        time.sleep(1)
                        print(
                            'All of the walls are white and there is no furniture...'
                        )
                        print()
                        time.sleep(1)
                        print('Except for a single odd chair in the centre')
                        ExtraCutscene3 = (
                            '''That is when you spot a window facing and showing the outside.
It is facing the area of the neighbourhood on which your house is located on. As soon as you realize this,
you make a run for it''' + "\n")
                        print()
                        for character in ExtraCutscene3:
                            sys.stdout.write(character)
                            time.sleep(0.1)
                        print('THUD THUD THUD')
                        print()
                        time.sleep(1)
                        print(
                            'As you take a look behind you, you  see James Miller...'
                        )
                        print()
                        time.sleep(1)
                        print('He runs up to you and pushes you to the ground')
                        ExtraCutscene4 = ('''" Hello there, Mr.Watson.
Don\'t get up, scum. I have waited to get rid of
you for a long time and now is my chance. Your existence has caused a
fire to start burning inside me...
Now is my chance to extinguish it"''' + "\n")
                        print()
                        for character in ExtraCutscene4:
                            sys.stdout.write(character)
                            time.sleep(0.1)
                        print()
                        time.sleep(1)
                        print('Miller jumps at you with his knife')
                        print()
                        time.sleep(1)
                        print('Somehow, you manage to dodge the attack')
                        print()
                        time.sleep(1)
                        Move16 = 0
                        while Move16 < 3:
                            print()
                            print('*Press P to punch*')
                            print('*Press R to run*')
                            print('*Press K to kick*')
                            Move17 = input()
                            Move16 = Move16 + 1
                            if Move17 == ('p') or Move17 == ('k'):
                                print('You connected')
                                print()
                                time.sleep(1)
                                print('But, he manages to get back up')
                            if Move17 == ('r'):
                                print('He\'s too fast')
                                print()
                                time.sleep(1)
                                print('He will end up catching you')
                            else:
                                print(
                                    'You are not able to do that at this time')
                        ExtraCutscene5 = (
                            '''"Whatever you do is futile, you cannot hurt me.
Now, it\'s my turn..."''' + "\n")
                        print()
                        for character in ExtraCutscene5:
                            sys.stdout.write(character)
                            time.sleep(0.1)
                        print()
                        time.sleep(1)
                        ExtraCutscene6 = (
                            '''Miller jumps at you again and this time you can feel something
go through your stomach. As you look down, you can see Miller's massive blade sticking
out of your body, surrounded by loads of your blood. You suddenly fall
to the floor and Miller runs out of the room''' + "/n")
                        for character in ExtraCutscene6:
                            sys.stdout.write(character)
                            time.sleep(0.1)
                        print()
                        time.sleep(1)
                        ExtraCutscene7 = ('''Now, you lay there on the floor
with evrything rushing through your mind. You keep wondering what
you did to make Miller develop such a deep hatred for you''' + "\n")
                        for character in ExtraCutscene7:
                            sys.stdout.write(character)
                            time.sleep(0.1)
                        ExtraCutscene8 = ('''As you continue wondering, the
pain gradually increases. To solve that, you close your eyes and accept your fate...'''
                                          + "\n")
                        print()
                        print('Play Again?')
                        PlayAgain2 = input()
                        if PlayAgain2 == ('yes') or PlayAgain2 == ('y'):
                            PlayAgain = True
                        if PlayAgain2 != ('yes') or PlayAgain2 != ('y'):
                            print('Okay')
                            print()
                            print('Goodbye')
                            exit()
                    if Move12 == ('2') or Move12 == ('room 2'):
                        time.sleep(2)
                        print(
                            'As you open this door and walk down the short hallway, you reach the main living room!'
                        )
                        print()
                        time.sleep(1)
                        print(
                            'Without hesitation, you see the main entrance door open and rush to escape...'
                        )
                        time.sleep(2)
                        print('THUD!')
                        print()
                        print('GLUB!')
                        time.sleep(2)
                        print()
                        print(
                            'Before you know it, James Miller has caught up to you and shuts the door in front of you...'
                        )

                        FinalCutsceneThree = (
                            '''"Well, well, well. If it isn\'t the neighbour, Mr.Wilson.
How come you are leaving so soon. I wanted to have a nice calm dinner with
my neighbours to get to know them better. I guess that was never possible considering the
fact that I\'ve hated this filthy area and the all of the people in it
from the start! Especially because of the way it looks and how the people act and behave"'''
                            + "\n")
                        print()
                        time.sleep(2)
                        for character in FinalCutsceneThree:
                            sys.stdout.write(character)
                            time.sleep(0.1)
                        FINALCutsceneThree = (
                            '''"So when I moved here, I made it my goal to get rid of every single
person in this neighbourhood even if that meant...''' + "\n")
                        print()
                        time.sleep(1.5)
                        for character in FINALCutsceneThree:
                            sys.stdout.write(character)
                            time.sleep(0.1)
                        EXFinalCutsceneThree = ('''"KILLING them!"''')
                        print()
                        time.sleep(1.5)
                        for character in EXFinalCutsceneThree:
                            sys.stdout.write(character)
                            time.sleep(0.25)
                        print()
                        time.sleep(0.5)
                        print(
                            'With that, Miller leaps towards you with his knife pointing towards you'
                        )
                        Move13 = True
                        while Move13 == True:
                            print()
                            print('*Press P to punch*')
                            print('*Press R to run*')
                            if Move13 == ('p') or Move13 == ('P'):
                                print('You connected!')
                                break
                            if Move13 == ('r') or Move13 == ('R'):
                                print(
                                    'You try to run, but he keeps getting in your way'
                                )
                                Move13 = True
                            else:
                                print(
                                    'You are not able to do that at this moment'
                                )
                                Move13 = True
                        ExtraCutscene1 = (
                            '"AHHH! You bastard! Im going to kill you!!"')
                        for character in ExtraCutscene1:
                            sys.stdout.write(character)
                            time.sleep(0.1)
                        print()
                        time.sleep(1)
                        print('He runs at you again')
                        Move14 = True
                        while Move14 == True:
                            print()
                            print('*Press P to punch*')
                            print('*Press R to run*')
                            print('*Press K to kick*')
                            if Move14 == ('p') or Move14 == ('P'):
                                print('You connected!')
                                break
                            if Move14 == ('r') or Move14 == ('R'):
                                print(
                                    'You try to run, but he keeps getting in your way'
                                )
                                Move14 = True
                            if Move14 == ('k') or Move14 == ('K'):
                                print('You connected!')
                                break
                            else:
                                print(
                                    'You are not able to do that at this moment'
                                )
                                Move14 = True
                        time.sleep(1)
                        print()
                        print(
                            'You have weakened him and now he is on the floor')
                        time.sleep(1)
                        print()
                        print('Now is your chance to run!')
                        Move15 = True
                        while Move15 == True:
                            print()
                            print('*Press P to punch*')
                            print('*Press R to run*')
                            print('*Press K to run*')
                            if Move15 == ('p') or Move15 == ('P'):
                                print('You have a chance to escape!')
                                Move15 = True
                            if Move15 == ('r') or Move15 == ('R'):
                                print('You make a run for the door')
                                break
                            if Move15 == ('k') or Move15 == ('K'):
                                print('You have a chance to escape!')
                                Move15 = True
                            else:
                                print(
                                    'You are not able to do that at this moment'
                                )
                                Move15 = True
                        print()
                        time.sleep(1)
                        ExtraCutscene2 = (
                            '''Without stopping, you bust open the door and
sprint out. As you look back, you can see James Miller on the floor staring at you
while holding his leg. When you see him not able to get up and pursuit, that is when
you know you are truly free''')
                        for character in ExtraCutscene2:
                            sys.stdout.write(character)
                            time.sleep(0.1)
                        print()
                        print('Play Again?')
                        PlayAgain2 = input()
                        if PlayAgain2 == ('yes') or PlayAgain2 == ('y'):
                            PlayAgain = True
                        if PlayAgain2 != ('yes') or PlayAgain2 != ('y'):
                            print('Okay')
                            print()
                            print('Goodbye')
                            exit()
