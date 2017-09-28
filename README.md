# Algorithms-and-Coding
Coding with Language of Choice

# PSEUDOCODE STANDARD
  - The "structured" part of pseudocode is a notation for representing six specific structured programming constructs: SEQUENCE, WHILE, IF-THEN-ELSE, REPEAT-UNTIL, FOR, and CASE.
      + **SEQUENCE** is a linear progression where one task is performed sequentially after another.
      + **WHILE** is a loop (repetition) with a simple conditional test at its beginning.
      + **IF-THEN-ELSE** is a decision (selection) in which a choice is made between two alternative courses of action.
      + **REPEAT-UNTIL** is a loop with a simple conditional test at the bottom.
      + **CASE** is a multiway branch (decision) based on the value of an expression. CASE is a generalization of IF-THEN-ELSE.
  - Several keywords are often used to indicate common input, output, and processing operations.
      + Input: READ, OBTAIN, GET
      + Output: PRINT, DISPLAY, SHOW
      + Compute: COMPUTE, CALCULATE, DETERMINE
      + Initialize: SET, INIT
      + Add one: INCREMENT, BUMP    
  - An example

    **"Adequate"**

        FOR X = 1 to 10
            FOR Y = 1 to 10
                IF gameBoard[X][Y] = 0
                    Do nothing
                ELSE
                    CALL theCall(X, Y) (recursive method)
                    increment counter                  
                END IF
            END FOR
        END FOR

    **"Better"**

        Set moveCount to 1
        FOR each row on the board
            FOR each column on the board
                IF gameBoard position (row, column) is occupied THEN
                    CALL findAdjacentTiles with row, column
                    INCREMENT moveCount
                END IF
            END FOR
        END FOR    

## Table of Contents

Sl no | Program Description                         | Language
------|---------------------------------------------|---------------
  1   | +-90 degree rotation of an 2d array in different ways checking the time/space complexity| Python 3.x
  2   | Return list of indices of two sum of an array given a target | Python 3.x
  3   | Sorting Efficiently using Insertion sort, Mergesort or mixedsort | Python 3.x



# CREDITS
  - pseudocode : http://users.csc.calpoly.edu/~jdalbey/SWE/pdl_std.html
  - CLRS solutions references : http://clrs.skanev.com/

# Coursera - algorithms-graphs-data-structures
Suggested Readings :
  + **CLRS - Cormen, Leiserson, Rivest, and Stein, Introduction to Algorithms (3rd edition)**
  + **DPV - Dasgupta, Papadimitriou, and Vazirani, Algorithms**
  + **KT - Kleinberg and Tardos, Algorithm Design**
  + **SW - Sedgewick and Wayne, Algorithms (4th edition)**
      - CLRS Chapter 22
      - DPV Chapter 3
      - KT Chapter 3, Section 3.5, 3.6
      - SW Chapter 4, Section 4.1,4.2
