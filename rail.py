import math

#for encrypt

def encRail(msg, key):
    msg = msg.replace(" ","")
    num_rows = key
    num_cols = math.ceil(len(msg)/num_rows)
    arr = [[' ' for j in range(num_cols)] for i in range(num_rows)]
    k = 0

    for j in range(num_cols):
        for i in range(num_rows):
            if k<len(msg):
                arr[i][j] = msg[k]
                k += 1

            else:
                break

    cphrtxt = ""
    for i in range(num_rows):
        for j in range(num_cols):
            cphrtxt += arr[i][j]

    return cphrtxt

#for decrypt

def decRail(cphrtxt, key):
    cphrtxt = cphrtxt.replace(" ","")
    num_rows = key
    num_cols = math.ceil(len(cphrtxt)/num_rows)
    arr = [[' ' for j in range(num_cols)] for i in range(num_rows)]
    k =0

    for i in range(num_rows):
        for j in range(num_cols):
            if k<len(cphrtxt):
                arr[i][j] = cphrtxt[k]
                k += 1

            else:
                break

    msg = ""
    k = 0

    for j in range(num_cols):
        for i in range(num_rows):
            if k<len(cphrtxt):
                if arr[i][j] != ' ':
                    msg += arr[i][j]
                    k += 1

            else:
                break

    return msg

#main code

msg = input("Enter the message to encrypt :")
key = int(input("Enter the key :"))

cphrtxt = encRail(msg,key)
print("Encrypted message :", cphrtxt)

decrypted = decRail(cphrtxt, key)
print("Decrypted message :", decrypted)