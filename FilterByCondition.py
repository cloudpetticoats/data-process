import pandas as pd

if __name__ == '__main__':


    # 读取CSV文件
    df = pd.read_csv('./data/vehicle.csv')

    # 过滤出aaa列中值为'eee'的行
    filtered_df = df[df['Location'] == 'lankershim']

    # 将过滤后的数据保存到一个新文件中
    filtered_df.to_csv('./data-afterprocess/1.csv', index=False)

    print("success, dataNum=", len(filtered_df))
