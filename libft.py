def mylen(string):
    count = 0
    for i in string:
        count += 1
    return count
string = ""
mylen(string)

def ft_bzero():
    text = "VALERABAKLAJAN"
    i = 0
    zam = ''
    while i < mylen(text):
        if i < 4:
            zam += str(0)
        else:
            zam += text[i]
        i +=1
    print(zam)
ft_bzero()


def ft_strlen():
    text = "VALERABAK\0LAJAN"
    j = 0
    zam = ""
    while j < mylen(text):
        if text[j] != '\0':
            zam += text[j]
        else:
            break
        j += 1
    print (mylen(zam))
ft_strlen()

def ft_strcat():
    text_one = "VALERA"
    text_two = "BAKLAJAN"
    zam = text_one + text_two
    print (zam)
ft_strcat()


def ft_strcmp():
    a = "VALERA"
    b = "VALRA"
    if a == b:
        print(1)
        return 1

    else:
        print(0)
        return 0

ft_strcmp()


def ft_atoi():
    string = "a"
    a = ord(string)
    print(a)
ft_atoi()

def ft_isdigit():
    text = 10
    if text >= 0 and text <= 9:
        print (1)
        return 1
    else:
        print(0)
        return 0
ft_isdigit()

def ft_isalpha():
    a = "A"
    b = ord(a)
    print (b)
    if (b >= 60 and b <= 90) or (b >= 97 and b <= 122) :
        print (1)
    else:
        print (0)
ft_isalpha()

def ft_isalnum():
    a = "9"
    b = ord(a)
    print (b)
    if (b >= 48 and b <= 57) or (b >= 60 and b < 90) or (b >= 97 and b <= 122) :
        print (1)
    else:
        print (0)
ft_isalnum()


def ft_toupper():
    string = "VALEraBaKlaJan"
    string1 = ''
    for i in string:
        if (i >= 'a' and i <= 'z'):
            string1 = string1 + chr((ord(i) - 32))
        else:
            string1 = string1 + i
    print(string1)
ft_toupper()

def ft_tolower():
    string = "VALEraBaKlaJan"
    string1 = ''
    for i in string:
        if (i >= 'A' and i <= 'Z'):
            string1 = string1 + chr((ord(i) + 32))
        else:
            string1 = string1 + i
    print(string1)
ft_tolower()

def ft_isprint():
    a = "9"
    b = ord(a)
    if b >= 32 and b <= 125:
        print (1)
        return 1
    else:
        print (0)
        return 0
ft_isprint()

def ft_isascii():
    a = "f"
    b = ord(a)
    if b >= 0 and b <= 127:
        print (1)
        return 1
    else:
        print (0)
        return 0
ft_isascii()