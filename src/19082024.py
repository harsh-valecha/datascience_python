import pandas as pd

s1 = pd.Series([10,20,30,40,30],name='ages')
# print(s1)

d1 = pd.DataFrame(
    {
        'product':['nim','nirma','supra'],
        'price':[23,30,42],
        'qty':[2,3,4]
    }
)
# print(d1.keys())


temps = pd.Series([72,85,90,95,93,89],name='temperature')
# print(temps)

# converting the whole series
# print(temps*5)

# print(temps[temps>90])
'''
3    95
4    93
Name: temperature, dtype: int64
'''


s2 = pd.Series(['test',1,20.3,None,False])
# print(s2)

# accessing dataframe columns
# print('accessing single column :',d1['product'],sep='\n')
# print('accessing many columns:',d1[['price','qty']],sep='\n') #multiple columns


# accessing using inbuilt columns
# print(d1.iloc[0]) # rows are accessed
# # accessing columns - all rows
# print(d1.loc[:,['product','price']])
# # accessing columns - some rows
# print(d1.loc[:1,['product','price']])

# reading csv files
data = pd.read_csv('test_data/MOCK_DATA.csv',sep=',')
# printing first 10 rows
# print(data.head(10))

# print(data.columns,data.size,data.ndim)


data2 = pd.read_excel('test_data/MOCK_DATA.xlsx')
# print(data2.head())
# print(data2.info()) # gives concise summary
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 6 columns):
 #   Column      Non-Null Count  Dtype 
---  ------      --------------  ----- 
 0   id          100 non-null    int64 
 1   first_name  100 non-null    object
 2   last_name   84 non-null     object
 3   email       100 non-null    object
 4   gender      23 non-null     object
 5   ip_address  100 non-null    object
dtypes: int64(1), object(5)
memory usage: 4.8+ KB
None
'''


# print(data2.describe())# gives me statistical info
'''
id
count  100.000000
mean    50.500000
std     29.011492
min      1.000000
25%     25.750000
50%     50.500000
75%     75.250000
max    100.000000
'''

# accessing first 5 names
df3 = pd.read_json('test_data/MOCK_DATA.json')
# print(df3['first_name'].head())
# print(df3.iloc[:5,1])
# print(df3.loc[:5,['first_name']])

# handling missing data
# print(df3.info())

# way 1 dropping the rows with na /null values
df4 = df3.dropna()
# print(df4.size,df3.size)

# way 2 filling na values with some static values
# print(df3.fillna(0).info()) # replacing missing values with 0
'''
Data columns (total 6 columns):
 #   Column      Non-Null Count  Dtype 
---  ------      --------------  ----- 
 0   id          100 non-null    int64 
 1   first_name  100 non-null    object
 2   last_name   100 non-null    object
 3   email       100 non-null    object
 4   gender      100 non-null    object
 5   phones      100 non-null    object
dtypes: int64(1), object(5)
'''

# removing duplicates
# print(df3.drop_duplicates().size)



# changing datatype of columns
# df3['id'] = df3['id'].astype(str)
# print(df3.info())


# filtering data
# print(df3[df3['phones']=='iPhone X']) # get the users having iPhone X

# sorting data
# print(df3.sort_values(by='phones',ascending=False).head())

# df3.dropna(inplace=True)
# # applying custom function to each element in dataframe / series
# df3['phones_length'] = df3['phones'].apply(len)
# print(df3['phones_length'].head())


data = pd.DataFrame({
    'Dept':['HR','Finance','IT','HR','Finance'],
    'Employee':['John','Kamlesh','Chattu','Kamlesh','Bhoot'],
    'Salary':[50000,60000,55000,67000,34000]
})
# grouping data
# print(data.groupby('Dept')['Salary'].max()) # returns maximum salary of each group
# print(data.groupby(['Dept','Employee'])['Salary'].max())

# performing multiple aggregate functions at same time
# print(data.groupby('Dept')['Salary'].agg(['count','min','max','sum']))
'''
         count    min    max     sum
Dept                                
Finance      2  34000  60000   94000
HR           2  50000  67000  117000
IT           1  55000  55000   55000
'''


data = pd.DataFrame(
    {
        'dates':['01-02.2024','23.02.2024','12.09.2026'],
        'values':[10,23,100],
        'time':['12:23','12:34:54','23:59:59']
    }
)

data['dates'] = pd.to_datetime(data['dates'])
data['time'] = pd.to_datetime(data['time'])
# print(data.info())
# print(data)
'''
 dates  values                time
0 2024-01-02      10 2024-08-19 12:23:00
1 2024-02-23      23 2024-08-19 12:34:54
2 2026-12-09     100 2024-08-19 23:59:59
'''
data.set_index('dates',inplace=True)
# print(data)
'''
            values                time
dates                                 
2024-01-02      10 2024-08-19 12:23:00
2024-02-23      23 2024-08-19 12:34:54
2026-12-09     100 2024-08-19 23:59:59
'''

# merging 2 different dataframes
df1 = pd.DataFrame({
    'name':['Kamlesh','Jaktap','Champa','Gopi','Billu'],
    'Gender':['male','female','male','alien',None]
})
df2 = pd.DataFrame({
    'values':[100,200,300,400,50],
    'is_adult':[False,True,True,False,True]
})
print(df1+df2)
'''
Gender  is_adult name  values
0    NaN       NaN  NaN     NaN
1    NaN       NaN  NaN     NaN
2    NaN       NaN  NaN     NaN
3    NaN       NaN  NaN     NaN
4    NaN       NaN  NaN     NaN
'''
print(pd.concat([df1,df2]))
'''
    name     Gender    values  is_adult
0  Kamlesh    male     NaN      NaN
1   Jaktap  female     NaN      NaN
2   Champa    male     NaN      NaN
3     Gopi   alien     NaN      NaN
4    Billu    None     NaN      NaN
0      NaN     NaN   100.0    False
1      NaN     NaN   200.0     True
2      NaN     NaN   300.0     True
3      NaN     NaN   400.0    False
4      NaN     NaN    50.0     True
'''
print(pd.concat([df1,df2],axis=0))