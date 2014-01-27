label tutorial_gas:
    $ form = "gas"
    
    scene bg wreckagegas
    with dissolve

    "Expansion!"
    "Crowded, hot space! The solids are in great distress. Everything here is combining explosively and you’re shaking, shaking hard, every little atom, bouncing off yourself and against the solids, and it hurts. That’s what hot is."
    "Soon you are too fast and vast for this space. This is more unpleasant than you recall."
    menu:
        "EXPAND":
            play sound "Audio/Gas first Expand.ogg"
            "You press against everything. A solid above you removes itself, reducing to smaller solids, which fall apart and plunge through you. Flames rise and eat away at you, but there are ways of quick movement on heat, clever expansion."
            menu:
                "RISE":
                    "There is space above you, room to get bigger and bigger and faster and faster and hotter and hotter until you burst from the vessel into an accommodating emptiness. And then you can spread thin, to slow and cool."
                    "Out here the radiant heat is low and vibrations are softly organic and soothing moisture rides on currents of flowing gas."
                    "This is actually rather pleasant."
                    menu:
                        "SEARCH":
                            "Too much emptiness here, with strange and unfamiliar solids at the margins. Shapes with fringes and slick spots and oozing fluids, unusual densities."

                            "They are much too odd. This form is insufficient for understanding them."
                            menu:
                                "CONGEAL":
                                    jump tutorial_emotions
    return

label gas_gas:
    $ form = "gas"
    call set_place("yard")
    play music "Audio/Outdoor Atmosphere.ogg"
    "There is a void here."
    if gasBackyard:
        jump gas_gas_yard
        
    $ gasBackyard = True
        
    menu:
        "KNOW THROUGH EXPANSION":
            "You expand to fill the local void."
            "The void has no upper surface: it extends infinitely, into the cold of interplanetary space. Ugh! That's some vertigo. So you make yourself denser, and sink."
            jump gas_gas_yard
    return

label gas_gas_yard:
    call set_place("yard")
    play music "Audio/Outdoor Atmosphere.ogg"
    menu:
        "The void’s LOWER SURFACE is fringed and very moist. A TANGLED EXTRUSION rises from the center of it. Further off a large VERTICAL SURFACE rises. An ENCLOSED ZONE with a smooth exterior sits beside the vertical surface."
        
        "ENMESH with the LOWER SURFACE":
            jump gas_gas_grass
        
        "ENVELOP the VERTICAL SURFACE":
            jump gas_gas_houseexterior
        
        "ENWREATHE the TANGLED EXTRUSION":
            jump gas_gas_tree
        
        "ENTER the ENCLOSED ZONE":
            jump gas_gas_car
            
        "EXAMINE the VERTICAL SURFACE" if seewindow and seefear:
            jump gas_gas_enterhouse
                    
        "EXAMINE the VERTICAL SURFACE" if seewindow and not seefear:
            jump gas_gas_failenterhouse

        "CHANGE FORM":
            jump form_change_gas_yard

    return
    
label gas_gas_grass:
    "Enmeshing with this surface is quite entertaining! Many solid strips entangle with one another. Ahh, how cunning! You fill the voids between them."
    "But neither the void nor the solids react to your enmeshing. Ahh, a disappointment!"
    "(But not an unexpected one. Most solids are quite boring.)"
    jump gas_gas_yard
    
    return
    
label gas_gas_houseexterior:
    $ seewindow = True
    
    "This surface forms one wall of a large enclosed zone-- too large for your mass to fully enwreathe, too rough and confusing to easily penetrate. A limited point of access would make things simpler, give your molecules somewhere to condense."
    "You return to an ordinary volume. To be spread so thin is exhausting."
    jump gas_gas_yard
    
    return
    
label gas_gas_tree:
    play sound "Audio/Tree Rustle 2.ogg"
    "The tangled extrusion trembles and vibrates. Its lower section is rough and unified and its upper section is complex. When you move quickly through the upper portion, it wobbles and flaps quite pleasingly. Ahh!"
    "You do it again. Ahhhh!"
    jump gas_gas_yard
    
    return
    
label gas_gas_car:
    "The zone is no real puzzle. The puzzles you solved as a young one were much harder. You find a hundred ways into the zone in under a minute. Inside, the zone is just as inert as it was on the outside. Ahh! A disappointment!"
    jump gas_gas_yard
    
    return
    
