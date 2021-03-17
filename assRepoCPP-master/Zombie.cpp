//
// Created by ccpin on 12/8/2020.
//

#include<string>
#include <iostream>
#include <utility>
#include <vector>
#include "Zombie.h"
#include <random>
#include <algorithm>    // std::random_shuffle

Zombie::Zombie(int x, int y) : Entity(x, y) {}

// Get a direction for the human that is being turned into a zombie
std::string Zombie::turnZombie()
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
    } else if (direction == "North-West") {
        resetCounter();
        return "North-West";
    } else if (direction == "South-West") {
        resetCounter();
        return "South-West";
    } else if (direction == "North-East") {
        resetCounter();
        return "North-East";
    } else if (direction == "South-East") {
        resetCounter();
        return "South-East";
    }

    return "You're Stupid :)";
}

// Move all zombies
void Zombie::move()
{
    if (hasTarget()) {
        resetHunger();
    } else {
        incrementHunger();
    }

    incrementCounter();

    std::string direction = getRandomDirection();

    int x = _xPosition;
    int y = _yPosition;

    if (direction == "North") {
        _yPosition = _yPosition - 1;
    } else if(direction == "South") {
        _yPosition = _yPosition + 1;
    } else if (direction == "East") {
        _xPosition = _xPosition + 1;
    } else if (direction == "West") {
        _xPosition = _xPosition - 1;
    } else if (direction == "North-West") {
        _yPosition = _yPosition - 1;
        _xPosition = _xPosition - 1;
    } else if (direction == "South-West") {
        _yPosition = _yPosition + 1;
        _xPosition = _xPosition - 1;
    } else if (direction == "North-East") {
        _yPosition = _yPosition - 1;
        _xPosition = _xPosition + 1;
    } else if (direction == "South-East") {
        _yPosition = _yPosition + 1;
        _xPosition = _xPosition + 1;
    }
}

bool Zombie::isStarved()
{
    return (_lastEaten - 1 >= 3);
}

void Zombie::resetHunger()
{
    _lastEaten = 0;
}

void Zombie::incrementHunger()
{
    _lastEaten++;
}

int Zombie::getLastEaten() {
    return _lastEaten;
}

bool Zombie::canTurn()
{
    return getCounter() - 1 >= 8;
}

void Zombie::setTargeting()
{
    _hasTarget = true;
}

void Zombie::loseTarget()
{
    _hasTarget = false;
}

bool Zombie::hasTarget()
{
    return _hasTarget;
}

Zombie::~Zombie() = default;


