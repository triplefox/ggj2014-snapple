label form_change_gas_yard:
    call form_change
    call set_place("yard")
    if form == "gas":
        jump gas_gas_yard
    elif form == "brain":
        jump gas_brain_yard
    elif form == "mouth":
        jump gas_mouth_yard
    elif form == "emotions":
        jump gas_emotions_yard

label form_change_mouth_bathroom:
    call form_change
    call set_place("bathroom")
    if form == "gas":
        jump mouth_gas_bathroom
    elif form == "brain":
        jump mouth_brain_bathroom
    elif form == "mouth":
        jump mouth_mouth_bathroom
    elif form == "emotions":
        jump mouth_emotions_bathroom

label form_change_brain_livingroom:
    call form_change
    call set_place("livingroom")
    if form == "gas":
        jump brain_gas_livingroom
    elif form == "brain":
        jump brain_brain_livingroom
    elif form == "mouth":
        jump brain_mouth_livingroom
    elif form == "emotions":
        jump brain_emotions_livingroom

label form_change_emotions_bedroom:
    call form_change
    call set_place("bedroom")
    if form == "gas":
        jump emotions_gas_bedroom
    elif form == "brain":
        jump emotions_brain_bedroom
    elif form == "mouth":
        jump emotions_mouth_bedroom
    elif form == "emotions":
        jump emotions_emotions_bedroom
