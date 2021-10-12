import camelot as cm
import pandas as pd
import seaborn as sns


sInputFolder = "pdf_table_extraction\\in\\"
sOutputFolder = "pdf_table_extraction\\out\\"
input_pdf = cm.read_pdf(sInputFolder + "india_factsheet_economic_n_hdi.pdf", flavor='lattice', pages = '1,2')


"""
for n in input_pdf:
    print(n)
"""

input_pdf[2].df

df = input_pdf[2].df.loc[11:14, 1:3]

df = df.reset_index(drop = True)

df.columns = ["KPI", "2001", "2011"]

df.loc[:,["2001", "2011"]] = df.loc[:, ["2001", "2011"]].astype(float)

df.to_csv(sOutputFolder + "table_from_pdf.csv")

df.to_excel(sOutputFolder + "table_from_pdf.xlsx")

df2 = pd.read_csv(sOutputFolder + "table_from_pdf.csv")

df_melted = df.melt('KPI', var_name = 'Year', value_name = '[%]')

bar = sns.barplot(x="KPI", y='[%]', hue = "Year", data = df_melted)

image = bar.get_figure()

image.savefig(sOutputFolder + "bar.jpg")

