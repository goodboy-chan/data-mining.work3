import pandas as pd

# 电子游戏市场分析：受欢迎的游戏、类型、发布平台、发行人等

def loader():   # 读取数据
    filepath ="xxx\\vgsales.csv" #使用的数据集文件地址
    df = pd.read_csv(filepath, header=0)
    return df

def topk(str, data, k):     # 输出str属性总销量前k个数据
    Data = data[[str, "Global_Sales"]]
    Data.dropna(axis = 0) # 删除NaN值
    datasum = Data.groupby(str, as_index=False).sum() # 重复行累加并和
    datasum.sort_values(by="Global_Sales", ascending=False, inplace=True)  # 按总销量降序排序
    # print(datasum)
    print("Global_Sales前%d的%s及其Global_Sales:" %(k,str))
    print(datasum.head(k))

if __name__ == "__main__":
    df = loader()
    topk("Name", df, 3) # 按游戏名称
    topk("Genre", df, 3)  # 按游戏类型
    topk("Platform", df, 3)  # 按游戏平台
    topk("Publisher", df, 3)  # 按游戏发行人