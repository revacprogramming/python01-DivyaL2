
filename = "mbox-short.txt"
fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        t=line.find('0')
        num=float(line[t:])
        count =count+1
        total=total+num
Average=total/count
print('Average spam confidence:',Average)
    


