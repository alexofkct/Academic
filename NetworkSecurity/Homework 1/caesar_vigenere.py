UID=120395246
Last_Name="Bharathiraja"
First_Name="Rithik Sarvesh"
def formatter(text):
    formatted_text=text.upper().replace(" ","")
    return formatted_text
def caesar_str_enc(text,shift):
    text=formatter(text)
    cipher=[]
    for i in text:
        position=ord(i)
        if(position>64 and position<91):
            position+=shift
            if(position>90):
                position-=26
        cipher.append(chr(position))
    return ''.join(cipher)
def caesar_str_dec(cipher,shift):
    text=[]
    for i in cipher:
        position=ord(i)
        if(position>64 and position<91):
            position-=shift
            if(position<65):
                position+=26
        text.append(chr(position))
    return ''.join(text)
def vigenere_enc(key,text):
    text=formatter(text)
    key=formatter(key)
    cipher=[]
    len_text=len(text)
    len_key=len(key)
    key=((len_text//len_key)*key)+key.join(key[:len_text%len_key])
    for i in range(0,len_text):
        t_position=ord(text[i])
        k_position=ord(key[i])
        if(t_position>64 and t_position<91):
            t_position+=k_position
            t_position-=65
            if(t_position>90):
                t_position-=26
        cipher.append(chr(t_position))
    return ''.join(cipher)
def vigenere_dec(key,cipher):
    cipher=formatter(cipher)
    key=formatter(key)
    text=[]
    len_c=len(cipher)
    len_k=len(key)
    key=((len_c//len_k)*key)+key.join(key[:len_c%len_k])
    for i in range(0,len_c):
        c_position=ord(cipher[i])
        k_position=ord(key[i])
        if(c_position>64 and c_position<91):
            c_position-=k_position
            c_position+=65
            if(c_position<65):
                c_position+=26
        text.append(chr(c_position))
    return ''.join(text)

#print(caesar_str_dec((caesar_str_enc("Hello World!",2)),2))
#print(vigenere_dec("Hello",(vigenere_enc("Hello","This is a sample sentence"))))
def main():
    while(True):
        print("\n\nEnter the number of the operation you like to perform\n")
        print("1.Caesar's cipher encryption\n2.Caesar's cipher decryption\n3.Vigenere cipher encryption\n4.Vigenere cipher decryption\n5.Exit")
        operation=int(input())
        if(operation>4):
            break
        print("\n\nEnter the plain text/cipher you like to work upon")
        inputt=input()
        match operation:
            case 1:
                shift=int(input("Enter the shift number\n"))
                print(caesar_str_enc(inputt,shift))
            case 2:
                shift=int(input("Enter the shift number\n"))
                print(caesar_str_dec(inputt,shift))
            case 3:
                key=input("Enter the key........(Trust me, I keep it safe)\n")
                print(vigenere_enc(key,inputt))
            case 4:
                key=input("Enter the key........(Trust me, I keep it safe)\n")
                print(vigenere_dec(key,inputt))

if __name__ == "__main__":
    main()