import matplotlib.pyplot as plt
import numpy as np
#intitail
def create_deck():
  for i in range(0,13):
    card[i][0]*=num_deck
  if(debug[0]):
    print("start : ",card,"\n")
  return card

#first_draw
def new_draw():
  broker_hand.append(np.random.choice(draw_able)) #broker draw
  card[broker_hand[0]-1][0]-=1 #amount of card in deck -1
  if(card[broker_hand[0]-1][0]==0):draw_able.remove(broker_hand[0]) #if there are no type of that card, 
                                                        #remove it from the card that u can draw

  player_hand.append(np.random.choice(draw_able)) #player draw
  card[player_hand[0]-1][0]-=1 #amount of card in deck -1
  if(card[player_hand[0]-1][0]==0):draw_able.remove(player_hand[0])

  broker_hand.append(np.random.choice(draw_able)) #broker darw
  card[broker_hand[1]-1][0]-=1 #amount of card in deck -1
  if(card[broker_hand[1]-1][0]==0):draw_able.remove(broker_hand[1])
  value[0]=card[broker_hand[0]-1][1]+card[broker_hand[1]-1][1] #value of card in hand
  value[0]%=10

  player_hand.append(np.random.choice(draw_able)) #player draw
  card[player_hand[1]-1][0]-=1
  if(card[player_hand[1]-1][0]==0):draw_able.remove(player_hand[1])
  value[1]=card[player_hand[0]-1][1]+card[player_hand[1]-1][1]
  value[1]%=10
  if(debug[1]): #print debug
    print("=============================================")
    print("hand player: ",player_hand)
    print("card left",card)
    print("value player : ",value[1])
    print("hand broker: ",broker_hand)
    print("card left",card)
    print("value broker : ",value[0])

#second draw

def broker_draw():
  broker_hand.append(np.random.choice(draw_able)) #broker_hand draw
  card[broker_hand[2]-1][0]-=1 #amount of card in deck -1
  if(card[broker_hand[2]-1][0]==0):draw_able.remove(broker_hand[2]) #if there are no type of that card, 
                                                        #remove it from the card that u can draw
  value[0]+=card[broker_hand[2]-1][1] #update the value of card in hand of broker
  value[0]%=10
  if(debug[2]): #print debug
    print(">>><<<\nbroker draw again")                                                     
    print("broker_hand: ",broker_hand)
    print("card left",card)
    print("value broker : ",value[0])
    print(">>><<<") 

def player_draw():
  player_hand.append(np.random.choice(draw_able)) #broker_hand draw
  card[player_hand[2]-1][0]-=1 #amount of card in deck -1
  if(card[player_hand[2]-1][0]==0):draw_able.remove(player_hand[2]) #if there are no type of that card, 
                                                        #remove it from the card that u can draw
  value[1]+=card[player_hand[2]-1][1] #update the value of card in hand of player
  value[1]%=10 
  if(debug[2]): #print debug
    print(">>><<<\nplayer draw again")    
    print("player_hand: ",player_hand)
    print("card left",card)
    print("value player : ",value[1]) 
    print(">>><<<")            

  #check bet
