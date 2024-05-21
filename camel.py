def camelcase(text):
    result = ''
    for char in text:
        if char.isupper():
            result += '_' + char.lower()
        else:
            result += char.lower()
    return result

string = input("camelCase: ")
converted = camelcase(string)
print("snake_case: ", converted)
