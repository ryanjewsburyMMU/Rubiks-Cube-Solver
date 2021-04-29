# Rubiks-Cube-Solver

Rubiks Cube Solver Using OpenCV. 

This is a current work in progress as it is my final project at university. I aim to add more documentation as the project becomes more finalised. 

The main solver class makes use of Rubik-Cube from PyPi
https://pypi.org/project/rubik-cube/

# Using The Solver
<details>
  <summary>Click to see code!</summary>
  
  ## Solving A Cube
  ``` Python
  from rubik.cube import Cube

  new_cube = Cube("OOOOOOOOOGGGWWWBBBYYYGGGWWWBBBYYYGGGWWWBBBYYYRRRRRRRRR")

  S = SolveCube(new_cube)

  S.solveCube()

  ```
</details>

