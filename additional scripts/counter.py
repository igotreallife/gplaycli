''' simple script to count the different hex strings before a package name '''

t = open("before.txt", "r")
i = 0
summe = 0
# one list as all of them the other only once
tobecounted = list()
counter = list()
for line in t:
    if line in counter:

        tobecounted.append(line)
    else:
        counter.append(line)
        tobecounted.append(line)
t2 = open("counted.txt", "w")
for elemt in counter:
    t2.write(str(elemt + ': ' + str(tobecounted.count(elemt)) + '\n'))
    summe += tobecounted.count(elemt)
# "summe" should equal the number of lines in the given .txt document
print summe
t.close()
