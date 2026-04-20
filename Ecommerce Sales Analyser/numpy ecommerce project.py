import numpy as np
ecom_data = np.array([[12,34,np.nan,76],[np.nan,43,55,44],[55,65,np.nan,33],[22,44,55,66]])

#handling nan
product_average = np.nanmean(ecom_data,axis = 0)
indexes = np.where(np.isnan(ecom_data))
ecom_data[indexes] = np.take(product_average,indexes[1])

new_day_sales = np.array([12,34,54,67])
new_day_sales = new_day_sales.reshape(1,4)

ecom_data = np.concatenate((ecom_data,new_day_sales),axis = 0)

new_product = np.array([12,34,55,43,22])
new_product = new_product.reshape(5,1)

ecom_data = np.concatenate((ecom_data,new_product),axis = 1)

total_sales = np.sum(ecom_data,axis=1)
total_sales_product = np.sum(ecom_data,axis = 0)

best_product = np.argmax(total_sales_product)
best_sales_day = np.argmax(total_sales)

discount = ecom_data * 0.85

normalise = ecom_data / np.max(ecom_data)

split_data = np.vsplit(ecom_data,[2,4])