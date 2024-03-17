import random

def playGame(seed1, seed2):
  favoriteSeed = min(seed1, seed2)
  underdogSeed = max(seed1, seed2)
  randNum = random.randint(1,100)
  upsetPct = 27
  if randNum < upsetPct:
    return underdogSeed
  else:
    return favoriteSeed
