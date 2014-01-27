label tutorial_mouth:
    
    scene bg wreckagemouth
    with dissolve

    play music "Audio/Burning Ship.ogg"
    "HOT."
    "HOT."
    "HOTTTTTTTTTTTTTTTT."
    "FLYMOBILE BROKEDED. NO FLY NO MORE. JUST SPIT ANGRY HEAT CANDY AND FLICKERY ELECTRIC CANDY AND POOFY SMOKE CANDY. ALSO, LARGE METAL ROD CRUSHING ALL KNOW ORGANS. HURT IT HURTS BOO-BOO HURRRRRRTS."
    "EAT? CAN EAT. ALWAYS CAN EAT."
    menu:
        "CONSUME AND ANALYZE 'HEAT CANDY'":
            "PFFFFTTTTBBTHTTTT. OWWWWW. NO GOOD! HEAT CANDY MADE UP OF 12.7 PERCENT ZESTY MACHINE OILS AND OWN FLESH NOW TASTE LIKE MAGIC BARBEQUE, BUT NO GOOD BECAUSE KILLING ME. HELLLLLP. WAAAAAAAAAH, WAAAAAAAAAH, WAAAAAAAAAH."
            menu:
                "CONSUME AND ANALYZE 'ELECTRIC CANDY'":
                    play sound "Audio/Eat Electronics.ogg"
                    "BZZZZZZZZTAAAAAAAAAAAAAAAUGGGGGH."
                    "DELICIOUS! *ANALYZING* SUBSTANCES DISCOVERED: ELECTRICITY, ELECTRICITY, AND ELECTRICITY. NOTE SELF: ALWAYS LICK ELECTRICAL SOCKETS FOR TASTETONGUE GOODTASTES."
                    menu:
                        "CONSUME AND ANALYZE 'SMOKE CANDY'":
                            "COUGHCOUGHCOUGHCOUGH. LESS CORPOREAL THAN LOOKS. REMINDS SELF OF OWN LARGELY GASEOUS MOMMYDADDY, WHO SELF ALSO YUMDEVOURED. MISS MOMMYDADDY WAAAAAAAAAAAAH."

                            "*ANALYZING* SMOKE CANDY PROBABLE INDICATOR THAT SHIP IS ABOUT TO ‘SPLODE. SEE SOON MOMMYDADDY!"
                            menu:
                                "CONSUME METAL ROD":
                                    play sound "Audio/Eating a Metal Bar.ogg"
                                    "MUNCHCRUNCHMMMMM. TASTE LIKE FREEDOM. ALSO SEARING ARGHBLARGHMANTIUM COOKED TO PERFECT TEMPERATURE. FAVORITE TASTEBLAST WHEEEEEE SQURIMFLAIL."
                                    "STILL TRAPPED THOUGH. BUT GOOD LAST MEAL. TIME FOR PRESS SHINY BUTTONS UNTIL THE FUN NOISESOUNDS HAPPEN YAY. THEN DEATH. YAY!"
                                    "BUT ALSO WHAAAAAAAAAAA HATE EVERYYYYTHING."
    stop music
    play music "Audio/Outdoor Atmosphere.ogg"
    jump tutorial_gas

label gas_mouth:
    menu:
        "STRANGE, POSSIBLY INHOSPITABLE SURROUNDINGS? LICK EVERYTHING.":
            "OOOOOOOO OUTSIDE LAND MADE OF TOO MANY FLAVORS FOR COUNT. ONE, TWO… GIVE UP."
            jump gas_mouth_yard
    return

label gas_mouth_yard:
    call set_place("yard")
    play music "Audio/Outdoor Atmosphere.ogg"
    menu:
        "TASTESEE GROUND FROSTING, MIGHTY CHOCOLATE VEGETABLE STICK, WHEELED JELLOCAKE, AND SHELTER FULL OF A BILLIONTY WONDERFUL TASTEFEELS. WANT INNNNNNNNNNNNN."
        
        "ULTRAGARGLE GROUND FROSTING":
            jump gas_mouth_grass
        
        "UNHINGE ENTIRE SPINE AND DEVOUR SHELTER":
            jump gas_mouth_houseexterior
        
        "CHEWCHOMP ON GIANT CHOCOLATE VEGETABLE STICK":
            jump gas_mouth_tree
        
        "GIANT WHEELED JELLOCAKE. MEGAMOUTH. NOW.":
            jump gas_mouth_car
                    
        "LAP AND PAW AT SEE-THROUGH WALL" if seewindow:
            jump gas_mouth_failenterhouse

        "SMELLTONGUE BADFEELS" if seefear:
            jump gas_mouth_fear
            
        "CHANGE FORM":
            jump form_change_gas_yard    

    return
    
