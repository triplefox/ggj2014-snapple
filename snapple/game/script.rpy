# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")

# The game starts here.
label start:
    call init_

    menu:
        "From Beginning":
            jump tutorial_brain
        "2. Gas Puzzle":
            jump gas_gas
        "3. Mouth Puzzle":
            menu:
                "3. Mouth Puzzle (Gas)":
                    jump mouth_gas
                "3. Mouth Puzzle (Mouth)":
                    jump mouth_mouth
                "3. Mouth Puzzle (Brain)":
                    jump mouth_brain
                "3. Mouth Puzzle (Emotions)":
                    jump mouth_emotions
        "4. Warrior Scene":
            jump warrior
        "5. Brain Puzzle":
            jump brain_brain
        "6. Emotions Puzzle":
            menu:
                "6. Emotions Puzzle (Gas)":
                    jump emotions_gas
                "6. Emotions Puzzle (Mouth)":
                    jump emotions_mouth
                "6. Emotions Puzzle (Brain)":
                    jump emotions_brain
                "6. Emotions Puzzle (Emotions)":
                    jump emotions_emotions
        "7. End":
            menu:
                "7. End (Gas)":
                    jump end_gas
                "7. End (Mouth)":
                    jump end_mouth
                "7. End (Brain)":
                    jump end_brain
                "7. End (Emotions)":
                    jump end_emotions
        "Dev sandbox":
            jump sandbox
    return

label init_:
    $ fenceExamined = False
    $ fenceOpen = False
    $ seewindow = False
    $ seefear = False
    $ seemirror = False
    $ seesink = False
    $ seetoothbrush = False
    $ seeduckey = False
    $ seegameboy = False
    $ televisionOn = False
    $ closetOpen = False
    $ gasBackyard = False
    $ gasBathroom = False
    $ gasLivingroom = False
    $ gasBedroom = False
    $ outOfTheCloset = False
    $ selectedToy = False
    $ lickedtoilet = False
    $ aterug = False
    $ ateduck = False
    $ atebrush = False
    $ ategameboy = False
    $ brainDone = False    
    
    return
