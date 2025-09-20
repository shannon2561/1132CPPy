#class
    #game
    #player
    #card

class Cards:
    def __init__(self, value, color):
        self.value=value
        self.color=color

    def __repr__(self):
        color_code = {"red": 31, "yellow": 33, "green": 32, "blue": 36}
        if self.color is None:
            ansi_code = 0
        else:
            ansi_code = color_code[self.color]
        return f"\033[{ansi_code}m{self.value}\033[0m"
    
    def is_playable(self, top_value, top_color):
        if self.color == top_color or self.value == top_value or self.value in ["wild", "+4"]:
            return True
        else:
            return False
    
    #tuple
    def __iter__(self):
        if self.value in ["wild", "+4"]:
            return iter((self.value,))
        else:
            return iter((self.value, self.color))
    
    def __getitem__(self, index):
        if self.value in ["wild", "+4"]:
            return (self.value,)[index]
        else:
            return (self.value, self.color)[index]
    
    def __len__(self):
        if self.value in ["wild", "+4"]:
            return 1
        else:
            return 2


class Player:
    def __init__(self, ID, cards):
        self.ID=ID
        self.cards=cards

    def play_card(self, top_card):
        number=[]
        skip=[]
        reverse=[]
        draw_two=[]
        wild=[]
        wild_draw_four=[]
        can_play={1:number, 2:skip, 3:reverse, 4:draw_two, 5:wild, 6:wild_draw_four}

        for card in self.cards:
            if card.is_playable(top_card.value, top_card.color):
                if type(card.value)==int:
                    number.append(card)
                elif card.value=="skip":
                    skip.append(card)
                elif card.value=="reverse":
                    reverse.append(card)
                elif card.value=="+2":
                    draw_two.append(card)
                elif card.value=="wild":
                    wild.append(card)
                else:
                    wild_draw_four.append(card)
            
        for _, value_list in can_play.items():
            if value_list!=[]:
                played_card=value_list[0]
                break
        else:
            return None
        
        self.cards.remove(played_card)

        if len(played_card)==1:   #wild, +4
            played_card.color=self.choose_color()

        return played_card
    
    def draw_card(self, total_cards):
        drawn_card=total_cards.pop(0)
        self.cards.append(drawn_card)
        return drawn_card

    def choose_color(self):
        red=0
        yellow=0
        green=0
        blue=0
        for card_tuple in self.cards:
            if len(card_tuple)==2:
                if card_tuple[1]=="yellow":
                    yellow+=1
                elif card_tuple[1]=="green":
                    green+=1
                elif card_tuple[1]=="blue":
                    blue+=1
                else:
                    red+=1

        if red==yellow==green==blue==0:
            return "red"
        else:
            color_counts={"red": red, "yellow": yellow, "green": green, "blue": blue}
            return max(color_counts, key=color_counts.get)
            #在Python中使用max(a, b, c, d)時，如果有兩個或以上的值一樣且是最大值，max()會回傳第一個出現的最大值。

    def won(self):
        if self.cards==[]:
            return True
        else:
            return False



class GameRule:
    def __init__(self, player_ID):
        self.player_ID=player_ID
        adverse=False
        self.adverse=adverse

    def next_player(self):
        #順
        if self.adverse==False:
            if self.player_ID==4:
                self.player_ID=0
            else:
                self.player_ID+=1
        #逆
        else:
            if self.player_ID==0:
                self.player_ID=4
            else:
                self.player_ID-=1
        return self.player_ID
    
    # def skip_player(self):
    #     #順
    #     if self.adverse==False:
    #         if self.player_ID==3:
    #             self.player_ID=0
    #         elif self.player_ID==4:
    #             self.player_ID=1
    #         else:
    #             self.player_ID+=2
    #     #逆
    #     else:
    #         if self.player_ID==1:
    #             self.player_ID=4
    #         elif self.player_ID==0:
    #             self.player_ID=3
    #         else:
    #             self.player_ID-=2
    #     return self.player_ID
    
    def reverse(self):
        if self.adverse==False:
            self.adverse=True
        else:
            self.adverse=False