def check(bet):
  type_print=0
  
  if(type_bet == 1): #bet player
    if(value[0]<value[1]): #player win
      status[0]+=1
      type_print=1
      money[0]+=bet*1
    if(value[0]>value[1]):#broker win
      status[1]+=1
      type_print=2
      money[0]-=bet*1
    if(value[0]==value[1]):#tiesum
      status[2]+=1
      type_print=3  
      money[0]-=bet*1

  if(type_bet == 2): #bet broker
    if(value[0]<value[1]): #player win
      status[0]+=1
      type_print=1
      money[0]-=bet*1
    if(value[0]>value[1]):#broker win
      status[1]+=1
      type_print=2
      money[0]+=bet*0.95
    if(value[0]==value[1]):#tiesum
      status[2]+=1
      type_print=3  
      money[0]-=bet*1
 
  if(type_bet == 3): #bet tiesum
    if(value[0]<value[1]): #player win
      status[0]+=1
      type_print=1
      money[0]-=bet*1
    if(value[0]>value[1]):#broker win
      status[1]+=1
      type_print=2
      money[0]-=bet*1
    if(value[0]==value[1]):#tiesum
      status[2]+=1
      type_print=3  
      money[0]+=bet*8

  if(type_bet == 4):  #bet tie2
    if(value[0]<value[1]): #player win
      status[0]+=1
      type_print=1
      money[0]-=bet*1
    if(value[0]>value[1]):#broker win
      status[1]+=1
      type_print=2
      money[0]-=bet*1
    if(value[0]==value[1] and value[1]!=2):#tiesum
      status[2]+=1
      type_print=3  
      money[0]-=bet*1
    if(value[0]==value[1] and value[1]==2):#tie2
      status[4]+=1
      type_print=3  
      money[0]+=bet*220

  if(type_bet == 5):  #bet pair player
    if(player_hand[0]==player_hand[1]):
      status[5]+=1  
      money[0]+=bet*11
    if(player_hand[0]!=player_hand[1]):
      if(value[0]<value[1]): #player win
        status[0]+=1
        money[0]-=bet*1
      if(value[0]>value[1]):#broker win
        status[1]+=1
        money[0]-=bet*1
      if(value[0]==value[1] and value[1]!=2):#tiesum
        status[2]+=1 
        money[0]-=bet*1
      if(value[0]==value[1] and value[1]==2):#tie2
        status[4]+=1  
        money[0]-=bet*1

  if(type_bet == 6):  #bet pair broker
    if(broker_hand[0]==broker_hand[1]):
      status[6]+=1  
      money[0]+=bet*11
    if(broker_hand[0]!=broker_hand[1]):
      if(value[0]<value[1]): #player win
        status[0]+=1
        money[0]-=bet*1
      if(value[0]>value[1]):#broker win
        status[1]+=1
        money[0]-=bet*1
      if(value[0]==value[1] and value[1]!=2):#tiesum
        status[2]+=1 
        money[0]-=bet*1
      if(value[0]==value[1] and value[1]==2):#tie2
        status[4]+=1  
        money[0]-=bet*1

  if(type_bet == 7):  #bet perfect pair
    if(broker_hand[0]==broker_hand[1] and (player_hand[0]==player_hand[1])):
      status[7]+=1  
      money[0]+=bet*25
    if(broker_hand[0]!=broker_hand[1] or player_hand[0]!=player_hand[1]):
      if(value[0]<value[1]): #player win
        status[0]+=1
        money[0]-=bet*1
      if(value[0]>value[1]):#broker win
        status[1]+=1
        money[0]-=bet*1
      if(value[0]==value[1] and value[1]!=2):#tiesum
        status[2]+=1 
        money[0]-=bet*1
      if(value[0]==value[1] and value[1]==2):#tie2
        status[4]+=1  
        money[0]-=bet*1

  if(type_bet == 8):  #bet high
    if(np.size(player_hand)==3 or np.size(broker_hand)==3):
      status[8]+=1  
      money[0]+=bet*0.54
    if(np.size(player_hand)==2 and np.size(broker_hand)==2):
      if(value[0]<value[1]): #player win
        status[0]+=1
        money[0]-=bet*1
      if(value[0]>value[1]):#broker win
        status[1]+=1
        money[0]-=bet*1
      if(value[0]==value[1] and value[1]!=2):#tiesum
        status[2]+=1 
        money[0]-=bet*1
      if(value[0]==value[1] and value[1]==2):#tie2
        status[4]+=1  
        money[0]-=bet*1

  if(type_bet == 9):  #bet low
    if(np.size(player_hand)==2 and np.size(broker_hand)==2):
      status[9]+=1  
      money[0]+=bet*1.5
    if(np.size(player_hand)==3 or np.size(broker_hand)==3):
      if(value[0]<value[1]): #player win
        status[0]+=1
        money[0]-=bet*1
      if(value[0]>value[1]):#broker win
        status[1]+=1
        money[0]-=bet*1
      if(value[0]==value[1] and value[1]!=2):#tiesum
        status[2]+=1 
        money[0]-=bet*1
      if(value[0]==value[1] and value[1]==2):#tie2
        status[4]+=1  
        money[0]-=bet*1

  times[0]+=1
  if(draw_able==[] and money[0]!=money[1]):
    type_print=4
    
  
  if(debug[3]):
    print("broker vs player :",value)
    if (type_print==1) : print("player win , money : ",money[0]) 
    if (type_print==2) : print("broker win , money : ",money[0])
    if (type_print==3) : print("tie , money : ",money[0])
    if (type_print==4) : print("---------deck out---------")
    print("")  


#reset
def reset_hand():
  broker_hand.clear()
  player_hand.clear()
  value[0]=0
  value[1]=0     


#check_deck
def check_deck():
  sum=0 #sum of card left
  for i in range(0,13):
    sum+=card[i][0]
  if(sum<7):
    draw_able.clear()
    for i in range(0,13):
      card[i][0]=4*num_deck
      draw_able.append(i+1)
  return 1

#check_money
def check_money():
  if(money[0]!=0 and money[0]!=money[1]):
    return 1
  return 0

#check_time
def check_times():
  if(times[0]!=times_limit):
    return 1
  return 0                 

