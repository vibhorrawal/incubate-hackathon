def graphplot(sheet):  
  import pandas as pd
  import matplotlib.pyplot as plt
  data = pd.read_csv(sheet)
  data1 = data.drop(columns=['Unnamed: 2','Unnamed: 3','Unnamed: 4',	'Unnamed: 5'],axis=1)
  data2 = data1.drop(index=[0])
  data3 = data2.rename(columns={'Unnamed: 0':'Sr Number:','Unnamed: 1':'Captured Date and Time','Unnamed: 6':'Active Energy(kWh) Import',\
                       'Unnamed: 7':'Active Energy(kWh) Export','Unnamed: 8':'Apparent Energy(kVAh)	Import','Unnamed: 9':'Apparent Energy(kVAh)	Export',\
                       'Unnamed: 10':'Average Voltage(V)','Unnamed: 11':'Average Current(A)','Unnamed: 12':'Neutral Current(A)','Unnamed: 13':'Status Byte'})
  data4 = data3.drop(index=[1,2,3])
  data5 = data4
  data5.head()
  data5['Average Current(A)'] = data5['Average Current(A)'].astype('float64')
  data5['Average Voltage(V)'] = data5['Average Voltage(V)'].astype('float64')
  data5['Average Power'] = (data5['Average Current(A)']*data5['Average Voltage(V)']).astype('float64')
  data5[['Captured Date and Time', 'Average Power']].head()
  data6 = data5[['Captured Date and Time', 'Average Power']].iloc[-96:]
  data6.plot.line(x = 'Captured Date and Time', y = 'Average Power',  figsize=(18,9), linewidth=5, fontsize=10)
  plt.show()
  
graphplot('sheet2.csv')