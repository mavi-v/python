text = input("File name: ")
if ".gif" in text:
    print("image/gif")
elif ".jpg" in text:
    print("image/jpeg")
elif ".jpeg" in text:
    print("image/jpeg")
elif ".png" in text:
    print("image/png")
elif (".pdf" in text.lower()):
    print("application/pdf")
elif ".txt" in text:
    print("text/plain")
elif ".zip" in text:
    print("application/zip")
else:
    print("application/octet-stream")
