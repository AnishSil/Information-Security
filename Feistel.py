from random import randint

global count
global n_rounds
global key
global block_size
block_size = 8

# Feistel Round Structure 
def feistel(plain: list , n: int, key: str) -> list:
    global count
    count -= 1
    left = plain[:n//2]
    right = plain[n//2:]
    func = [right[x]^key[count][x] for x in range(n//2)]
    fright = [left[x]^func[x] for x in range(n//2)]
    if count == 0:
        return fright + right
    else:
        return feistel(right+fright,n,key) 

# Key Generation
def gen_keys(key_size: int, rounds: int) -> list:
    keys = []
    for i in range(rounds):
        keys.append([randint(0,1) for _ in range(key_size)])
    return keys

# Converts a charcter into a list of size 8
def plaintext(character: str) -> list:
    num = ord(character)
    arr = []
    for i in range(7,-1,-1):
        ref = 2**i
        if num>=ref:
            arr.append(1)
            num -= ref
        else:
            arr.append(0)
    return arr

# Converts a list of size 8 into a character
def cipher(cipher: list) -> str:
    num = 0
    for i in range(len(cipher)):
        num += (2**i)*cipher[7-i]
    return chr(num)

# Complete Encryption Block
def encode(plain: str):
    global key 
    global count
    global n_rounds
    m = ""
    for i in plain:
        cip = feistel(plaintext(i), block_size, key)
        count = n_rounds
        m += cipher(cip)
    return m

# Complete Decryption Block
def decode(plain: str):
    global key 
    global count
    global n_rounds
    key.reverse()
    m = ""
    for i in plain:
        cip = feistel(plaintext(i), block_size, key)
        count = n_rounds
        m += cipher(cip)
    key.reverse()
    return m



# Main Function
if __name__ =="__main__": 
    n_rounds = int(input("number of rounds: "))
    message = input("Enter your Message: ")

    count = n_rounds
    key = gen_keys(4,count)

    cipher_text = encode(message)
    plain_text = decode(cipher_text)

    for i in cipher_text:
        print(i, end = "")
    print("")
    print(plain_text)