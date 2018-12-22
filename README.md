## Generate all partition's of a set and the set of equivalence relations


This is a bonus problem for the Algebra course at the UBB University

### About the source code

To represent a partition, we will use a vector of integers, each integer representing the number of the subset in which
the corresponding element is in

Partitioning -> Encoding
* {1, 2, 3} -> (1, 1, 1)
* {1} {2, 3} -> (2, 1, 1)
* {2} {1, 3} -> (1, 2, 1)
* {1, 2} {3} -> (2, 2, 1)
* {1} {2} {3} -> (3, 2, 1)

If we write the encodings backwards we obtain:
* 111
* 112
* 121
* 122
* 123

**Be aware that** the number 113 is missing because the encodings 112 and 113 translate to the same partitions

So, for a partition we just need to generate all the numbers with n-1 "digits"  and the difference between the biggest
two digits should be 1

#### If the number of elements of the set is to big(>10) we generate only the number of partitions of that set using [Bell's triangle](https://en.wikipedia.org/wiki/Bell_triangle)

