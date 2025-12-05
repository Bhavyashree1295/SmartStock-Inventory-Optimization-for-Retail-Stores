import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
 
data=pd.DataFrame({
    "Land_area":[1000,1500,2000,2500,3000,],
    "Price":[10,15,18,22,27]
})
 
x=data[["Land_area"]] # feature 
y=data[["Price"]]# Target
 
#Train-test Split 
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
 
# make Training 
model=LinearRegression()
model.fit(x_train,y_train)
 
# Make Prediction 
pred=model.predict(x_test)
 
print("Prediction Prices :",pred)
print("Actual  Prices :",y_test.values)
 
#predict for new land area 
new_land_area=[[2800]]
new_price=model.predict(new_land_area)
 
print("prediction for 2800 sq.ft",new_price)