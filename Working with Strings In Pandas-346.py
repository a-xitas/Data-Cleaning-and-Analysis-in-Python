## 1. Introduction ##

import pandas as pd

world_dev = pd.read_csv("World_dev.csv")
col_renaming = {'SourceOfMostRecentIncomeAndExpenditureData': 'IESurvey'}

world_dev.rename(mapper=col_renaming, inplace=True, axis=1)

merged = pd.merge(left=happiness2015, right=world_dev,
                  how='left', left_on=happiness2015['Country'],
                  right_on=world_dev['ShortName'])

## 2. Using Apply to Transform Strings ##

def extract_last_word(element):
    element=str(element)
    element=element.split()[-1]
    return element

merged['Currency Apply'] = merged['CurrencyUnit'].apply(extract_last_word)

merged['Currency Apply'].head()


## 3. Vectorized String Methods Overview ##

merged['Currency Vectorized'] = merged['CurrencyUnit'].str.split().str.get(-1)

merged['Currency Vectorized'].head()

## 4. Exploring Missing Values with Vectorized String Methods ##

lengths = merged['CurrencyUnit'].str.len()
value_counts = lengths.value_counts(dropna=False)

## 5. Finding Specific Words in Strings ##

#os parenteses rectos [] no Nn é para dizer que tanto procuramos por National como national accounts:
pattern = r"[Nn]ational accounts"

national_accounts = merged['SpecialNotes'].str.contains(pat=pattern)

national_accounts.head()
national_accounts.value_counts(dropna=False)

## 6. Finding Specific Words in Strings Continued ##

pattern = r"[Nn]ational accounts"

national_accounts = merged['SpecialNotes'].str.contains(pat=pattern, na=False)

merged_national_accounts = merged[national_accounts]

merged_national_accounts.head()

## 7. Extracting Substrings from a Series ##

pattern =r"([1-2][0-9]{3})"
pattern1 = r"[Ee]uro"

years = merged['SpecialNotes'].str.extract(pat=pattern)
currencies = merged['CurrencyUnit'].str.contains(pat=pattern1, na=False)

merged[currencies].head()

## 8. Extracting Substrings from a Series Continued ##

pattern = r"([1-2][0-9]{3})"

years = merged['SpecialNotes'].str.extract(pat=pattern, expand=True)


## 9. Extracting All Matches of a Pattern from a Series ##

pattern = r"(?P<Years>[1-2][0-9]{3})"

years = merged['IESurvey'].str.extractall(pat=pattern)
value_counts = years['Years'].value_counts()
print(value_counts)

#merged = merged.set_index('Region')
#merged_ext = merged['SpecialNotes'].str.extractall(pat=pattern)


## 10. Extracting More Than One Group of Patterns from a Series ##

# desta vez Nós criamos 3 grupos de captura, o grupo First_Year, o grupo /, e o grupo Second_Year. Isto para podermos capturar linhas que contenham info de datas no formato 2010/11. Colocamos ainda um ponto de interrogação a seguir a estes grupos (?) para que a Nossa regular expression seja opcional para estes grupos. Se encontrar estes grupos, saca-os, se não os encontrar, saca apenas o 1º. O facto de não ter os outros 2 grupos n invalida que não possa sacar o 1º grupo da Nossa regex!
pattern = r"(?P<First_Year>[1-2][0-9]{3})/?(?P<Second_Year>[0-9]{2})?"

years = merged['IESurvey'].str.extractall(pattern)
first_two_year = years['First_Year'].str.slice(stop=2)
years['Second_Year'] = first_two_year + years['Second_Year']

years.sort_values('Second_Year')

## 11. Challenge: Clean a String Column, Aggregate the Data, and Plot the Results ##

incomes = merged['IncomeGroup']

incomes = incomes.str.upper()
incomes = incomes.str.strip()
#LOW:
incomes = incomes.str.replace(pat='LOW INCOME', repl='LOW')
#ALL
incomes = incomes.str.replace(pat='INCOME', repl='')
incomes = incomes.str.replace(pat=' :', repl='')
incomes = incomes.str.strip()
n_incomes = incomes.value_counts()

#OECD:
#pattern = r"(OECD)"
#OECD = income.str.contains(pattern, na=False)
#income_OECD = income[OECD]
#income_OECD0 = income_OECD.str.split().str.get(0)
#income_OECD1 = income_OECD.str.split().str.get(-1)
#income_OECD_final = income_OECD0+' '+income_OECD1
#income.str.replace(pat=pattern, repl=income_OECD_final)
#n_income = income.value_counts()

pv_incomes = merged.pivot_table(values='Happiness Score', index=incomes)

pv_incomes.plot(kind='bar', rot=30, ylim=(0,10))
plt.show()
