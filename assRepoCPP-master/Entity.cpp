//
// Created by ccpin on 12/8/2020.
//

#include "Entity.h"

int Entity::idCounter = 0;

// Entity Constructor
Entity::Entity(int x, int y)
{
    this->_xPosition = x;
    this->_yPosition = y;
    _id = ++idCounter;
}

// Set the counter to 0
void Entity::resetCounter()
{
    counter = 0;
}

// Get the counter
int Entity::getCounter()
{
    return counter;
}

// Get the x position I never use this :)
int Entity::xPosition()
{
    return _xPosition;
}

// Get the y position I never use this :)
int Entity::yPosition()
{
    return _yPosition;
}

int Entity::id()
{
    return _id;
}

// Increment the counter :)
void Entity::incrementCounter()
{
    counter++;
}

void Entity::setOpenDirections(std::vector<std::string> directions)
{
    openDirections = directions;
}

std::string Entity::getRandomDirection()
{
    return ! openDirections.empty() ? openDirections.at(rand() % openDirections.size()) : "";
}

Entity::~Entity() = default;
