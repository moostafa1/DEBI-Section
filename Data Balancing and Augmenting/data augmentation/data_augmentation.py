import pandas as pd

def save_df(lines_lst, df_len = 50):
    df = pd.DataFrame()
    labels = [0 for i in range(df_len)]
    df['label'] = labels
    df['sentence'] = lines_lst[5 :df_len+5]
    df.to_csv('data.csv', index=False)



with open('Sherlock Holmes Dataset.txt') as f:
    lines = f.read()

lines_lst = lines.replace('"', '').replace("'","").replace('\n','').replace("    ", "").split(".")
lines_lst = [l+'.'.strip() for l in lines_lst]

# print(lines_lst)
# print(len(lines_lst))


save_df(lines_lst, df_len = 6023 - 2528)
