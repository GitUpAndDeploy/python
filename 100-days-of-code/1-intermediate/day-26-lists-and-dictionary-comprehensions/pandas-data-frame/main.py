import pandas as pd

student_dict = {
  "student": ["Angela", "James", "Lily"],
  "score": [56, 76, 98]
}
# Dictionary comprehension
# for (key,value) in student_dict.items():
#   print(value)

student_data_frame = pd.DataFrame(student_dict)

# print(student_data_frame)

# Loop through data frame
# for (key,value) in student_data_frame.items():
#   print(value)

# Loop through rows of a data frame
for (index,row) in student_data_frame.iterrows():
  # print(index)
  # print("---")
  # print(row)
  # print(row.score)
  # print(row.student)
  if row.student == "Angela":
    print(row.score)
