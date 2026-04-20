import numpy as np
#data creation
ecom_data = np.array([[12,34,np.nan,76],[np.nan,43,55,44],[55,65,np.nan,33],[22,44,55,66]])

#handling nan and replacing it 
product_average = np.nanmean(ecom_data,axis = 0)
indexes = np.where(np.isnan(ecom_data))
ecom_data[indexes] = np.take(product_average,indexes[1])

# adding new day sales data
new_day_sales = np.array([12,34,54,67])
new_day_sales = new_day_sales.reshape(1,4)
ecom_data = np.concatenate((ecom_data,new_day_sales),axis = 0)

# new product data 
new_product = np.array([12,34,55,43,22])
new_product = new_product.reshape(5,1)
ecom_data = np.concatenate((ecom_data,new_product),axis = 1)

#finding total sales per day and as well as total sales per product
total_sales = np.sum(ecom_data,axis=1)
total_sales_product = np.sum(ecom_data,axis = 0)

#finding the best product as well as best day
best_product = np.argmax(total_sales_product)
best_sales_day = np.argmax(total_sales)

#implementing discount
discount = ecom_data * 0.85

#normalise the data [all data in 0,1 form]
normalise = ecom_data / np.max(ecom_data)

#spliting the data
split_data = np.vsplit(ecom_data,[2,4])
