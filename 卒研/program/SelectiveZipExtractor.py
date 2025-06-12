import os
import zipfile

# **処理対象のフォルダー（ZIPファイルがある場所）**
zip_folder = "./XbrlZipFolder"  # ZIPファイルがあるフォルダー

# **抽出したい拡張子**
target_extension = ".xbrl"

# **ターゲットの階層（例: ZIP 内の `data/target/` フォルダ内）**
target_folder = "XBRL/PublicDoc"  # ZIPの中の特定フォルダ名

# **抽出先フォルダー**
output_folder = "./"
os.makedirs(output_folder, exist_ok=True)  # フォルダーがなければ作成

# **ZIPファイルを処理**
for zip_filename in os.listdir(zip_folder):
    zip_path = os.path.join(zip_folder, zip_filename)
    
    # ZIPファイルのみ処理
    if zip_filename.endswith(".zip"):
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            # ZIP内のファイルリストを取得
            for file in zip_ref.namelist():
                # ✅ 指定したフォルダ内のファイルのみ抽出
                if file.startswith(target_folder) and file.endswith(target_extension):
                    zip_ref.extract(file, output_folder)
                    print(f"抽出: {file} → {output_folder}")

print("指定階層のファイル抽出が完了しました！")
