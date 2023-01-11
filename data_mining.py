from typing import List
import numpy as np
import pandas
import pandas as pd
import openpyxl
import functions

list1 = []
list2 = []
list3 = []


with open("applications.txt", 'r') as file:
    apply_data = file.readlines()
    print(apply_data)

    for item in apply_data:
        item.strip("\n")
        floor = item[:2].strip(" ")
        pickup_time = item[14:22].strip(" ")
        people_number = item[-11:-9].strip("(")

        list1.append(floor)
        list2.append(pickup_time)
        list3.append(people_number)

        col1 = "Floor"
        col2 = "Pickup time"
        col3 = "number of people"
        col4 = "sum of total people"

        data = pd.DataFrame({col1:list1, col2:list2, col3:list3})
        data.to_excel('data.xlsx', sheet_name='application', index=False)