if __name__=="__main__":
    Total_Cards=[]
    while True:
        Input=input()
        if Input=="q":
            break
        # elif Input=="wild":
        #     Card_tuple=tuple("wild")
        # elif Input=="+4":
        #     Card_tuple=tuple("+4")
        else:
            Card_list=Input.split("-")
            Value=Card_list[0]
            if len(Card_list)==2:
                if Value!="+2":
                    try:
                        Value=int(Card_list[0])
                    except ValueError:
                        pass
                Color=Card_list[1]
                c=Cards(Value, Color)
            elif Card_list==["wild"]:
                c=Cards("wild", None)
            else:   #+4
                c=Cards("+4", None)
            # Card_tuple=tuple(Card_list)
        Total_Cards.append(c)
    # print(Total_Cards)
    
    #發牌
    Cards_0=[]
    Cards_1=[]
    Cards_2=[]
    Cards_3=[]
    Cards_4=[]
    for _ in range(5):
        Cards_0.append(Total_Cards.pop(0))
        Cards_1.append(Total_Cards.pop(0))
        Cards_2.append(Total_Cards.pop(0))
        Cards_3.append(Total_Cards.pop(0))
        Cards_4.append(Total_Cards.pop(0))
    
    Top_Card=Total_Cards.pop(0)
    # print("Cards_0:", Cards_0)
    # print("Cards_1:", Cards_1)
    # print("Cards_2:", Cards_2)
    # print("Cards_3:", Cards_3)
    # print("Cards_4:", Cards_4)
    # print("Top Card:", Top_Card)
    
    Players=[]
    Players.append(Player(0, Cards_0))
    Players.append(Player(1, Cards_1))
    Players.append(Player(2, Cards_2))
    Players.append(Player(3, Cards_3))
    Players.append(Player(4, Cards_4))

    #GameSetUp
    if Top_Card.value in ["wild", "+4"]:
        Top_Color="red"
        Top_Value=Top_Card.value
    else: 
        Top_Color=Top_Card.color
        Top_Value=Top_Card.value
    is_first_card=True
    # elif Top_Card.value in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    #     Top_Color=Top_Card.color
    #     Top_Value=Top_Card.value
    # else:
    #     Top_Color=Top_Card.color
    #     Top_Value=None
    
    #開始
    g=GameRule(0)
    skip_player=False
    draw_two=False
    draw_four=False
    Round=0
    while True:
        Round+=1
        # print("Round", Round)
        # print("Cards_0:", Cards_0)
        # print("Cards_1:", Cards_1)
        # print("Cards_2:", Cards_2)
        # print("Cards_3:", Cards_3)
        # print("Cards_4:", Cards_4)
        # print("Top Card:", Top_Card)
        # print()
        p=Players[g.player_ID]

        if draw_two==True:
            for _ in range(2):
                p.draw_card(Total_Cards)
            draw_two=False

        if draw_four==True:
            for _ in range(4):
                p.draw_card(Total_Cards)
            draw_four=False


        #打牌
        played=False
        result=p.play_card(Top_Card)
        if result!=None:
            Top_Card=result
            if is_first_card==False:
                if Top_Card.value=="skip":
                    skip_player=True
                elif Top_Card.value=="reverse":
                    g.reverse()
                elif Top_Card.value=="+2":
                    draw_two=True
                elif Top_Card.value=="+4":
                    draw_four=True
                else:
                    pass
            else:
                is_first_card=False
                
            Top_Value=Top_Card.value
            Top_Color=Top_Card.color
            played=True

        #if沒牌，抽牌
        #如果可以打，要打出去
        if played==False:
            if p.draw_card(Total_Cards).is_playable(Top_Value, Top_Color):
                Top_Card=p.play_card(Top_Card)
                if is_first_card==False:
                    if Top_Card.value=="skip":
                        skip_player=True
                    elif Top_Card.value=="reverse":
                        g.reverse()
                    elif Top_Card.value=="+2":
                        draw_two=True
                    elif Top_Card.value=="+4":
                        draw_four=True
                    else:
                        pass
                else:
                    is_first_card=False
                
                Top_Value=Top_Card.value
                Top_Color=Top_Card.color
            else:
                pass

        if p.won()==True:
            print(f"Player {p.ID} win!")
            break

        if skip_player==True:
            g.next_player()
            skip_player=False

        g.next_player()


