label tutorial_emotions:
    $ form = "emotions"
    call set_place("yard")    

    "rush of sensations"
    "hints of familiar and new"
    "follow sweet sense trail"
    
    menu:
        "follow":
            jump tutorialbrain2

label gas_emotions_yard:
    jump gas_emotions
label gas_emotions:
    $ form = "emotions"
    call set_place("yard")    
    menu:
        "A place."
        
        "grass":
            "united blanket"
            "radiating million"
            "determinations"
            jump gas_emotions
            
        "tree":
            "large and powerful"
            "connections flow under the"
            "blanket in search of...?"
            jump gas_emotions
        
        "back yard":
            "gentle laps of sensation"
            "drifts down along air currents"
            "carrying unknowns"
            $ seefear = True
            jump gas_emotions
            
        "FEAR" if seefear:
            "approach and digest"
            "surprise. interest. anger."
            "discomfort. spikes."
            $ seewindow = True
            jump gas_emotions
            
        "house":
            "permeates the air"
            "stems from single location"
            "approach the unknown"
            jump gas_emotions
        "change":
            jump form_change_gas_yard

    return

label mouth_emotions_bathroom:
    jump mouth_emotions

label mouth_emotions:
    $ form = "emotions"
    call set_place("bathroom")    
    menu:
        "A place."
        
        "toilet":
            "determination"
            "relief and satisfaction"
            "pure abject horror"
            jump mouth_emotions
            
        "gameboy" if seegameboy:
            "grim focus. delight."
            "achievement and fantasy"
            "distraction from fear"
            jump mouth_emotions
            
        "counter":
            "pride and vanity"
            "meticulous precession"
            "contented delight"
            jump mouth_emotions
            
        "bathtub":
            "sensations rain down"
            "dripping wet relaxation"
            "an object of joy"
            jump mouth_emotions
            
        "ducky" if seeduckey:
            "an object of joy"
            "overwhelming sensations"
            "warm and distracting"
            jump mouth_emotions

        "change":
            jump form_change_mouth_bathroom

    return

label brain_emotions_livingroom:
    jump brain_emotions

label brain_emotions:
    $ form = "emotions"
    call set_place("livingroom")    
    menu:
        "A place."
        
        "couch":
            "delightful tender"
            "remnant negativity"
            "dissolving away"
            jump brain_emotions
            
        "coffee table":
            "sphere of enmity"
            "irritated misery"
            "along perimeter"
            jump brain_emotions
            
        "tv":
            "onslaught of content"
            "waves of pleasure, terror, joy"
            "sensing the unknown"
            jump brain_emotions

        "change":
            jump form_change_brain_livingroom
            
    return

label emotions_emotions:
    $ form = "emotions"
    call set_place("bedroom")    
    menu:
        "A place."
        
        "bed":
            "serenity, joy"
            "amazement, hostility"
            "and discovery"
            jump emotions_emotions
            
        "toys":
            "excitement, fondness"
            "allegiance, adoration"
            "appreciation"
            jump emotions_emotions
            
        "lava lamp":
            "comfort, enchantment"
            "always a hint of surprise"
            "novel knowledge"
            jump emotions_emotions
            
        "child" if closetOpen:
            "muted and layered"
            "apprehensive interest"
            "curiosity"
            jump emotions_emotions
            
        "approach" if closetOpen and outOfTheCloset and selectedToy:
            "combined joy and trust"
            "excited relaxation"
            "trail of the unknown"
            "..."
            "muted and layered"
            "apprehensive interest"
            "curiosity"
            "..."
            "disgusted surprise"
            "aggression and submission"
            "cloaked over sadness"
            "..."
            "current levels are:"
            "unknown (low), acquiescence"
            "(high and rising)"
            "..."
            "willing to engage"
            "eradicates loneliness"
            "many now are one"
            "..."
            "....."
            jump end_gas

        "change":
            jump form_change_emotions_bedroom

    return

label end_emotions:
    $ form = "emotions"
    "PLaceholder"

    return
