import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.options.mode.chained_assignment = None


def extract_country(path, continent):
    my_col = [0, 1, 2, 4]
    df = pd.read_csv(path, usecols=my_col)
    return df


def etl_catagories():
    df = pd.read_csv(r'data\catagory.csv')
    df.insert(0, "category_id", [*range(len(df))])
    df.rename(columns={'Categories': 'Category'}, inplace=True)
    df = remove_extra(df)
    df = trim_rows(df)
    return df


def etl_countries():
    africa = extract_country(r'data\asia.csv',  "Africa")
    asia = extract_country(r'data\asia.csv',  "Asia")
    n_america = extract_country(r'data\n_america.csv', "North America")
    s_america = extract_country(r'data\s_america.csv', "South America")
    europe = extract_country(r'data\europe.csv',  "Europe")
    oceania = extract_country(r'data\oceania.csv',  "Oceania")

    countries_list = [africa, asia, n_america, s_america, europe, oceania]
    continents = ["Africa", "Asia", "North_America", "South_America", "Europe", "Oceania"]

    countries = add_continent(countries_list, continents)
    countries = remove_extra(countries)
    countries.rename(columns={'Country ': 'Country'}, inplace=True)
    countries.rename(columns={'Year Founded': 'year_founded'}, inplace=True)
    countries["year_founded"] = pd.to_numeric(countries["year_founded"])
    countries = countries.drop_duplicates(subset=['Country'])
    countries = trim_rows(countries)
    return countries


def add_continent(data_frames, continents):
    data = pd.DataFrame()
    for i, df in zip(range(len(data_frames)), data_frames):
        df["continent"] = [continents[i] for x in range(len(df))]
        data = data.append(df)
    return data


def remove_extra(df):
    df = df[~df.Category.isin(['No data', 'No Data'])]
    df["Category"] = df.Category.str.replace(r"\([^()]*\)", '')
    return df

def trim_rows(df):
    df["Category"] = df["Category"].str.strip()
    if len(df.columns) > 2 :
        df["Business"] = df["Business"].str.strip()
        df['Country'] = df['Country'].str.strip()
    return df

def add_keys(df1, df2):
    df1.insert(0, "country_id", [*range(len(df1))])
    df1 = df1.merge(df2, on='Category', how='left')
    return df1


fact = etl_countries()
categories = etl_catagories()
fact = add_keys(fact, categories)
countries = fact[["country_id","Country","continent"]]
business = fact[["Business","year_founded","country_id","category_id"]]

business.to_csv('business.csv', sep='\t', encoding='utf-8')
countries.to_csv('countries.csv', sep='\t', encoding='utf-8')
categories.to_csv('categories.csv', sep='\t', encoding='utf-8')
