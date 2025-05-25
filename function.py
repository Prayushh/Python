def emoji_converter(message):
    output=""
    words=message.split(" ")
    emoji_dict={
        ":)":"😊",
        ":(":"😢"
    }
    for word in words:
        output+= emoji_dict.get(word, word)+ " "
    return output


message=input("Enter some text: ")
print(emoji_converter(message))


