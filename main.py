import pandas as pd
import os

if 'CURRENCY' not in os.environ:
    raise Exception("Final Currency Not given")
opCurrency = os.environ['CURRENCY']

inputCSV = pd.read_csv("./input/input.csv")
forexCSV = pd.read_csv("./input/forex.csv")

print(inputCSV)
print(forexCSV)
data = pd.merge(inputCSV,forexCSV,on='Currency',how="left")

# FIXME: use a proper way of setting this
import warnings
warnings.filterwarnings('ignore')
data[data['Currency'] == 'INR']['Currency'] = 1
data['Spending'] = data['Cost']
translation = 1
if opCurrency != 'INR':
 translation = forexCSV[forexCSV['Currency'] == opCurrency].iloc[0]['Value']
op = data[["Date","Spending"]].groupby(by='Date',as_index=False).sum()
op.iloc[:,1] /= translation
open("./output/output.csv","w")