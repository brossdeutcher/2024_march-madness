import gameSims

class BracketNode:
  def __init__(self, team=None, seed=None, round=0, region=0):
    self.team = team
    self.seed = seed
    self.round = round
    self.region = region
    self.left = None
    self.right = None

def createBracket():
  root = BracketNode(round=6)
  firstRoundSeeds = [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15, 1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15, 1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15, 1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]
  regions = [1,2,3,4]
  def generateRound(node, firstRoundSeeds, regions):
    if node.round > 0:
      region1 = node.region
      region2 = node.region
      if node.round == 5:
        region1 = regions.pop(0)
        region2 = regions.pop(0)
      curSeed1 = None
      curSeed2 = None
      if node.round == 1:
        curSeed1 = firstRoundSeeds.pop(0)
        curSeed2 = firstRoundSeeds.pop(0)
      node.left = BracketNode (region=region1, seed=curSeed1, round=node.round-1)
      node.right = BracketNode(region=region2, seed=curSeed2, round=node.round-1)
      generateRound(node.left, firstRoundSeeds, regions)
      generateRound(node.right, firstRoundSeeds, regions)
  generateRound(root, firstRoundSeeds, regions)
  return root

def populateBracket(node):
  if node is not None:
    populateBracket(node.left)
    populateBracket(node.right)
    if node.round > 0:
      node.seed = gameSims.playGame(node.left.seed, node.right.seed)
      print(f"round: {node.round} | region: {node.region} | matchup: {node.left.seed}-{node.right.seed} | winning seed: {node.seed}")