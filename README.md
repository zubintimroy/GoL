# The Game of Life
This is a python project that produces a Game of Life Model simulation for visualisation using matplotlib or output measurement. The evolution of the Game of Life on a lattice is fully deterministic and is set by the following set of rules:

Rules:
1. Any live cell with less than 2 neighbours dies
2. Any live cell with 2 or 3 live neighbours lives on to the next step
3. Any live cell with more than 3 live neighbours dies
4. Any dead cell with exactly 3 live neighbours becomes alive

**N.B:** *In the Game of Life, it is conventional to consider as neighbours
all cells which have at least a point in contact with a given cell; i.e.
there are 8 neighbours for each cell (north, south, east, west, and the
four neighbours along the lattice diagonals)*

## Setup Python Virtual Environment and Install Packages
- ``` python -m pip install -U pip ```
- ``` pip install virtualenv ```
- ``` python -m venv env ```
- ``` pip install -r requirements.txt ```

## Activate Virtual Environment and Running the Script
- ``` .\env\Scripts\activate ```
- ``` python main.py Size of Lattice Dynamics Mode ```

## Outputs
Example output .txt files and visualisation python scripts using matplotlib include:

- Matplotlib visualisation of both random and pre determined initial conditions
- Histogram of the time needed to reach an equilibrium for simulations starting with a random initial condition
- Plot of the centre of mass vs time for the glider initial condition with fits and calculation of glider speed