label gas_mouth_grass:
    "MMMMMMMM. FULL OF NOURISHING SPROINGLES AND WARBOBS. PROLLY PLANET’S MOST VALLABLE RESOURCE. V’RY RARE, WANT EAT ALL."
    "*ANALYZING* SUBSTANCES DISCOVERED: PLANT LIFE, FUNGI, DIRT, TRACE AMOUNTS OF DNA FROM ZILLIONTY CREATURES. MAYBE ALL LIVE IN DELICIOUS SHELTER FOR EATS AT ONCE? FOUND GIANT HAPPY MEAL YAAAAAAAAAAY HOPE TOY INSIDE WAILFLAILBABBLEDROOL."
    jump gas_mouth_yard
    
    return
    
label gas_mouth_houseexterior:
    "MRRRRRRRRRRRRRRRRGHHHHHHBLARF. NO DO. SHELTER TOO BIG. FIND INVISIBLE-COLORED SEE-THROUGH WALL, THOUGH. GO THROUGH SOMEHOW?"
    jump gas_mouth_yard
    
    return
    
label gas_mouth_tree:
    play sound "Audio/Tree Rustle 2.ogg"
    "TOO TALL, MADE OF ARMOR. WILL TAKE LONGTIMES FOR GASTRIC FLUIDS TO MASHBASH INTO FOODPILE. BOOOOOOOOOOOGARGLESPITPOOP."
    "INITIAL LICKINGS FIND DNA OF BIG AND LITTLE FLESHCREATURES. WONDER IF FRIENDLY?!! HOPE EDIBLE! IF CAN’T EAT FRIENDS, WHO CAN COUNT ON?"
    jump gas_mouth_yard
    
    return
    
label gas_mouth_car:
    "MMMMMMMMM. CAKE BITES MADE OF MORE THINGS THAN EXPECT. FULL TANGY OIL CREAMS TOO! MILDLY LETHAL TOXINS DETECTED. PROBABLY FAVORITE MILDLY LETHAL TOXINS EVER DROOLSLURPED. CAN’T WAIT FOR EXPLOSIVE WASTE EXPULSION PROCESS. ALWAYS FUNFUNFUN WHEEEEEE."
    jump gas_mouth_yard
    
    return
    
label gas_mouth_fear:
    "EMOTIONBLARGHS DETECTED. PROLLY FROM FLESHCREATURE IN SHELTER. NO CAN SEE, BUT FEEL. EAT ANYWAY! EAT ALL. ALWAYSALWAYSALWAYS."
    "URRRRGH, THESE DIFFERENT. SPOILED? NO, USUALLY LIKE SPOILED THINGS. AND ALL THINGS. TASTE LIKE NO WANT BE HERE. TRYING ESCAPE INTO HIDE HOLE. WHAT MEAN?"

    return
    
label gas_mouth_failenterhouse:
    "SEE-THROUGH WALL TASTES INVISIBLE TOO! UNDERSTATED FLAVOR. LIGHT ON PALETTE, YET DECEPTIVELY SATISFYING. A VERITABLE FLAVOR ADVENTURE."
    "GONNA POOP NOW WOOOOOOOOOOOOOOO."
    "NO CAN EAT TO INSIDE, THOUGH. CAN NO GET GOOD BITE. GIVE UP, TAKE 47 SECOND NAP THEN SQUEEEEEEEEAL FOR TWO HOURS."
    jump gas_mouth_yard

    return

