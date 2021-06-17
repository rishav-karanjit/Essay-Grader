import language_tool_python
import os
import pandas as pd

class gcheck():
    def Check_Grammer(self):
        tool = language_tool_python.LanguageTool('en-US')
         
        f = open("backend/essay.txt", "r")
        fw = open("backend/grammer_mistake.txt","w")
        text = f.read()
         
        # get the matches
        matches = tool.check(text)
        fw.write("No. of grammatical mistake:"+str(len(matches))+"\n\n")

        df = pd.read_csv("Backend/essay.csv")
        df.loc[0,"Grammer Mistakes"] = len(matches)
        df.to_csv("Backend/essay.csv",index=False)

        fw.write("------------------------------------------\n")
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

            fw.write(text[previousprint:printable])

            tillfullstop = text[printable:].split('.')[0] + "."
            printable += len(tillfullstop)

            fw.write(tillfullstop+"\n\n")
            #Remove ^
            i = i.translate(translation_table)

            #split each line to list and remove last element. Then print.
            i = i.splitlines(True)[:-1]
            for j in i:
                fw.write(j)
            fw.write("------------------------------------------\n")