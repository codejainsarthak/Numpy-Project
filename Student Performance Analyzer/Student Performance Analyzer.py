import numpy as np 

student_data = np.array([
    [78, np.nan, 88, 92],
    [85, 76, np.nan, 80],
    [np.nan, 90, 84, 88],
    [70, 65, 78, np.nan]
])

#Handling Missing Value
Subject_average = np.nanmean(student_data,axis = 0)
index = np.where(np.isnan(student_data))
student_data[index] = np.take(Subject_average,index[1])

# Adding New student
new_student = np.array([[82, 79, 85, 90]])
new_student = new_student.reshape(1,4)
student_data = np.concatenate((student_data,new_student),axis = 0)

# Adding New Subject

new_subject = np.array([[75, 80, 85, 70, 88]])
new_subject = new_subject.reshape(5,1)
student_data = np.concatenate((student_data,new_subject),axis = 1)

# Total Marks Per student

total_marks = np.sum(student_data,axis = 1)

#average marks per subject

average_marks = np.mean(student_data,axis = 0)

# topper student

topper_student = np.argmax(total_marks)

#Toughest subject

toughest_subject = np.argmin(average_marks)

# bonus marks

student_data = student_data + 5

# Normalization 

Normalised_data = student_data / np.max(student_data)

#spliting the dataset

split_data = np.vsplit(student_data,[3])

