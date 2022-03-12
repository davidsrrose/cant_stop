# runs multiple games which attempt a "perfect game"
# aka winning on the first roll capturing 3 numbers aka what chuck did
# gathers and reports data about those simulated games

# inputs:

# outputs:

# notes on improvements and additions to function
# get the p(winning on first roll)
# get the p(winning on the first roll, with dad's #s)
# get the p(winning on the first roll)
# difficulty of first roll win probability
    #is that influened by the "brain" for the game aka decision making engine 

#-------------------------------------------------------------------------------
game_looper <- function(n_simulations = 100)
  # initialize variables
  # dataframe for stats/numbers to record about the simulation












      wins <- as.integer(0)
    #count of games to throw out because they did not start with a 4,7,9 (for chuck's perfect game)
      throws <- as.integer(0)
    #goals vector of our goals
      goals <- as.integer(c(num1,num2,num3))
    #columns captured
      captured <- as.integer(0)
    #exit variable for each game simulated
      done <- as.logical(FALSE)
    #return matrix - the final output of probability we want to see
      returnmatrix <- matrix(0,nrow = 4, ncol = 1)
      rownames(returnmatrix) <- c("Games Simulated: ","Wins: ","Throws: ","p(Win): ")
      colnames(returnmatrix) <- c("")

  #loop game attempts (n game attempts!)
  for (i in 1:n){
      #inialize/restart variables that renew each game
        #reset exit variable for each game 
          done = FALSE
        #reset board progress
          board[2,] <- c(0,0,0,0,0,0,0,0,0,0,0)
          
    #simulate a game - each while loop is 1 game attempt
    while (done == FALSE){
      #reset "captured" variable
        captured = 0
      #reset advancement variable
        advanced = FALSE
  
      #roll and choose the 2 sums we want to pick for that roll
      sums <- rollpicker(chuckbrain,summer(roller()),board,goals)

      #advance the board (only if its on a goal though, only if it hasnt been captured)
            for (j in 1:2){
              #if the sum chosen is one of our goals & the sum chosen is not already captured
              if ((sums[j] %in% goals) & (board[1,sums[j]-1] != board[2,sums[j]-1])){
                board[2,sums[j]-1] = board[2,sums[j]-1] + 1
                #variable for whether we advanced
                advanced = TRUE
              }
            }
              #if we do not advance any numbers up the board, then we bust  
                if(advanced == FALSE){
                  done = TRUE
                }
          #check if board to see if we won, busted
            #win - check all goals, if we got all 3, we win
              for (j in 1:11){
                if (board[1,j] == board[2,j]){
                  captured = captured + 1
                  }
                }
                if (captured == 3){
                  wins = wins + 1
                  done = TRUE
                  }
    #count games to throw out - the game did not organically start with a chuck combo (4,7,9)
   #print("WHILE LOOP (roll the dice)")
   #print(sums)
    #I dont know
      #random
      #hightest probability of being rolled again?
      #go for numbers 
   #print(board)
  }
}
  #Fill up the return matrix
    #games
      returnmatrix[1] = n
    #of wins      
      returnmatrix[2] = wins
    #games thrown out
      returnmatrix[3] = throws
    #win percentage
      returnmatrix[4] = wins/n
    #avg rolls/game
      #use this + another script to verify that the model is working correctly?
    #total rolls
    #rolls distribution
      
 return(returnmatrix)
}