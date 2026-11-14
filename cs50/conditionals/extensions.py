# png, jpg, jpeg, txt, pdf, py, zip,txt, none
def getFileType(filename):
    if filename.endswith(".gif"):
        return "image/gif"
    elif filename.endswith((".jpg", ".jpeg")):
        return "image/jpeg"
    elif filename.endswith(".png"):
        return "image/png"
    elif filename.endswith(".py"):
        return "application/x-python-code"
    elif filename.endswith(".txt"):
        return "text/plain"
    elif filename.endswith(".pdf"):
        return "application/pdf"
    elif filename.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

def main():
    filename = input("File name: ")
    print(getFileType(filename))

main()


