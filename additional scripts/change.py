import binascii
# script changes hex to binary and puts them into "binary.txt"
t = open("counted.txt", "r")
i = 0
t2 = open("binary.txt", "w")
for line in t:

    if i % 2 == 0:
        trail = line.replace('\n', '')
        trail = trail.replace(' ', '')
        binary = bin(int(trail, 16))
        t2.write(binary + '\n')
        #print binary
    i += 1
t2.close()

t2 = open('binary.txt', 'r')
i = 0
tobecounted = list()
counter = list()
for line in t2:
    if line in counter:

        tobecounted.append(line)
    else:
        counter.append(line)
        tobecounted.append(line)

t.close()
t2.close()
