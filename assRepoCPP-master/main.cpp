//
// Created by ccpin on 12/11/2020.
//

#include <iostream>
#include <ctime>
#include "Human.h"
#include "Zombie.h"
#include "vector"
#include <windows.h>
#include <algorithm>

using namespace std;

// Initialization Constants
const int gridSize = 50;

// Status Constants
const int _EMPTY = 0;
const int _HUMAN = 1;
const int _ZOMBIE = 2;

// Vector Initialization
vector<Zombie> ListOfAllZombies;
vector<Human> ListOfAllHumans;

// Grid Initialization
int grid[gridSize][gridSize] = { 0 };

// Initialization of all functions
pair<int, int> getCoordinates(int x, int y, string direction);
int getIdOfHumanAtLocation(int x, int y);
int getIdOfZombieAtLocation(int x, int y);
void removeKilledHumans(vector<int> killedHumans);
void removeStarvedZombies(vector<int> starvedZombies);
int getRandomNumber();
void InitializeEntities(int numOfZombies, int numOfHumans);
void getStarvedZombies();
void getRecruitedHumans();
void getTurnedZombies();
void moveAllZombies();
void moveAllHumans();
void printOut();
vector<string> getOpenSpacesZombie(Zombie &zombie);
vector<string> getOpenSpacesHuman(Human human);

void getTurnedZombies()
{
    vector<int> transformedHumans;
    vector<Zombie> newZombies;

    for (auto &zombie : ListOfAllZombies) {
        vector<string> openSpaces = getOpenSpacesZombie(zombie);

        if (! zombie.hasTarget() || ! zombie.canTurn()) {
            continue;
        }

        zombie.setOpenDirections(openSpaces);
        string direction = zombie.turnZombie();

        // When they turn they eat a bit so
        zombie.resetHunger();
        zombie.loseTarget();

        // The killed human
        pair<int, int> newPosition = getCoordinates(zombie.xPosition(), zombie.yPosition(), direction);

        int humanId = getIdOfHumanAtLocation(newPosition.first, newPosition.second);
        transformedHumans.emplace_back(humanId);

        // Set the new XY to 2
        grid[newPosition.second][newPosition.first] = _ZOMBIE;
        newZombies.emplace_back(Zombie(newPosition.first, newPosition.second));
    }

    removeKilledHumans(transformedHumans);

    for (auto zombie : newZombies) {
        ListOfAllZombies.emplace_back(zombie);
    }
}

pair<int, int> getCoordinates(int x, int y, string direction)
{
    int newX = 0;
    int newY = 0;

    if (direction == "North") {
        newY = y - 1;
        newX = x;
    } else if (direction == "South") {
        newY = y + 1;
        newX = x;
    } else if (direction == "East") {
        newY = y;
        newX = x + 1;
    } else if (direction == "West") {
        newY = y;
        newX = x - 1;
    } else if (direction == "North-West") {
        newY = y - 1;
        newX = x - 1;
    } else if (direction == "South-West") {
        newY = y + 1;
        newX = x - 1;
    } else if (direction == "North-East") {
        newY = y - 1;
        newX = x + 1;
    } else if (direction == "South-East") {
        newY = y + 1;
        newX = x + 1;
    }

    return make_pair(newX, newY);
}


void getRecruitedHumans()
{
    vector<Human> newHumans;

    for (auto &human : ListOfAllHumans) {
        string direction = "";
        vector<string> openSpaces = getOpenSpacesHuman(human);

        if (openSpaces.empty() || ! human.canRecruit()) {
            continue;
        }

        human.setOpenDirections(openSpaces);
        direction = human.recruitHuman();

        pair<int, int> newHuman = getCoordinates(human.xPosition(), human.yPosition(), direction);

        grid[newHuman.second][newHuman.first] = _HUMAN;
        newHumans.emplace_back(Human(newHuman.first, newHuman.second));
    }

    for (auto human : newHumans) {
        ListOfAllHumans.emplace_back(human);
    }
}

void getStarvedZombies()
{
    vector<int> starvedZombies;

    for (auto &zombie : ListOfAllZombies) {
        // For each zombie check if they are starved
        if (! zombie.isStarved()) {
            continue;
        }

        // Add the deleted zombies index to the deleted zombie index vector
        int zombieId = getIdOfZombieAtLocation(zombie.xPosition(), zombie.yPosition());
        starvedZombies.emplace_back(zombieId);

        // Make it return vector of pairs
        grid[zombie.xPosition()][zombie.yPosition()] = _HUMAN;
        ListOfAllHumans.emplace_back(Human(zombie.xPosition(), zombie.yPosition()));
    }

    removeStarvedZombies(starvedZombies);
}

// Get a random int between 0-gridSize
int getRandomNumber()
{
    return rand() % gridSize;
}