#-------------------------------------------------------------------------
# 65分
# class Cards:
#     def __init__(self, value, color):
#         self.value=value
#         self.color=color

#     def __repr__(self):
#         color_code = {"red": 31, "yellow": 33, "green": 32, "blue": 36}
#         if self.color is None:
#             ansi_code = 0
#         else:
#             ansi_code = color_code[self.color]
#         return f"\033[{ansi_code}m{self.value}\033[0m"
    
#     def is_playable(self, top_value, top_color):
#         if self.color == top_color or self.value == top_value or self.value in ["wild", "+4"]:
#             return True
#         else:
#             return False
    
#     #tuple
#     def __iter__(self):
#         if self.value in ["wild", "+4"]:
#             return iter((self.value,))
#         else:
#             return iter((self.value, self.color))
    
#     def __getitem__(self, index):
#         if self.value in ["wild", "+4"]:
#             return (self.value,)[index]
#         else:
#             return (self.value, self.color)[index]
    
#     def __len__(self):
#         if self.value in ["wild", "+4"]:
#             return 1
#         else:
#             return 2


# class Player:
#     def __init__(self, ID, cards):
#         self.ID=ID
#         self.cards=cards

#     def play_card(self, top_card):
#         number=[]
#         skip=[]
#         reverse=[]
#         draw_two=[]
#         wild=[]
#         wild_draw_four=[]
#         can_play={1:number, 2:skip, 3:reverse, 4:draw_two, 5:wild, 6:wild_draw_four}

#         for card in self.cards:
#             if card.is_playable(top_card.value, top_card.color):
#                 if len(card)==2:
#                     #number
#                     if type(card.value)==int:
#                        number.append(card)
#                     elif card.value=="skip":
#                         skip.append(card)
#                     elif card.value=="reverse":
#                         reverse.append(card)
#                     elif card.value=="+2":
#                         draw_two.append(card)
#                     elif card.value=="wild":
#                         wild.append(card)
#                     else:
#                         wild_draw_four.append(card)
            
#         for _, value_list in can_play.items():
#             if value_list!=[]:
#                 played_card=value_list[0]
#                 break
#         else:
#             return None
        
#         self.cards.remove(played_card)

#         if len(played_card)==1:   #wild, +4
#             played_card.color=self.choose_color()

#         return played_card
    
#     def draw_card(self, total_cards):
#         drawn_card=total_cards.pop(0)
#         self.cards.append(drawn_card)
#         return drawn_card

#     def choose_color(self):
#         red=0
#         yellow=0
#         green=0
#         blue=0
#         for card_tuple in self.cards:
#             if len(card_tuple)==2:
#                 if card_tuple[1]=="yellow":
#                     yellow+=1
#                 elif card_tuple[1]=="green":
#                     green+=1
#                 elif card_tuple[1]=="blue":
#                     blue+=1
#                 else:
#                     red+=1

#         if red==yellow==green==blue==0:
#             return "red"
#         else:
#             color_counts={"red": red, "yellow": yellow, "green": green, "blue": blue}
#             return max(color_counts, key=color_counts.get)
#             #在Python中使用max(a, b, c, d)時，如果有兩個或以上的值一樣且是最大值，max()會回傳第一個出現的最大值。

#     def won(self):
#         if self.cards==[]:
#             return True
#         else:
#             return False



# class GameRule:
#     def __init__(self, player_ID):
#         self.player_ID=player_ID
#         adverse=False
#         self.adverse=adverse

#     def next_player(self):
#         #順
#         if self.adverse==False:
#             if self.player_ID==4:
#                 self.player_ID=0
#             else:
#                 self.player_ID+=1
#         #逆
#         else:
#             if self.player_ID==0:
#                 self.player_ID=4
#             else:
#                 self.player_ID-=1
#         return self.player_ID
    
#     def skip_player(self):
#         #順
#         if self.adverse==False:
#             if self.player_ID==3:
#                 self.player_ID=0
#             elif self.player_ID==4:
#                 self.player_ID=1
#             else:
#                 self.player_ID+=2
#         #逆
#         else:
#             if self.player_ID==1:
#                 self.player_ID=4
#             elif self.player_ID==0:
#                 self.player_ID=3
#             else:
#                 self.player_ID-=2
#         return self.player_ID
    
