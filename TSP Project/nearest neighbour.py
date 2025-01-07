from math import hypot
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
        




    billTheHolder = []
    lenOfPoints = len(points)
    tomTheCounter = 1
    for i in points:
        for j in range(numOfPoints):
            v = distance(points[0], points[j+1])
            billTheHolder.append([[points[0],points[j+1]],v])
            if j == numOfPoints - 2:
                break
        
        if tomTheCounter == lenOfPoints:
            theLast = points[0]
            for r in range(numOfPoints - 1):
                points[r] = points[r + 1]

            points[numOfPoints - 1] = theLast

            break

        points[0], points[tomTheCounter] = points[tomTheCounter], points[0]
        tomTheCounter = tomTheCounter + 1

    
    
    for pointsnn in points:   #to execute at number of points to use them as starting point
        
        seenNode = []
        sumCost = 0
        currentPoint = pointsnn
        for pointsl2 in points:    # to create the tour for each starting point
            elList = []
            for i in billTheHolder:
                if currentPoint == i[0][0]:
                    elList.append(i) # a list of curent point and every path and cost

            for a in elList:
                if a[0][1] not in seenNode:   
                    minElCost = a[1]
                    minElNext = a[0][1]
                    break

            for el in elList:
                if minElCost > el[1] and el[0][1] not in seenNode: #to find the least cost next node
                    minElCost = el[1]
                    minElNext = el[0][1]

            sumCost = sumCost + minElCost
            seenNode.append(currentPoint)
            currentPoint = minElNext

        sumCost = sumCost + distance(currentPoint, seenNode[0])
        seenNode.append(seenNode[0])

        #outputFile = open('nearest neighbour answer.txt','a')
        #outputFile.write(f"starting {pointsnn} the cost is {sumCost} and the order of nodes is {str(seenNode)}" + '\n')
        #outputFile.close()

        
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
