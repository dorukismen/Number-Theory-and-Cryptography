# Number-Theory-and-Cryptography
Coursera course Number Theory and Cryptograph quize answers

This repository includes the course's quiz answers. The answers are mostly done by me and some of codes are inspired by Google :)

- Tile-a-Rectangle-with-Squares - 

Given an n × m grid (where n,mn,m are integers), we would like to tile it with the minimal number of same size squares. Clearly, it can always be tiled with nm squares of size 1 × 1, but it is not always optimal. For example, a 6 × 10 grid can be tiled by 15 squares of size 2 × 2.

My goal in this problem is to implement a function squares(n, m) that returns the minimum number of same size squares required to tile a grid of size n × m.

- Diophantine-Equations -

Solving two unknown parameter equations ( Diophantine Equations)

This solution is taken from "http://new.math.uiuc.edu/public348/python/jimcarlsonpy.pdf" and the following paragraphs are taken from the same site.

We will use the recursive implementation of the Euclidean algorithm to design a function isolve for solving the Diophantine equation ax + by = c. (1) Such equations are solvable if and only if the gcd(a, b) divides c. First note that if b divides a then we can write down a solution: x = 0, y = c/b. If b does not divide a, write a = bq + r as in the (long) divsion algorithm and then substitute into (1): (bq + r)x + by = c. Rearrange as b(qx + y) + rx = c. Set u = qx + y, v = x and substitute again to obtain the equation bu + rv = c. (2) We have reduced the equation (1) to the equivalent equation (2) with smaller coefficients. If we can solve the new equation, then we recover a solution of the old equation by the formulas x = v, y = u − qv. 11 The process eventually terminates (by the theory of the Euclidean algorithm) with an equaiton where the second coefficient divides the first. These ideas are embodied in the Python code below. Note the use of the divmod operation to compute the quotient and remainder at the same time. The function divmod returns a pair of numbers, the quotient and remainder, which we store in q, r. Note also the use of lists for the return value.

- Modular Division -

Now that we know how to use extended Euclid's algorithm for finding modular inverses, implement an efficient algorithm for dividing b by a modulo n.

Given three integers a, b, and n, such that gcd(a,n)=1 and n > 1, the algorithm should return an integer x such that

0 <= x <=  n - 1, and

b / a = x (modn) (that is, b = a x (modn)).