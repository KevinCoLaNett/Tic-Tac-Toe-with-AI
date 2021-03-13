
document.querySelector(".tryAgain").addEventListener('click', () => window.location.reload());

let board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ];

const Items = document.querySelectorAll(".fill-div");
	for (const item of Items) {
	  item.addEventListener("click", () => mainFunction(item.id));
	}


function insertLetter(letter, pos){
  board[pos] = letter;
}

function spaceIsFree(pos){
  return board[pos] == ' ';
}

function isBoardFull(){
  let count = 0;
    for(let i=0; i<10; i++){
      if(board[i]==" "){
        count++;
      }
    }

  if(count>1){
    return false;
  }
  else{
    return true;
  }
}

function isWinner(board, letter){
  return (board[4] == letter && board[5] == letter && board[6] == letter) || 
  (board[1] == letter && board[2] == letter && board[3] == letter) || 
  (board[1] == letter && board[4] == letter && board[7] == letter) || 
  (board[2] == letter && board[5] == letter && board[8] == letter) ||  
  (board[3] == letter && board[6] == letter && board[9] == letter) || 
  (board[1] == letter && board[5] == letter && board[9] == letter) || 
  (board[3] == letter && board[5] == letter && board[7] == letter) ||
  (board[7] == letter && board[8] == letter && board[9] == letter);
}

function playerMove(move){
  if(spaceIsFree(move)){
    insertLetter('X', move);
    document.querySelector("[id='"+ move +"']").innerHTML = '<div class="blue-text"> X </div>';
    document.querySelector("#message").innerHTML = " ";
    console.log(board);

    if(!isWinner(board, "X"))
    {
      let move = compMove();
      if(move != 0)
      {
        insertLetter('O', move);
        document.querySelector("[id='"+ move +"']").innerHTML = '<div class="red-text"> O </div>';
        document.querySelector("#message").innerHTML = `Computer placed an 'O' in position ${move}`;
        if(isWinner(board, "O"))
        {
          document.querySelector("#message").innerHTML = `<div class="red-text">Sorry, O's won this time! </div>`;
        }
        console.log(board);
      }
    }
    else
    {
      document.querySelector("#message").innerHTML = '<div class="blue-text">You Won! Congratulation! </div>';
    }
  }
  else{
    document.querySelector("#message").innerHTML = "Sorry, this space is occupied!";
  }

}

function compMove(){
  let possibleMoves = [];
  let move = 0;
  let letter = ['O', 'X'];
  //getting all the possible moves
  for(let i=1; i<10; i++){
    if(board[i]==" "){
      possibleMoves.push(i);
    }
  }

  for(let a=0; a<letter.length; a++)
  {
    for(let b=0; b<possibleMoves.length; b++)
    {
      let boardCopy = [...board];
      boardCopy[possibleMoves[b]] = letter[a];
      if(isWinner(boardCopy, letter[a]))
      {
        move = possibleMoves[b];
        return move;
      } 
    }
  }

  cornersOpen = [];
  for(let c=0; c<possibleMoves.length; c++)
  {
    if(possibleMoves[c] == 1 || possibleMoves[c] == 3 || possibleMoves[c] == 7 || possibleMoves[c] == 9)
    {
      cornersOpen.push(possibleMoves[c]);
    }
  }

  if(cornersOpen.length > 0)
  {
    move = cornersOpen[Math.floor(Math.random() * cornersOpen.length)];
    return move;
  }

  edgesOpen = [];
  for(let d=0; d<possibleMoves.length; d++)
  {
    if(possibleMoves[d] == 2 || possibleMoves[d] == 4 || possibleMoves[d] == 6 | possibleMoves[d] == 8)
    {
      edgesOpen.push(possibleMoves[d]);
    }
  }

  if(edgesOpen.length > 0)
  {
    move = edgesOpen[Math.floor(Math.random() * edgesOpen.length)];
    return move;
  }
  
  for(let e=0; e<possibleMoves.length; e++)
  {
    if(possibleMoves[d] == 5)
    {
      move = 5;
    }
  }

  
  return move;

}

function mainFunction(move){
  if(!isWinner(board, "O"))
  {
    playerMove(move);  
  }

  if (isBoardFull())
  {
    document.querySelector("#message").innerHTML = `<div class="green-text">Tie Game! </div>`;
  }
}

