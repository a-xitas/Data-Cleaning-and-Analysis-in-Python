## 1. Introduction ##

shape_2015 = happiness2015.shape
shape_2016 = happiness2016.shape
shape_2017 = happiness2017.shape

## 2. Identifying Missing Values ##

missing_2016 = happiness2016.isnull().sum()
missing_2017 = happiness2017.isnull().sum()

missing_2015_quais = happiness2015[happiness2015['Happiness Score'].isnull()]
missing_2016_quais = happiness2016[happiness2016['Happiness Score'].isnull()]
missing_2017_quais = happiness2017[happiness2017['Happiness.Score'].isnull()]



## 3. Correcting Data Cleaning Errors that Result in Missing Values ##

happiness2017.columns = happiness2017.columns.str.replace('.', ' ').str.replace('\s+', ' ').str.strip().str.upper()
#limpar as cols do happiness2015:
#print(happiness2015.columns)
happiness2015.columns = happiness2015.columns.str.replace(')', '').str.replace('(','').str.strip().str.upper()
#print(happiness2015.columns)
#limpar as cols do happiness2016:
#print(happiness2016.columns)
happiness2016.columns = happiness2016.columns.str.replace('(','').str.replace(')','').str.strip().str.upper()
#print(happiness2016.columns)

#Criar um novo DF, juntando os 3(happiness2015+happiness2016+happiness2017):
combined = pd.concat([happiness2015, happiness2016, happiness2017], ignore_index=True)
#checar se existem NaN's no novo DF (combined):
missing = combined.isnull().sum()

## 4. Visualizing Missing Data ##

import seaborn as sns

heat_map_combined = combined.set_index('YEAR')
sns.heatmap(heat_map_combined.isnull(), cbar=False, yticklabels=20)
plt.show()

regions_20177 = combined[combined['YEAR']==2017][['REGION']]
#OU:
a=combined[combined['YEAR']==2017]
regions_2017 = a['REGION']

missing = regions_2017.isnull().sum()




## 5. Using Data From Additional Sources to Fill in Missing Values ##

combined = pd.merge(left=combined, right=regions, how='left', on='COUNTRY').drop('REGION_x', axis=1)

missing = combined.isnull().sum()

## 6. Identifying Duplicates Values ##

#Standardizar a col COUNTRY, para que todos os países estejam em uppercase, e n uns em upper e outros em camelcase ou em low. Fazemos isto pq o método duplicate ñ detecta estas nuances:
combined['COUNTRY'] = combined['COUNTRY'].str.upper()
#Checar se temos linhas duplicadas no Nosso DF, mas com incidência nas cols COUNTRY E ANO, isto pq para cada ano só poderemos ter um país apenas, e n 2 países iguais:
dups = combined.duplicated(['COUNTRY', 'YEAR'])
print(combined[dups])


## 7. Correcting Duplicates Values ##

combined['COUNTRY'] = combined['COUNTRY'].str.upper()

combined.drop_duplicates(['YEAR', 'COUNTRY'], inplace=True)

dups = combined[combined.duplicated(['YEAR', 'COUNTRY'])]

## 8. Handle Missing Values by Dropping Columns ##

columns_to_drop = ['LOWER CONFIDENCE INTERVAL', 'STANDARD ERROR', 'UPPER CONFIDENCE INTERVAL', 'WHISKER HIGH', 'WHISKER LOW']

combined.isnull().sum()

combined = combined.drop(columns_to_drop, axis=1)

missing = combined.isnull().sum()

## 9. Handle Missing Values by Dropping Columns Continued ##

non_NaNs = combined.notnull().sum().sort_values()

combined.dropna(thresh=159, axis=1, inplace=True)

missing = combined.isnull().sum()

## 11. Handling Missing Values with Imputation ##

happiness_mean = combined['HAPPINESS SCORE'].mean()
print(happiness_mean)

sorted = combined.set_index('REGION').sort_values(['HAPPINESS SCORE'])
sns.heatmap(sorted.isnull(), cbar=False, yticklabels=20)


combined['HAPPINESS SCORE UPDATED'] = combined['HAPPINESS SCORE'].fillna(happiness_mean)
happiness_mean_updated = combined['HAPPINESS SCORE UPDATED'].mean()
print(happiness_mean_updated)

## 12. Dropping Rows ##

combined = combined.dropna()
missing = combined.isnull().sum()