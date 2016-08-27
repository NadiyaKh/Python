x=int(input("enter count:"))
def encode(s, x):
    """Encodes a string (s) using ROT (ROT_number) encoding."""
    ROT_number %= x  # To avoid IndexErrors
    alpha = "abcdefghijklmnopqrstuvwxyz" * 2
    alpha += alpha.upper()
    def get_i():
        for i in range(x):
            yield i  # indexes of the lowercase letters
        for i in range(53, 78):
            yield i  # indexes of the uppercase letters
    ROT = {alpha[i]: alpha[i + ROT_number] for i in get_i()}
    return "".join(ROT.get(i, i) for i in s)


def decode(s, x):
    """Decodes a string (s) using ROT (ROT_number) encoding."""
    return encrypt(s, abs(ROT_number % x - x))




    #####################################
    from string import ascii_lowercase 
    a = ascii_lowercase
    x=4
    b = a[-x:] + a[:-x]
    d=dict(zip(a,b))

    s="testeee"

    encoded = ""

    for letter in s:
    	if letter in d:
    	encoded+=d[letter]
    	else encoded+=letter
    print (encoded)


####

    for letter in s:
    	encoded+=d.get(letter, letter)
    print (encoded)

