#ifndef __MAIN_H__
#define __MAIN_H__


//prototypes for multiplayer mode
void multiPlayer();
void drawBoard();
void placeholder();
int checkWin();

//prototypes for single player mode
void singlePlayer();
void computerMove();
void playerMove();
void resetBoard();
void printBoard();
int checkFreeSpaces();
char checkWinner();
void printWinner(char);


#endif