import language_tool_python
import os
tool = language_tool_python.LanguageTool('en-US')
 
f = open("essay.txt", "r")
text = f.read()
 
# get the matches
matches = tool.check(text)
print("No. of grammatical mistake:",len(matches),end="\n\n")
print("------------------------------------------")
translation_table = dict.fromkeys(map(ord, '^'), None)

printable = 0
for i in matches:
    i = str(i)

    #Get offset+length
    offset = i.split(',')[0]
    length = i.split(',')[1]

    length = int(length.replace("length ",""))
    offset = int(offset.replace("Offset ",""))
    
    #Get range to print
    previousprint = printable
    printable = length + offset

    print(text[previousprint:printable],end="")

    tillfullstop = text[printable:].split('.')[0] + "."
    printable += len(tillfullstop)

    print(tillfullstop,end="\n\n")
    #Remove ^
    i = i.translate(translation_table)

    #split each line to list and remove last element. Then print.
    i = i.splitlines(True)[:-1]
    for j in i:
        print(j,end="")
    print("------------------------------------------")