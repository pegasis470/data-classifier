#!/usr/bin/env python3
# importing pandas library 
import pandas as pd
import numpy as np

def remove_k(df,column):
    new_col=[]
    for i in df[column]:
        new_col.append(int(i.strip("k")))
    df[column]=new_col
def main(df):
    global final_df
    print("Enter No. of parameters:")
    pam=int(input())
    final_df=pd.DataFrame()
    for i in range(pam):
        print("Type Column Name from the following:")
        column_list=list(df.columns.values)
        column_list.remove(df.columns[0])
        print(column_list)
        column=input()
        if type(df[column].values[0])==str:
            print("Choose the desired value from the once below:")
            if len(list(final_df.values))==0:
                print(list(set(df[column].values)))
            else:
                print(list(set(sort[column].values)))
            query=input()
            sort=df.loc[df[column] == query]
            final_df=sort
        elif type(df[column].values[0])==np.int64:
            print("press 1 for high to low and 2 for low to high")
            secquence=int(input())
            if len(list(final_df.values))==0:
                if secquence == 1:
                    sort=df.sort_values(by=[column], ascending=True)
                else:
                    sort=df.sort_values(by=[column], ascending=False)
                final_df=sort

            else:
                if secquence == 1:
                    sort=sort.sort_values(by=[column], ascending=True)
                else:
                    sort=sort.sort_values(by=[column], ascending=False)
                final_df=sort

    return final_df




if __name__=="__main__":
    df=pd.read_csv("~/jupyter notebooks/data/data.csv")
    remove_k(df,"Avg. Cost($)")
    final=main(df)
    print(final)
    print("save a csv file?")
    save=input()
    if save == "yes":
      print("please enter the name of file ")
      file_name=input()
      final.to_csv(f"{file_name}.csv")      
