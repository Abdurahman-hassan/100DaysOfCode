from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(inputTextFromUser, shift_index, dir):
    var = " "
    if dir == "decode":
        shift_index *= -1
    for i in range(len(inputTextFromUser)):
        if inputTextFromUser[i] in alphabet:
            index = alphabet.index(inputTextFromUser[i])
            new_postion = index + shift_index
            if new_postion >= len(alphabet) and dir == "encode":
                new_index = new_postion - len(alphabet)  # 30 - 26  = 4 -> 0,1,2,3
                var += alphabet[new_index]
            else:
                var += alphabet[new_postion]
        else:
            var += inputTextFromUser[i]
    print(f"The encoded text is {var}")


print(logo)

isRepeted = True

while isRepeted:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26
    caesar(inputTextFromUser=text, shift_index=shift, dir=direction)

    repeted_input_messege = input("Type 'yes' if you want to continue or no to stop").islower()

    if repeted_input_messege == "no":
        isRepeted = False
    else:
         print("Please Type \'yes\' if you want to continue or 'no' to stop")
