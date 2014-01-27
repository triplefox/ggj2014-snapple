
label tutorial_brain:
    $ seewindow = False
    $ seefear = False

    play music "Audio/UFO Drone.ogg" fadein 5.0
    
    scene bg shipdashboard

    "Three holodiodes on the console flash brightly in a standard Veluvian alert pattern. One, one, three, one, two, three. One, one, three, one, two, three. Alert. Alert."
    play sound "Audio/alarm.ogg"
    "The display shows the planet, doused as it is in saltwater, at standard magnification. Everything is standard. Very excellent. The salty planet’s gravitational field is currently overpowering the ship’s hologravity engine booster magnets, as indicated by the Veluvian alarm."
    "The alarm is still functioning standardly. Very excellent. The holodiodes are well-designed, with a long lifespan and a bright, clear flash at each moment. One, one, three, one, two, three. Alert."
    "The craft is crashing down through the atmosphere of the saltwater sphere. One, one, three, one, two, three. Alert."    
    stop music
    stop sound
    play sound "Audio/UFO Powers off.ogg"
    "Blue gives way to green. Red, red, red, red, red, red. The green interrupts, colliding into the ship with a loud crunching shudder. Black."
    
    jump tutorial_mouth

label tutorialbrain2:
    $ form = "brain"
    scene bg fencebrain
    with dissolve

    menu:
        "SURVEY":
            jump tutorial_brain_outside

    return
    
label tutorial_brain_outside:
    menu:
        "Odd: a series of long, thin rectangular obelisks half-embedded in the ground in a rigid pattern. There are many bright-green life-things gathered around it, perhaps in silent prayer."
        "EXAMINE LIFE-THINGS":
            "Countless and very-many. Each seems to be reaching for the thin obelisks. Are these the dominant life-thing in this planet-place?"
            jump tutorial_brain_outside
        "EXAMINE OBELISKS" if not fenceOpen:
            "A strange-thing. The surface has an incredible level of detail, as if it were carefully and reverently sculpted. Religious significance, assuredly."
            "Some of the obelisks float above the ground, held in place by small metal objects, one of which seems to be capable of triggering a glorious release."
            "Hypothesis: freeing the floating obelisks has an 86\% chance of endearing you to the bright-green life-things."
            $ fenceExamined = True
            jump tutorial_brain_outside
        "FREE OBELISK" if fenceExamined and not fenceOpen:
            play sound "Audio/Open Obelisk.ogg"
            "The metal device swings easily open. The floating obelisks gently glide out at an angle from the buried obelisks. The life-things show no signs of recognition for this act."
            "Beyond the obelisks, there is a wide area enclosed on each side by obelisks and filled with even more life-things."
            $ fenceOpen = True
            jump tutorial_brain_outside
        "GO OBELISK CATHEDRAL" if fenceOpen:
            call set_place("yard")
            jump gas_brain_yard

    return

label gas_brain:
    if brainBackyard:
        jump gas_brain_yard
    
    $ brainBackyard = True
    
    menu:
        "SURVEY":
            jump gas_brain_yard
    
    return

label gas_brain_yard:
    $ form = "brain"
    call set_place("yard")
    menu:
        "The obelisks enclose three sides of a wide rectangular area filled with masses of life-things. The fourth side is mostly occupied by a tall, flat surface adorned with squares of a reflective material. Ahead is a tremendous life-thing, menacingly towering above the others by orders of magnitude."
        "EXAMINE KING OF THE LIFE-THINGS":
            "Is this stoic monstrosity the ruler of these mute revelers?"
            "Dour and terrible, this silent tyrant glowers from on high at the countless life-things that shiver in fear or reverence below it. Foul, inky shadows gather in pools at its feet in tribute to what is doubtlessly a hideous might."
            "It does not react. Best to leave it."
            jump gas_brain_yard
        "EXAMINE FLAT SURFACE":
            "The wall is largely unadorned, except for a flat rectangular gem, reflective and almost completely transparent."
            jump gas_brain_yard
        "EXAMINE MACHINE":
            "It’s a car, obviously."
            jump gas_brain_yard
        "CHANGE FORM":
            jump form_change_gas_yard
    return

label mouth_brain:
    if brainBathroom:
        jump mouth_brain_bathroom
    
    $ brainBathroom = True

    menu:
        "SURVEY":
            jump mouth_brain_bathroom

    return

