'''
    Project
    Hasan Khwaja
    Puzzle game file
'''

import m1_prework
import m2_gameboard
import m3_placement

def run_game():
    '''
    Function: Takes in functions used to for puzzle game

    Runs completed puzzle game
    '''
    
    m2_gameboard.splash_screen() # get splash screen
    m3_placement.dialog_box() # Get user name and moves

    # construct game with default puzzle
    
    m1_prework.draw_tile()  
    m2_gameboard.get_hud()  
    m3_placement.get_mario_play() 

def main():
    run_game()

if __name__ == "__main__":
    main()
