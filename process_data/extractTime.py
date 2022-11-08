from datetime import datetime
import sys

fname = sys.argv[1]
file1 = open("%s.txt" % fname, "r")
file2 = open('%s_machineTime.csv' % fname, 'w')
#file3 = open('moto_file_list_realTime.csv', 'w')
lines = file1.readlines()
for line in lines:
    machineDate = int(line[6:19])/1000
    file2.write(line[6:19]+'\n')
    date = datetime.utcfromtimestamp(machineDate)
    str = date.strftime('%Y-%m-%d %H:%M:%S'+'\n')
    #file3.write(str)
