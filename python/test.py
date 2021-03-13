isBoardFull = True

while not(isBoardFull):
  print('not full')
  isBoardFull = True
  
possible = [1, 3, 4, 5]
#for i in possible:
#  print(f'{i} | ')
  
#for i in range(len(possible)):
#  print(i)


board = [' ' for x in range(10)]
possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]

for letter in ['O', 'X']:
  for i in possibleMoves:
    board[i] = letter
    
for i in board:
  print(i)  


cornersOpen = []
for i in possibleMoves:
  if i in [1, 3, 7, 9]:
    cornersOpen.append(i)
    
for i in cornersOpen:
  print(i) 
  
#move = input('Please select a position to place an \'X\' (1-9): ')
try:
  move = int(move)
  print(move)
except:
  print('error')

board = [' ' for x in range(10)]  
print(board)







a=0
Moves = [2, 4, 5]      
for letter in ['O', 'X']:
    for i in Moves:
      boardCopy = board[:]
      boardCopy[i] = letter
      print(i)