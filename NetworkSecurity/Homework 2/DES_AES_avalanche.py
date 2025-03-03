from Crypto.Cipher import DES,AES

UID=120395246
Last_Name="Bharathiraja"
First_Name="Rithik Sarvesh"

def des_magic(text,key):
    function=DES.new(key, DES.MODE_ECB)
    return function.encrypt(text)

def aes_magic(text,key):
    function=AES.new(key, AES.MODE_ECB)
    return function.encrypt(text)

def bit_converter(text):
    array=[]
    for i in text:
        array.append(bin(int(i))[2:].zfill(8))
    array=''.join(array)
    array=list(array)
    return array

def father_of_comparison(cipher_a,cipher_b):
    array_a=bit_converter(cipher_a)
    array_b=bit_converter(cipher_b)
    size=len(array_a)
    result=size
    for i in range(0,size):
        if(array_a[i]==array_b[i]):
            result-=1
    return result

def master_of_flipper(av_text,position):
    result=''
    array2=[]
    array=bit_converter(av_text)
    helper={'0':'1','1':'0'}
    array[position]=helper[array[position]]
    array=''.join(array)
    for i in range(0,len(array)//8):
            array2.append(array[i*8:(i*8)+8])
    array2=''.join(array2)
    result=int(array2, 2).to_bytes(len(array2) // 8, byteorder='big')
    return result

def des_input_av_test(text,key,position_list):
    result=[]
    actual_cipher=des_magic(text,key)
    for position in position_list:
        altered_text=master_of_flipper(text,position)
        new_cipher=des_magic(altered_text,key)
        result.append(father_of_comparison(actual_cipher,new_cipher))
    return result

def des_key_av_test(text,key,position_list):
    result=[]
    actual_cipher=des_magic(text,key)
    for position in position_list:
        altered_key=master_of_flipper(key,position)
        new_cipher=des_magic(text,altered_key)
        result.append(father_of_comparison(actual_cipher,new_cipher))
    return result    
        
def aes_input_av_test(text,key,position_list):
    result=[]
    actual_cipher=aes_magic(text,key)
    for position in position_list:
        altered_text=master_of_flipper(text,position)
        new_cipher=aes_magic(altered_text,key)
        result.append(father_of_comparison(actual_cipher,new_cipher))
    return result
        
def aes_key_av_test(text,key,position_list):
    result=[]
    actual_cipher=aes_magic(text,key)
    for position in position_list:
        altered_key=master_of_flipper(key,position)
        new_cipher=aes_magic(text,altered_key)
        result.append(father_of_comparison(actual_cipher,new_cipher))
    return result

def main():
    #print(des_input_av_test(b'thisoneis16bytes',b'deskey!!',[3, 25, 36]))
    #print(des_key_av_test(b'thisoneis16bytes',b'deskey!!',[3, 25, 36]))
    print(aes_input_av_test(b'\x01\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x10',b'\x0f\x15\x71\xc9\x47\xd9\xe8\x59\x0c\xb7\xad\xd6\xaf\x7f\x67\x98',[7]))
    #print(aes_key_av_test(b'thisoneis16bytes',b'veryverylongkey!',[5, 29, 38]))

if __name__ == "__main__":
    main()



