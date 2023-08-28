import pandas as pd


data = pd.read_csv('Gross National Income Per Capita.csv')




numeric_columns = [
    'HDI Rank (2021)',
    'Gross National Income Per Capita (1990)',
    'Gross National Income Per Capita (1991)',
    'Gross National Income Per Capita (1992)',
    'Gross National Income Per Capita (1993)',
    'Gross National Income Per Capita (1994)',
    'Gross National Income Per Capita (1995)',
    'Gross National Income Per Capita (1996)',
    'Gross National Income Per Capita (1997)',
    'Gross National Income Per Capita (1998)',
    'Gross National Income Per Capita (1999)',
    'Gross National Income Per Capita (2000)',
    'Gross National Income Per Capita (2001)',
    'Gross National Income Per Capita (2002)',
    'Gross National Income Per Capita (2003)',
    'Gross National Income Per Capita (2004)',
    'Gross National Income Per Capita (2005)',
    'Gross National Income Per Capita (2006)',
    'Gross National Income Per Capita (2007)',
    'Gross National Income Per Capita (2008)',
    'Gross National Income Per Capita (2009)',
    'Gross National Income Per Capita (2010)',
    'Gross National Income Per Capita (2011)',
    'Gross National Income Per Capita (2012)',
    'Gross National Income Per Capita (2013)',
    'Gross National Income Per Capita (2014)',
    'Gross National Income Per Capita (2015)',
    'Gross National Income Per Capita (2016)',
    'Gross National Income Per Capita (2017)',
    'Gross National Income Per Capita (2018)',
    'Gross National Income Per Capita (2019)',
    'Gross National Income Per Capita (2020)',
    'Gross National Income Per Capita (2021)'
]

data[numeric_columns] = data[numeric_columns].astype(float)

# Converter colunas categóricas para tipo category
categorical_columns = [
    'ISO3',
    'Country',
    'Continent',
    'Hemisphere',
    'Human Development Groups',
    'UNDP Developing Regions'
]

data[categorical_columns] = data[categorical_columns].astype('category')

# Preencher valores ausentes com zero
data[numeric_columns] = data[numeric_columns].fillna(0)


# Verificar os tipos de dados após a conversão
print(data.dtypes)

print(data.isnull().sum())

data.to_csv('GNI_per_capita_processed.csv', index=False)