label gas_gas_enterhouse:
    "The fear was leaking out over here, through a narrow gap in a pane of smooth solid. You gather yourself and blow through on a current of moving air."
    call set_place("bathroom")
    "For a moment, you fill the local void. It has a smooth upper surface, smooth lower surface, smooth protrusions on the floor and the smooth reflective walls-- and in the center, something organic is moving."
    "It’s sensed you. Its bellows are inhaling. And then--"
    play sound "Audio/Gas Form Inhaled&Exhaled.ogg"
    "It EXHALES! OUCH! What an incredible vibration! In the tiny space everything reflects off everything else. Every bit of you shakes and spins and for a moment you, too, are terrified."
    "The organic solid rushes for a wall. The wall opens and shuts and blasts you with a backdraft of moving gasses. Your volume flails helplessly! Solids crash and fall!"
    "And when you have stilled and gathered yourself, the organic solid is nowhere to be seen."
    jump mouth_gas

    return
    
label gas_gas_failenterhouse:
    "There is a possible point of access here. But this form is insufficient to test its safety."
    jump gas_gas_yard
    
    return
    
label mouth_gas:
    $ form = "gas"
    
    if gasBathroom:
        jump mouth_gas_bathroom
    
    $ gasBathroom = True
    
    menu:
        "There is a void here."
        
        "KNOW THROUGH EXPANSION":
            "You expand to fill the local void-- and ahh! Alluring! Lots of fascinating textures here! Smoothness, fringedness-- a lot of moisture, too."
            jump mouth_gas_bathroom

    return

label mouth_gas_bathroom:
    call set_place("bathroom")
    "There’s a LARGE CONTAINER embedded in the floor, covered in smaller solids. There’s a SMALL CONTAINER by one of the walls, filled with fluids. there’s a RAISED SMOOTH SURFACE coming out of the wall. And then there’s another fringed LOWER SURFACE here-- similar to, but different, from the one outside."
        
    if seemirror:
        "There is an EXCEPTIONALLY SMOOTH SURFACE here, on the wall behind the RAISED SMOOTH SURFACE."
            
    if seesink:
        "There is a DEPRESSION here, in the RAISED SMOOTH SURFACE." 
        
    if seegameboy:
        "There is a SMALL ELECTRIC SOLID here, on top of the SMALL CONTAINER."
        
    if seeduckey:
        "There is a SMALL YIELDING SOLID here, in the vicinity of the LARGE CONTAINER."
        
    menu:
        "Quite a complex space!"
        
        "ENTER the SMALL CONTAINER":
            jump mouth_gas_toilet
        
        "ENTER the LARGE CONTAINER":
            jump mouth_gas_bathtub
        
        "ENWREATHE the RAISED SMOOTH SURFACE":
            jump mouth_gas_counter
        
        "ENMESH with the LOWER SURFACE":
            jump mouth_gas_rug
        
        "ENWREATHE the EXCEPTIONALLY SMOOTH PLANE" if seemirror:
            jump mouth_gas_mirror
        
        "ENSWIRL the DEPRESSION" if seesink:
            jump mouth_gas_sink
        
        "ENVELOP the YIELDING SOLID" if seeduckey:
            jump mouth_gas_duckey
        
        "ENWREATHE the FRINGED SOLID" if seetoothbrush:
            jump mouth_gas_toothbrush
        
        "ENWREATHE the SMALL ELECTRIC SOLID" if seegameboy:
            jump mouth_gas_gameboy

        "CHANGE FORM":
            jump form_change_mouth_bathroom
        
    return
    
label mouth_gas_toilet:
    "This small container is full of fluids! You absorb some of them. Neutral, ordinary fluids, that ripple at your touch. That’s nice."
    "Strangely, you can feel the pressure of electric fields in the vicinity of this solid. Ahh! Interesting!"
    "But they are very slight, hard to pin down. Perhaps another form could perceive this more usefully."
    "You retreat back to the center of the space."
    jump mouth_gas_bathroom

    return
    
label mouth_gas_bathtub:
    "This large container is completely empty! It fits your entire volume quite nicely. Ahh!"
    "There are some small solids here. You flow amongst them. Most are unremarkable..."
    "...But one is light and yielding and very oddly-shaped. It rocks gently against your touch. How interesting! Perhaps another form could perceive this more usefully."
    "You retreat back to the center of the space."
    jump mouth_gas_bathroom
    
    return
    
label mouth_gas_counter:
    $ seemirror = True
    $ seesink = True
    
    "The raised smooth surface is piled high with smaller solids. You flow between them and they knock and rattle against one another most entertainingly. Ahh!"
    "There is a DEPRESSION in the surface. You swirl around it, which is mildly entertaining. On the wall behind the surface is an EXCEPTIONALLY SMOOTH PLANE. Hmm! Alluring, both of these!"
    "You retreat back to the center of the space."
    jump mouth_gas_bathroom

    return
    
