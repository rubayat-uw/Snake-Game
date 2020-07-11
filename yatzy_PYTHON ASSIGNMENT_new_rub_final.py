import os
import sys
import random

from collections import namedtuple

score_pad_dict={'ONCE':'0','TWOS':'0','THREES':'0','FOURS':'0','FIVES':'0','SIX':'0','PAIR':'0','TWO_PAIR':'0',
'THREE_OF_KIND':'0','FOUR_OF_KIND':'0','SMALL_STRAIGHT':'0','LARGE_STRAIGHT':'0','FULL_HOUSE':'0',
'CHANCE':'0','YATZY':'0'}

#Implementation of scoring pad
player_name=[];final_lst=[];roll_1=[];roll_2=[];roll_3=[];dice_list_4=[]
once=[];two=[];three=[];four=[];five=[];six=[];pair=[];tpair=[];thpair=[];fkind=[];small=[];large=[];fh=[];ch=[];yatzy1=[]
once_count=0;points=0

#player Board
player_score=namedtuple("player_Board",['Names','Scoreing_pad','Dice_used'])

#Implementation of dies
def dice(n):
    for i in range(n):
        yield random.randint(1,6)


def roll_dice():
    #roll 1
    roll_1=list(dice(5))
    print("roll no 1")
    print(roll_1)
    print('Enter the no. of dice u want to keep:')
    #Number of dice player is keeping
    keep_num=int(input())
    
    check=keep_num
    l=len(roll_1)
    # Check whether the dices kept by the player is within the list or not  
    while (check>0):
        #print(roll_1)
        print('Enter the value u want to keep:')
        keep=int(input())
        flag=0;
        #print(l)
        for i in range (0,l):
            #print(roll_1)
            if keep==roll_1[i]:
                final_lst.append(keep)
                roll_1.remove(keep)
                l=len(roll_1)
                    #print (roll_1)
                check=check-1
                flag=1
                #print (check)
                break;
        if flag==0:
            print('Entered value not in the list')
            
    rem_dice=5 - keep_num
    #roll 2
    print("roll no 2")
    roll_2 = list(dice(rem_dice))
    print(roll_2)
    print('enter the no of dice u want to keep')
    keep_num_1=int(input())
    
    check=keep_num_1
    l=len(roll_2)
    while (check>0):
        print('Enter the value u want to keep:')
        keep=int(input())
        flag=0;
        for i in range (0,l):
            if keep==roll_2[i]:
                final_lst.append(keep)
                roll_2.remove(keep)
                l=len(roll_2)
                check=check-1
                flag=1;
                break;
        if flag==0:
            print('Entered value not in the list')
   
    rem_dice=rem_dice-keep_num_1
    #roll 3
    print("roll no 3")
    roll_3=list(dice(rem_dice))
    print(roll_3)
    #Stores the dices kept by the user
    final_lst.extend(roll_3)
    
def onces():
    count=0
    points=0
    count=final_lst.count(1)
    #counts the number of 1's in the list
    points=count*1
    return(points)
    # returns total point scored in this catagory

def twos():
    count=0
    points=0
    count=final_lst.count(2)
    #counts the number of 2's in the list
    points=count*2
    return(points)
    # returns total point scored in this catagory

def threes():
    count=0
    points=0
    count=final_lst.count(3)
    #counts the number of 3's in the list
    points=count*3
    return(points)
    # returns total point scored in this catagory

def fours():
    count=0
    points=0
    count=final_lst.count(4)
    #counts the number of 4's in the list
    points=count*4
    return(points)
    # returns total point scored in this catagory

def fives():
    count=0
    points=0
    count=final_lst.count(5)
    #counts the number of 5's in the list
    points=count*5
    return(points)
    # returns total point scored in this catagory

def sixs():
    count=0
    points=0
    count=final_lst.count(6)
    #counts the number of 6's in the list
    points=count*6
    return(points)
    # returns total point scored in this catagory

def pairs():
    points=0
    test=0
    for k in range(1,7):
        if final_lst.count(k)>=2:
            test=test+1
            #If suppot increases it indicate a pair has occured
            if(test>=1):
                points=k*2
        k=k+1
    return(points)
    # returns total point scored in this catagory

