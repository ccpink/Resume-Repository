//
// Created by ccpin on 12/8/2020.
//

#ifndef ZOMBIESVSHUMANS_HUMAN_H
#define ZOMBIESVSHUMANS_HUMAN_H

#include "vector"
#include "Entity.h"

class Human: public Entity
{
public:
    Human(int x1, int x2);

    std::string recruitHuman();
    void move() override;
    bool canRecruit();
    ~Human();
};


#endif //ZOMBIESVSHUMANS_HUMAN_H
