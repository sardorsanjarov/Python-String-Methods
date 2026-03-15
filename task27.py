text = input('text: ')
if text.endswith(".pdf") or text.endswith(".docx") or text.endswith(".txt"):
    print(True)
else:
    print(False)