label mouth_brain_bathroom:
    call set_place("bathroom")

    menu:
        "A cold room with a number of plain, smooth surfaces. There are several basins. On the ground-place is a rectangle which seems to be filled with curious facsimiles of the life-things."
        
        "EXAMINE EMPTY BASIN":
            "The long, empty basin has several metal tubes which looming precariously over it. If this device has a purpose, it is indiscernible. An art object, perhaps."
            jump mouth_brain_bathroom

        "EXAMINE RAISED BASIN" if seesink:
            "Two odd wheels jut out from either side of a metal tube on top of the basin."
            "Turning one of the wheels, a fluid pours out from the metal tube and flows down a hole at the bottom of the basin. Turning the wheel in the reverse direction, the fluid stops."
            "A standard nutrient sludge dispenser."
            jump mouth_brain_bathroom

        "EXAMINE FILLED BASIN":
            "A basin filled with some sort of cold nutrient sludge. Discarded from a previous meal, perhaps. Behind the basin is a rectangular silo, perhaps intended for storage, and on top of which rests a grey rectangular object."
            $ seegameboy = True
            jump mouth_brain_bathroom

        "EXAMINE LIFE-THING RECTANGLE":
            "There is a rectangle of things which appear to be similar in shape to the life-things, but which seem slightly less filled with life."
            jump mouth_brain_bathroom

        "EXAMINE REFLECTIVE GEM" if seemirror:
            "Another flat gem, which is highly reflective. You can see your floating crystalline shellskin in the reflection, beautiful and perfect."
            "Along one side are a set of metal devices similar to the ones which held the floating obelisks in place. You angle the gem, revealing an interior compartment which holds a number of curious artifacts."
            $ seetoothbrush = True
            jump mouth_brain_bathroom

        "EXAMINE HOLLOW OBJECT" if seeduckey:
            "Along the edge of the empty basin is a small yellow object, which smells hollow. Another art object, perhaps."
            jump mouth_brain_bathroom

        "EXAMINE ARTIFACT" if seetoothbrush:
            "One of the artifacts is a small, thin rod. On one end are a number of short fibers that jut out in a mostly singular direction. The fibers appear to be slightly damp."
            jump mouth_brain_bathroom

        "EXAMINE GREY RECTANGLE" if seegameboy:
            "It appears to be some sort of non-holographic device, widely agreed to be the most delicious of all classes of devices."
            jump mouth_brain_bathroom

        "CHANGE FORM":
            jump form_change_mouth_bathroom

    return


label brain_brain:
    $form = "brain"
    menu:
        "SURVEY":
            jump brain_brain_livingRoom

    return

label brain_brain_livingroom:
    jump brain_brain_livingRoom

label brain_brain_livingRoom:
    call set_place("livingroom")

    menu:
        "This room appears to be some sort of bridge. An odd command chair lies opposite a display screen. Near the command chair is a light-emitter and a flat surface."
        
        "EXAMINE GLOWTOWER":
            "A tall vertical spindle, flared at the base and at the top. Light spills out the top of the spindle and fills the room."
            jump brain_brain_livingRoom

        "EXAMINE COMMAND CHAIR":
            "A very strange command chair. It must be for a very wide sort of creature, as the chair is nearly four times as wide as any sort of standard model."
            jump brain_brain_livingRoom

        "EXAMINE RECTANGLE" if not televisionOn:
            "Another of the strange non-holographic devices that seem prevalent on this planet. If there is a means of interfacing with this, it is one which is beyond the understanding of your mindcrystal."
            jump brain_brain_livingRoom

        "EXAMINE GLOWRECTANGLE" if televisionOn:
            "The command screen is active, showing a series of images of life-things with their appendages wrapped around each other. They are also offering objects to one another and vibrating the air particles surrounding them."
            "Do these life-things communicate by exchanging objects and making vibrations? They are perhaps not so alien after all."
            "It would be easy to replicate these particular vibrations using rudimentary crystallic harmonic vibrationization. Which objects are appropriate is another issue entirely."
            $ brainDone = True
            jump brain_brain_livingRoom

        "EXAMINE BUTTONPLANK" if televisionOn:
            "A slender plank, studded with a number of beautiful grey gems. It is glistening and damp."
            jump brain_brain_livingRoom

        "CHANGE FORM" if not brainDone:
            jump form_change_brain_livingroom

        "FOLLOW LIFE-THING" if brainDone:
            "You follow after the life-thing..."
            jump emotions_brain

    return

label emotions_brain:
    menu:
        "SURVEY":
            jump emotions_brain_bedroom

    return

label emotions_brain_bedroom:
    menu:
        "This seems to be a sort of intelligence room. A map hangs suspended in midair above a command table of sorts, and on the ground there are artifacts splayed out in a particular arrangement. On a stand rests what appears to be a display case for some aquatic organism."

        "EXAMINE ARTIFACTS":
            if not selectedToy:
                "A number of what appear to be communication tokens lie in various configurations on the ground. This could perhaps be used in tandem with vibrations to send messages, but it’s difficult to ascertain which would be correct to use."
            if selectedToy:
                "Your other-shape has selected what it believes to be a suitable artifact to offer."
            jump emotions_brain_bedroom

        "EXAMINE AQUARIUM":
            "A cone which seems to hold prisoner some sort of primitive organism. It is vibrating at a frequency which produces slight heat."
            jump emotions_brain_bedroom

        "EXAMINE GALACTIC MAP":
            "Some sort of odd holographic map. It shows an array of planets suspended in midair. There seems to be no power crystal attached to the device, however. How do the holograms hold their form, otherwise?"
            jump emotions_brain_bedroom

        "EXAMINE OPENING" if closetOpen and not outOfTheCloset:
            "An ugly gem panel hangs from a slight angle. Inside, there is mostly shadow, but vibrations are emanating from the place in a regular pattern."
            jump emotions_brain_bedroom

        "OFFER ARTIFACT" if closetOpen and selectedToy and not outOfTheCloset:
            "As shown on the display panel in the command room, you offer what you believe to be a correctly significant communication object while making correct vibrations."
            "The life-thing emerges from the shadow-place and makes vibrations in response. In what is most likely a ritual form of accepting the vibrations, the life-thing takes the communication object and is standing in front of you expectantly."
            $ outOfTheCloset = True
            jump emotions_brain_bedroom

        "EXAMINE FLESHBEAST" if outOfTheCloset:
            "The curious thing appears to be completely not-crystal in form. How odd! It is most similar to the wretched eaterbeasts of Crebulin VII, with the distinctive difference that it is not trying to use its singular wet tentacle to eagerly ascertain the properties of everything in the immediate vicinity."
            jump emotions_brain_bedroom

    return