// Initialize all the zombie and human entities
void InitializeEntities(int numOfZombies, int numOfHumans)
{
    int x;
    int y;

    for (int i = 0; i < numOfZombies; i++) {
        while (true) {
            x = getRandomNumber();
            y = getRandomNumber();

            if (grid[y][x] == _EMPTY) {
                ListOfAllZombies.emplace_back(Zombie(x, y));
                grid[y][x] = _ZOMBIE;

                break;
            }
        }
    }

    for (int i = 0; i < numOfHumans; i++) {
        while (true) {
            x = getRandomNumber();
            y = getRandomNumber();

            if (grid[y][x] == _EMPTY) {
                ListOfAllHumans.emplace_back(Human(x, y));
                grid[y][x] = _HUMAN;
                break;
            }
        }
    }
}

// Get the open spaces for the zombie
vector<string> getOpenSpacesZombie(Zombie &zombie)
{
    int xPos = zombie.xPosition();
    int yPos = zombie.yPosition();
    vector<string> openSpaces; // Open or targets

    bool canHeadNorth = true;
    bool canHeadSouth = true;
    bool canHeadEast = true;
    bool canHeadWest = true;

    // Get the cardinal directions the entity can go
    if (xPos == gridSize - 1) {
        canHeadEast = false;
    }

    if (xPos == 0) {
        canHeadWest = false;
    }

    if (yPos == gridSize - 1) {
        canHeadSouth = false;
    }

    if (yPos == 0) {
        canHeadNorth = false;
    }

    // Get the directions the entity can go // Iteration 8 //
    if (canHeadNorth && grid[yPos - 1][xPos] == _HUMAN) {
        openSpaces.emplace_back("North");
    }

    if (canHeadSouth && grid[yPos + 1][xPos] == _HUMAN) {
        openSpaces.emplace_back("South");
    }

    if (canHeadEast && grid[yPos][xPos + 1] == _HUMAN) {
        openSpaces.emplace_back("East");
    }

    if (canHeadWest && grid[yPos][xPos - 1] == _HUMAN) {
        openSpaces.emplace_back("West");
    }

    if (canHeadNorth && canHeadEast && grid[yPos - 1][xPos + 1] == _HUMAN) {
        openSpaces.emplace_back("North-East");
    }

    if (canHeadNorth && canHeadWest && grid[yPos - 1][xPos - 1] == _HUMAN) {
        openSpaces.emplace_back("North-West");
    }

    if (canHeadSouth && canHeadWest && grid[yPos + 1][xPos - 1] == _HUMAN) {
        openSpaces.emplace_back("South-West");
    }

    if (canHeadSouth && canHeadEast && grid[yPos + 1][xPos + 1] == _HUMAN) {
        openSpaces.emplace_back("South-East");
    }

    // if there is a target**
    if (! openSpaces.empty()) {
        zombie.setTargeting();
        return openSpaces;
    }

    // If there are no humans to eat or targets
    if (canHeadNorth && grid[yPos - 1][xPos] == _EMPTY) {
        openSpaces.emplace_back("North");
    }

    if (canHeadSouth && grid[yPos + 1][xPos] == _EMPTY) {
        openSpaces.emplace_back("South");
    }

    if (canHeadEast && grid[yPos][xPos + 1] == _EMPTY) {
        openSpaces.emplace_back("East");
    }

    if (canHeadWest && grid[yPos][xPos - 1] == _EMPTY) {
        openSpaces.emplace_back("West");
    }

    if (canHeadNorth && canHeadWest && grid[yPos - 1][xPos - 1] == _EMPTY) {
        openSpaces.emplace_back("North-West");
    }

    if (canHeadNorth && canHeadEast && grid[yPos - 1][xPos + 1] == _EMPTY) {
        openSpaces.emplace_back("North-East");
    }

    if (canHeadSouth && canHeadEast && grid[yPos + 1][xPos + 1] == _EMPTY) {
        openSpaces.emplace_back("South-East");
    }

    if (canHeadSouth && canHeadWest && grid[yPos + 1][xPos - 1] == _EMPTY) {
        openSpaces.emplace_back("South-West");
    }

    return openSpaces;
}

// Get the open spaces the Human can go
vector<string> getOpenSpacesHuman(Human human) {
    int xPos = human.xPosition();
    int yPos = human.yPosition();
    vector<string> openSpaces; // Open or targets

    bool canHeadNorth = true;
    bool canHeadSouth = true;
    bool canHeadEast = true;
    bool canHeadWest = true;

    // Get the cardinal directions the entity can go
    if (xPos == gridSize - 1) {
        canHeadEast = false;
    }

    if (xPos == 0) {
        canHeadWest = false;
    }

    if (yPos == gridSize - 1) {
        canHeadSouth = false;
    }

    if (yPos == 0) {
        canHeadNorth = false;
    }

    // Get the directions the entity can go
    if (canHeadNorth && grid[yPos - 1][xPos] == _EMPTY) {
        openSpaces.emplace_back("North");
    }

    if (canHeadSouth && grid[yPos + 1][xPos] == _EMPTY) {
        openSpaces.emplace_back("South");
    }

    if (canHeadEast && grid[yPos][xPos + 1] == _EMPTY) {
        openSpaces.emplace_back("East");
    }

    if (canHeadWest && grid[yPos][xPos - 1] == _EMPTY) {
        openSpaces.emplace_back("West");
    }

    return openSpaces;
}

