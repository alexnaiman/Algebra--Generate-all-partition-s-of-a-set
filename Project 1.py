# Globally scoped variables
'''
To represent a partition, we will use a vector of integers, each integer representing the number of the subset in which
the corresponding element is in
Partitioning -> Encoding
{1, 2, 3} -> (1, 1, 1)
{1} {2, 3} -> (2, 1, 1)
{2} {1, 3} -> (1, 2, 1)
{1, 2} {3} -> (2, 2, 1)
{1} {2} {3} -> (3, 2, 1)

If we write the encodings backwards we obtain:
111
112
121
122
123
! the number 113 is missing because the encodings 112 and 113 translate to the same partitions
So, for a partition we just need to generate all the numbers with 1-n "digits"  and the difference between the biggest
two digits should be 1
'''

partitions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # the encoding of one partition - we make the number to be
n = 0  # the number of elements of the subset
numberOfSubsets = 0  # the number of subsets we have in the actual partition we generate( the maximum digit
                        # we can have in an encoding)
numberOfPartitions = 0  # the number of partitions we generate


def bell_numbers(start, stop):

    t = [[1]]                        # Initialize the triangle as a two-dimensional array
    c = 1                            # Bell numbers count
    while c <= stop:
        if c >= start:
            yield t[-1][-1]          # Yield the Bell number of the previous row
        row = [t[-1][-1]]            # Initialize a new row
        for b in t[-1]:
            row.append(row[-1] + b)  # Populate the new row
        c += 1                       # We have found another Bell number
        t.append(row)                # Append the row to the triangle


def printPartition():
    global numberOfPartitions, numberOfSubsets, n, partitions
    numberOfPartitions += 1
    encoding = [x for x in partitions if x != 0]
    partition = "Partition: " + '\033[92m' + str(numberOfPartitions) + '\033[0m\n'
    # we convert the encoding in to a partition
    for i in range(1, numberOfSubsets+1):
        partition += '{ '
        for j in range(1, n+1):
            if partitions[j] == i:
                partition += '\033[92m' + str(j) + '\033[0m, '
        partition+='\b\b }'
    # we add the encoding
    partition += '\n Code Encoding\n' + str(encoding) + '\n'
    # we generate the set of equivalence relations
    partition += 'Set of equivalence relations: \n' + str(encodingToEquivalenceRelations(encoding) + "\n")

    print(partition)


def encodingToEquivalenceRelations(encode):
    setOfEquivalenceRelations = "{"
    for i in range(len(encode)):
        for j in range(len(encode)):
            if encode[j] == encode[i]:
                setOfEquivalenceRelations += "(\033[92m" + str(i+1) + "\033[0m,\033[92m" + str(j+1) + "\033[0m), "

    setOfEquivalenceRelations += "\b\b}"
    return setOfEquivalenceRelations


def generatePartition(index):
    '''
     Here we recursively generate the partition of number using the encoding explained above
     ex: for n = 3 we obtain
     111
     112
     121
     122
     123
    '''
    global n, numberOfSubsets, partitions
    if index == n+1:
        printPartition()
    else:
        for i in range(1, numberOfSubsets+1):
            partitions[index] = i
            generatePartition(index+1)
        numberOfSubsets += 1
        partitions[index] = numberOfSubsets
        generatePartition(index+1)
        numberOfSubsets -= 1


def start():
    global n, numberOfPartitions

    n = int(input("n = "))
    if n < 10:
        generatePartition(1)
        print("The number of partitions is:\n\t" + str(numberOfPartitions))
    else:
        print('\033[91m Number is to big so we will use Bell\'s triangle to generate the number of partitions')
        for b in bell_numbers(n, n):
            print(str(b))


start()