label mouth_mouth_bathroom:
    call set_place("bathroom")
    "USE HEARTONGUE AND SMELLTONGUE AND BARF EVERYWHERE. EVERYTHING NOW COATED IN OWN DELICIOUS SYRUPS. HAPPYWOBBLE! WHAT NEW THING DEVOUR FIRST?"
    "CAN TASTESEE STRANGE FURRYGROUND, MAJESTIC PORCELAIN DONUT THRONE, LARGE PORCELAIN CRATER, AND BEAAAAAUTIFUL PORCELAIN CARAMEL ALTAR."

        
    if seemirror:
        "OH! NOW SEE SHINY PORTAL TOO!"
            
    if seesink:
        "ALSO SEE TASTYTASTE-LOOKING FLUID TUBE." 
        
    if seegameboy:
        "AND A BABY MACHINE BOX. CAN'T WAIT FOR EATS."
        
    if seeduckey:
        "IS A RUBBER FOWL CHEWCAKE TOO."
        
    menu:
        "HOPE ALL FITS IN MOUTH. MAYBE TASTEFIND TASTEFORMATION ON FLESHBEAST FOR HIVEMIND LARVAL BRAINFRAME. WILL DO WITH GREAT YESNESS."
        
        "LICK THE PORCELAIN DONUT THRONE":
            jump mouth_mouth_toilet
        
        "GIGANTOSLURP PORCELAIN CRATER":
            jump mouth_mouth_bathtub
        
        "GIGANTOSLURP PORCELAIN CARAMEL ALTAR":
            jump mouth_mouth_counter
        
        "INGEST ENTIRE FURRYGROUND":
            jump mouth_mouth_rug
        
        "TURBOLICK SHINY PORTAL" if seemirror:
            jump mouth_mouth_mirror
        
        "BITE FLUID TUBE" if seesink:
            jump mouth_mouth_sink
        
        "CONSUME RUBBER FOWL CHEWCAKE" if seeduckey:
            jump mouth_mouth_duckey
        
        "CHOMP CHOMP BRISHY BRUSH" if seetoothrbrush:
            jump mouth_mouth_toothbrush
        
        "TURBOSLURP BABY MACHINE BOX" if seegameboy:
            jump mouth_mouth_gameboy

        "TRACK FLESHBEAST" if lickedtoilet and ateduck and atebrush and ategameboy:
            jump mouth_mouth_completion
    
        "CHANGE FORM":
            jump form_change_mouth_bathroom
        
    return
    
label mouth_mouth_toilet:
    $ lickedtoilet = True
                                     
    "COLD. TOO COLD!!!!! SYRUP BURP SALIVA FOR MAKE WARM. NOW FEELS GOOD ON TASTETONGUE. MMMMMMMM. GIGGLEFART. *ANALYZING* SUBSTANCES DISCOVERED: SKIN CELLS, FECAL MATTER, HAIR, BLOOD, COCAINE, FAINT ECHOES OF FLUSHED 'GOLDFISH'"
    "HAPPYSQUEAL. TARGET PRESUMABLY COMPOSED OF THESE THINGS. HIVEMIND LARVAL BRAINFRAME UPDATED."
    jump mouth_mouth_bathroom

    return
    
label mouth_mouth_bathtub:
    "TASTETONGUE FEEL FUNNY. DECIDE TO SCREECH BECAUSE PROBABLE DEATH AND ALSO BECAUSE JUST FEEL LIKE SCREECHING RIGHT NOW. UNFURL TASTETONGUE. WHAT IS IN IT THERE IS SOMETHING IT SCREAAAAAAAAAAMKILLLLLLLLLLLLLLLLLLLLLLLLLL."
    "PLOP. IT IS A TINY BABY CLEANBAR. TASTETONGUE FEELS FRESH AND SPARKLES. WONDERRRRRFUL. *ANALYZING* CREATURE USE FOR RUB ON SKIN EVEN THOUGH IS MOST WONDERFUL DELICACY. SILLY FLESHBEAS--"
    "OK GONNA SCREEEEEECH AGAIN TIME FOR MORE SCREECHING ALWAYS SCREECHING."
    jump mouth_mouth_bathroom
    
    return
    
