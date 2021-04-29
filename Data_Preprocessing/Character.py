class Characters():
    def Get_No_of_char(self,essay):
        data = essay.replace(" ","")
        number_of_characters = len(data)
        return(str(number_of_characters))