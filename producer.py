import pandas as pd
from sklearn.model_selection import train_test_split
import time

from services.kafka import kafka_producer


def rename_columns_15_16(df, year):
    df.rename(columns={
        'Happiness Score': 'happiness_score',
        'Happiness Rank': 'rank',
        'Economy (GDP per Capita)': 'gdp_per_capita',
        'Family': 'social_support',
        'Health (Life Expectancy)': 'life_expectancy',
        'Trust (Government Corruption)': 'corruption'
    }, inplace=True)
    df.columns = map(str.lower, df.columns)
    df['year'] = year
    return df[['country', 'rank', 'happiness_score', 'gdp_per_capita', 'social_support', 'freedom', 'life_expectancy', 'generosity', 'corruption', 'year']]  

def rename_columns_17(df, year):
    df.rename(columns={
        'Happiness.Score': 'happiness_score',
        'Happiness.Rank': 'rank',
        'Economy..GDP.per.Capita.': 'gdp_per_capita',
        'Family': 'social_support',
        'Health..Life.Expectancy.': 'life_expectancy',
        'Trust..Government.Corruption.': 'corruption',
    }, inplace=True)
    df.columns = map(str.lower, df.columns)
    df['year'] = year
    return df[['country', 'rank', 'happiness_score', 'gdp_per_capita', 'social_support', 'freedom', 'life_expectancy', 'generosity', 'corruption', 'year']]

def rename_columns_18_19(df, year):
    df.rename(columns={
        'Overall rank': 'rank',
        'Country or region': 'country',
        'Score': 'happiness_score',
        'GDP per capita': 'gdp_per_capita',
        'Social support': 'social_support',
        'Healthy life expectancy': 'life_expectancy',
        'Perceptions of corruption': 'corruption',
        'Freedom to make life choices': 'freedom',
        'Generosity': 'generosity'
    }, inplace=True)
    df['year'] = year
    return df

def etl_process():
    happiness_2015 = pd.read_csv("./data/2015.csv")
    happiness_2016 = pd.read_csv("./data/2016.csv")
    happiness_2017 = pd.read_csv("./data/2017.csv")
    happiness_2018 = pd.read_csv("./data/2018.csv")
    happiness_2019 = pd.read_csv("./data/2019.csv")

    happiness_2015 = rename_columns_15_16(happiness_2015, 2015)
    happiness_2016 = rename_columns_15_16(happiness_2016, 2016)
    happiness_2017 = rename_columns_17(happiness_2017, 2017)
    happiness_2018 = rename_columns_18_19(happiness_2018, 2018)
    happiness_2019 = rename_columns_18_19(happiness_2019, 2019)
    
    dataframes = [happiness_2015, happiness_2016, happiness_2017, happiness_2018, happiness_2019]
    happiness_df = pd.concat(dataframes, ignore_index=True)
    happiness_df.dropna(inplace=True)
    happiness_df.drop(columns=["rank","year","generosity","corruption"], inplace=True)
    return happiness_df
    
def selected_features(df):
    selected_features = [
        "gdp_per_capita",
        "social_support",
        "freedom",
        "life_expectancy",
        "happiness_score",
    ]
    happiness_analysis = df[selected_features]
    y = happiness_analysis["happiness_score"]
    X = happiness_analysis.drop(columns=["happiness_score"])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
    return df.loc[y_test.index]
    
if __name__ == "__main__":
    happiness_df = etl_process()
    happiness_df = selected_features(happiness_df)
    for index, row in happiness_df.iterrows():
        kafka_producer(row)
        # time.sleep(1)