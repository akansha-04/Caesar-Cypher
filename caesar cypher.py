import caesarart
print(caesarart.logo) 
import sys
alphabet = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_end=True
while  should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    def caesar(plain_text,shift_no,caesar_dir):
        shift_no=shift_no%26
        caesar=[]
        if caesar_dir=='encode':
            shift_no=shift_no*1
        elif caesar_dir=='decode':
            shift_no=shift_no*(-1)
        else:
            print('Type the correct function')
            sys.exit()
        plain_text=list(plain_text)
        for i in plain_text:
            if i in alphabet:
               early_index=alphabet.index(i)
               new_alphabet=alphabet[early_index+shift_no]
               caesar.append(new_alphabet)
            else:
                caesar.append(i)
        caesar=''.join(caesar)
        print(caesar)
        start_again=input('Do you want to start again: yes or no?').lower()
        if start_again=='no':
            sys.exit('End of the code')
    caesar(plain_text=text,shift_no=shift,caesar_dir=direction)
