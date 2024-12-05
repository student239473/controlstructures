plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    if char.isalpha(): 
      
        if char.islower():
            new_char = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
        elif char.isupper():
            new_char = chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
    else:
       
        new_char = char

    
    encrypted_text += new_char

print(f'Original text: {plain_text}')
print(f'Encrypted text: {encrypted_text}')