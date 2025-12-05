import pandas as pd
#data
df=pd. DataFrame({'Item ':['Soap', 'chocolates', 'books', 'pens', 'laptop', 'Mobile'], 
'Quantity ': [50, 10, 50, 30, 70, 60],
'Price':[55, 15, 45, 5, 80, 45], 
'Sales': [30, 50, 45, 10, 50, 15]})

print(df)

print('sum of sales:',df['Sales'].sum())