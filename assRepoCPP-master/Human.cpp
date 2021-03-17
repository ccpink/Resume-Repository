//
// Created by ccpin on 12/8/2020.
//

#include <iostream>
#include "Human.h"
#include <random>
#include <utility>
#include <vector>
#include <algorithm>    // std::random_shuffle
#include <ctime>        // std::time
#include <cstdlib>      // std::rand, std::srand

Human::Human(int x1, int x2) : Entity(x1, x2) {}

//Human move function
void Human::move()
{
    incrementCounter();

    std::string direction = getRandomDirection();

    if(direction == "North") {
        _yPosition = _yPosition - 1;
    } else if(direction == "South") {
        _yPosition = _yPosition + 1 ;
    } else if (direction == "East") {
        _xPosition = _xPosition + 1;
    } else if (direction == "West") {
        _xPosition = _xPosition - 1;
    }
}

// Recruit a human
std::string Human::recruitHuman()
{
    std::string direction = getRandomDirection();

    if (direction == "North") {
        resetCounter();
        return "North";
    } else if(direction == "South") {
        resetCounter();
        return "South";
    } else if (direction == "East") {
        resetCounter();
        return "East";
    } else if (direction == "West") {
        resetCounter();
        return "West";
    }

    return "";
}

bool Human::canRecruit()
{
    return getCounter() - 1 >= 3;
}

Human::~Human() = default;
