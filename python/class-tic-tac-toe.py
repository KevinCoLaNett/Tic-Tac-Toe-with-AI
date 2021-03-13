
class TicTacToe:
  def insertLetter(self, board, letter, pos) :
    board[pos] = letter

  def spaceIsFree(self, board, pos) :
    return board[pos] == ' '
  
  def printBoard(self, board) :
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
  
  def isWinner(self, board, letter) :
    return (board[7] == letter and board[8] == letter and board[9] == letter) or (board[4] == letter and board[5] == letter and board[6] == letter) or (board[1] == letter and board[2] == letter and board[3] == letter) or (board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[8] == letter) or  (board[3] == letter and board[6] == letter and board[9] == letter) or (board[1] == letter and board[5] == letter and board[9] == letter) or (board[3] == letter and board[5] == letter and board[7] == letter)
  
  def playerMove(self, board) :
    run = True
    while run:
      move = input('Please select a position to place an \'X\' (1-9): ')
      try:
        move = int(move)
        if move > 0 and move < 10:
          if self.spaceIsFree(board, move):
            run = False
            self.insertLetter(board, 'X', move)
          else:
            print('Sorry, this space is occupied!')
        else:
          print("Please type a number within the range!")
      except:
        print('Please type a number!')
        
  def compMove(self, board) :
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    
    for letter in ['O', 'X']:
      for i in possibleMoves:
        boardCopy = board[:]
        boardCopy[i] = letter
        if self.isWinner(boardCopy, letter):
          move = i
          return move
        
    cornersOpen = []
    for i in possibleMoves:
      if i in [1,3,7,9]:
        cornersOpen.append(i)
    
    if len(cornersOpen) > 0:
      move = self.selectRandom(cornersOpen)
      return move
    
    if 5 in possibleMoves:
      move = 5
      return move
    
    edgesOpen = []
    for i in possibleMoves:
      if i in [2,4,6,8]:
        edgesOpen.append(i)
    
    if len(edgesOpen) > 0:
      move = self.selectRandom(edgesOpen)
      
    return move
  
  def selectRandom(self, li) :
    import random
    length = len(li)
    r = random.randrange(0, length)
    return li[r]

  def isBoardFull(self, board) :
    if board.count(' ') > 1 :
      return False
    else:
      return True
    
  def main(self, board) :
    print('Welcome to Tic Tac Toe!')
    self.printBoard(board)
    
    while not(self.isBoardFull(board)):
      if not(self.isWinner(board, 'O')):
        self.playerMove(board)
        self.printBoard(board)
      else:
        print('Sorry, O\'s won this time!')
        break
      
      if not(self.isWinner(board, 'X')):
        move = self.compMove(board)
        if not(move == 0):
          self.insertLetter(board, 'O', move)
          print('Computer placed and \'O\' in position', move, ' :')
          self.printBoard(board)
      else:
        print('X\'s won this time! Good Job!')
        break
    
    if self.isBoardFull(board):
      print('Tie Game!')
      
  def tryAgain(self) :
    while True:
      ans = input('Try Again? (y/n): ')
      if ans == 'n' or ans == 'N' or ans == 'y' or ans == 'Y':
        if ans == 'n' or ans == 'N':
          return False
        else:
          return True
      else:
        print('Please type \'y\' or \'n\' only!')
        
  def play(self):
    ans = True
    while ans:
      board = [' ' for x in range(10)]
      self.main(board)
      ans = self.tryAgain()
        
        
game1 = TicTacToe()
game1.play()
