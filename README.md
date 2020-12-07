### fractal_lungs_critique
Various models for BIOL309 Final Paper Critique of:
Gas Diffusion through the Fractal Landscape of the Lung: How Deep Does Oxygen Enter the Alveolar System?
by Chen Hour, Stefal Gheorghiu, Marc-Olivier Coppens, Virginia H. Huxley, and Peter Pfeifer.

## To set up these programs:
Both programs are written in Python 3. https://www.python.org/
The simulations themselves require no extra packages, but the plotting was done using Matplotlib's Pyplot https://matplotlib.org/3.2.1/index.html

For installation instructions for Python3 or Matplotlib, refer to the websites above. 

# To install these in linux terminal:
```
$ cd ./your_program_folder
$ git clone https://github.com/afarme3/fractal_lungs_critique.git
$ cd ./fractal_lungs_critique
```
Optional, but it's nice to create a virtual environment
```
$ python3 -m venv . 
```
To install matplotlib using pip, 
```
$ python3 -m pip install matplotlib

```
To run either program, 
```
$ python3 velRatio.py
$ python3 minBifurcations.py
```

## About the programs
# velRatio.py 
This model corresponds with the "Velocity Reduction Ratio" section of our critique. 
Using the equations from Hou et al., it simulates 10 different bronchial trees with a tree diameter exponent of 2.0-3.0 in increments of 0.1. Each tree iterates 14 times.

The program outputs a pyplot graph corresponding to figure 1, and prints to terminal the multiDucts list. The first list shows the 10 values for tree diameter exponent used, and the second list shows the velocity ratio corresponding to those values. 

# minBifurcations.py
This model corresponds to the "Optimal Diffusion Gradients and the Peclet Number" section of our critique. 
Using the same equations for Hou et al., this program simulates 20 different bronchial trees with diameter exponent of 2.05-3.0 in increments of 0.05. The trees continue to iterate until the Peclet number is less than one, meaning there is suffeciently low concentration gradients of oxygen in the airway and optimal diffusion can take place. This simulation records the number of generations needed for this condition to be met, the initial/final velocity ratio at each final generation, and the diameter of the bronchial tube at each final generation. 

It outputs the ductInfo list to terminal. The first list shows the 20 values for tree diameter used. The second list shows the number of bifurcations needed to fulfill the Peclet condition for oxygen diffusion in each tree. The third shows the final/initial velocity ratio for each tree. The fourth shows the diameter of the final generation of bronchial tubes for each tree. This data is plotted using pyplot, corresponding to figures 2, 3 and 4. 

