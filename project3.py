import random
def rockpaperscissors(user_player,bot_player):
  youwin=0
  botwin=0
  if(user_player==bot_player):
      print("ITS A TIE")
  
  elif(user_player=="p" and bot_player=="r")or(user_player=="r" and bot_player=="s")or(user_player=="s" and bot_player=="p"):
      
      print("you have chosen",user_player)
      print("bot has chosen ",bot_player)
      print("User Wins")
      print("MAZEL TOV!!!...YOU WON THE GAME")
      youwin+=1
      
  elif(user_player=="r" and bot_player=="p")or(user_player=="s" and bot_player=="r")or(user_player=="p" and bot_player=="s"):
      
      print("you have chosen",user_player)
      print("bot has chosen ",bot_player)
      print("Bot Has Won")
      print("OOPS! YOU GOT BROWBEATEN BY THE BOT....BOT WINS THIS....BETTER LUCK NEXT TIME!!!:")
      botwin+=1
  
  print("------ Score Board ------")
  print(" User :",youwin," | Computer: ",botwin)
  print("===============================")
  print("")
  
def points(botwin,userwin):
    botwin=0
    userwin=0
    if(botwin==userwin):
      print("its a tie")
    
    elif(user_player=="p" and bot_player=="r")or(user_player=="r" and bot_player=="s")or(user_player=="s" and bot_player=="p"):
        print("MAZEL TOV!!!...YOU WON THE GAME")
        userwin+=1

    elif(user_player=="r" and bot_player=="p")or(user_player=="s" and bot_player=="r")or(user_player=="p" and bot_player=="s"):
        print("OOPS! YOU GOT BROWBEATEN BY THE BOT....BOT WINS THIS....BETTER LUCK NEXT TIME!!!:")
        botwin+=1

print("==== WELCOME ====")
print("$$$$$$$$$$$$$$$$$$$$$")
print("| Rock Paper Scissors  |")
print("*******************")
NAME=input("Enter your name here: ")
print("WELCOME",NAME)
print("""
    Winning Rules:
    1.paper vs Rock-->paper
    2.Rock vs paper-->Rock
    3.scissors vs paper-->scissors""")
    
x=int(input("Enter the number of chances you want to play: "))
for i in range(1,x+1):
  print("Round",i,"Start:")
  user=(input(" r,p,s\n:$[r]->ROCK\n:$[p]->PAPER\n:$[s]->SCISSOR\n ENTER YOUR CHOICE:"))
  selection=["r","p","s",]
  bot=random.choice(selection)
 
  print("Now its Bot's turn:")
  print("Bot has selected:",bot)
  rockpaperscissors(user,bot)

