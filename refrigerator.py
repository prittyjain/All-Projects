import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

###  Exporting the data set in to python using pandas

df = pd.read_csv(r'C:\Users\HP\Downloads\Refrigerator.csv')
print(df)

###  UNDERSTANDING THE DATA  ###

# To load the first five rows of the data set we use head() function.
head=df.head()
print(head)
"""To get the summary of each and every column present in the data set we use describe() function
PRICE: There are 37 data  points for price. the mean value of price is 626.35, standard deviation is 139.79. The minimum price is 460 and the maximum price is 1200
ECOST: This also have 37 data points with minimum value as 60 and maximum value as 94. The avarage value of spending on operations is 70.5.
RSIZE: 37 data points are there for this also. The average size of a refrigerator is 13.4 sq.ft with a minimum size 12.6 and maximum size 14.7.
SHELVES: The average number of shelves preferred is 2 to 3 with maximum number of shelves is 5 and minimum 1.
FEATURES: The most preferrded number of features is 3-4. The refrigerator having 12 number of feature is the best one."""
summary = df.describe()
print(summary)
# To get the over all idea ie; number of column and number of rows we use shape() function
# Here 37 rows and 8 columns are there.
shap= df.shape
print(shape)
# This will give the column headings ie; the variables we used here
# Here the variables are Price, Ecost, Rsize, fsize, Shelves, S_SQ_FT, features and Brandnam
colum= df. columns
print(colum)
# The nunique() function Will give an idea about the number of unique value inside each colums
# The price have 29 unique value in it. The ecost have 13, rsize have 11,fsize have 10, shelves have 5, S_SQ_FT have 22, features have 9 and brandnam have 16 unique values
uniq= df.nunique()
print(uniq)
# We can mention the variable name inside the unique function and we will get the unique values in that column
# 16 brands are their in the dataset
uniqbrand= df['BRANDNAM'].unique()
print(uniqbrand)
# Sorting the values
# The data is sorted in alphabetic order by  brand name
sorting= df.sort_values("BRANDNAM")
print(sorting)

###   CLEANNING THE DATA   ###

# We use drop() function to eliminate one or more colum from the dataset
# Here we are dropping the column named S_SQ_FT
ref=df.drop(['S_SQ_FT'],axis=1)
print(ref)
# isnull() function is used to identify the presence of null value
# In this data there is no null value.
fridge=ref.isnull().sum()
print(fridge)
"""To check there is any outliers are present or not
# We used box plot to identify the outliers. First we drop the column named BRANDNAM because,that is not in numeric nature.
PRICE: Price have one outlier in the range 1200. Price range is from 460 to 880
ECOST: The operation cost have two outliers. The values of outliers are 90 and 94
RSIZE: It doesn,t have any outliers
FSIZE: This also doesn't have any outliers
SHELVES: This variable contain one outlier. The value is 5. Rest all values in between 1 and 4
FEATURES: This variable contain two outliers"""
boxdata=ref.drop(['BRANDNAM'],axis=1)
collist = list(boxdata.columns)
for i in range (0, len(boxdata.columns)):
    boxdata.boxplot(column=collist[i])
    plt.show()


###  RELATIONSHIP ANALYSIS  ###
"""From the correlation analysis we can understand that the variable FSIZE is more related to PRICE
the corelation value for ECOST is 0.52,RSIZE is -0.02, FSIZE is 0.72, SHELVES is 0.39 and FEATURES is 0.69
 There are some variables having strong relation with price. They are ECOST,FSIZE and FEATURES """
correlation= ref.corr()
print(correlation)

###   REGRESSION ANALYSIS   ###

from sklearn import linear_model
X = boxdata[['ECOST','RSIZE','FSIZE','SHELVES','FEATURES']]
y = df['PRICE']

regr = linear_model.LinearRegression()
regr.fit(X, y)
print(regr.coef_)
"""From the regression we will get to know that most of the people choose their fridge by it's size.
Then they are looking for the number of features available.
 """

###  DATA VISUALIZATION  ###
#Price and Ecost
a= boxdata.iloc[:, 0]
b=boxdata.iloc[:,1]
plt.scatter(a,b,c="blue")
plt.show()
# Price and Rsize
a= boxdata.iloc[:, 0]
b=boxdata.iloc[:,2]
plt.scatter(a,b,c="red")
plt.show()
# PRICE and FSIZE
a= boxdata.iloc[:, 0]
b=boxdata.iloc[:,3]
plt.scatter(a,b,c="orange")
plt.show()
# PRICE and SHELVES
a= boxdata.iloc[:, 0]
b=boxdata.iloc[:,4]
plt.scatter(a,b,c="black")
plt.show()
# PRICE and FEATURES
a= boxdata.iloc[:, 0]
b=boxdata.iloc[:,5]
plt.scatter(a,b,c="green")
plt.show()





