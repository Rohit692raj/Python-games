def Flames(name1,name2):
    n1 = list(name1)
    n2 = list(name2)
    i = j = 0
    while i < len(n1):
        while j < len(n2):
            if n1[i] == n2[j]:
                n1.pop(i)
                n2.pop(j)
                break
            else:
                j += 1
        j = 0
        i += 1
    x = len(n1) + len(n2)
    meaning = {
        "F" : "Friend",
        "L": "Lover",
        "A": "Affection",
        "M": "Marriage",
        "E": "Enemy",
        "S": "Sister",
    }
    cut = ["F","L","A","M","E","S"]
    while len(cut) != 1:
        num = (x % len(cut)) - 1
        cut.pop(num)
    return meaning[cut[0]]
name1 = str(input("Enter your name: ")).upper()
name2 = str(input("Enter crush name: ")).upper()
print(f'She is your {Flames(name1,name2)}')