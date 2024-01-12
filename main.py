from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(direction, text, shift):
  if direction == "decode" or direction == "encode":
    letter = []
    word = []
    if direction == "decode":
      shift *= -1
      
    for i in text:
      letter.append(i)
    for l in letter:
      if l in alphabet:
        if alphabet.index(l)+shift <= 25:
          word.append(alphabet[alphabet.index(l)+shift])
        else:
          word.append(alphabet[alphabet.index(l)+shift-26])
      else:
        word.append(l)  
    encoded_word = "".join(word)
    print(f"The {direction}d text is: {encoded_word}\n")
  else:
    print("I didn't understand the comand. Please, try again!\n")


loop = True
while loop == True:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))%26
  
  ceaser(direction, text, shift)
  
  repeat = input("Type 'yes if you want to go again. Otherwise type 'no'.").lower()
  if repeat == 'yes':
    loop = True
  else:
    loop = False