def two_pairs():
    points=0
    test=0
    for k in range(1,7):
        if final_lst.count(k)>=2:
            test=test+1
            if(test>=2):
                points=points+k*2
        k=k+1
    return(points)
    # returns total point scored in this catagory

def three_kind():
    points=0
    test=0
    for k in range(1,7):
        if final_lst.count(k)>=3:
            test=test+1
            if(test>=1):
                points=k*3
        k=k+1
    return(points)
    # returns total point scored in this catagory

def four_kind():
    points=0
    test=0
    for k in range(1,7):
        if final_lst.count(k)>=4:
            test=test+1
            if(test>=1):
                points=points+k*4
        k=k+1
    return(points)
    # returns total point scored in this catagory

def small_straight():
    points=0
    final_lst.sort()
    if [1,2,3,4,5]==final_lst:
        points=points+15
    return(points)
    # returns total point scored in this catagory

def large_straight():
    points=0
    final_lst.sort()
    if [2,3,4,5,6]==final_lst:
        points=points+20
    return(points)
    # returns total point scored in this catagory

def full_house():
    points=0
    test=0
    for k in range(1,7):
        if final_lst.count(k)>=3:
            test=test+1
            if(test>=1):
                points=points+k*3
        k=k+1
    for k in range(1,7):
        if final_lst.count(k)>=2:
            test=test+1
            if(test>=1):
                points=points+(k*2)
        k=k+1
    return(points)
    # returns total point scored in this catagory

def chance():
    points=0
    summ=sum(final_lst)
    points=points+summ
    return(points)
    # returns total point scored in this catagory


def yatzy():
    points=0
    for k in range(1,7):
        if final_lst.count(k)==5:
            test=test+1
            if(test==1):
                print("YATZY")
                points=points+50
        k=k+1
    return(points)
    # returns total point scored in this catagory

def delete():
    del final_lst[:]
    # delete function to clear used list for another player's turn
    del roll_1[:]
    del roll_2[:]
    del roll_3[:]

