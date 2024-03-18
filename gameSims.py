import pandas as pd
import random

def getUpsetPercent(seed1, seed2):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv("upset-percents.csv", encoding='utf-16')
    favoriteSeed = min(seed1, seed2)
    upsetSeed = max(seed1, seed2)
    # Filter rows where the match_column matches the specified match_value
    matching_rows = df.loc[(df['favorite_seed'] == favoriteSeed) & (df['underdog_seed'] == upsetSeed), 'upset_percent']
    # Return values from the return_column for matching rows
    if not matching_rows.empty:
      return matching_rows.iloc[0]
    else:
      return '27%'  # or any default value you prefer

print(getUpsetPercent(3,2))
print(getUpsetPercent(1,6))
print(getUpsetPercent(10,7))
print(getUpsetPercent(6,4))

def playGame(seed1, seed2):
  favoriteSeed = min(seed1, seed2)
  underdogSeed = max(seed1, seed2)
  randNum = random.randint(1,100)
  upsetPct = 27
  if randNum < upsetPct:
    return underdogSeed
  else:
    return favoriteSeed
  
playGame(1,2)