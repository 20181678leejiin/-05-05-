from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return "Error!"

    if n >= 4000:
        return "Error!"

    romans = [(1000, 'M'),(900,'CM'),(500,'D'),(400,'CD'),
              (100, 'C'),(90,'XC'),(50, 'L'),(40, 'XL'),
              (10, 'X'),(9, 'IX'),(5, 'V'),(4, 'IV'),
              (1, 'I'),
              ]

    result = ''
    for value, letters in romans: # 보기에 훨씬 좋음! & 사전을 연속시키면 순서가 정해지지 않아서 계산 순서 고려 ㄴㄴ!
        while n >= value:
            result += letters
            n -= value
    return str(result)

def romanToDec(numStr):
    try:
        n = numStr
    except:
        return "Error!"

    romans = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),
              (100,'C'),(90,'XC'),(50,'L'),(40,'XL'),
              (10,'X'),(9,'IX'),(5,'V'),(4,'IV'),
              (1,'I'),
    ]

    result = 0

    for j in range(len(romans)):
        while(n.find(romans[j][1]) == 0):
            result += romans[j][0]
            n = n[len(romans[j][1]):]

    return str(result)