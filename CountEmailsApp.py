# First lets define the name of the file with the words we want to count

name = input("Enter file:")
if len(name) < 1:
    name = "Sample_Text.txt"
handle = open(name)

# Now we can start striping the text from the file to select only the emails sent using the word "From"

counts = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    if len(words) < 1:
        continue
    if words[0] != 'From':
        continue

# At this point we can create a list of all the emails and keep track of how many times they appear in the text

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

# Done! You should now see the email and the amount of times it appeared in the text
