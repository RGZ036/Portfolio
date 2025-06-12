import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import math

# ✅ CSVファイルを読み込む（1行目をスキップ）
df = pd.read_csv("./JoinedCompany.csv")

# ✅ 説明変数（3,4,5列目）と目的変数（2列目）を取得
X = df.iloc[:,[2, 3, 4, 6, 7, 8, 10, 11, 12, 14, 15, 16]]  # 説明変数
y = df.iloc[:, 1]       # 目的変数
print(X)


# ✅ データを訓練用とテスト用に分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ モデルの作成・学習
model = LinearRegression()
model.fit(X_train, y_train)

# ✅ 予測と評価
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = math.sqrt(mse)

#行平均
column_mean = df.iloc[:, 1].mean()


# ✅ 結果を表示
print(f"回帰係数: {model.coef_}")
print(f"切片: {model.intercept_}")
print(f"平均二乗誤差 (MSE): {mse}")
print(f"平均二乗誤差の平方根 (RMSE): {"{:.5e}".format(rmse)}")
print(f"目的変数の平均: {"{:.5e}".format(column_mean)}")
print(f"RMSE/目的変数の平均: {rmse/column_mean}")