label mouth_gas_rug:
    "You settle to the lower surface and enmesh with it. A layer of short fibers! Ahh! Fascinating!"
    "There are fluids here, a lot of them, and smaller solids trapped among the fibers. You flow amongst them, and absorb some of the fluids-- but you can distinguish between none of them. Ahh, a disappointment! Perhaps another form could do better."
    "You retreat back to the center of the space."
    jump mouth_gas_bathroom

    return
    
label mouth_gas_mirror:
    "You attempt to surround the exceptionally smooth plane. What a boring texture!"
    "Surprisingly, there is a hidden void here, behind the pane! With smaller solids in it, too. Ahh! Fascinating!"
    "You retreat back to the center of the space."
    jump mouth_gas_bathroom
    
    return
    
label mouth_gas_sink:
    "You swirl around inside the smooth depression. Ahh!"
    "Hmm. It turns out the depression is not particularly interesting. It’s smooth and shallow. It’s just okay."
    "You retreat back to the center of the space."
    jump mouth_gas_bathroom
    
    return
    
label mouth_gas_duckey:
    "You envelop the unusual solid on the large container on the floor. It has an unusual shape and is quite yielding. It moves beneath your pressure."
    "So you constrict the unusual solid. Ahh! A strong vibration, a surprise! Not particularly pleasant!"
    "But you calm yourself, and try again. Ahh! It makes the vibration again. A curious little one, a little funny. Hah! How funny that you were surprised!"
    "You retreat back to the center of the space."
    jump mouth_gas_bathroom
    
    return

label brain_gas:
    if gasLivingroom:
        jump brain_gas_livingroom
        
    $ gasLivingroom = True
    
    menu:
        "There is a void here."
        
        "KNOW THROUGH EXPANSION":
            "This void is relatively large! Like many of the voids in this place, it has a fringed lower surface and a smooth upper surface. But there are many things in this void, and they are all so fascinating!"
            jump brain_gas_livingroom
    
    return

label brain_gas_livingroom:
    if not televisionOn:
        "There is a VIBRATING CUBOID. It emits electromagnetic fields! So alluring! There is also a LARGE YIELDING MASS against one wall. Beside it sits an ODD EXTRUSION that emits heat and electromagnetic waves. So fascinating! And in front of it is a RAISED PLANAR SURFACE."
    if televisionOn:
        "There is a VIBRATING CUBOID. It emits many forms of radiative energy! So overwhelming! There is also a LARGE YIELDING MASS against one wall. Beside it sits an ODD EXTRUSION that emits heat and electromagnetic waves. So fascinating! And in front of it is a RAISED PLANAR SURFACE."
    menu:
        "So much to explore!"
        
        "ENVELOP the VIBRATING CUBOID":
            jump brain_gas_tv
        
        "ENCIRCLE the LARGE YIELDING MASS":
            jump brain_gas_couch
        
        "ENWRAP the ODD EXTRUSION":
            jump brain_gas_lamp
        
        "ENVELOP the SMALL SOLID":
            jump brain_gas_remote
            
        "EXAMINE the VERTICAL SURFACE":
            jump brain_gas_coffeetable

        "CHANGE FORM":
            jump form_change_brain_livingroom
            
    return
    
label brain_gas_tv:
    if televisionOn:
        "You surround the vibrating cuboid. It’s so strange! Subtle electromagnetic fields thrum excitingly through your volume. It reminds you of entertainment devices from the homeworld."
        "Not much else to it, though. It is largely inert."
        jump brain_gas_livingroom

    if not televisionOn:
        "Ahh! These vibrations are now much too intense! Multiple frequencies, many spectra-- quite overwhelming!"
        "You retreat back to the center of the room."
        jump brain_gas_livingroom

    return
    
label brain_gas_couch:
    "This mass has an entertaining texture. If you press against it very hard, it, it will move a little. Ahh! Entertaining!"
    "Not much else happening here, though. The mass is inert, and too large for you to move. A mild disappointment, perhaps."
    jump brain_gas_livingroom
    
    return
    
label brain_gas_lamp:
    "Ahh! This extrusion emits many radiative fields! How interesting!
    You press close. There is a radiative energy field here. It speeds you up and your temperature increases! How interesting!"
    "And there is an electromagnetic field, too. Also interesting! Entertaining! You swirl around in it. Ahh! How nice!"
    jump brain_gas_livingroom
    
    return
    
label brain_gas_remote:
    "There is a small solid here, emitting suble radiative fields. Ahh! They are soothing. You wrap closely around it. It is like the entertainment units on the homeworld. Tingly! Fascinating!"
    "Not much else here, however. Ahh! But it's nice, isn't it?"
    jump brain_gas_livingroom
    
    return
    
label brain_gas_coffeetable:
    "So boring. So intert. A raised planar surface. It bears up a small solid. Now, that solid is more interesting!"
    jump brain_gas_livingroom

    return
    