#     def reverse(self):
#         if self.adverse==False:
#             self.adverse=True
#         else:
#             self.adverse=False


# if __name__=="__main__":
#     Total_Cards=[]
#     while True:
#         Input=input()
#         if Input=="q":
#             break
#         # elif Input=="wild":
#         #     Card_tuple=tuple("wild")
#         # elif Input=="+4":
#         #     Card_tuple=tuple("+4")
#         else:
#             Card_list=Input.split("-")
#             if len(Card_list)==2:
#                 try:
#                     Value=int(Card_list[0])
#                 except ValueError:
#                     Value=Card_list[0]
#                 Color=Card_list[1]
#                 c=Cards(Value, Color)
#             elif Card_list==["wild"]:
#                 c=Cards("wild", None)
#             else:   #+4
#                 c=Cards("+4", None)
#             # Card_tuple=tuple(Card_list)
#         Total_Cards.append(c)
#     # print(Total_Cards)
    
#     #發牌
#     Cards_0=[]
#     Cards_1=[]
#     Cards_2=[]
#     Cards_3=[]
#     Cards_4=[]
#     for _ in range(5):
#         Cards_0.append(Total_Cards.pop(0))
#         Cards_1.append(Total_Cards.pop(0))
#         Cards_2.append(Total_Cards.pop(0))
#         Cards_3.append(Total_Cards.pop(0))
#         Cards_4.append(Total_Cards.pop(0))
    
#     Top_Card=Total_Cards.pop(0)
#     # print("Cards_0:", Cards_0)
#     # print("Cards_1:", Cards_1)
#     # print("Cards_2:", Cards_2)
#     # print("Cards_3:", Cards_3)
#     # print("Cards_4:", Cards_4)
#     # print("Top Card:", Top_Card)
    
#     Players=[]
#     Players.append(Player(0, Cards_0))
#     Players.append(Player(1, Cards_1))
#     Players.append(Player(2, Cards_2))
#     Players.append(Player(3, Cards_3))
#     Players.append(Player(4, Cards_4))

#     #GameSetUp
#     if Top_Card.value in ["wild", "+4"]:
#         Top_Color="red"
#         Top_Value=Top_Card.value
#     else: 
#         Top_Color=Top_Card.color
#         Top_Value=Top_Card.value
#     is_first_card=True
#     # elif Top_Card.value in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     #     Top_Color=Top_Card.color
#     #     Top_Value=Top_Card.value
#     # else:
#     #     Top_Color=Top_Card.color
#     #     Top_Value=None
    
#     #開始
#     g=GameRule(0)
#     draw_two=False
#     draw_four=False
#     while True:
#         p=Players[g.player_ID]
#         if draw_two==True:
#             for _ in range(2):
#                 p.draw_card(Total_Cards)
#             draw_two=False

#         if draw_four==True:
#             for _ in range(4):
#                 p.draw_card(Total_Cards)
#             draw_four=False

#         #打牌
#         played=False
#         result=p.play_card(Top_Card)
#         if result!=None:
#             Top_Card=result
#             if is_first_card==False:
#                 if Top_Card.value=="skip":
#                     g.skip_player()
#                 elif Top_Card.value=="reverse":
#                     g.reverse()
#                 elif Top_Card.value=="+2":
#                     draw_two=True
#                 elif Top_Card.value=="+4":
#                     draw_four=True
#                 else:
#                     pass
#             else:
#                 is_first_card=False
                
#             Top_Value=Top_Card.value
#             Top_Color=Top_Card.color
#             played=True

#         #if沒牌，抽牌
#         #如果可以打，要打出去
#         if played==False:
#             if p.draw_card(Total_Cards).is_playable(Top_Value, Top_Color):
#                 Top_Card=p.play_card(Top_Card)
#                 if is_first_card==False:
#                     if Top_Card.value=="skip":
#                         g.skip_player()
#                     elif Top_Card.value=="reverse":
#                         g.reverse()
#                     elif Top_Card.value=="+2":
#                         draw_two=True
#                     elif Top_Card.value=="+4":
#                         draw_four=True
#                     else:
#                         pass
#                 else:
#                     is_first_card=False
                
