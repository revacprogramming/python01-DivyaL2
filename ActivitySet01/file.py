r="ActivitySet01/File.txt"
a=open(r,"r")

print(a)
count=0

for line in a:
  if line.startswith("X-Content"):
    print(line)
    count=count+1
print(count)    
  