import csplot
from time import sleep
import sys

class Life():

def createOneRow( n ):
  """ returns rows of n zeros...ï¿½ You might use
  this as the INNER loop in createBoard """
  R = []
  for col in range(n):
    R += [0]
  return R

def createBoard(i, j ):
  [ [0,0,0], [0,0,0], [0,0,0] ]
