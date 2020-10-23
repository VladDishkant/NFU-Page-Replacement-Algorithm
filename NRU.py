#NRU page replacement algorithm implementation in python
#Created By: Vladyslav Dyshkant

print("Введіть кількість сторінок: ",end="")
capacity = int(input()) # enter the number of memory pages
bitsR = dict.fromkeys(range(capacity), '')

for i in range(5): # loop for entering bits for pages 0-n, for a counter of 5 cycles
    goToNext = 1
    while(goToNext): # input bits according to the following pattern: %d %d %d %d %d,
        # (where% d is a number in the range of total pages)
        goToNext = 0
        print("Ввести біти для {0} такту: ".format(i), end="")
        s = list(map(int, input().strip().split()))
        if len(s) != capacity:
            goToNext = 1
        for j in s:
            if j < 0 or j > capacity - 1:
                goToNext = 1
    for j in range(len(s)):
        bitsR[j] = str(s[j]) + bitsR[j]

bitsR = list(map(lambda x: '{0}000'.format(x), bitsR.values())) # an array of 8-bit values in the form of a string,
# where each element of the array is the final value of the bits of access to the page in 5 cycles

for elem in [str(i) for i in list(range(8, 0, -1))]:
    if elem == "8":
        print("Bits:    " + elem, end="")
    elif elem == "1":
        print("--" + elem)
    else:
        print("--" + elem, end="")

for i in range(capacity):
    print("Page %d:  " % i, end="")

    if i == 0:
        frequency = int("0b" + bitsR[i], 2)
        page = i
    else:
        if frequency >= int("0b" + bitsR[i], 2): # if the bit value is less than the previous one, the number of
            # the least used page is indicated in the variable 'page'
            page = i
            frequency = int("0b" + bitsR[i], 2)
    print("  ".join(bitsR[i]))

print("NFU: page %d" % page) # output Not Frequently Used page