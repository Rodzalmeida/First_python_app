name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    if len(words) < 1:
        continue
    if words[0] != 'From':
        continue
    emails = list()
    emails.append(words[1])
    for recebidos in emails:
        counts[recebidos] = counts.get(recebidos,0)+1
bigcount = None
bigword = None
for x,y in counts.items():
    if bigcount is None or y > bigcount:
        bigword = x
        bigcount = y
print(bigword,bigcount)
