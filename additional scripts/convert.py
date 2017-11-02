import binascii
import md5
m = md5.new()
t = open("binary.txt", "r")
t2 = open("test.3.txt", "w")

for line in t:
    print "ascii"
    print binascii.b2a_uu(line)
    print "crc vergleich"
    print line
    print binascii.crc32("com.ebay.kleinanzeigen")
    print "md5 maybe?"
    print line
    print m.update("com.ebay.kleinanzeigen")
    t2.write( str(m.digest()))
    break
