def convert(faces):
    faces = faces.replace(":)","🙂")
    faces = faces.replace(":(","🙁")
    print(faces)

text = input("Input text... ")
convert(text)
