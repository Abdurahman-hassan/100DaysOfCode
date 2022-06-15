alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(inputTextFromUser, shift_index):
    # var = []
    var2 = " "
    for i in range(len(inputTextFromUser)):
        index = alphabet.index(inputTextFromUser[i]) + shift_index
        if index >= len(alphabet):
            new_index = index - len(alphabet)  # 30 - 26  = 4 -> 0,1,2,3
            var2 += alphabet[new_index]
        else:
            # var.append(alphabet[index])
            var2 += alphabet[index]
    print(f"The encoded text is {var2}")


def decrypt(decrept_text, shift_back):
    var = ""
    for letter in decrept_text:
        index_back = alphabet.index(letter) - shift_back
        var += alphabet[index_back]

    print(f"The encoded text is {var}")

if direction == "encode":
    encrypt(inputTextFromUser=text, shift_index=shift)
elif direction == "decode":
    decrypt(decrept_text=text, shift_back=shift)
