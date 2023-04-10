
import statsmodels.api as sm
import numpy as np
import pandas as pd
mtcars = sm.datasets.get_rdataset('mtcars')
mtcars_data = mtcars.data

#display first 6 rows
n = 6
n_col  = mtcars_data.iloc[:n, :]
#print(n_col)

#avg mpg of all cars
avg = mtcars_data['mpg'].mean()
#print("avg mpg of all cars = " ,avg)

#select rwo with where all cars have 6 cylinders
cyl_6 = mtcars_data.loc[mtcars_data['cyl'] == 6] 
#print(cyl_6)

#select colomns am, gear, carb
col = mtcars_data[["am", "gear", "carb" ]]
#print(col)

#create a new colomn 'performance'
mtcars_data['performance'] = mtcars_data.apply(lambda row: row.hp/row.wt, axis = 1)
#print(mtcars_data)

#what is mgp of hornet sportabout
mpg_h_s = mtcars_data.iloc[[4],[0]]
print(mpg_h_s)





