#!/bin/bash


conan remove -f top/1.0.0
conan remove -f mid_left/1.0.0
conan remove -f mid_right/1.0.0
conan remove -f lower/1.0.0


conan create ./lower -o my_option=a
conan create ./lower -o my_option=b
conan create ./mid_left
conan create ./mid_right
conan create ./top