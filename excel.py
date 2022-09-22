

import pandas as pd
import numpy as np

pd.options.display.max_rows= 9999
df = pd.read_csv("c:/temp/coreco.core2019co_full990.csv")
# #first filter out hospital and churches
df1=df.query("`NTMAJ12` != 'EH' and `NTMAJ12` != 'RE'")

# for all rows for education charities, housing and shelter charities, and public safety charities
df2=df1.query("(`NTEE1` == 'B') or (`NTEE1` == 'L') or (`NTEE1` == 'M')")
# Revenue columns missing: totcntrbgfts, prgmservcode2acd, totrev2acola, prgmservcode2bcd, totrev2bcola, prgmservcode2ccd, 
# Revenue columns missing: totrev2ccola, prgmservcode2dcd, totrev2dcola, prgmservcode2ecd, totrev2ecola, totrev2fcola, 
# totprgmrevnue
# invstmntinc, txexmptbndsproceeds, royaltsinc, grsrntsreal, grsrntsprsnl, rntlexpnsreal, rntlexpnsprsnl
# rntlincreal, rntlincprsnl,
# df2 = df2[["NAME"]]
print(df2.head(5))

# grsincfndrsng
# Numeric
# (1)	990 Core Pt VIII-8a
# Gross fundraising
# lessdirfndrsng
# Numeric
# (1)	990 Core Pt VIII-8b
# Fundraising expenses
# netincfndrsng
# Numeric
# (1)	990 Core Pt VIII-8c(A)
# Fundraising income


#  & (df.NTEE1 == 'L') & (df.NTEE1 == 'M')
# print(df)
# #column name, data type, fraction missing, if numeric avg & stdev
# if 'data type' == float:
#     newtable= {'column_name': df.iloc[0], 'data type': df.dtypes, 'fraction missing:' , 'avg': , 'stdev': }
# print(newtable)

# #remove data of hospitals and churches
# df= df[(df.FNDNCD != 10) & (df.FNDNCD != 12)]

# #for education charities, housing and shelter charities, and public safety charities
# df=df[(df.NTEE1 == 'B') & (df.NTEE1 == 'L') & (df.NTEE1 == 'M')]
# #avg fundraising income
# avg= df['NETINCFNDRSNG'].mean()
# #print(total)
# #avg=total/len(df)
# print(avg)
# #avg_fund_inc= 
# #total revenue
# totrev= df['TOTREVENUE'].sum()
# print(totrev)
# #share of revenue spent of fundraising



#print(df)

#from tabulate import tabulate

#import csv
#with open('sample.csv') as file_obj:
#    reader_obj = csv.reader(file_obj)
#    for row in reader_obj:
#        print(row)