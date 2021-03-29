#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void solution(int numOfAllPlayers, int numOfQuickPlayers, char *namesOfQuickPlayers, int numOfGames, int *numOfMovesPerGame) {
    
}

struct input_data {
  int numOfAllPlayers;
  int numOfQuickPlayers;
  char *namesOfQuickPlayers;
  int numOfGames;
  int *numOfMovesPerGame;
};

void process_stdin(struct input_data *inputData) {
  int i = 0;
  size_t linecap = 0;
  char *line = NULL, *brkt = NULL, *token = NULL, *sep = " \n";

  getline(&line, &linecap, stdin);
  inputData->numOfAllPlayers = atoi(line);

  getline(&line, &linecap, stdin);
  inputData->numOfQuickPlayers = atoi(line);
  
  getline(&line, &linecap, stdin);
  inputData->namesOfQuickPlayers = calloc(inputData->numOfQuickPlayers, sizeof(char));
  for (i = 0, token = strtok_r(line, sep, &brkt); i < inputData->numOfQuickPlayers && token != NULL; i++, token = strtok_r(NULL, sep, &brkt)) {
    inputData->namesOfQuickPlayers[i] = token[0];
  }

  getline(&line, &linecap, stdin);
  inputData->numOfGames = atoi(line);

  getline(&line, &linecap, stdin);  
  inputData->numOfMovesPerGame = calloc(inputData->numOfGames, sizeof(int));
  for (i = 0, token = strtok_r(line, sep, &brkt); i < inputData->numOfGames && token != NULL; i++, token = strtok_r(NULL, sep, &brkt)) {
    inputData->numOfMovesPerGame[i] = atoi(token);
  }
}

int main() {
  struct input_data inputData;
  process_stdin(&inputData);

  solution(inputData.numOfAllPlayers, inputData.numOfQuickPlayers, inputData.namesOfQuickPlayers, inputData.numOfGames, inputData.numOfMovesPerGame);
  return 0;
}