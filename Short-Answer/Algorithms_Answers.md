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

Let's discuss a solution to a general problem with 'n' eggs and 'k' floors. The solutions is to try dropping an egg from every floor (from 1 to k) and recursively calculate the minimum number of droppings needed in the worst case. The floor which gives the minimum value in the worst case is going to be part of the solution. 

We return the minimum number of trials in the worst case. 

Meaning of a worst-case scenarios: It gives the user the surety of the threshold floor. i.e. If we have '1' egg and 'k' floors, we will start dropping the egg from the first floor till the egg breaks suppose on the 'kth' floor so the number of tries to give us surety is 'k'. 

When we drop an egg from a floor x, there can be two cases (1) The egg breaks, (2) The egg doesn't break. 

If the egg breaks after dropping from 'xth' floor, then we only need to check for floors lower than 'x' with remaining eggs as some floor should exist lower than 'x' in which egg would not break: so the problem reduces to x-1 floors and n-1 eggs. 

If the egg doesn't break after dropping from the 'xth' floor, then we only need to check for floors higher than 'x'; so the problem reduces to 'k-x' floors and n eggs. 

Since we need to minimize the number of trials in worst case, we take the maximum of two cases. We consider the max of above two cases for every floor and choose the floor which yields minimum number of trials. 

# Pseudocode

k => Number of floors 
n => Number of eggs 
eggDrop(n, k) => Minimum number of trials needed to find the critical floor in worst case. 

eggDrop(n, k) = 1 + min{max(eggDrop(n - 1, x -1), eggDrop(n, k -x)), where x is in {1, 2, ..., k}}

Concept of worst case: 
i.e.: Let there be '2' eggs and '2' floors then:

If we try throwing from '1st' floor:
Number of tries in worst case = 1 + max(0, 1)

0 => If the egg breaks from first floor then it is threshold floor (best case possibility)
1 => If the egg does not break from first floor, we will now hav '2' eggs and 1 floor to test which will give answer as '1' (worst case possibility)
We take the worst case possibility in account, so 1 + max(0, 1) = 2

If we try throwing from '2nd' floor: 
Number of tries in worst case = 1 + max(1, 0)
1 => If the egg breaks from second floor, then we will have 1 egg and 1 floor to find threshold floor. (Worst Case)
0 => If egg does not break from second floor, then it is threshold floor. (Bets Case)
We take worst case possibility for surety, so 1 + max(1, 0) = 2

The final answer is min(1st, 2nd, 3rd ..., kth floor)
So answer here is '2'


## Dynamic Programming method: 

The dynamic programming solution is based on above recursive nature of the problem. 

We work on the idea of neglecting the case of calculating the answers to sub-problems again and again. The approach will be to make a table which will store the results of sub-problems so that to solve a sub-problem, it would only require a look-up from the table which will take constant time, which ealier took expenential time

Filling DP[n][k] state where 'n' is the number of eggs and 'k' is the number of floors: 

We have to traverse for each floor 'x' from '1' to 'k' and find minimum of: (1 + max( DP[n-1][k-1], DP[n][k-x] ))

n => Number of eggs
k => Number of floors
Look up find maximum
Let's fill the table for the following case:
Floors = '4'
Eggs = '2'

1 2 3 4

1 2 3 4 => 1 

1 2 3 4 => 2

For 'egg-1' each case is the base case so the number of attempts is equal to floor number.

For 'egg-2' it will take '1' attempt for 1st floor which is base case.

For floor-2 => 
Taking 1st floor 1 + max(0, DP[1][1])
Taking 2nd floor 1 + max(0, DP[1][1], 0)
DP[2][2] = min(1 + max(0, DP[1][1]), 1 + max(DP[1][1],0))

For floor-3 => 
Taking 1st floor 1 + max(0, DP[2][2])
Taking 2nd floor 1 + max(DP[1][1], DP[2][1])
Taking 3rd floor 1 + max(0, DP[2][2])
DP[2][3] = min('all three floors) = 2

For floor-4 => 
Taking 1st floor 1 + max(0, DP[2][3])
Taking 2nd floor 1 + max(DP[1][1], DP[2][2])
Taking 3rd floor 1 + max(DP[1][2], DP[2][1])
DP[2][4] = min('all four floors) = 3


# Runtime Complexity

Time Complexity: O(N * K^2). Where 'N' is the number of eggs and 'K' is the number of floors, as we use a nested for loop 'K^2' times for each egg

Auxiliary Space: O(N * K). As a 2-D array of size 'N*K' is used for storing elements





