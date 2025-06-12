import os
import csv
import pandas as pd

def merge_csv_from_folder(folder_path, output_file):
    
    data = {"CompanyName": [], "2023": [], "2022": [],"2021": [],"2020": [],"2019": [],"2018": []}
    df = pd.DataFrame(data)

    # フォルダ内のすべてのファイルを処理
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            file_path = os.path.join(folder_path, file_name)
            InfoList = file_name.split('_')
            CompanyName = InfoList[0]
            year = InfoList[1]
            DfReaded =  pd.read_csv(file_path, encoding="utf-8")
            print(DfReaded)
            MatchingIndice = df[df["CompanyName"] == CompanyName].index.tolist()
            if MatchingIndice == []:
                try:
                    df.loc[len(df)] = {"CompanyName": CompanyName, "2023": 0, "2022": 0,"2021": 0,"2020": 0,"2019": 0,"2018": 0}
                except Exception as e:
                    print(e)
                    print(file_name)
                    print(CompanyName)
                else:
                    if len(DfReaded) == 4:
                        df.loc[df["CompanyName"] == CompanyName, year] = DfReaded.at[3,"Data"]
                        df.loc[df["CompanyName"] == CompanyName, str(int(year)-1)] = DfReaded.at[2,"Data"]
                        df.loc[df["CompanyName"] == CompanyName, str(int(year)-2)] = DfReaded.at[1,"Data"]
                        df.loc[df["CompanyName"] == CompanyName, str(int(year)-3)] = DfReaded.at[0,"Data"]
                    elif len(DfReaded) == 3:
                        df.loc[df["CompanyName"] == CompanyName, year] = DfReaded.at[2,"Data"]
                        df.loc[df["CompanyName"] == CompanyName, str(int(year)-1)] = DfReaded.at[1,"Data"]
                        df.loc[df["CompanyName"] == CompanyName, str(int(year)-2)] = DfReaded.at[0,"Data"]
                    elif len(DfReaded) == 2:
                        df.loc[df["CompanyName"] == CompanyName, year] = DfReaded.at[1,"Data"]
                        df.loc[df["CompanyName"] == CompanyName, str(int(year)-1)] = DfReaded.at[0,"Data"]
                    elif len(DfReaded) == 1:
                        df.loc[df["CompanyName"] == CompanyName, year] = DfReaded.at[0,"Data"]
            else:
                df.loc[df["CompanyName"] == CompanyName, year] = DfReaded.at[3,"Data"]
        df.to_csv(output_file, encoding="utf-8-sig", index=False)
        

# 属性指定
FolderName = 'ProfitLossBeforeTaxIFRSSummaryOfBusinessResults'
folder_path = 'data2\\' + FolderName  # フォルダのパス
output_file = f'merged_{FolderName}.csv'  # 出力ファイルの名前
merge_csv_from_folder(folder_path, output_file)