// Move all the zombie entities
void moveAllZombies()
{
    vector<int> killedHumans;

    for (auto &zombie : ListOfAllZombies) {
        vector<string> openSpaces = getOpenSpacesZombie(zombie);
        zombie.setOpenDirections(openSpaces);

        // Move the zombie, update the grid
        grid[zombie.yPosition()][zombie.xPosition()] = _EMPTY;
        zombie.move();

        grid[zombie.yPosition()][zombie.xPosition()] = _ZOMBIE;

        // Mark human for removal
        if (zombie.hasTarget()) {
            int id = getIdOfHumanAtLocation(zombie.xPosition(), zombie.yPosition());
            killedHumans.emplace_back(id);
            zombie.loseTarget();
        }
    }

    removeKilledHumans(killedHumans);
}

// Move all the human entities
void moveAllHumans()
{
    for (auto &human : ListOfAllHumans) {
        vector<string> openHumanSpaces = getOpenSpacesHuman(human);
        human.setOpenDirections(openHumanSpaces);

        // Move the human, update the grid
        grid[human.yPosition()][human.xPosition()] = _EMPTY;
        human.move();
        grid[human.yPosition()][human.xPosition()] = _HUMAN;
    }
}

// Print out the 2d array
void printOut()
{
    int column = 0;

    for (auto &row : grid) {
        for (int &value : row) {
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 15);
            column++;

            if (value == _EMPTY) {
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 15);
                cout << char(32);
            } else if (value == _HUMAN) {
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 3);
                cout << char(111);
            } else if (value == _ZOMBIE) {
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 4);
                cout << char(90);
            }

            if (column == gridSize) {
                column = 0;
                cout << "" << endl;
            }
        }
    }

    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 15);
    printf("Zombies: %d, Humans: %d\n", ListOfAllZombies.size(), ListOfAllHumans.size());
}

int main() {
    int zombiesLeft;
    int humansLeft;
    srand((unsigned) GetTickCount());
    // Entities on Grid
    InitializeEntities(maxZombie, maxHumans);

    double counter = 0;
    double pauseInterval = 0.9;
    clock_t startTime = clock();
    clock_t previousTime = startTime;

    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 15);
    int iterationNum = 1;
    cout << "" << endl << endl << endl << endl;
    cout << "Current Iteration: " << endl;
    cout << iterationNum << endl << endl << endl;
    printOut();

    while(true) {
        startTime = clock();
        counter += startTime - previousTime;
        previousTime = startTime;

        if (counter > (pauseInterval * CLOCKS_PER_SEC)) {
            moveAllZombies();
            moveAllHumans();
            getTurnedZombies();
            getRecruitedHumans();
            getStarvedZombies();

            iterationNum++;
            cout << "" << endl << endl << "Current Iteration: " << endl;
            cout << iterationNum << endl << endl;
            printOut();

            counter = 0;

            zombiesLeft = ListOfAllZombies.size();
            humansLeft = ListOfAllHumans.size();

            if (iterationNum == 1000 || zombiesLeft == 0 || humansLeft == 0) {
                cout << "Game Over..." << endl;
                break;
            }
        }
    }
}

int getIdOfHumanAtLocation(int x, int y)
{
    for (auto human : ListOfAllHumans) {
        if (x == human.xPosition() && y == human.yPosition()) {
            return human.id();
        }
    }
}

int getIdOfZombieAtLocation(int x, int y)
{
    for (auto zombie : ListOfAllZombies) {
        if (x == zombie.xPosition() && y == zombie.yPosition()) {
            return zombie.id();
        }
    }
}

void removeKilledHumans(vector<int> killedHumans)
{
    for (auto id : killedHumans) {
        ListOfAllHumans.erase(remove_if(ListOfAllHumans.begin(), ListOfAllHumans.end(), [&](Human human) -> bool {
            return human.id() == id;
        }), ListOfAllHumans.end());
    }
}

void removeStarvedZombies(vector<int> starvedZombies)
{
    for (auto id : starvedZombies) {
        ListOfAllZombies.erase(remove_if(ListOfAllZombies.begin(), ListOfAllZombies.end(), [&](Zombie zombie) -> bool {
            return zombie.id() == id;
        }), ListOfAllZombies.end());
    }
}
