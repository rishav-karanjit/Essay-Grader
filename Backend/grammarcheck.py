import language_tool_python
import os
import pandas as pd

class gcheck():
    def Check_Grammer(self):
        tool = language_tool_python.LanguageTool('en-US')
         
        f = open("Backend/essay.txt", "r")
        fw = open("Backend/grammer_mistake.txt","w")
        text = f.read()
         
        # get the matches
        matches = tool.check(text)
       	fw.write("No. of grammatical mistake:"+str(len(matches))+"\n\n"+"________________________________________________________\n")

        printable = 0
        a = 0
        for i in matches:
        	a = a + 1
        	ruleId = i.ruleId
        	message = i.message
        	replacements = i.replacements
        	context = i.context
        	str1 = " "
        	write = "Grammer Mistake "+str(a)+".\n"+"RuleId:"+ruleId+"\nmessage:"+message+"\ncontext:"+context
        	if replacements:
        		write = write + "\nSuggestion:"+str1.join(replacements)+"\n"
        	fw.write(write + "\n________________________________________________________\n")
        # f.close()
        fw.close()