label mouth_mouth_counter:
    "CANNOT INGEST FOR TOO MUCH BIGNESS. SMELLTONGUE CAN HEARTASTE MUCH FROM ABOVE, THOUGH. MUST GO UP. UP. UPPPPPPPPPPPPPPPPPPPPPWAAAAAAAAAAAAAAHHH."
    jump mouth_mouth_bathroom

    return
    
label mouth_mouth_rug:
    $ aterug = True
                                                                                                                                                                                                                                    
    "SO MANY THINGS. FURRY THE BILLIONTASTE! MMMMMMMMMSNART."
    "*ANALYZING* SUBSTANCES DISCOVERED: ANIMAL FUR, SKIN CELLS, FECAL MATTER, DIRT OF A THOUSAND DAYS, A HYPER-EVOLVED GERM SMARTER THAN ANY OTHER CREATURE ON THIS ENTIRE MUDMASS, INSECT GUTS, CREATURE’S FOOTPRINTS."
    "HAPPYSQUEALFLAIL. FEET ATTACHED TO FLESHBEAST. HELP WITH THE FOLLOWMENT. HIVEMIND BRAINFRAME UPDATED."
    jump mouth_mouth_bathroom

    return
    
label mouth_mouth_mirror:
    "SEE SELF IN SHINY PORTAL AND LICK SELF BECAUSE OF COURSE LICK SELF ALWAYS LICK SELF (EXCEPT WHEN LICKING OTHER THINGS). WHY NO TASTE LIKE ALWAYS TASTE WHEN ALWAYS LICK SELF. DOES NOT COMPUTE SO CRYWAILBAMFLAIL. RAGE BITE SHINY PORTAL, BUT IS INVINCIBLE."
    "DON’T GET. CAN’T ANYTHING. NEED HELP FROM THINKFRIEND."
    jump mouth_mouth_bathroom
    
    return
    
label mouth_mouth_sink:
    "MUNCH MUNCH MUNCH MUNCH. CRUNCHY METALLIC OUTSIDE WITH CREAMY LIQUID FILLING. SALIVA CHAMBERS RE-NOURISHED. STOMACH ACID BURBLE POWERS OVERWHELMING."
    "TIME TO PUKE YAAAAAAAAAAAAAAAY."
    jump mouth_mouth_bathroom
    
    return
    
label mouth_mouth_duckey:
    $ ateduck = True                                                                                                                                                                                                                                
                                                                                                                                                                                                                                    
    "CHEW CHEW CHEW CHEWY. SQUEAK? WHY IT SQUEAK? THE DEVILLLLLLLLLLL. OR PERHAPS SOUNDFOOD? DELICIOUS TO TASTETONGUE AND HEARTONGUE. WONDERFUL! GIGGLE WIGGLE WET SELF UNCONTROLLABLY."
    "ANALYZING* FLESHBEAST FEELS MANY THINGS FOR THIS THING. MADE OF MANY CHEWY SUBSTANCES BUT EMOTIONBLARGHS TOO. EMOTIONBLARGHS TASTE LIKE BLOOD."
    "YAYSQUEAL. UNDERSTAND FLESHBEAST’S EMOTIONAL RESONANCE KINDA. HIVEMIND BRAINFRAME UPDATED."
    jump mouth_mouth_bathroom
    
    return
           
label mouth_mouth_toothbrush:
    $ atebrush = True                                                                                                                                                                                                                                
                                                                                                                                                                                                                                    
    "OOOOOOOOOOOO SO MANY HAIRSPIKES. TASTETONGUE AND FEELTONGUE DEVOURING EACH OTHER IN HAPPINESS. AGAIN! AGAIN! I WILL PUKE UP AND EAT BIRSHY BRUSH AGAIN."
    "SLURP SLURP GOBBLE CHOMP EVEN BETTER SECOND TIME."
    "*ANALYZING* BILLIONFINITY MOUTH DNAS YUM! FLESHBEAST BACTERIA NOW MY BACTERIA TOO! FLESHBEAST CAN LOSE TEETH AND MAKE NEW TEETH. WANT TO EAT ITS TEETH!"
    "BURPSQUEAL. MANY INFORMATIONS GAINED. HIVEMIND BRAINFRAME UPDATED."                                                                                                                                                                                                                                
    jump mouth_mouth_bathroom
    
    return   
          
