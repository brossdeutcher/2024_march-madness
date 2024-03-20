import pandas as pd
import random

def getUpsetPercent(seed1, seed2):
    favoriteSeed = min(seed1, seed2)
    upsetSeed = max(seed1, seed2)

    df = pd.read_csv("upset-percents.csv", encoding='utf-16')
    matching_rows = df.loc[(df['favorite_seed'] == favoriteSeed) & (df['underdog_seed'] == upsetSeed), 'upset_percent']

    if not matching_rows.empty:
      if pd.isna(matching_rows.iloc[0]):
        return 27
      # print(f'rawVal: {matching_rows.iloc[0]} | seeds: {seed1}-{seed2}')
      return int(matching_rows.iloc[0].rstrip('%'))
    else:
      return 27

def playGame(seed1, seed2):
  favoriteSeed = min(seed1, seed2)
  underdogSeed = max(seed1, seed2)
  randNum = random.randint(1,100)
  upsetPct = getUpsetPercent(seed1, seed2)
  if randNum < upsetPct:
    return underdogSeed
  else:
    return favoriteSeed