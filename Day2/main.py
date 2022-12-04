import numpy as np
import pandas as pd
import os
from enum import Enum

# -> Ground rules:
    # -> Player 1
        # - A : Rock
        # - B : Paper
        # - C : Scissors
    # -> Player 2
        # - X : Rock
        # - Y : Paper
        # - Z : Scissors
    # -> Score for each shape
        # Rock - 1
        # Paper - 2
        # Scissors - 3
    # -> Score for each round
        # 0 lost
        # 3 draw 
        # 6 won

# -> Example:
    # A Y -> Player 1 : 1 ; Player 2 : 2 -> Player 1 : 1 + 0 = 1 ; Player 2 : 2 + 6 = 8 -> Player 2 Wins
    # B X -> Player 1 : 2 ; Player 2 : 1 -> Player 1 : 2 + 6 = 8  ; Player 2 : 1 + 0 = 1 -> Player 1 Wins
    # C Z -> Player 1 : 3 ; Player 2 : 3 -> Player 1 : 3 + 3 = 6 ; Player 2 : 3 + 3 = 6 -> Draw
    # B Z -> Player 1 : 2 ; Player 2 : 3 -> Player 1 : 2 + 0 = 2 ; Player 2 : 3 + 6 = 9 -> Win
    # Total -> Player 1 : 15 ; Player 2 : 15

#    A X -> Draw
#    B X -> Lose
#    C X -> Win
#    A Y -> Win
#    B Y -> Draw
#    C Y -> Lose
#    A Z -> Lose
#    B Z -> Win
#    C Z -> Draw

absolute_path = os.path.dirname(__file__)

class Shape1(Enum):
    A = 1
    B = 2
    C = 3

class Shape2(Enum):
    X = 1
    Y = 2
    Z = 3

def is_win(key1, key2):
        d={
            (Shape2.X,Shape1.C): True,
            (Shape2.Z,Shape1.B): True,
            (Shape2.Y,Shape1.A): True,
         }
        return d.get((key1,key2),False)

def is_draw(key1, key2):
    d={
        (Shape2.Z,Shape1.C): True,
        (Shape2.Y,Shape1.B): True,
        (Shape2.X,Shape1.A): True,
        }
    return  d.get((key1, key2),False)

def calculate_result_player_2_(x):
    shape1 = Shape1[x['Player1']]
    shape2 = Shape2[x['Player2']]

    result = 0
    if is_win(shape2,shape1):
        result = 6 
    elif is_draw(shape2,shape1):
            result = 3
    else :
        result = 0
    
    result += shape2.value
    print(result)
    return  (result)

def calculate_part1():
    input_file  = os.path.join(absolute_path, 'input.txt')

    df = pd.read_table(input_file, delimiter=" ", names=['Player1','Player2'])
    #df = df.reset_index()    

    df['Result'] = df.apply(lambda x : calculate_result_player_2_(x), axis=1) 
    

    print(df['Result'].sum())
    return df

##Part 2
# X -> means lose
# Y -> means draw
# Z -> means Win 

def calculate_part2(df):

    def convert_strategy_guide(x):
        shape1 = Shape1[x['Player1']]
        shape2 = Shape2[x['Player2']]

        def gets_win(key) :
            d={
            (Shape1.C) : Shape2.X.name,
            (Shape1.B) : Shape2.Z.name,
            (Shape1.A) : Shape2.Y.name,
            }
            return  d.get((key),False)

        def gets_draw(key) :
            d={
            (Shape1.C) : Shape2.Z.name,
            (Shape1.B) : Shape2.Y.name,
            (Shape1.A) : Shape2.X.name,
            }
            return  d.get((key),False)

        def gets_lose(key) :
            d={
            (Shape1.B) : Shape2.X.name,
            (Shape1.C) : Shape2.Y.name,
            (Shape1.A) : Shape2.Z.name,
            }
            return  d.get((key),False)

        def get_match_fix(player2,player1) :
            d={
            (Shape2.X) : gets_lose,
            (Shape2.Y) : gets_draw,
            (Shape2.Z) : gets_win,
            }
            return  d.get((player2),False)(player1)
        x['Player2'] = get_match_fix(shape2, shape1)
        return x

    df = df.apply(lambda x : convert_strategy_guide(x), axis=1)
    df['Result'] = df.apply(lambda x : calculate_result_player_2_(x), axis=1) 

    print(df['Result'].sum())
    return df
    

def main():
    df = calculate_part1()
    df = calculate_part2(df)
    df = df.replace(to_replace=["A", "X"],
           value="Rock")
    df = df.replace(to_replace=["B", "Y"],
           value="Paper")
    df= df.replace(to_replace=["C", "Z"],
           value="Scissors")

    print(df)


if __name__ == "__main__":
    main()

