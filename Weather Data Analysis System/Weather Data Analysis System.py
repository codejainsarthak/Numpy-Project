import numpy as np
weather_data = np.array([
    [30, 80, np.nan, 5],
    [32, np.nan, 60, 10],
    [np.nan, 75, 55, 8],
    [28, 70, 50, np.nan]
])

column_average = np.nanmean(weather_data,axis = 0)
indexes = np.where(np.isnan(weather_data))
weather_data[indexes] = np.take(column_average,indexes[1])

#adding new day data
new_day = np.array([31, 78, 65, 7])
new_day = new_day.reshape(1,4)
weather_data = np.concatenate((weather_data,new_day),axis = 0)

#adding new feature(air quality index)
new_feature = np.array([[120, 110, 130, 125, 140]])
new_feature = new_feature.reshape(5,1)
weather_data = np.concatenate((weather_data,new_feature),axis = 1)

#daily analysis

average_condition_perday = np.mean(weather_data,axis = 1)
weather_intensity = np.sum(weather_data,axis = 1)

# feature analysis

average_feature = np.mean(weather_data,axis = 0)
highest_value = np.argmax(average_feature,axis = 0)

#Extreme Condition 

day_highest_temprature = np.argmax(weather_data[:,0],axis = 0)
lowest_humidity = np.argmin(weather_data[:,1],axis = 0)

#weather adjustment
weather_data[:,0] = weather_data[:,0] + 2
weather_data[:,1] = weather_data[:,1] * 0.9

# normalise data

Normalised_data = weather_data/np.max(weather_data) 

# spliting the data

split_data = np.hsplit(weather_data[3])
print(split_data)