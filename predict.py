import pandas as pd
import statsmodels.api as sm

# 利用线性回归预测每年电子游戏销售额

def loader():   # 读取数据
    filepath ="xxx\\vgsales.csv" #使用的数据集文件地址
    df = pd.read_csv(filepath, header=0)
    return df

if __name__ == "__main__":
    df = loader()

    # 错误信息更正，根据https://www.kaggle.com/gregorut/videogamesales/discussion/24969
    df.loc[df['Name'] == "Imagine: Makeup Artist", "Year"] = 2009
    df.loc[df['Name'] == "Phantasy Star Online 2 Episode 4: Deluxe Package", "Year"] = 2016
    df.loc[df['Name'] == "Brothers Conflict: Precious Baby", "Year"] = 2016
    # 2016年数据并不完整，不纳入处理范围，根据https://www.kaggle.com/gregorut/videogamesales/discussion
    df = df[~df['Year'].isin([2016])]

    Data = df[["Year", "Global_Sales"]]
    Data.dropna(axis=0)  # 删除NaN值
    datasum = Data.groupby("Year", as_index=False).sum() # 重复行累加并和

    print(datasum)
    # 设置预测变量和结果变量，用Year预测Global_Sales
    X = datasum.Year  # 预测变量
    y = datasum.Global_Sales  # 结果变量
    # 执行最小二乘回归
    est = sm.OLS(y, X)
    # 模型拟合
    model = est.fit()
    # 预测
    year = int(input("请输入预测年份："))
    P = []
    P.append(year)
    P = pd.DataFrame(P)
    predictions = model.predict(P)
    print("预测Global_Sales：", end='')
    print(predictions[0])
    # print(est.summary()) # 查看模型拟合的结果








