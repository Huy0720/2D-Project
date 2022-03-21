# 2D Project
This is a SUTD Computer Science Term 4 2D Project (executed in one week), comprised of these courses:

* 50.001 Introduction to Information Systems & Programming (sat-solver)
* 50.002 Computation Structures (optimized-adder)
* 50.004 Introduction to Algorithms (Kosaraju-solver)

## Computational Equivalent Checking (CEC) Verifier
For the CEC Verifier, we implemented a Davis–Putnam–Logemann–Loveland (DPLL) algorithm as the default algorithm. This program takes a .cnf file as the input, and verifies whether the circuit is logically possible (Satisfiable). 

## OPtimized 32-bit adder
A simple circuit simulation done in jsim (proprietary language by MIT). This circuit follows a similar concept to the Brent-Kung adder circuit, but with slight modifications which enhance the runtime of the adder (by running 2 16-bit adders asynchronously).

## 2 SAT Solver
For the deterministic 2-SAT Solver, we implemented Kosaraju's algorithm to achieve polynomial time asymptotics. 
A detailed explanation of the implementation as well as performance analysis can be found in the 50.004 report.
