import os
import csv
import pandas as pd

def merge_csv_from_folder(folder_path, output_file):
    
    data = {"CompanyName": [],
            "ProfitLossBeforeTaxIFRSSummaryOfBusinessResults_2023":[],
            "ProfitLossBeforeTaxIFRSSummaryOfBusinessResults_2022":[],
            "ProfitLossBeforeTaxIFRSSummaryOfBusinessResults_2021":[],
            "ProfitLossBeforeTaxIFRSSummaryOfBusinessResults_2020":[],
            "NetAssetsSummaryOfBusinessResults_2023": [],
            "NetAssetsSummaryOfBusinessResults_2022": [], 
            "NetAssetsSummaryOfBusinessResults_2021": [],
            "NetAssetsSummaryOfBusinessResults_2020": [],  
            "CashAndCashEquivalentsIFRSSummaryOfBusinessResults_2023": [],
            "CashAndCashEquivalentsIFRSSummaryOfBusinessResults_2022": [],
            "CashAndCashEquivalentsIFRSSummaryOfBusinessResults_2021": [],
            "CashAndCashEquivalentsIFRSSummaryOfBusinessResults_2020": [],
            "CapitalStockSummaryOfBusinessResults_2023": [],
            "CapitalStockSummaryOfBusinessResults_2022": [],
            "CapitalStockSummaryOfBusinessResults_2021": [],
            "CapitalStockSummaryOfBusinessResults_2020": []}
    df = pd.DataFrame(data)

    # フォルダ内のすべてのファイルを処理
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            file_path = os.path.join(folder_path, file_name)
            InfoList = file_name.split('_')
            attribute = InfoList[2].split('.')[0]
            DfReaded =  pd.read_csv(file_path, encoding="utf-8")
            print(DfReaded)
            for row in DfReaded.itertuples(index=True, name="Data"):
                MatchingIndice = df[df["CompanyName"] == row.CompanyName].index.tolist()
                if MatchingIndice == []:
                    df.loc[len(df)] = {"CompanyName": row.CompanyName,
                                        "ProfitLossBeforeTaxIFRSSummaryOfBusinessResults_2023":0,
                                        "ProfitLossBeforeTaxIFRSSummaryOfBusinessResults_2022":0,
                                        "ProfitLossBeforeTaxIFRSSummaryOfBusinessResults_2021":0,
                                        "ProfitLossBeforeTaxIFRSSummaryOfBusinessResults_2020":0,
                                        "NetAssetsSummaryOfBusinessResults_2023": 0,
                                        "NetAssetsSummaryOfBusinessResults_2022": 0, 
                                        "NetAssetsSummaryOfBusinessResults_2021": 0,
                                        "NetAssetsSummaryOfBusinessResults_2020": 0,  
                                        "CashAndCashEquivalentsIFRSSummaryOfBusinessResults_2023": 0,
                                        "CashAndCashEquivalentsIFRSSummaryOfBusinessResults_2022": 0,
                                        "CashAndCashEquivalentsIFRSSummaryOfBusinessResults_2021": 0,
                                        "CashAndCashEquivalentsIFRSSummaryOfBusinessResults_2020": 0,
                                        "CapitalStockSummaryOfBusinessResults_2023": 0,
                                        "CapitalStockSummaryOfBusinessResults_2022": 0,
                                        "CapitalStockSummaryOfBusinessResults_2021": 0,
                                        "CapitalStockSummaryOfBusinessResults_2020": 0}
                match attribute:
                    case "ProfitLossBeforeTaxIFRSSummaryOfBusinessResults":
                        df.loc[df["CompanyName"] == row.CompanyName,(attribute+"_2023")] = row.d2023
                        df.loc[df["CompanyName"] == row.CompanyName,(attribute+"_2022")] = row.d2022
                        df.loc[df["CompanyName"] == row.CompanyName,(attribute+"_2021")] = row.d2021
                        df.loc[df["CompanyName"] == row.CompanyName,(attribute+"_2020")] = row.d2020
                    case "NetAssetsSummaryOfBusinessResults":
                        df.loc[df["CompanyName"] == row.CompanyName,(attribute+"_2023")] = row.d2023
                        df.loc[df["CompanyName"] == row.CompanyName,(attribute+"_2022")] = row.d2022
                        df.loc[df["CompanyName"] == row.CompanyName,(attribute+"_2021")] = row.d2021
                        df.loc[df["CompanyName"] == row.CompanyName,(attribute+"_2020")] = row.d2020
                    case "CashAndCashEquivalentsIFRSSummaryOfBusinessResults":
                        df.loc[df["CompanyName"] == row.CompanyName,(attribute+"_2023")] = row.d2023
                        df.loc[df["CompanyName"] == row.CompanyName,(attribute+"_2022")] = row.d2022
                        df.loc[df["CompanyName"] == row.CompanyName,(attribute+"_2021")] = row.d2021
                        df.loc[df["CompanyName"] == row.CompanyName,(attribute+"_2020")] = row.d2020
                    case "CapitalStockSummaryOfBusinessResults":
                        df.loc[df["CompanyName"] == row.CompanyName,(attribute+"_2023")] = row.d2023
                        df.loc[df["CompanyName"] == row.CompanyName,(attribute+"_2022")] = row.d2022
                        df.loc[df["CompanyName"] == row.CompanyName,(attribute+"_2021")] = row.d2021
                        df.loc[df["CompanyName"] == row.CompanyName,(attribute+"_2020")] = row.d2020
        df.to_csv(output_file, encoding="utf-8-sig", index=False)
        

# 属性指定
folder_path = 'Saped_Merged_csv'  # フォルダのパス
output_file = f'joined.csv'  # 出力ファイルの名前
merge_csv_from_folder(folder_path, output_file)