label mouth_mouth_gameboy:
    $ ategameboy = True                                                                                                                                                                                                                                
                                                                                                                                                                                                                                    
    "TINY MACHINE FULL OF LIGHT AND SOUND. ANT MAN STOMP ANT TURTLES UNTIL POOF CLOUD. TURTLE MURDER DELICIOUS! PROBABLOBS FLESHBEAST FIGHT LIKE THIS. VALABLE INFRMATION!"
    "TASTES LIKE RAGE BUT ALSO HAPPYGUNFUN. WHAT MEAN? WHAT DO? OH NO! FLESHBEAST PROBABLY MUDMASS’ MIGHTIEST FIGHTMAN. SCARRRRRRYCRY."
    "*ANALYZING* OUTER SUBSTANCE ARTIFICIAL AND MEGAMIGHTY EVEN WITH AUXILIARY GASTRO-SYRUPS ENGAGED. NO FULLY DIGEST. WILL STORE IN ANAL RESERVOIR POUCH FOR LATER."
    "SCAREDSQUEAL. HIVEMIND BRAINFRAME UPDATED."                                                                                                                                                                                                                                
    jump mouth_mouth_bathroom
    
    return  
      
label mouth_mouth_completion:
    "MMMMM-MMMMM WHEEEEEE. HIVEMIND BRAINFRAME SWELLING WITH DELICIOUS DATA. NOW READY TO FIND FLESHCREATURE AND ENGAGE FOREVER HUG."
    jump brain_mouth                                                                                                                                                                                                                                
                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                    

label brain_mouth:
    menu:
        "ROOM OF LOTSA LITTLE THINGS AND FEW BIG THINGS. MANY SOFT, LIKE SLUMBERCHAMBER OR COLONY OF SLEEPING AMINALS CURRENTLY MARINATING IN FLAVOR SACS. THEY FOR LATER. THEY FOR LATER."
        
        "TIME TO PUKE JUICES ON EVERYTHING AGAIN YAAAAAAAAY":
            jump brain_mouth_livingroom
    
    return

label brain_mouth_livingroom:
    if not televisionOn:
        "SEE STRANGE SCREENBOX, LARGE SLEEPSURFACE, GLOWY CANDY HIVE, FLAT TABLON, AND BITE-SIZE BROWNIE SQUARE."
    if televisionOn:
        "SEE SCARY GLOWY AND SCREAMING SCREENBOX, LARGE SLEEPSURFACE, GLOWY CANDY HIVE, FLAT TABLON, AND BITE-SIZE BROWNIE SQUARE."
    menu:
        "SO MANY THINGS WHAT FOR SLURPSCARFING!"
        
        "NIBBLE SCREENBOX":
            jump brain_mouth_tv
        
        "TAKE CHUNK OUT OF SLEEP SURFACE":
            jump brain_mouth_couch
        
        "CHOMP ON GLOWY CANDY HIVE":
            jump brain_mouth_lamp
        
        "BOBBLEGOBBLE THE BROWNIE SQUARE":
            jump brain_mouth_remote
            
        "SCARF TABLON LEG":
            jump brain_mouth_coffeetable

        "CHANGE FORM":
            jump form_change_brain_livingroom
            
    return
    
label brain_mouth_tv:
    if televisionOn:
        "HMMHUMM TASTE LIKE ALMOST NOTHING. BORRRRRRRRRING ‘CEPT OWN GASTROJUICES AND FAINT HINTS OF EMOTIONBLARGHS. FLESHBEAST FEEL SCARED HERE. ALSO EXCITED, HAPPY. AND ALONE."
        jump brain_mouth_livingroom

    if not televisionOn:
        "INITIATE KILL RITUAL ON SCARY SCREENBOX."
        "CHANT CHANT CHANT SCREAAAAAAAAAAAAAAAAAM. DESTROY SCARYSCARE ENEMY. TURN SELF INSIDE OUT FOR REVEAL COMBAT ORGANS. HEE-HEE KILL MODE TICKLES."
        "NOW CHAAAAAAAAAAAAARGEBOUNCEOFFINEFFECTIVELY OK RUN HIDE FOREVER."
        jump brain_mouth_livingroom

    return
    
