dealcards <- function(players,pack,N_cards){
  
  hands <- array(0, dim=c(players,52))
  
  dum <- sample(pack,52,replace=FALSE)
  
  for (p in 1:players){
    
    hands[p,1:N_cards] <- dum[(N_cards*(p-1)+1):(N_cards*(p-1)+1+N_cards-1)]
    
  }
  
  return(hands)}

pickcards <- function(players,card_players,hands){
  
  cards <- array(0,dim=c(players,1))
  
  for (k in card_players){
    
    cards[k,1] <- sample(hands[k,hands[k,]!=0],1)
    
  }
  
  return(cards)}

updatehand <- function(hands,cards,players){
  
  newhands <- array(0, dim=c(players,52))
  
  newhands <- hands
  
  for (k in 1:players){
    
    newhands[k,which(newhands[k,] == cards[k,1])[1]] <- 0
    
    newhands[k,] <- sort(newhands[k,],decreasing=TRUE)
    
  }
  
  return(newhands)}

selectmax <- function(cards){
  
  winners <- which(cards == max(cards))
  
  return(winners)}

playhidden <- function(players,hands){return(side_pile)}


wincards <- function(winner,pile,side_pile,hands,players){

  newhands <- array(0, dim=c(players,52))
  
  newhands <- hands
  
  num_cards <- length(hands[winner,][hands[winner,]!=0])
  
  newhands[winner,(num_cards+1):(num_cards+length(pile[pile!=0]))] <- pile[1:length(pile[pile!=0])]
  
  num_cards <- length(newhands[winner,][newhands[winner,]!=0])
  
  if (length(side_pile[side_pile!=0]) > 1){
    
    newhands[winner,(num_cards+1):(num_cards+length(side_pile[side_pile!=0]))] <- side_pile[1:length(side_pile[side_pile!=0])]
    
    print("Checking newhands")
    
    print(newhands)
    
  }
  
  return(newhands)}

still_play <- function(hands){
  
  A <- sum(hands[1,]) 
  B <- sum(hands[2,])
  C <- sum(hands[3,])
  
  if (A > 0 && B > 0 || A > 0 && C > 0 || B > 0 && C > 0){
    
    result <- TRUE
    
  } else {
    
    result <- FALSE
    
  }
  
  return(result)}

iterations = 20

for (i in 1:iterations) { #for loop 1
  
  pack <- rep(seq(1,13),4)
  
  players <- 3
  
  N_cards <- as.integer(52/players)
  
  # Define the pile
  
  pile <- c(rep(0,52))
  
  side_pile <- c(rep(0,52))
  
  # deal the cards
  
  hands <- dealcards(players,pack,N_cards)
  
  while (still_play(hands)){ # while loop 1

  # Check hands
  
  #print("Hands before")
  
  #print(hands)
  
  # pick cards
  card_players <- c(1:players)
  cards <- pickcards(players,card_players,hands)
  
  # update the hands
  
  hands <- updatehand(hands,cards,players)
  
  #print("The players place :")
  
  #print(cards)
  
  # Place cards on the pile
  
  pile <- cards[,]
  
  print("On the pile :")
  
  #print(pile)
  
  # Select the winner - multiple is possible
  
  winners <- selectmax(cards)

  print("The winner(s) : ")
  
  print(winners)
  
  if (length(winners) == 1){ # if 1
    
    print("Winners new hand is  :")
    
    hands <- wincards(winners[1],pile,side_pile,hands,players)
    
    #print(hands[winners[1],])
    
    print("Full list of hands")
    
    #print(hands)
    
  } #if 1
  else {
    
    while (length(winners) > 1){
    
      print("Multiple winners")
        
      # pick cards for the side_pile
        
      cards <- pickcards(players,winners,hands)
        
      # update the hands
        
      hands <- updatehand(hands,cards,players)
        
      print("The players place :")
        
      #print(cards)
        
      # Place cards on the side_pile
        
      side_pile <- cards[,]
      
      print("Side pile")
      #print(side_pile)
        
      # pick cards for the pile
      
      cards <- pickcards(players,winners,hands)
      
      # update the hands
      
      hands <- updatehand(hands,cards,players)
      
      print("The players place :")
      
      #print(cards)
      
      # Place cards on the pile
      
      pile[length(pile)+1:length(cards)] <- cards[,]
  
      # Select the winner - multiple is possible
      
      winners <- selectmax(cards)
      
      print("The winner(s) : ")
      
      print(winners)
      
    } # while loop for multiple winners
    
  } # if-else
  
  print("WE HAVE A WINNER")
  
  print("Winners new hand is  :")
  
  hands <- wincards(winners[1],pile,side_pile,hands,players)
  
 } # While loop tp keep playing 
  
} #  for loop 1