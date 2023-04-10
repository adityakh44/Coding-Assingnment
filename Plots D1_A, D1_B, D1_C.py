import pandas as pd


varA = pd.read_excel(r"F:\Python Scripts\Neoperk Assignment\D1 to D1_A, D1_B, D1_C.xlsx", 
                    "D1_A")
varB = pd.read_excel(r"F:\Python Scripts\Neoperk Assignment\D1 to D1_A, D1_B, D1_C.xlsx", 
                    "D1_B")
varC = pd.read_excel(r"F:\Python Scripts\Neoperk Assignment\D1 to D1_A, D1_B, D1_C.xlsx", 
                    "D1_C")


varA.dropna(inplace=True)
varA.sort_values("A")

varB.dropna(inplace=True)
varB.sort_values("B")

varC.dropna(inplace=True)
varC.sort_values("C")

df_A = varA
df_B = varB
df_C = varC


#Histogram of D1_A, D1_B, D1_C
df_A[["A",]].plot.hist() 
df_B[["B",]].plot.hist() 
df_C[["C",]].plot.hist() 