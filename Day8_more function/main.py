alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def ceaser(original_text,shift_amount,encode_or_decode) :
    if encode_or_decode == "decode" :
        shift_amount += -1

    changed_text = ""

    for i in original_text :
        text_index = alphabet.index(i)
        text_index += shift_amount
        text_index = text_index % len(alphabet)
        changed_text += alphabet[text_index]
    print(changed_text)\

should_continue = True

while should_continue :
    ceaser(original_text = input("Type your message:\n").lower(), shift_amount =int(input("Type the shift number:\n")), encode_or_decode=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower() )

    restart = input("Will you restart? yes or no\n").lower()

    if restart == "no" :
        print("Good Bye")
        should_continue = False
