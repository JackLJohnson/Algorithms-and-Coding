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
  4   | Kosaraju's two Pass Algorithm for finding Strongly connected componenents | Python 3.x



# CREDITS
  - pseudocode : http://users.csc.calpoly.edu/~jdalbey/SWE/pdl_std.html
  - CLRS solutions references : http://clrs.skanev.com/
  - http://blog.moertel.com/posts/2013-05-11-recursive-to-iterative.html

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
  + **Heaps and Binary search trees**
    - CLRS Chapter 6,11,12,13
    - DPV Section 4.5
    - SW Section 3.3, 3.4

# Legacy Shortest path algorithms
 + Dijkstra's [Faster, More thought involved, needs D's greedy criterion]
 + Bellmanford [O(VE), slower but simpler, can get negative weigths also]    

# Coursera 2SUM Problem

 + Tried this using hashmap/Dictionary. improved the O(n^2) solution a bit by breaking immediately as we find a solution pair, removed all duplicates

        Size of the hashtable 999752
        427
        [Finished in 4722.281s]

+ After changing the logic , using the bisect module we can reduce the time crazy good , we find the leftmost and rightmost insert index as the samples array is already sorted for us , so we only need to look at that part of the array

        Size of samples 1000000
        427
        [Finished in 4.331s]
