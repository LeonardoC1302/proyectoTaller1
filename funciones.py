def codificarCifradoCesar(pmensaje):
    traduccion = ""
    for i in pmensaje:
        if i.isalpha():
            num = ord(i.lower())
            num+=3
            if num > ord('z'):
                num -= 26
            elif num < ord('a'):
                num += 26
            traduccion+=chr(num)
        else:
            traduccion+=i
    print(traduccion)

def decodificarCifradoCesar(pmensaje):
    traduccion = ""
    for i in pmensaje:
        if i.isalpha():
            num = ord(i.lower())
            num-=3
            if num > ord('z'):
                num -= 26
            elif num < ord('a'):
                num += 26
            traduccion+=chr(num)
        else:
            traduccion+=i
    print(traduccion)

