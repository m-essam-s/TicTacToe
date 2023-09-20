/**
 * @file Tictactoe.c
 * @author Suara Ayomide (aysuarex@gmail.com)
 * 
 * multiPlayer - Driver function for multi-player mode
 * drawBoard - Draws the board for the player tokens
 * placeholder(); - Draws the board with the numbers 1-9 inscribed
 * checkWin - funtion that defines how to win the game
 * 
 * @date 2022-06-07
 */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include "main.h"
char position[9]= {'1', '2', '3', '4', '5', '6', '7', '8', '9'};
int turn;

void multiPlayer()
{
    char mark, mark_1, mark_2;
    char replay;
    char choice;
    int player;
    int Player_1, Player_2;
    unsigned int turn = 1;

    system("cls");
    printf("===============================\nWelcome to Multiplayer Mode!\n");
    Sleep(800);
    placeholder();

    Start: //Reference Point
    //Placeholders on game board
    position[0]= ' ';
    position[1]= ' ';
    position[2]= ' ';
    position[3]= ' ';
    position[4]= ' ';
    position[5]= ' ';
    position[6]= ' ';
    position[7]= ' ';
    position[8]= ' ';

    Sleep(1000);
    Mark: //Reference Point
    
    printf("-----------------------------------------------\n");
    printf("Player_1, Enter a choice (X or O): \n\t");
    scanf("%s", &mark);
    
    if (mark== 'X' || mark== 'x')
    {
        mark_1 = 'X';
        mark_2 = 'O';
        printf("Player_1 = X\nPlayer_2 = O\n");
    }   
    else if (mark == 'O' || mark== 'o') {
        mark_1 = 'O'; 
        mark_2= 'X';
        printf("Player_1 = O\nPlayer_2 = X\n");
    }
    else {
        printf("ERROR! Enter invalid Choice\n\n");
        Sleep(500);
        goto Mark;
    }

    Next: //Reference Point
    turn++;
    turn= (turn % 2);
    if(turn == 1)
        player = 1;
    else
        player = 2;

    Position: //Reference Point
    drawBoard();
    Sleep(500);
    printf("\nPlayer_%d's turn. Enter a position to play (1-9): \n\t", player);
    scanf("%s", &choice);
    if(player == 1) 
        mark = mark_1;
    else
        mark = mark_2;
    //mark = (player ==1) ? 'X' :'O'
    if(choice=='1' && position[0]==' ')
        position[0] = mark;
    else if(choice =='2' && position[1] ==' ')
        position[1] = mark;
    else if(choice =='3' && position[2] == ' ')
        position[2] = mark;
    else if (choice =='4' && position[3] == ' ')
        position[3] = mark;
    else if (choice =='5' && position[4] == ' ')
        position[4] = mark;
    else if (choice =='6' && position[5] ==' ')
        position[5] = mark;
    else if (choice =='7' && position[6] ==' ')
        position[6] = mark;
    else if (choice =='8' && position[7] == ' ')
        position[7] = mark;
    else if (choice =='9' && position[8] ==' ') 
        position[8] = mark;
    else {
        printf("ERROR! Invalid Option\n");
        turn--;
    }
    checkWin();
    if (checkWin() == 0)
    {
        drawBoard();
        printf("==> Game Draw \n\n\n");
        Sleep(500);

        Replay: //Reference point
        printf("Do you want to play again(Y/N)?  ");
        scanf("%s", &replay);
        
        if (replay == 'Y' || replay == 'y') {
            system("cls");
            goto Start;
        }
        else if (replay == 'N' || replay == 'n') {
            printf("\nGame Over!\n");
            Sleep(2000);
            system("cls");
            return;
        }  else {
            printf("=============================\nERROR!\n"
            "Press Y for Yes\n"
            "Press N for No\n"
            "\n=================================\n");
            Sleep(500);
            goto Replay;
        }
    }
    else if (checkWin() == 1)   {
        drawBoard();
        printf("\n\n\n==> Player_%d won!\n\n", player--);
        Sleep(500);
        
        printf("Do you want to play again(Y/N)?  ");
        scanf("%s", &replay);
        
        if (replay == 'Y' || replay == 'y') {
            system("cls");
            goto Start;
        }
        else if (replay == 'N' || replay == 'n') {
            printf("\nGame Over!\n");
            Sleep(2000);
            system("cls");
            return;
        }
        else {
            printf("=============================\nERROR!"
            "\nPress Y for Yes\n"
            "Press N for No\n"
            "\n=================================\n");
            Sleep(500);
            goto Replay;
        }
    }
    goto Next;
    return;
}

void drawBoard()
{
    printf("\t\t\t\t\t\t      |      |      \n");
    printf("\t\t\t\t\t\t   %c  |   %c  |  %c  \n", position[0], position[1], position[2]);
    printf("\t\t\t\t\t\t______|______|______\n");
    printf("\t\t\t\t\t\t      |      |      \n");
    printf("\t\t\t\t\t\t   %c  |   %c  |  %c  \n", position[3], position[4], position[5]);
    printf("\t\t\t\t\t\t______|______|______\n");
    printf("\t\t\t\t\t\t      |      |      \n");
    printf("\t\t\t\t\t\t   %c  |   %c  |  %c  \n", position[6], position[7], position[8]);
    printf("\t\t\t\t\t\t      |      |      \n");
    return;
}

void placeholder()
{
    printf("\t\t\t\t\t\t      |      |      \n");
    printf("\t\t\t\t\t\t   1  |   2  |  3   \n");
    printf("\t\t\t\t\t\t______|______|______\n");
    printf("\t\t\t\t\t\t      |      |      \n");
    printf("\t\t\t\t\t\t   4  |   5  |  6   \n");
    printf("\t\t\t\t\t\t______|______|______\n");
    printf("\t\t\t\t\t\t      |      |      \n");
    printf("\t\t\t\t\t\t   7  |   8  |  9   \n");
    printf("\t\t\t\t\t\t      |      |      \n");
    return;
}

int checkWin()
{
    if (position[0] == position[1] && position[1] == position [2] && position[1] != ' ')
        return 1;
    else if (position[3] == position[4] && position[4] == position[5] && position[4] != ' ')
        return 1;
    else if (position[6] == position[7] && position[7] == position[8] && position[7] != ' ')
        return 1;
    else if (position[0] == position[4] && position[4]== position[8] && position[4] != ' ')
        return 1;
    else if (position[0] == position[3] && position[3]== position[6] && position[3] != ' ')
        return 1;
    else if (position[1] == position[4] && position[4] == position[7] && position[4] != ' ')
        return 1;
    else if (position[2] == position[5] && position[5]== position[8] && position[5] != ' ')
        return 1;
    else if (position[2] == position[4] && position[4]== position[6] && position[4] != ' ')
        return 1;
    else if (position[0] != ' ' && position[1] != ' ' && position[2] != ' ' && position[3] != ' ' && position[4] != ' ' && position[5] != ' ' && position[6] != ' ' && position[7] != ' ' && position[8] != ' ')
        return 0;
    else 
        return -1;
}