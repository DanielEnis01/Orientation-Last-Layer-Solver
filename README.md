# Orientation-Last-Layer-Solver
 - Python based rubix cuber solver. View current tag to download latest version.
 - Understanding notation of the Rubix Cube: https://jperm.net/3x3/moves
 - Additional Documentation can be found @ [danielenis.dev](https://danielenis.dev/ollsolver.html)

`Interface`

![Screenshot 2025-03-10 131005](https://github.com/user-attachments/assets/2e1a0b11-3b62-495a-af94-124845a4e4ec)

- The squares represent the yellow face of the rubix cube (side with the yellow center)
- The rectangles represent the 'edges' of the yellow face, or the top rows from the adjecent sides
- Patterns will look similar to the following: 

![05-yellow-top](https://github.com/user-attachments/assets/9865e8eb-0b41-4f9a-aa23-3cc331698162)

- Click each square and edge to directly map to your cube's respective pattern.
- There should only be 9 highlighted buttons, for there are only 9 yellow squares on a rubix cube.
- When every button is highlighte, click the solve button and a solving sequence will be printed.

![Screenshot 2025-03-10 131420](https://github.com/user-attachments/assets/ae25254c-1da2-450d-b41a-91f788cdd265)

- The solve sequence is a list of rubix cube notation moves to be read from left to right (https://jperm.net/3x3/moves)
- Hold the cube with the side that correlates to the bottom of the gui facing yourself, and proceed with notation moves.
- If directions are followed correctly, the sequence will either lead to a new pattern or fully solve the yellow face.
- If the cube isn't fully solved (new pattern), repeat the process as the gui says.
