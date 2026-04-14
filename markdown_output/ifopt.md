\
![\|width=\"220\"](https://i.imgur.com/ZOfGZwB.png)

## Installation

```
$ sudo apt-get install ros-<distro>-ifopt
``` If this package has not yet made it to the
binaries or for additional information, visit
\'\'\'<https://github.com/ethz-adrl/ifopt>\'\'\'.

## Problem

Nonlinear with constraints.

![\|width=\"220\"](https://i.imgur.com/YGi4LrR.png)

## Solution

See
[here](https://github.com/ethz-adrl/ifopt/blob/master/ifopt_core/test/ifopt/test_vars_constr_cost.h)
how the above problem is formulated using Eigen. Then it can be solved
with, e.g. Ipopt, as: ```cplusplus
int main() {

  // Define the solver independent problem
  Problem nlp;
  nlp.AddVariableSet  (std::make_shared<ExVariables>());
  nlp.AddConstraintSet(std::make_shared<ExConstraint>());
  nlp.AddCostSet      (std::make_shared<ExCost>());

  // Initialize solver and options
  IpoptSolver ipopt;
  ipopt.SetOption("linear_solver", "mumps");
  ipopt.SetOption("jacobian_approximation", "exact");

  // Solve
  ipopt.Solve(nlp);

  std::cout << nlp.GetOptVariables()->GetValues().transpose() << std::endl;
}
```

Output: ```
1.00 0.00
```

## Publications

If you use this work in an academic context, please consider citing as
```
@misc{ifopt,
  author = {Alexander W Winkler},
  title  = {{Ifopt - A modern, light-weight, Eigen-based C++ interface to 
             Nonlinear Programming solvers Ipopt and Snopt.}},
  year   = {2018},
  doi    = {10.5281/zenodo.1135046},
  url    = {https://doi.org/10.5281/zenodo.1135046}
}
```

This software has been used in the following
[publications](https://www.alex-winkler.com):

  -- -------------------------------------------------------- -- -- --
     [Youtube](https://www.youtube.com/watch?v=0jE46GqzxMM)         
     [Youtube](https://www.youtube.com/watch?v=5WLeQMBuv30)         
  -- -------------------------------------------------------- -- -- --