def __main__game__():
    pno=0
    print("\n\n WELCOME TO YATZY! \n")
    print("THERE ARE 15 ROUNDS IN THIS GAME\n")
    while True:
        print("PLEASE ENTER PLAYER NAME THEN ENTER 'start' TO START THE GAME\n")
        name=input()
        player_name.append(name)
        if(name=="start"):
            player_name.remove('start')
            pno=len(player_name)
            break

    print("\n**players before shuffle**")
    print(player_name)
    print("\n**players after shuffle**")
    random.shuffle(player_name)
    print(player_name)

    def init_player():
        print("\nplayer",i+1,"has to roll the dice")
        print("press 'r' to roll the dice")
        playing_=input()
        if(playing_=='r'):
            roll_dice()

    def score():
        player=player_score(player_name,score_pad_dict,final_lst)
        print(player)
        delete()
        #clears the list for another player
    

    print("\nCATEGORY 1 (Ones): Try to get as many ones as possible.\n")
    i = 0
    while(1):
        init_player()
        poi=onces()
        once.append(poi)
        score_pad_dict['ONCE']=once
        score()
        i +=1
        if(i==pno):
            break
    
    print("\nCATEGORY 2 (Twos): Try to get as many twos as possible\n")
    i = 0
    while(1):
        init_player()
        poi=twos()
        two.append(poi)
        score_pad_dict['TWOS']=two
        score()
        i +=1
        if(i==pno):
            break
    
    print("\nCATEGORY 3 (Threes): Try to get as many threes as possible.\n")
    i = 0
    while(1):
        init_player()
        poi=threes()
        three.append(poi)
        score_pad_dict['THREES']=three
        score()
        i +=1
        if(i==pno):
            break
    
    print("\nCATEGORY 4 (Four): Try to get as many fours as possible.\n")
    i = 0
    while(1):
        init_player()
        poi=fours()
        four.append(poi)
        score_pad_dict['FOURS']=four
        score()
        i +=1
        if(i==pno):
            break

    print("\nCATEGORY 5 (Five): Try to get as many fives as possible.\n")
    i = 0
    while(1):
        init_player()
        poi=fives()
        five.append(poi)
        score_pad_dict['FIVES']=five
        score()
        i +=1
        if(i==pno):
            break

    print("\nCATEGORY 6 (Six): Try to get as many six as possible.\n")
    i = 0
    while(1):
        init_player()
        poi=sixs()
        six.append(poi)
        score_pad_dict['SIX']=six
        score()
        i +=1
        if(i==pno):
            break

    print("\nCATEGORY 7 (Pair): Try to get a pair of any number.\n")
    i = 0
    while(1):
        init_player()
        poi=pairs()
        pair.append(poi)
        score_pad_dict['PAIR']=pair
        score()
        i +=1
        if(i==pno):
            break

    print("\nCATEGORY 8 (Two Pairs): Try to get two distinct pairs.\n")
    i = 0
    while(1):
        init_player()
        poi=two_pairs()
        tpair.append(poi)
        score_pad_dict['TWO_PAIR']=tpair
        score()
        i +=1
        if(i==pno):
            break

    print("\nCATEGORY 9 (Three of a kind): Try to get three dice showing the same number.\n")
    i = 0
    while(1):
        init_player()
        poi=three_kind()
        thpair.append(poi)
        score_pad_dict['THREE_OF_KIND']=thpair
        score()
        i +=1
        if(i==pno):
            break

    print("\n CATEGORY 10 (Four of a kind): Try to get four dice showing the same number.\n")
    i = 0
    while(1):
        init_player()
        poi=four_kind()
        fkind.append(poi)
        score_pad_dict['FOUR_OF_KIND']=fkind
        score()
        i +=1
        if(i==pno):
            break

    print("\nCATEGORY 11 (Small straight): Try to get the sequence 1, 2, 3, 4, 5 across the dice.\n")
    i = 0
    while(1):
        init_player()
        poi=small_straight()
        small.append(poi)
        score_pad_dict['SMALL_STRAIGHT']=small
        score()
        i +=1
        if(i==pno):
            break

    print("\nCATEGORY 12 (Large straight): Try to get the sequence 2, 3, 4 ,5, 6 across the dice.\n")
    i = 0
    while(1):
        init_player()
        poi=large_straight()
        large.append(poi)
        score_pad_dict['LARGE_STRAIGHT']=large
        score()
        i +=1
        if(i==pno):
            break

    print("\nCATEGORY 13 (Full house): Try to get one Three of a kind and one Pair.\n")
    i = 0
    while(1):
        init_player()
        poi=full_house()
        fh.append(poi)
        score_pad_dict['FULL_HOUSE']=fh
        score()
        i +=1
        if(i==pno):
            break

    print("\nCATEGORY 14 (Chance): Try to get the dice to show as high of a total as possible.\n")
    i = 0
    while(1):
        init_player()
        poi=chance()
        ch.append(poi)
        score_pad_dict['CHANCE']=ch
        score()
        i +=1
        if(i==pno):
            break

    print("\nCATEGORY 15 (Yatzy): Try to get all dice showing the same number.\n")
    i = 0
    while(1):
        init_player()
        poi=yatzy()
        yatzy1.append(poi)
        score_pad_dict['YATZY']=yatzy1
        score()
        i +=1
        if(i==pno):
            break

__main__game__()

print("\n FINAL SCORE BOARD IS\n")

#Displaying final score board
total_score=[]
for i in range(0,len(player_name)):
    total=once[i]+two[i]+three[i]+four[i]+five[i]+six[i]+pair[i]+tpair[i]+thpair[i]+fkind[i]+small[i]+large[i]+fh[i]+ch[i]+yatzy1[i]
    total_score.append(total)
    #Total scores of each player

print("\nThe total scores got by the players:",player_name,total_score)
print("\nPlayers are displayed according to score(the higher the better). The player on top u have won the game")

index=0
for j in range(1,6):
    win=max(total)
    index=total_score.index(win)
    print(player_name[index])
    #Player names in decending order according to total scores
    del total_score[index]
    del player_name[index]
    if(len(total_score)==0):
        break
        
