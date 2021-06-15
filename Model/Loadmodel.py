import pandas as pd
import pickle
class Load_model():
	def Load_StackModel(self):
		df = pd.read_csv("Backend/essay.csv")
		StackModel = pickle.load(open('Model/Stack_model.sav', 'rb'))
		
		return(StackModel.predict(df.iloc[0,:].values.reshape(1,-1)))

# a = Load_model()
# print(a.Load_StackModel())