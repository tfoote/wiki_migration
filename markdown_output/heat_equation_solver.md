## Algorithm

In a n-dimensional grid, each cell is connected to its 2n neighbors by a
thermal conductivity k (called \"smoothness\" in the code), and to an
external temperature source, with temperature and thermal conductivity
given as input.

This class computes the equilibrium solution according to the heat
equation. It can give an approximate solution using a multigrid method,
i.e. solving first on a very coarse grid and extending the solution to
finer and finer grids, and it can solve iteratively the original system
(finest grid). All vector operations rely on Eigen.

Here is an example solution in 2D (rendered with matlab).

  -- ------------------------------------------------- -- ------------------------------------------------- --
     \<)\> Input sources of heat and cold                 \<:\> ![](attachment:heat_equation_solver1.png)   
     \<)\> Equilibrium solution of the heat equation      \<:\> ![](attachment:heat_equation_solver2.png)   
  -- ------------------------------------------------- -- ------------------------------------------------- --
