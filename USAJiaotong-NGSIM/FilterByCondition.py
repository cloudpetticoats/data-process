import pandas as pd
"""
    对USA联邦交通局数据的处理：
        1.取名为lankershim主干道的数据
        2.过滤出v_Class=2|3的数据（汽车和卡车）
"""


if __name__ == '__main__':

    # 读取CSV文件
    df = pd.read_csv('../data-afterprocess/1.csv')

    # 过滤出Location列中值为'lankershim'的行
    filtered_df = df[(df['v_Class'] == 2) | (df['v_Class'] == 3)]

    # 将过滤后的数据保存到一个新文件中
    filtered_df.to_csv('./data-afterprocess/auto&truck.csv', index=False)

    print("success, dataNum=", len(filtered_df))