#                 Top_Value=Top_Card.value
#                 Top_Color=Top_Card.color
#             else:
#                 pass

#         if p.won()==True:
#             print(f"Player {p.ID} win!")
#             break

#         g.next_player()

    

#-----------------------------------------------
# 50分

# class Cards:
#     def __init__(self, value, color):
#         self.value=value
#         self.color=color

#     def __repr__(self):
#         color_code = {"red": 31, "yellow": 33, "green": 32, "blue": 36}
#         if self.color is None:
#             ansi_code = 0
#         else:
#             ansi_code = color_code[self.color]
#         return f"\033[{ansi_code}m{self.value}\033[0m"
    
#     def is_playable(self, top_value, top_color):
#         if self.color == top_color or self.value == top_value or self.value in ["wild", "+4"]:
#             return True
#         else:
#             return False
    
#     #擬tuple
#     def __iter__(self):
#         if self.value in ["wild", "+4"]:
#             return iter((self.value,))
#         else:
#             return iter((self.value, self.color))
    
#     def __getitem__(self, index):
#         if self.value in ["wild", "+4"]:
#             return (self.value,)[index]
#         else:
#             return (self.value, self.color)[index]
    
#     def __len__(self):
#         if self.value in ["wild", "+4"]:
#             return 1
#         else:
#             return 2


# class Player:
#     def __init__(self, ID, cards):
#         self.ID=ID
#         self.cards=cards

#     def play_card(self, top_value, top_color):
#         for card in self.cards:
#             if card.is_playable(top_value, top_color):
#                 if len(card)==2:   #一般
#                     top_card=card
#                 else:  #wild, +4
#                     top_card=card
#                     top_card.color=self.choose_color()
#                 self.cards.remove(card)
#                 return top_card
#         return None
    
#     def draw_card(self, total_cards):
#         drawn_card=total_cards.pop(0)
#         self.cards.append(drawn_card)
#         return drawn_card

#     def choose_color(self):
#         red=0
#         yellow=0
#         green=0
#         blue=0
#         for card_tuple in self.cards:
#             if len(card_tuple)==2:
#                 if card_tuple[1]=="yellow":
#                     yellow+=1
#                 elif card_tuple[1]=="green":
#                     green+=1
#                 elif card_tuple[1]=="blue":
#                     blue+=1
#                 else:
#                     red+=1

#         if red==yellow==green==blue==0:
#             return "red"
#         else:
#             color_counts={"red": red, "yellow": yellow, "green": green, "blue": blue}
#             return max(color_counts, key=color_counts.get)
#             #在Python中使用max(a, b, c, d)時，如果有兩個或以上的值一樣且是最大值，max()會回傳第一個出現的最大值。

#     def won(self):
#         if self.cards==[]:
#             return True
#         else:
#             return False



# class GameRule:
#     def __init__(self, player_ID):
#         self.player_ID=player_ID
#         adverse=False
#         self.adverse=adverse

#     def next_player(self):
#         #順
#         if self.adverse==False:
#             if self.player_ID==4:
#                 self.player_ID=0
#             else:
#                 self.player_ID+=1
#         #逆
#         else:
#             if self.player_ID==0:
#                 self.player_ID=4
#             else:
#                 self.player_ID-=1
#         return self.player_ID
    
#     def skip_player(self):
#         #順
#         if self.adverse==False:
#             if self.player_ID==3:
#                 self.player_ID=0
#             elif self.player_ID==4:
#                 self.player_ID=1
#             else:
#                 self.player_ID+=2
#         #逆
#         else:
#             if self.player_ID==1:
#                 self.player_ID=4
#             elif self.player_ID==0:
#                 self.player_ID=3
#             else:
#                 self.player_ID-=2
#         return self.player_ID
    
#     def reverse(self):
#         if self.adverse==False:
#             self.adverse=True
#         else:
#             self.adverse=False

#     # def plus_two(self):
#     #     #順
#     #     if self.adverse==False:

#     #if top card
#     #+4



