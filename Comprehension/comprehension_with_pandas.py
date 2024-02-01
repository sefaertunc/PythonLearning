import pandas as pd

student_dict = {
    "names": ["John", "Smith", "Aden"],
    "ages": [20, 30, 40]
}

student_df = pd.DataFrame(student_dict)
for (index, row) in student_df.iterrows():
    print(row.names, row.ages)
