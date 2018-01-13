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

# OA Amzn [Qualified]

  + Though process for subsequence problem : [a,b,c,a,b,c,a,d,e,d,e,f,d,g,h,i]

            Keep Extracting from the list given and pushing the new values into a queue or a list .
            Use while loop to shorten up the stack or can also use a for loop
            A = queue.Queue.()
            B = Left out of the sequence/stack
            if set(A)&set(B) :
                keep pushing as still we have the original values inside the queue
            else :
                Nothing is similar between the pushed seq(A) and the left sequences(B) , so you have got the complete sequence, clean the queue and increment counter
                You can store the sequence somewhere also like a list of lists
            return (final value of the counter)

            For the case when the sequence is [a, a, a], you will never reach the else part , for that case you would need to check this case.
            ```
            from collections import deque
            class Solution(object):
                """docstring for Solution."""
                def __init__(self):
                    super(Solution, self).__init__()

                def uniqueseq(self, seq):
                    q,stack,res = deque(seq),[],[]
                    while q:
                        stack.append(q.popleft())
                        if not (set(stack)&set(q)):
                            res.append(stack)
                            stack = []
                    return(len(res))
            obj = Solution()
            seq = ['a','b','c','a','b','c','a','d','e','d','e','f','d','g','h','i','g']
            #seq = ['a','a','a']
            print(obj.uniqueseq(seq))
            ```


# Text Justification [Level - Difficult]

 + Tried the Bottom Up approach , with O(n2) Time complexity , taken help for logic : https://www.youtube.com/watch?v=RORuwHiblPc
 + Next try memoization/top down approach ie, based on the MIT lecture

# TopologicalSort
 + Added Recurssive reverse DFS  to solve - try 1
 + Non Recurssive based on Kahn's approach - try 2

# Karatsuba recurssion for multiplying large numbers
 + https://en.wikipedia.org/wiki/Karatsuba_algorithm
```
def karatsuba(num1, num2):
  if len(num1)==1 or len(num2)==1:return num1*num2
  else:
    mid=max(len(num1),len(num2))/2
    a,b,c,d = num1 // 10^mid , num1%10^mid ,num2 // 10^mid , num2%10^mid
    ac = Karatsuba(a,c)
    bd = karatsuba(b,d)
    z = karatsuba(a+b, c+d) - ac - bd
    return (ac*10^(2*mid))+(z*10^(mid))+(bd)  
```

# Constructing a Binary Search tree for the given three Orders
  + Given Preorder , Postorder
  + Given Inorder ,  Preorder
  + Given Inorder ,  Postorder

# Very Nice Explaination of the Kosaraju's Algorithm for finding the SCCs .
 + http://theory.stanford.edu/~tim/w11/l/scc.pdf

# Great Algorithm Course
 + http://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15451-f13/www/

## CountInversions in a list using MergeSort
  ```
  Output:
  [1--100000], 2407905288)
  The time taken : 2.0174179077148438
  ```

## GG
  + BackTracking
    + SumString Problem , https://www.geeksforgeeks.org/check-given-string-sum-string/
    + permutations of a String problem , Different ways to do it. BFS/DFS/BackTracking

## Algorithms C1W2
  + Test set 3 (Quicksort)

  ```
  1. Let 0<α<.5 be some constant (independent of the input array length n). Recall the Partition subroutine employed by the QuickSort algorithm, as explained in lecture. What is the probability that, with a randomly chosen pivot element, the Partition subroutine produces a split in which the size of the smaller of the two subarrays is ≥α times the size of the original array?

  Ans: 1-2α

  2. Now assume that you achieve the approximately balanced splits above in every recursive call --- that is, assume that whenever a recursive call is given an array of length k, then each of its two recursive calls is passed a subarray with length between αk and (1−α)k (where α is a fixed constant strictly between 0 and .5). How many recursive calls can occur before you hit the base case? Equivalently, which levels of the recursion tree can contain leaves? Express your answer as a range of possible numbers d, from the minimum to the maximum number of recursive calls that might be needed.

  Ans: −log(n)/log(α) ≤d≤ −log(n)/log(1−α)

  3. Define the recursion depth of QuickSort to be the maximum number of successive recursive calls before it hits the base case --- equivalently, the number of the last level of the corresponding recursion tree. Note that the recursion depth is a random variable, which depends on which pivots get chosen. What is the minimum-possible and maximum-possible recursion depth of QuickSort, respectively?

  Ans: maximum = O(logn) and minumum = o(n)

  4. Consider a group of k people. Assume that each person's birthday is drawn uniformly at random from the 365 possibilities. (And ignore leap years.) What is the smallest value of k such that the expected number of pairs of distinct people with the same birthday is at least one?

  [Hint: define an indicator random variable for each ordered pair of people. Use linearity of expectation.]
  
  Ans:
  ```
