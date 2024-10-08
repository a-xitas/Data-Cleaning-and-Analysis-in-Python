## 1. Introduction ##

import pandas as pd
happiness2015 = pd.read_csv("World_Happiness_2015.csv")
happiness2016 = pd.read_csv('World_Happiness_2016.csv')
happiness2017 = pd.read_csv('World_Happiness_2017.csv')

happiness2015['Year'] = 2015
happiness2016['Year'] = 2016
happiness2017['Year'] = 2017


## 2. Combining Dataframes with the Concat Function ##

head_2015 = happiness2015[['Country','Happiness Score', 'Year']].head(3)
head_2016 = happiness2016[['Country','Happiness Score', 'Year']].head(3)

concat_axis0 = pd.concat([head_2015, head_2016], axis=0)
concat_axis1 = pd.concat([head_2015, head_2016], axis=1)

question1 = concat_axis0.shape[0]
question2 = concat_axis1.shape[0]


## 3. Combining Dataframes with the Concat Function Continued ##

head_2015 = happiness2015[['Year','Country','Happiness Score', 'Standard Error']].head(4)
head_2016 = happiness2016[['Country','Happiness Score', 'Year']].head(3)

concat_axis0 = pd.concat([head_2015, head_2016], axis=0)
rows = concat_axis0.shape[0]
columns = concat_axis0.shape[1]

concat_axis1 = pd.concat([head_2015, head_2016], axis=1)


## 4. Combining Dataframes with Different Shapes Using the Concat Function ##

head_2015 = happiness2015[['Year','Country','Happiness Score', 'Standard Error']].head(4)
head_2016 = happiness2016[['Country','Happiness Score', 'Year']].head(3)

concat_update_index = pd.concat([head_2015, head_2016], axis=0, ignore_index=True)

concat_update_index_false = pd.concat([head_2015, head_2016], axis=0, ignore_index=False)

## 5. Joining Dataframes with the Merge Function ##

three_2015 = happiness2015[['Country','Happiness Rank','Year']].iloc[2:5]
three_2016 = happiness2016[['Country','Happiness Rank','Year']].iloc[2:5]

merged = pd.merge(left=three_2015, right=three_2016, on='Country')

## 6. Joining on Columns with the Merge Function ##

three_2015 = happiness2015[['Country','Happiness Rank','Year']].iloc[2:5]
three_2016 = happiness2016[['Country','Happiness Rank','Year']].iloc[2:5]

merged_left = pd.merge(left=three_2015, right=three_2016, on='Country', how='left')

merged_left_updated = pd.merge(left=three_2016, right=three_2015, on='Country', how='left')

## 7. Left Joins with the Merge Function ##

three_2015 = happiness2015[['Country','Happiness Rank','Year']].iloc[2:5]
three_2016 = happiness2016[['Country','Happiness Rank','Year']].iloc[2:5]
merged_suffixes = pd.merge(left=three_2015, right=three_2016, how='left', on='Country', suffixes=('_2015', '_2016'))

merged_updated = pd.merge(left=three_2016, right=three_2015, how = 'left', on='Country')

merged_updated_suffixes = pd.merge(left=three_2016, right=three_2015, how = 'left', on='Country', suffixes=('_2016','_2015'))
                          

## 8. Join on Index with the Merge Function ##

import pandas as pd

four_2015 = happiness2015[['Country','Happiness Rank','Year']].iloc[2:6]
three_2016 = happiness2016[['Country','Happiness Rank','Year']].iloc[2:5]

merge_index_left = pd.merge(left = four_2015, right = three_2016, left_index = True, right_index = True, suffixes = ('_2015','_2016'), how='left')

rows = 4
columns = 6

merge_index_right = pd.merge(left=four_2015, right=three_2016, left_index=True, right_index=True, how='right', suffixes=('_2015', '_2016'))

## 9. Challenge: Combine Data and Create a Visualization ##

happiness2017.rename(columns={'Happiness.Score': 'Happiness Score'}, inplace=True)

combined = pd.concat([happiness2015, happiness2016, happiness2017], axis=0, ignore_index=False) 

pivot_table_combined = pd.pivot_table(combined, values='Happiness Score', index='Year', aggfunc='mean')

pivot_table_combined.plot(kind='barh', title='Mean Happiness Scores by Year', xlim=(0,10)) 
plt.show()