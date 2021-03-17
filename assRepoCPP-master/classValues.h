//
// Created by ccpin on 12/9/2020.
//

#ifndef ZOMBIESVSHUMANS_CLASSVALUES_H
#define ZOMBIESVSHUMANS_CLASSVALUES_H

#include <vector>


class classValues {

private:

public:
    classValues();

    const int GRIDSIZE = 20; // size of the square grid
    const int HUMAN_STARTCOUNT = 100; // inital Humans
    const int ZOMBIE_STARTCOUNT = 5; //initial Zombie count
    const int HUMAN_BREED = 3; // steps until an Human breeds
    const int ZOMBIE_BREED = 8; // steps until an Zombie breeds
    const int ZOMBIE_STARVE = 3; // steps until a Zombie starves and converts back
    const char HUMAN_CH = 111;//79 "o"// ascii Human
    const char SPACE_CH = 32; // " " ascii space
    const char ZOMBIE_CH = 90;//90 "Z"// ascii zombie
    const double PAUSE_SECONDS = .09; // pause between steps
    const int ITERATIONS = 1000; // max number of steps
    const int HUMAN_COLOR = 3; // turquoise
    const int ZOMBIE_COLOR = 14; // bright yellow
};


#endif //ZOMBIESVSHUMANS_CLASSVALUES_H