label brain_mouth_couch:
    "SOFT LIKE SPACE MARSHMALLOW, FURRY LIKE SPACEDOG. *ANALYZING* FLESHBEAST USES FOR RECLINING. SHAPE SUGGEST FLESHBEAST KNEES BEND ONLY ONE WAY, UNLIKE ALL OTHER KNOWN LIFE."
    "WISH HADN’T EATEN OWN KNEES THAT ONE TIME."
    jump brain_mouth_livingroom
    
    return
    
label brain_mouth_lamp:
    "MMMMMMMMYUMFUFFERFUL. SO GLOWY I CAN SEE TASTE IN OWN 18 DIGESTIONAL SACS. LOOKS LIKE SEETONGUE NEED GET NEW JOB HEEEEEEEEEGIGGLEPEE."
    jump brain_mouth_livingroom
    
    return
    
label brain_mouth_remote:
    $ televisionOn = True

    "MMMMMMM TASTY BROWNIE GOES DOWN FAST, MORE FAST THAN MOMMYDADDY DID BUT WITH MORE CREAM, LESS SCREAM. WHAAAAAAAAA NO LIKE INSIDE BRAIN REMINDS OF THE BADFEELS. JUST WANT TO BE HOOOOME."
    "BZZZTFLORP. REBOOTING."
    "TASTY TASTES! *ANALYZING* BROWNIE SQUARE CONTAINS--"
    "HUH? SOUND AND LIGHT COME FROM SCREENBOX. SCARYSCARY NO LIKE WHY MOMMYDADDY LEAVE?"
    jump brain_mouth_livingroom
    
    return
    
label brain_mouth_coffeetable:
    "TOUGHER THAN LOOKS. BUT DELICIOUS BECAUSE CHALLENGE AND ALSO TINY BUGTHINGS LIVING INSIDE. WORMSQUIRM IN TUMMY PARTY MOUTHFUN HOPE THEY CAN SWIM!"
    "*ANALYZING* MADE OF SAME SUBSTANCE AS OUTSIDE CHOCOLATE VEGETABLE STICK. NO THINK FLESHBEAST UNDERSTAND WHAT VEGETABLE FOR. I TOO SMART FOR OWN GUD SOMETIMESZ."
    jump brain_mouth_livingroom

    return
    
label emotions_mouth:
    menu:
        "COLORFUL TINY TASTYPLACE. YAAAAAAAAAAAY. FULL OF TOYS! WAS RIGHT: IS GIANT HAPPY MEAL. BESTDAYBESTDAYBESTDAY. EXCEPT… WHY FEEL FAMILIAR? BADFEELS COMING BACK JUST WANT PLAYEAT GO AWAY BADFEELS SCREEEEEEEEEECHSCREAM."
        
        "POOPUKE ON EVERYTHING WITH A SENSE OF KNOWING FINALITY":
            "WHEEEEEEEEEEE NEVER GETS OLD."
            jump emotions_mouth_bedroom
    
    return

label emotions_mouth_bedroom:
    "FLESHBEAST IN LITTLE ATTACHED ROOM FOR SOME REASON. LOCKED BARRIER WAAAAAAAAAH. MAYBE FIND SOMETHING FOR MAKE COME OUT AND PLAYTIMES? SEE CEILING FOOD ORBS, GLOWY LAVA PASTRY, SOFT SLEEPSURFACE, AND PILE OF FUNTRONS (YAY FUNTRONS). "
    if closetOpen:
        "HELLO FLESHBEAST HI FLESHBEAST SEE YOU PLAYDROOL."
        
    menu:
        "TOYYYYYYYYS AND FUNNNNNNNN."
                
        "SEETONGUE DOUBLE-PUKE ON TOYS":
            jump emotions_mouth_toys
            
        "NIBBLE SOFT SLEEPSURFACE":
            jump emotions_mouth_bed
            
        "SUCK DELICIOUS WARMCREAMS FROM GLOW PASTRY":
            jump emotions_mouth_lamp
            
        "ATTEMPT MOUTHFACE CATAPULT MANEUVER":
            jump emotions_mouth_mobile
            
        "LICK FLESHBEAST" if closetOpen:
            jump emotions_mouth_child

        "CHANGE FORM":
            jump form_change_emotions_bedroom
        
    return
    
