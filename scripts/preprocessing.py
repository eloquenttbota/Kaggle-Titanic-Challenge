import pandas as pd

def extract_group_survival(df):
    """Извлекает признак выживаемости группы (семья/билет)."""
    df['Last_Name'] = df['Name'].apply(lambda x: x.split(',')[0])
    DEFAULT_SURVIVAL_VALUE = 0.5
    df['Group_Survival'] = DEFAULT_SURVIVAL_VALUE

    for _, grp_df in df.groupby(['Last_Name', 'Fare']):
        if len(grp_df) > 1:
            for ind, row in grp_df.iterrows():
                smax = grp_df.drop(ind)['Survived'].max()
                smin = grp_df.drop(ind)['Survived'].min()
                if smax == 1.0:
                    df.loc[ind, 'Group_Survival'] = 1
                elif smin == 0.0:
                    df.loc[ind, 'Group_Survival'] = 0

    for _, grp_df in df.groupby('Ticket'):
        if len(grp_df) > 1:
            for ind, row in grp_df.iterrows():
                if (df.loc[ind, 'Group_Survival'] == 0.5):
                    smax = grp_df.drop(ind)['Survived'].max()
                    smin = grp_df.drop(ind)['Survived'].min()
                    if smax == 1.0:
                        df.loc[ind, 'Group_Survival'] = 1
                    elif smin == 0.0:
                        df.loc[ind, 'Group_Survival'] = 0
    return df

def clean_data(df):
    """Базовая очистка: заполнение Fare и кодирование Sex."""
    df['Fare'] = df['Fare'].fillna(df['Fare'].median())
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    return df