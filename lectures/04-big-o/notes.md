# 04 — Big-O

how code slows as data grows

1. describes the performance of an algorithm as athe amount of data increases
2. machine independent (# of steps to completion)
3. ignore smaller operations

example: 
- 0(1): constant time
    random access of an element in array
- 0(n): linear time
- searching through a linked list
- 0(log n): logarithmic time
    binary search
- 0(n^2): quadratic time
    insertion, selection, and bubble sort
- 0(n log n): quasilinear time
  quicksort, mergesort, heapsort

  
*n = amount of data (varable like x or y)*

## They do
- [ ] big-O intuition: nested loops get slow (~10 min)

# 0(1) constant time
int addUpp(int n){ 
  int sum = n * (n + 1) / 2;
  return sum;
}

# 0(n) Linear Time
int addUp(int n) {
  int sum = 0;
  for (int i = 0; i <= n; i++) {
    sum += i
    }
  return sum;
}

# 0(log n)

# o(n^2)

## We do
- rep 1:

## I do (unseen, solo)
- attempt:

## Stuck points
- i have sorting algorithms as repos in my main, any way i can reference back to shell/comb/other sort?

- constant time is better than linear but how is it more efficient?
