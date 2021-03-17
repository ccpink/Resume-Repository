//
// Created by ccpin on 12/8/2020.
//

#ifndef ZOMBIESVSHUMANS_ENTITY_H
#define ZOMBIESVSHUMANS_ENTITY_H

#include <vector>
#include <string>

class Entity
{
private:
    int _id;
    static int idCounter;
protected:
    int _xPosition;
    int _yPosition;
    int counter = 0;
    std::vector<std::string> openDirections;
    std::string getRandomDirection();
public:
    Entity(int x, int y);

    void resetCounter();
    int getCounter();
    void incrementCounter();
    virtual void move() = 0;
    int xPosition();
    int yPosition();
    int id();
    void setOpenDirections(std::vector<std::string> directions);

    ~Entity();
};

#endif //ZOMBIESVSHUMANS_ENTITY_H
