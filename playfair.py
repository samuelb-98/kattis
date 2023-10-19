import sys

def generate_key(key_text):
    not_used = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z']
    key = []
    for char in key_text:
        if char in not_used:
            key.append(char)
            not_used.remove(char)
    for char in not_used:
        key.append(char)
    return(key)



def encrypt(input_text, key):
    letters = [i for i in input_text]
    output_text = ""
    while len(letters) != 0:
        if len(letters) == 1 or letters[0] == letters[1]:
            letters.insert(1,"x")
        ki1 = key.index(letters[0])
        ki2 = key.index(letters[1])
        if letters[0] == letters[1]:
            output_text += letters.pop(0) + "x"
        elif ki1//5 == ki2//5:
            output_text += key[(ki1+1)%5 + ki1//5 * 5] + key[(ki2+1)%5 + ki2//5 * 5]
            letters = letters[2:]
        elif ki1 % 5 == ki2 % 5:
            output_text += key[(ki1+5)%25] + key[(ki2+5)%25]
            letters = letters[2:]
        else:
            output_text += key[ki1 + ki2%5 - ki1%5] + key[ki2 - ki2%5 + ki1%5]
            letters = letters[2:]
    return(output_text.upper())

input_nr = 1
for line in sys.stdin:
    line = line.strip()
    line = line.replace(" ","")
    if input_nr == 1:
        key_text = line
    else:
        input = line
        break
    input_nr += 1

print(encrypt(input, generate_key(key_text)))