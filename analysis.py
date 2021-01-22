import link_using as lu
import matplotlib.pyplot as plt
plt.stackplot(lu.temp['Date'],lu.temp.iloc[:,1],lu.temp.iloc[:,2],lu.temp.iloc[:,3],lu.temp.iloc[:,4],lu.temp.iloc[:,5])
plt.legend(lu.temp.columns)
plt.show()