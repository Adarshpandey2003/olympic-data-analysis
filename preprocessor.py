import pandas as pd

def preprocess(df):
    # filtering for summer olympics
    df = df[df['Season'] == 'Summer']
    # set region as Team
    df['region'] = df['Team']
    # dropping duplicates
    df.drop_duplicates(inplace=True)
    # one hot encoding medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df