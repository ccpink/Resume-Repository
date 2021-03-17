cmake_minimum_required(VERSION 3.15)
project(ZombiesVSHumans)

set(CMAKE_CXX_STANDARD 14)

add_executable(ZombiesVSHumans main.cpp Zombie.cpp Zombie.h Human.cpp Human.h Entity.cpp Entity.h classValues.cpp classValues.h)