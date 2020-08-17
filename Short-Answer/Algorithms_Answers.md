#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The running time of this snippet of pseudocode (while loop) with respect to the input size n of each is O(N). The loop executes N times, so the sequence of statements also executes N times. Since we assume the statements are O(1), the total time for the while loop is N * O(1), which is O(N) overall.


b) The running time of this snippet (nested loops) of pseudocode with respect to the input size n of each is O(N^2). 

First, we will consider loops where the number of iterations of the inner loop is dependent of the value of the outer loop's index. We can't just multiply the number of iterations of the outer loop times the number of iterations of the inner loop, because the inner loop has a different number of iterations each time. So, let's think about how many iterations that inner loop has: 

Value of j        Number of iterations of inner loop
0                 N
1                 N-1
2                 N-2
...               ...
N-2               2
N-1               1

So, we can see that the total number of times the sequence of statements executes is: N + N-1 + N-2 + ... + 3 + 2 + 1


c) The running time of this snippet of pseudocode (if-then-else statement) with respect to the input size n of each is O(N) because either sequence 1 will execute, or sequence 2 will execute. Therefore, the worst-case time is the slowest of the two possibilities: max(time(sequence 1), time(sequence 2)). In this case, the sequence 1 is O(1) and sequence 2 is O(N), the worst-case time for this whole if-then-else statement would be O(N).


## Exercise II

We can make a few assumptions:

1. If an egg doesn't break when dropped from some floor, then it will not break when dropped from any lower floor

2. An egg that survives a fall can be used again

3. A broken egg must be discarded

4. The effect of a fall is the same for all eggs

5. If an egg breaks when dropped, then it would break if dropped from a higher floor

# My proposed algorithm (Binary Search Solution) in plain English

n = n-story building
f = Number of floors 
e = Number of eggs 

1. drop an egg from floor n/2

2a. if it breaks, drop the next egg from floor n/4

2b. if it doesn't break, drop the next egg from floor (3/4n)

If I have a certain number of floors and I'm trying to figure out where the "target point" is to see where the egg will break, I'd split the number of floors in half and start from there.

If I have 10 floors, I'd start at the 5th floor (n/2). If I drop an egg from there and it doesn't break, I'd split the top 5 in half and go up to the 7th floor and drop it. If it breaks at 7 but didn't at 5, then 6 is the target floor. 

But, if it broke at 5, I would split the bottom 5 in a half and go to the 2nd floor to drop an egg. If it doesn't break, I'd go up to the 4th floor. If it breaks there, I'd go down to 3rd floor. If it doesn't break there, that is the floor.

Regardless of the number of floors, I'd split the floors and continue to split the floors in a "binary search tree" until I found the "f-floor". 

# Runtime Complexity

Time Complexity: O(Log N). Logarithmic time. The algo increases the number of operations it performs as the logarithmic function of the input size n. 

The function log n grows very slowly. As n gets larger, the number of operations the algorithm needs to perform does not increase by very much.




