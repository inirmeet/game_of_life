# Conway's Game of Life!

Simple **Python** implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

## Logic of Game
The Game aka Universe consists of 2D grid of infinite numbers of cells. The state of a cell could be either living or dead. The Universe undergoes evolution, i.e. a cell may (or may not) change its state depending on the state of its neighbors. A cell can have from 3 to 8 neighbor depending upon its position in the grid.  

## The Rules

 1.  Any **live** cell with fewer than two live neighbors **dies**, as if by **underpopulation**.
2.  Any **live** cell with two or three live neighbors **lives** on to the next generation.
3.  Any **live** cell with more than three live neighbors **dies**, as if by **overpopulation**.
4.  Any **dead** cell with exactly three live neighbors becomes a **live** cell, as if by **reproduction**.