# if __name__=="__main__":
#     Total_Cards=[]
#     while True:
#         Input=input()
#         if Input=="q":
#             break
#         # elif Input=="wild":
#         #     Card_tuple=tuple("wild")
#         # elif Input=="+4":
#         #     Card_tuple=tuple("+4")
#         else:
#             Card_list=Input.split("-")
#             if len(Card_list)==2:
#                 try:
#                     Value=int(Card_list[0])
#                 except ValueError:
#                     Value=Card_list[0]
#                 Color=Card_list[1]
#                 c=Cards(Value, Color)
#             elif Card_list==["wild"]:
#                 c=Cards("wild", None)
#             else:   #+4
#                 c=Cards("+4", None)
#             # Card_tuple=tuple(Card_list)
#         Total_Cards.append(c)
#     # print(Total_Cards)
    
#     #發牌
#     Cards_0=[]
#     Cards_1=[]
#     Cards_2=[]
#     Cards_3=[]
#     Cards_4=[]
#     for _ in range(5):
#         Cards_0.append(Total_Cards.pop(0))
#         Cards_1.append(Total_Cards.pop(0))
#         Cards_2.append(Total_Cards.pop(0))
#         Cards_3.append(Total_Cards.pop(0))
#         Cards_4.append(Total_Cards.pop(0))
    
#     Top_Card=Total_Cards.pop(0)
#     # print("Cards_0:", Cards_0)
#     # print("Cards_1:", Cards_1)
#     # print("Cards_2:", Cards_2)
#     # print("Cards_3:", Cards_3)
#     # print("Cards_4:", Cards_4)
#     # print("Top Card:", Top_Card)
    
#     Players=[]
#     Players.append(Player(0, Cards_0))
#     Players.append(Player(1, Cards_1))
#     Players.append(Player(2, Cards_2))
#     Players.append(Player(3, Cards_3))
#     Players.append(Player(4, Cards_4))

#     #GameSetUp
#     if Top_Card.value in ["wild", "+4"]:
#         Top_Color="red"
#         Top_Value=Top_Card.value
#     else: 
#         Top_Color=Top_Card.color
#         Top_Value=Top_Card.value
#     is_first_card=True
#     # elif Top_Card.value in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     #     Top_Color=Top_Card.color
#     #     Top_Value=Top_Card.value
#     # else:
#     #     Top_Color=Top_Card.color
#     #     Top_Value=None
    
#     #開始
#     g=GameRule(0)
#     draw_two=False
#     draw_four=False
#     while True:
#         p=Players[g.player_ID]
#         if draw_two==True:
#             for _ in range(2):
#                 p.draw_card(Total_Cards)
#             draw_two=False

#         if draw_four==True:
#             for _ in range(4):
#                 p.draw_card(Total_Cards)
#             draw_four=False
        

#         for c in p.cards:
#             if c.is_playable(Top_Value, Top_Color) == True:
#                 result=p.play_card(Top_Card.value, Top_Card.color)
#                 if result!=None:   #有牌
#                     Top_Card=result
#                     if is_first_card==False:
#                         if Top_Card.value=="skip":
#                             g.skip_player()
#                         elif Top_Card.value=="reverse":
#                             g.reverse()
#                         elif Top_Card.value=="+2":
#                             draw_two=True
#                         elif Top_Card.value=="+4":
#                             draw_four=True
#                         else:
#                             pass
#                         Top_Value=Top_Card.value
#                         Top_Color=Top_Card.color
#                         played=True
#                     else:
#                         is_first_card=False
#                     break

#                 else:   #沒牌
#                     #如果可以打，要打出去
#                     if p.draw_card(Total_Cards).is_playable(Top_Value, Top_Color):
#                         Top_Card=p.play_card(Top_Card.value, Top_Card.color)
#                         if Top_Card.value=="skip":
#                             g.skip_player()
#                         elif Top_Card.value=="reverse":
#                             g.reverse()
#                         elif Top_Card.value=="+2":
#                             draw_two=True
#                         elif Top_Card.value=="+4":
#                             draw_four=True
#                         else:
#                             pass
#                     # Total_Cards.remove(Top_Card)
#                     # if Total_Cards!=[]:
#                     # else:   #is_not_playable
#                     #     Top_Card=Total_Cards.pop(0)
#                     else:
#                         pass

#         if p.won()==True:
#             print(f"Player {p.ID} win!")
#             break

#         g.next_player()

    