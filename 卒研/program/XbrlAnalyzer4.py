from lxml import etree
import csv
import os


def open_folder(FolderPath):
    #返り値のファイルパスリスト
    FilePathList = []
    #フォルダ内のxbrlファイルの探索
    for file_name in os.listdir(FolderPath):
        file_path = os.path.join(FolderPath, file_name)
        if os.path.isfile(file_path) and file_name.endswith(".xbrl"):
            FilePathList.append(file_path)
    return FilePathList

def OutputFile(FileName,DataList):
    OutputFileName = (f"{FileName}_{DataList[0][0]}.csv")
    FolderPath = "./data2/" + DataList[0][0]
    if len(DataList[0][0]) > 100:
        return
    if os.path.isdir(FolderPath):
        pass
    else:
        os.makedirs(FolderPath)
    with open((os.path.join(FolderPath,OutputFileName)), mode="w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(["CompanyName_Year","Data"])
        for data in DataList:
            writer.writerow([f"{data[0]}_{data[1]}",data[2]])
        
    
def open_xbrl(file):
    # XBRLファイルを読み込む
    xbrl_file = file

    # XMLパーサーで解析
    tree = etree.parse(xbrl_file)
    root = tree.getroot()
    
    #年代取得
    year = int(((xbrl_file.split("_"))[2].split("-"))[0]) - 1
    print(year)

    # 名前空間の取得（XBRLファイルによって異なる場合がある）
    if year >= 2023:
        ns = {"xbrl": "http://disclosure.edinet-fsa.go.jp/taxonomy/jpcrp/2023-12-01/jpcrp_cor"}
    elif year >= 2022:
        ns = {"xbrl": "http://disclosure.edinet-fsa.go.jp/taxonomy/jpcrp/2022-11-01/jpcrp_cor"}
    elif year >= 2021:
        ns = {"xbrl": "http://disclosure.edinet-fsa.go.jp/taxonomy/jpcrp/2021-11-01/jpcrp_cor"}
    elif year >= 2020:
        ns = {"xbrl": "http://disclosure.edinet-fsa.go.jp/taxonomy/jpcrp/2020-11-01/jpcrp_cor"}    
    elif year >= 2019:
        ns = {"xbrl": "http://disclosure.edinet-fsa.go.jp/taxonomy/jpcrp/2019-11-01/jpcrp_cor"}
    elif year >= 2018:
        ns = {"xbrl": "http://disclosure.edinet-fsa.go.jp/taxonomy/jpcrp/2018-03-31/jpcrp_cor"}
    else:
        return

    # 会社名の取得
    CompanyName = ""
    for element in root.findall(".//xbrl:*", namespaces=ns):
        name = ((element.tag).split("}"))[1]
        if name == "CompanyNameCoverPage":
            CompanyName = element.text.strip().split("\n")[0] if element.text else "None"
            print(CompanyName)
            break

    #財務諸表の様式の取得
    ns_jpdei = {"xbrl": "http://disclosure.edinet-fsa.go.jp/taxonomy/jpdei/2013-08-31/jpdei_cor"}
    DocumentTypeDEI = ""
    for element in root.findall(".//xbrl:*", namespaces=ns_jpdei):
        name = ((element.tag).split("}"))[1]
        if name == "DocumentTypeDEI":
            DocumentTypeDEI = element.text.strip() if element.text else "None"
            print(DocumentTypeDEI)
        elif name == "AccountingStandardsDEI":
            AccountingStandardsDEI = element.text.strip() if element.text else "None"
            print(AccountingStandardsDEI)
            if AccountingStandardsDEI != "IFRS": return
    OutputFileName = (f"{CompanyName}_{year}")
    
    # 財務データを取得する
    tmparr = []
    for element in root.findall(".//xbrl:*", namespaces=ns):
        name = ((element.tag).split("}"))[1]
        contextRef = element.attrib.get("contextRef")
        value = element.text.strip() if element.text else "N/A"
        try:
            value_num = float(value)
        except Exception:
            continue
        else:
            if "TextBlock" in name: continue
            elif tmparr == []: tmparr.append([name,contextRef,value_num])
            elif tmparr[0][0] == name: tmparr.append([name,contextRef,value_num])
            else:
                OutputFile(OutputFileName,tmparr)
                tmparr = []
                    
            

#main
if __name__ == "__main__":
    FolderPath = "./xbrl/PublicDoc"    
    FilePathList = open_folder(FolderPath)
    for file in FilePathList:
        open_xbrl(file)