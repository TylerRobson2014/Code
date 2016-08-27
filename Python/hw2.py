from __future__ import division
import random
import numpy as np
import math
import csv
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

df = pd.read_csv('/home/steve/Downloads/results.csv',na_values=['.'])
df['DATE'] = pd.to_datetime(df['DATE'])
#print data.columns
print "data"
d = df.XUDLUSS
print d
print "date"
t = df.DATE
print t

#data.index = data['DATE']
#del data['DATE']
#print data.ix['5-2000']

#data.DATE = data.DATE.apply(lambda d: datetime.strptime(d, "%dd"))
#print data.DATE.head()
df.plot()
#plt.plot(df)
plt.show()
#plt.hist(data["XUDLUSS"])
#plt.show()





		

