from pyscript import display, document


def intrams_checker(e):
    document.getElementById('output').innerHTML = ' '
    document.getElementById('image').innerHTML = ' '

    registration_el = document.querySelector('input[name="registration"]:checked')
    clearance_el = document.querySelector('input[name="clearance"]:checked')

    if not registration_el or not clearance_el:
        display("Please answer all the questions.", target="output")
        return

    registration = registration_el.value
    clearance = clearance_el.value
    grade_level = int(document.getElementById('level').value)
    section = document.getElementById('section').value

    if registration != 'registered':
        display('Not eligible: student is not registered for Intrams.', target='output')

    elif clearance != 'cleared':
        display('Not eligible: medical clearance required.', target='output')

    elif section == 'emerald':
        display('Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = "<img src='Green.png' width='300'>"

    elif section == 'ruby':
        display('Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = "<img src='Red.png' width='300'>"

    elif section == 'sapphire':
        display('Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = "<img src='Blue.png' width='300'>"

    else:
        display('Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = "<img src='Yellow.png' width='300'>"
