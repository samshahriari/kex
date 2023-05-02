import numpy as np
import pandas as pd

df = pd.read_csv("result_csv.csv")

errTypes = df['Noise type']
df2 = df.drop(axis=1, labels=['Noise type', 'Start Pos'])

df_start_0 = df2.iloc[0:8]
df_start_0 = df_start_0.iloc[0:7] - df_start_0.iloc[7]
df_start_0 = np.square(df_start_0)
rowSum0 = df_start_0.sum(axis=1)

tot0 = np.transpose(np.sqrt(rowSum0))
print(tot0)


df_start_1 = df2.iloc[8:len(df2)]
df_start_1 = df_start_1.iloc[0:7] - df_start_1.iloc[7]
df_start_1 = np.square(df_start_1)
rowSum1 = df_start_1.sum(axis=1)
tot1 = np.transpose(np.sqrt(rowSum1))
tot1.reset_index(inplace=True, drop=True)
print(tot1)

final_df = pd.DataFrame(
    {'Error Type': errTypes[0:7].to_numpy(),
     'Accuracy for starting position: 0000': tot0,
     'Accuracy for starting position: 1111': tot1})

final_df.loc['Average', 'Accuracy for starting position: 0000'] = final_df['Accuracy for starting position: 0000'].mean()
final_df.loc['Average', 'Accuracy for starting position: 1111'] = final_df['Accuracy for starting position: 1111'].mean()

final_df['Average'] = (tot0+tot1) / 2
print(final_df)

final_df.to_latex(buf='little_table.tex', index=False)


# final_df.to_csv('littleTable.csv', index=False)

# df_0_normed = np.sqrt(np.square(df_start_0).sum(axis=1))
# print(df_0_normed)
""" print(df2)
print(df_start_0)
print(df_start_1) """
