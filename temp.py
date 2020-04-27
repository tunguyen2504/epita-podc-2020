pa1 = ['sea', 'blue', 'sky', 'water']
pa2 = ['python', 'blue', 'sky']

# Just an example
def compare_paintings(pa1, pa2):
    len1 = len(pa1)
    len2 = len(pa2)
    intOfList = list(set(pa1) & set(pa2))
    len3 = len(intOfList)

    tmpList.append(len1)
    tmpList.append(len2)
    tmpList.append(len3)
    tmpList.sort()
    return min(tmpList)

compare_paintings(pa1, pa2)
