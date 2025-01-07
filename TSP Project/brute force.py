from math import hypot
import itertools
from itertools import permutations
import time

def distance(point1, point2):

    return hypot((point1[0] - point2[0]),(point1[1] - point2[1]))

def main():
    pointsFile = open("points.txt", "r")
    points = []
    strList = []

    for lineR in pointsFile:

        if("\n" in lineR):
            line = lineR[0:-1]

        else:
            line = lineR

        strList.append(line.split(","))

    numOfPoints = int(strList[0][0])

    for i in range(numOfPoints):
    
        points.append([0,0])
        points[i][0] = int(strList[i+1][0])
        points[i][1] = int(strList[i+1][1])
        
    
    b = list(itertools.permutations(points))
    listCost = []
    minCost = 0
    bestPerm = ()
    for perm in b:
        bobTheHolder = 0
        for z in range(numOfPoints):
            a = distance(perm[z], perm[z+1])
            bobTheHolder += a 
            if (z == numOfPoints - 2):
                a = distance(perm[z], perm[0])
                bobTheHolder += a
                listCost.append(bobTheHolder)
                if minCost == 0:
                    minCost = bobTheHolder
                    bestPerm = perm + tuple([perm[0]])
                break
        if minCost > bobTheHolder:
            minCost = bobTheHolder
            bestPerm = perm + tuple([perm[0]])

        

    bruteForceAnswerFile = open('brute force answer.txt', 'a')
    bruteForceAnswerFile.write(f"best permutation is {bestPerm} and the cost is {minCost}.")
    bruteForceAnswerFile.close()

   # print(listCost)
    #answer = open('answer.txt', 'w')
   # for p in listCost:
   #     answer.write(str(p)+'\n')

    #answer.close()


    
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
