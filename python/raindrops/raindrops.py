def convert(num):
    res = ""
    if num % 3 == 0:
        res += "Pling"

    if num % 5 == 0:
        res += "Plang"

    if num % 7 == 0:
        res += "Plong"
 
    return res if res else str(num)