label emotions_mouth_toys:
    $ selectedToy = True

    "COLORS! SHAPES! BENDY BLOBS AND “CARROTY CHOP ACHTUNG”! TINY BOXES, BIG BOXES, BOXES THAT SNAP TOGETHER. TINY GREEN FLESHBEAST STATUES. TINY WHEELED JELLOCAKES. LITTLE SHELTERS WITH PRETTY DRESS FLESHBEAST STATUES INSIDE. BEAN BAG CHILDREN. ALL MUST GO IN MOUTH. ALLLLLLLL AT ONCE FOR EXTRA COMBO TASTEPASTE. OPEN MOUF ANNNNND--"
    "MRRRGGH. WHY FAMILIAR? KNOW FROM SOMEWHERE. MOUTHFACEHEADBODY HURRRTS WHAAAAAAAAAA."
    "STOPSTOPSTOP. EMOTIONBLARGHS FROM TWO “GROWN-UP” FLESHBEAST STATUES. LONELYSAD WHAT MEAN? SMILESAPPY TOO BUT ONLY SOMETIMES. DNA ALL OVER THEM. SKIN. TEARS. USED FREQUENTLY. GIVE TO YOUNG FLESHBEAST? YES, GIVE! GIV--"
    "*REMEMBERRRRRING*. SO MANY HEADPICTURES AT ONCCCCE. MOMMYDADDY COMES INTO ROOM. GONE FOR LONG TIME. TOO LONG TIME. NEVER THOUGHT WOULD SEE AGAIN. LONELY. LONELY HURT. ANGRY. SAY “FOR OWN GOOD.” SAY “MONSTER. MUTANT. DANGEROUS.” NEVER WANT MOMMYDADDY LEAVE AGAIN. NEVERNEVERNEVER. MOVE CLOSE, CLOSER, PERFECT. MOMMYDADDY TURN BACK FOR LEAVE. NEVER GET CHANCE. MUNCHCRUNCHSPLRUNCH."
    "NOW TOGETHER FOREVER."
    "ALERT: Sensitive memory breached. Collective brainwipe software initiated."
    "..."
    "...."
    "....."
    "......"
    "......."
    "GOO-GOO?"
    jump emotions_mouth_bedroom

    return
    
label emotions_mouth_bed:
    "SOFT AND CHEWY, LIKE OTHER SLEEPSURFACE EXCEPT WITHOUT CRUNCHY OUTSIDE. TASTYPASTE, BUT SLEEPSURFACES USUALLY BETTER WITH SLEEPING THINGS ON THEM."
    "*ANALYZING* MANY EMOTIONBLARGHS HERE. MOSTLY SAD, LONELY."
    jump emotions_mouth_bedroom

    return
    
label emotions_mouth_lamp:
    "MAGNIFICENT! SUCH WARMS, SO SLITHERY. LIKE EATING DRACULA SNAKEBAT OF HYPERVENULON XII ONLY NO WAIT COMPLETELY SAME. NO THINGS THIS TASTYTASTE IN CAN’T REMEMBER HOW LONG."
    "CAN’T REMEMBER LOTS OF THINGS."
    jump emotions_mouth_bedroom

    return
    
label emotions_mouth_mobile:        
    "FLY TO FOOD ORBS AT CEILING GOGOGO! WHEEEEEEEEEEEEEEEEEE."
    "NO WORK. SMALL AND HAVE NO KNEES. ALSO NO UNDERSTAND CONCEPT OF “CATAPULT.”"
    jump emotions_mouth_bedroom
    
    return
    
label emotions_mouth_child:
    "IS SOFT, BUT AFRAID. PROBABLY DON’T EAT. MAYBE EAT A LITTLE. LATER. SQUIRMPOOPONITSFEETINAPPROPRIATELY."
    "FLESHBEAST SMILES. EMOTIONBLARGHS TASTE WARM. ALSO SAD UNDERNEATH. LONELY? WHAT MEAN?"
    "SEEM FAMILIAR, BUT NO REMEMBER WHY. GOO?"
    jump emotions_mouth_bedroom
    
    return