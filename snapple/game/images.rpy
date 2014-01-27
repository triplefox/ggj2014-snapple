image bg yardbrain = "Art/YardBrain.jpg"
image bg yardmouth = "Art/YardMouth.jpg"
image bg yardgas = "Art/YardGas.jpg"
image bg yardemotions = "Art/YardCloud.jpg"

image bg bathroombrain = "Art/BathroomBrain.jpg"
image bg bathroommouth = "Art/BathroomMouth.jpg"
image bg bathroomgas = "Art/BathroomGas.jpg"
image bg bathroomemotions = "Art/BathroomEmotion.jpg"

image bg bedroombrain = "Art/BedroomBrain.jpg"
image bg bedroomemotions = "Art/BedroomEmotion.jpg"
image bg bedroomgas = "Art/BedroomGas.jpg"
image bg bedroommouth = "Art/BedroomMouth.jpg"

image bg fencebrain = "Art/FenceBrain.jpg"

image bg livingroombrain = "Art/LivingRoomBrain.jpg"
image bg livingroomemotions = "Art/LivingRoomEmotion.jpg"
image bg livingroomgas = "Art/LivingRoomGas.jpg"
image bg livingroommouth = "Art/LivingRoomMouth.jpg"

image bg mothrage = "Art/MothRage.jpg"

image bg shipdashboard = "Art/ShipDashboard.jpg"
image bg wreckagegas = "Art/WreckageGas.jpg"
image bg wreckagemouth = "Art/WreckageMouth.jpg"

image bg title = "Art/TitlePage.jpg"

label form_change:
    while True:
        menu:
            "Gas":
                $ form = "gas"
                call set_place(cur_place)
            "Mouth":
                $ form = "mouth"
                call set_place(cur_place)
            "Brain":
                $ form = "brain"
                call set_place(cur_place)
            "Emotions":
                $ form = "emotions"
                call set_place(cur_place)
            "Done":
                return
    return

label set_place(place=None, transition="dissolve"):
    $ cur_place = place
    if cur_place == "yard":
        if form == "gas":
            scene bg yardgas
        elif form == "mouth":
            scene bg yardmouth
        elif form == "brain":
            scene bg yardbrain
        elif form == "emotions":
            scene bg yardemotions
    elif cur_place == "bathroom":
        if form == "gas":
            scene bg bathroomgas
        elif form == "mouth":
            scene bg bathroommouth
        elif form == "brain":
            scene bg bathroombrain
        elif form == "emotions":
            scene bg bathroomemotions
    elif cur_place == "bedroom":
        if form == "gas":
            scene bg bedroomgas
        elif form == "mouth":
            scene bg bedroommouth
        elif form == "brain":
            scene bg bedroombrain
        elif form == "emotions":
            scene bg bedroomemotions
    elif cur_place == "livingroom":
        if form == "gas":
            scene bg livingroomgas
        elif form == "mouth":
            scene bg livingroommouth
        elif form == "brain":
            scene bg livingroombrain
        elif form == "emotions":
            scene bg livingroomemotions
    else:
        "(place undefined)"
    if transition=="dissolve":
        with dissolve
    else:
        with fade
    return