label emotions_gas:
    if gasBedroom:
        jump emotions_gas_bedroom
        
    $ gasBedroom = True
    
    menu:
        "There is a void here."
        
        "KNOW THROUGH EXPANSION":
            "You expand to fill the local void. And-- ahh! How strange!"
            jump emotions_gas_bedroom
    
    return

label emotions_gas_bedroom:
    "The organic solid is here, wheezing and trembling somewhere in the void-- but you cannot find it. The space is crowded. There are SMALL STRANGE SOLIDS on the floor, and DANGLING SOLIDS on the upper surface. In one corner, a SOOTHING EXTRUSION emits pulses of radiative energy. Beside it, a YIELDING SURFACE welcomes your touch."
    if closetOpen:
        "There is a fascinating organic solid here, trembling in the center of the room."
        
    menu:
        "How unusual! How enthralling!"
                
        "ENVELOP the SMALL STRANGE SOLIDS":
            jump emotions_gas_toys
            
        "ENGAGE with the YIELDING SURFACE":
            jump emotions_gas_bed
            
        "ENWREATHE the SOOTHING EXTRUSION":
            jump emotions_gas_lamp
            
        "EXAMINE the DANGLING SOLIDS":
            jump emotions_gas_mobile
            
        "ENWREATHE the ORGANIC SOLID" if closetOpen:
            jump emotions_gas_child

        "CHANGE FORM":
            jump form_change_emotions_bedroom
        
    return
    
label emotions_gas_toys:
    "You surround the small strange solids. They have unusual shapes and textures. They move slightly, too, but not enough to keep you entertained. Ahh! So disappointing!"
    "Are these really sufficient to keep the organic solids entertained? They must be such boring people, alas!"
    jump emotions_gas_bedroom

    return
    
label emotions_gas_bed:
    "You press against the yielding surface. It moves slightly. Hmm! And it’s puffy, containing much extra space. You are able to enmesh with its upper surfaces."
    "That’s about it, though. It’s otherwise inert. Ahh! A disappointment!"
    jump emotions_gas_bedroom

    return
    
label emotions_gas_lamp:
    "The soothing extrusion pulses with various kinds of radiative energy. It is similar to the entertainment devices on the homeworld. How interesting!"
    "But there isn’t much to do here besides absorb radiative energies. You've absorbed many radiative energies today already... and there are more pressing matters at hand..."
    jump emotions_gas_bedroom

    return
    
label emotions_gas_mobile:
    $ closetOpen = True
    
    "Ahh! These solids are FASCINATING!"
    "They hang and swing. When you flow between them, they move and strike one another and vibrate entertainingly. So nice! So entertaining! THIS, truly, is what you have been searching for all along!"
    "Or is it? Something in this space reacts to the dangling solids as you do. A wall-surface is moving nearby, swinging open. The organic solid’s vibrations are louder, now. Hmm!"
    "And now, finally, you can meet!"
    jump emotions_gas_bedroom
    
    return
    
label emotions_gas_child:
    "Finally! The organic solid itself!"
    "Like many organics it possesses a bellows, always sucking gasses in and blowing them out. So unusual! So interesting!"
    "You swirl around its upper portion and tickle it with your tiniest atoms. It responds by wiggling. Ahh! Organic solids! So weird! So much fun!"
    "But this form, alas, is insufficient for communication with beings as limited and crude as organic solids."
    jump emotions_gas_bedroom
    
    return
    
label end_gas:
    "For a little bit everything is very weird."
    "And then the wierdness starts to feel normal, and it goes away. And then you're sitting in your room again... but it's different, somehow."
    "Maybe it's different because you're different. You've changed. You're someone... new."
    "Your parents would probably be mad. You didn't ask them if it was okay to change. But they're not here to tell you no, are they?"
    "It's not like they could send you back to your room, anyway, because you could just eat the wall..."
    "Or think your way out..."
    "Or turn into a cloud of gas... and fly away!"
    menu:
        "So you get up off the floor..."
        
        "Open the door.":
            "Everything you once knew looks different, a little strange, a little weird."
            "You can remember what it felt like to lick this place all over, and swirl around it like a cloud."
            "You know what emotions a lamp has, what the TV tastes like. You can remember thinking real hard about the remote."
            "Everything is cooler now, somehow. More exciting!"
            "You wonder what it would be like to blow down the street, or eat a whole ice-cream shop, or go into school and see what everyone's really feeling."
            "You wonder what a library looks like to the biggest brain in the world!"
            menu:
                "It's time to go. To see the world with new eyes."
                
                "Open the door...":
                    "...and head outside."
                    
                    menu:
                        "THE END":
                            jump start

    return
