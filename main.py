from pyscript import display, document 

def intrams_checker(e):
    document.getElementById('output').innerHTML = ' '
    document.getElementById('image').innerHTML = ' '

    registration_el = document.querySelector(
        'input[name="registration"]:checked'
    )
    clearance_el = document.querySelector(
        'input[name="clearance"]:checked'
    )

    if not registration_el or not clearance_el:
        display(
            "❌ Please answer all the questions before proceeding.", 
            target="output"
        )
        return

    registration = registration_el.value
    clearance = clearance_el.value
    grade_level = int(document.getElementById('level').value)
    section = document.getElementById('section').value

    if registration != 'registered':
        display(
            "😞 Not eligible. You are not yet registered for Intramurals.", 
            target='output'
        )

    elif clearance != 'cleared':
        display(
            "😞 Not eligible. Medical clearance is required.", 
            target='output'
        )

    elif section == 'emerald':
        display(
            "🎉 Congratulations!!! 💚\n"
            "Welcome to Green hornets — strength, unity, and sportsmanship!", 
            target='output'
        )
        document.getElementById("image").innerHTML = (
            "<img src='Green.png' width='300'>"
        )

    elif section == 'ruby':
        display(
            "🎉 Congratulations!!! ❤️\n"
            "You are officially part of Red bulldogs — passion and power on the field!", 
            target='output'
        )
        document.getElementById("image").innerHTML = (
            "<img src='Red.png' width='300'>"
        )

    elif section == 'sapphire':
        display(
            "🎉 Congratulations!!! 💙\n"
            "Blue bears it is — calm minds, sharp skills, strong wins!", 
            target='output'
        )
        document.getElementById("image").innerHTML = (
            "<img src='Blue.png' width='300'>"
        )

    else:
        display(
            "🎉 Congratulations!!! 💛\n"
            "Welcome to Yellow tigers — bright energy and unstoppable teamwork!", 
            target='output'
        )
        document.getElementById("image").innerHTML = (
            "<img src='Yellow.png' width='300'>"
        )



