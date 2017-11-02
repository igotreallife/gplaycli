import csv
import base64
import shutil
import binascii
import subprocess
from subprocess import Popen, PIPE
import os
from tempfile import NamedTemporaryFile



class decoder(object):
    control = 0
    def work_csv(self):

        csvfile = 'clps.csv'
        #tempfile = NamedTemporaryFile(delete=False)
        with open(csvfile, 'rb') as csvfile:

            codereader = csv.reader(csvfile, delimiter=' ', quotechar='|')

            # string before the package name
            t = open("before.txt", "w")
            # string after the package name
            t2 = open("after.txt", "w")
            # simple dump of all to control just in case
            t3 = open("control.txt", "w")
            # string after the ":S:"
            t4 = open("after_s.txt", "w")
            for row in codereader:

                helper = row[0].split('\t')[1].split(':')[0]
                after_s = row[0].split('\t')[1].split(':')[2]
                t4.write( after_s + '\n')
                #break
                self.decode_to_hex(helper,t,t2,t3)

                #print self.control
            t.close()
            t2.close()
            t3.close()
            t4.close()


    def decode_to_hex(self, base_String,t,t2,t3):

        self.control += 1
        
        # occasionally there is a "-" in the coding i found out that if i
        # replace it by "=" that there is an outcome source ->
        # https://toolbox.googleapps.com/apps/encode_decode/
        # same goes for "_"
        #bash sript as subprocess
        decoded = base_String.replace('-','=').replace('_','=')
        before = decoded[:16]
        decoded_len = len(decoded) - 8
        after = decoded[decoded_len:]
        # controll-group
        p = subprocess.Popen(['bash'], stdin=PIPE, stdout=PIPE)
        p.stdin.write('echo \"' + str(decoded) + '\" | base64 -d | xxd')
        stdout,stderr = p.communicate()
        t3.write(str(stdout))

        # write first 8 hex-digits
        p = subprocess.Popen(['bash'], stdin=PIPE, stdout=PIPE)
        p.stdin.write('echo \"' + str(before) + '\" | base64 -d | xxd')
        stdout,stderr = p.communicate()
        # make it pretty
        trim_it = str(stdout).split(' ')[1:4]
        t.write(str(trim_it[0]) + ' ' + str(trim_it[1]) + ' ' + str(trim_it[2])[:2] + '\n')

        # write last 8 hex-digits
        # if the package name is too long or not long enough
        # there gonna be blanks in the end
        if after.find("==") != -1:
            p = subprocess.Popen(['bash'], stdin=PIPE, stdout=PIPE)
            p.stdin.write('echo \"' + str(after) + '\" | base64 -d | xxd')
            stdout,stderr = p.communicate()
            trim_it2 = str(stdout).split(' ')[1:3]
            t2.write(str(trim_it2[0] + ' ' + trim_it2[1] + '\n' ))


        # so we cut off the first part since its the ending of the package name
        # which we already know
        elif after.find("=") != -1:
            p = subprocess.Popen(['bash'], stdin=PIPE, stdout=PIPE)
            p.stdin.write('echo \"' + str(after) + '\" | base64 -d | xxd')
            stdout,stderr = p.communicate()
            trim_it2 = str(stdout).split(' ')[1:4]
            t2.write(str(trim_it2[0])[2:] + ' ' + str(trim_it2[1]) + ' ' + str(trim_it2[2]) + '\n' )

        else:
            p = subprocess.Popen(['bash'], stdin=PIPE, stdout=PIPE)
            p.stdin.write('echo \"' + str(after) + '\" | base64 -d | xxd')
            stdout,stderr = p.communicate()
            trim_it2 = str(stdout).split(' ')[1:4]
            t2.write(str(trim_it2[1] + ' ' + trim_it2[2] + '\n' ))

        return 0

def main():

    dec = decoder()
    dec.work_csv()


if __name__ == '__main__':

    main()
