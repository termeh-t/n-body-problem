# N-Body Problem Simulation (2-Body Case)

This project is a simple numerical simulation of the **N-Body Problem**, specifically for **two interacting bodies** under Newtonian gravity. It was developed as part of a **Physics assignment** at university.

## Overview
The program models the motion of two bodies under their mutual gravitational attraction and visualizes their orbits in a **3D animation** using `matplotlib`.

## Features
- **Numerical Integration**: Updates positions and velocities using Newton's second law.
- **Graphical User Interface (GUI)**: Uses `tkinter` to take user input for initial conditions.
- **3D Animation**: Utilizes `matplotlib.animation` to visualize the motion.

## Dependencies
Ensure you have the following Python libraries installed:
```sh
pip install numpy matplotlib
```

## How It Works
1. **User Input**: The program prompts the user for mass and initial velocities of two objects via `tkinter` dialogs.
2. **Simulation**:
   - Computes acceleration due to gravity using Newton's Law of Universal Gravitation. The calculation is rather simple and uses basic mathematics as it is sufficent for two objects. I had intially planned to use Runge-Kutta approximations. However, the physics understanding of the n-body problem is not straight-forward and requires deep knowledge in the field. 
   - Updates position and velocity using time-stepping.
3. **Visualization**:
   - Displays a 3D animated trajectory of the two bodies.

## Code Structure
- `Mass` Class: Represents a body with mass, position, velocity, and methods for motion calculation.
- `calculate_coordinates()`: Performs the numerical simulation over a time span.
- `update()`: Updates the animation frame-by-frame.
- `FuncAnimation`: Animates the motion of the bodies in 3D.

## Running the Program
Run the script using:
```sh
python main.py
```
Follow the GUI prompts to enter values for mass and velocity.

## Future Improvements
- Extend to **N-Body Problem** (more than two bodies).
- Implement **energy conservation checks**.
- Improve numerical accuracy using **Runge-Kutta integration**.
- Add user-controlled **initial conditions through a GUI**.

## Author
Developed as part of a **Physics assignment** at Guilan university.

