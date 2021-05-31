import numpy as np
import pandas as pd


# Read into dataframe
df = pd.read_csv("../Data/ATP.csv", encoding="cp1252")

# Remove unnecessary features (carpet, pre-Federer)
df = df.drop(df[df.surface == 'carpet'].index)
df['tourney_date'] = pd.to_datetime(df['tourney_date'], format='%Y%m%d')
df['year'] = df['tourney_date'].dt.year
df = df[(df['year'] >= 1998)]

# Convert names to strings
df['winner_name'] = df['winner_name'].astype('str') 
df['loser_name'] = df['loser_name'].astype('str') 

# Normalize features to per set (3/5 set matches -> Set by Set)
df['minutes'] = df['minutes']/df['best_of']
df['w_ace'] = df['w_ace']/df['best_of']
df['l_ace'] = df['l_ace']/df['best_of']
df['l_bpFaced'] = df['l_bpFaced']/df['best_of']
df['w_bpFaced'] = df['w_bpFaced']/df['best_of']
df['w_svpt'] = df['w_svpt']/df['best_of']
df['w_1stIn'] = df['w_1stIn']/df['best_of']
df['w_1stWon'] = df['w_1stWon']/ df['best_of']
df['w_2ndWon'] = df['w_2ndWon']/df['best_of']
df['w_SvGms'] = df['w_SvGms']/df['best_of']
df['w_bpSaved'] = df['w_bpSaved']/df['best_of']
df['l_svpt'] = df['w_svpt']/df['best_of']
df['l_1stIn'] = df['l_1stIn']/df['best_of']
df['l_1stWon'] = df['l_1stWon']/ df['best_of']
df['l_2ndWon'] = df['l_2ndWon']/df['best_of']
df['l_SvGms'] = df['l_SvGms']/df['best_of']
df['l_bpSaved'] = df['l_bpSaved']/df['best_of']

# Rename Columns
df = df.rename(columns={df.columns[16]: "minutes per set" })
df = df.rename(columns={df.columns[17]: "w_ace per set" })
df = df.rename(columns={df.columns[26]: "l_ace per set" })

# Convert other players (not Federer, Nadal and Djokovic) to 'Other'
df['winner_name'] = np.where(df['winner_name'].isin(['Roger Federer', 'Rafael Nadal', 'Novak Djokovic']),
                             df['winner_name'], 'Other')

df['loser_name'] = np.where(df['loser_name'].isin(['Roger Federer', 'Rafael Nadal', 'Novak Djokovic']),
                             df['loser_name'], 'Other')

#Output CSV file for analysis.
df.to_csv('../Data/ATPnormalized.csv', index=False)
