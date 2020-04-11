# See problem statement at https://www.hackerrank.com/challenges/new-year-chaos
def minimumBribes(q: list):
    numBribes = 0
    for i in range(len(q), 0, -1):
        if q[i-1] != i:
            if q[i-2] == i:
                # the guy, one position to the left bribed the current guy
                numBribes += 1
                q[i-1], q[i-2] = q[i-2], q[i-1]
            elif q[i-3] == i:
                # the guy, two positions to the left bribed twice
                numBribes += 2
                q[i-2], q[i-3] = q[i-3], q[i-2]
                q[i-1], q[i-2] = q[i-2], q[i-1]
            else:
                print('Too chaotic')
                return
    print(numBribes)

minimumBribes([2, 1, 5, 3, 4])  # expects 3
minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])  # expects 7
