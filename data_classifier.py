#!/usr/bin/env python3
# importing pandas library 
import pandas as pd
## function is defined to take inputs and proccess them to genrate 
def main(df):
    global sort
    print("Please choose column")
    column_lst=list(df.columns)
    column_lst.remove(column_lst[0])
    print(column_lst)
    column=input()
    if column in column_lst:
        print(f"sorting by {column} ")
        print(list(set(df[column])))
        print("please choose one")
        query=input()
        for index, row in df.iterrows():
            if type(row[column]) == str:
                sort=df.loc[df[column] == query]
            if type(row[column]) == int:
                sort=df.loc[df[column] == int(query)]
        display(sort)
    else:
        print("invilaid input please choose one from displayed and try agian")
        return None
      
if __name__ == "__main__":
    df=pd.read_json("data.json")
    main(df)
    print("save a json file?")
    save=input()
    if save == "yes":
      print("please enter the name of file ")
      file_name=input()
      sort.to_json(f"{file_name}.json")      