#condition_draw
def condition_draw():
  #condition player draw
  if(value[1]==8 or value[1]==9):  #player got 8-9
    return
  if(value[0]==8 or value[0]==9):  #broker got 8-9
    return

  if(value[1]>=0 and value[1]<=5): #player got 0-5
    player_draw()
  #condition broker draw
  if(value[0]==7): #broker got 7
      return
  if(value[0]>=0 and value[0]<=2): #broker got 0-2
      broker_draw()
      return 

  if(np.size(player_hand)==3):

    if(value[0]==3): 
      if(card[player_hand[2]-1][1]==8):
        return
      else: 
        broker_draw()
        return
    
    if(value[0]==4):
      if(card[player_hand[2]-1][1]==1 or card[player_hand[2]-1][1]==0 or card[player_hand[2]-1][1]==8 or card[player_hand[2]-1][1]==9):
        return
      else: 
        broker_draw()
        return

    if(value[0]==5):
      if(card[player_hand[2]-1][1]==4 or card[player_hand[2]-1][1]==5 or card[player_hand[2]-1][1]==6 or card[player_hand[2]-1][1]==7):
        broker_draw()
        return
      else: 
        return

    if(value[0]==6):
      if(card[player_hand[2]-1][1]==6 or card[player_hand[2]-1][1]==7):
        broker_draw()
        return
      else: 
        return

def expected_value(type_bet):
    """Calculate the expected value of a baccarat bet."""
    commission = 0
    if type_bet == 1:  # Player bet
        probability = status[0]/times_limit
        payout = 1
    elif type_bet == 2:  # Banker bet
        probability = status[1]/times_limit
        payout = 0.95
    elif type_bet == 3:  # Tie with sum of 8:1
        probability = status[2]/times_limit
        payout = 8
    elif type_bet == 4:  # Tie with 2 points:1
        probability = status[4]/times_limit
        payout = 220
    elif type_bet == 5:  # bet player pair
        probability = status[5]/times_limit
        payout = 11
    elif type_bet == 6:  # bet broker pair
        probability = status[6]/times_limit
        payout = 11
    elif type_bet == 7:  # bet broker pair
        probability = status[7]/times_limit
        payout = 25
    elif type_bet == 8:  # bet broker pair
        probability = status[8]/times_limit
        payout = 0.54
    elif type_bet == 9:  # bet broker pair
        probability = status[9]/times_limit
        payout = 1.5

    else:
        raise ValueError("Invalid bet type")
    
    # Calculate the expected value
    expected_value = (probability * payout) - (1 - probability) * (1 - commission)
    status[3] = expected_value
    probabilitymain[0] = probability
    return (expected_value,probability)


money=[1000,1500] #money[0]=money now ,money[1]=the end point #relate with check_money()
money_graph=[]
bet=100 #cost of each bet
type_bet = 3 #type of bet 1=player 2=broker 3=tiewithsum 4=tiewith2point 5=playerpair 6=brokerpair 7=perfectpair 8=high 9=low
times_limit=100000 #relate with check_times()
status=[0,0,0,0,0,0,0,0,0,0,0,0] #win(of player) lose tie # 0=win 1=lose 2=tie 3=expected value 4=tie2 5=playerpair 6=brokerpair 7=perfectpair 8 =high 9=low
times =[0] #times
probabilitymain = [0]
value=[0,0] #value of hand each times,u will see it when draw already,value[0]=value of broker ,value[1]=value of player
broker_hand=[] #card in hand1 in term of address 
player_hand=[] #card in hand2 in term of address 
num_deck=1#amount of deck
card=[[4,1,1],[4,2,2],[4,3,3],[4,4,4],[4,5,5],[4,6,6],
      [4,7,7],[4,8,8],[4,9,9],[4,0,10],[4,0,11],[4,12],[4,0,13]]
      #[amount of card,value]
draw_able=[1,2,3,4,5,6,7,8,9,10,11,12,13] #types of card u still can draw
debug=[0,0,0,0] #1=on,2=off [0]start_card [1]new_draw [2]second draw [3]status and money left

card=create_deck()
while(check_times() and check_deck()): #dont delete check_deck() but can delete other check
  new_draw()
  condition_draw()
  check(bet)
  money_graph.append(money[0])
  reset_hand()
  expected_value(type_bet)
print("win :",status[0],",lose :",status[1],",times :",times[0],"\n",
      ",tie :",status[2],",tie 2:",status[4],",pair player :",status[5],",pair broker :",status[6],",perfect pair :",status[7],",high :",status[8],",low :",status[9],"\n",
      ",money :",money[0],',probability :',probabilitymain[0],',expected value :',status[3])
plt.plot(money_graph)
plt.show()