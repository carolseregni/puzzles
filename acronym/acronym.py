def abbreviate(words):
    letters = ""
    words = words.split()
    for word in words:
        letters = letters + word[0]
    output =""+(letters).upper()
    return(output)

print(abbreviate("Ciao bella"))






