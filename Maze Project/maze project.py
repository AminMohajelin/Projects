### Developed by Mohammad Amin Mohajelin ###
import sys

def nextNode(currentNode,currentColor,currentPath,prevNode):
    if currentNode[1] == 'j':
        print(path)
        sys.exit()

    if len(currentNode) == 2:

        node1Info = currentNode[0].split(' ')
        currentNodeName = currentNode[1]

        if(node1Info[1] == currentColor or node1Info[2] == currentPath) and (node1Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node1Info[0]]
            currentColor = node1Info[1]
            currentPath = node1Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)

    if len(currentNode) == 3:

        node1Info = currentNode[0].split(' ')
        node2Info = currentNode[1].split(' ')
        currentNodeName = currentNode[2]

        if(node1Info[1] == currentColor or node1Info[2] == currentPath) and (node1Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node1Info[0]]
            currentColor = node1Info[1]
            currentPath = node1Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)

        if(node2Info[1] == currentColor or node2Info[2] == currentPath) and (node2Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node2Info[0]]
            currentColor = node2Info[1]
            currentPath = node2Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)

    if len(currentNode) == 4:

        node1Info = currentNode[0].split(' ')
        node2Info = currentNode[1].split(' ')
        node3Info = currentNode[2].split(' ')
        currentNodeName = currentNode[3]

        if(node1Info[1] == currentColor or node1Info[2] == currentPath) and (node1Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node1Info[0]]
            currentColor = node1Info[1]
            currentPath = node1Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)

        if(node2Info[1] == currentColor or node2Info[2] == currentPath) and (node2Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node2Info[0]]
            currentColor = node2Info[1]
            currentPath = node2Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)

        if(node3Info[1] == currentColor or node3Info[2] == currentPath) and (node3Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node3Info[0]]
            currentColor = node3Info[1]
            currentPath = node3Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)

    if len(currentNode) == 5:

        node1Info = currentNode[0].split(' ')
        node2Info = currentNode[1].split(' ')
        node3Info = currentNode[2].split(' ')
        node4Info = currentNode[3].split(' ')
        currentNodeName = currentNode[4]
    
        if(node1Info[1] == currentColor or node1Info[2] == currentPath) and (node1Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node1Info[0]]
            currentColor = node1Info[1]
            currentPath = node1Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)

        if(node2Info[1] == currentColor or node2Info[2] == currentPath) and (node2Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node2Info[0]]
            currentColor = node2Info[1]
            currentPath = node2Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)

        if(node3Info[1] == currentColor or node3Info[2] == currentPath) and (node3Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node3Info[0]]
            currentColor = node3Info[1]
            currentPath = node3Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)

        if(node4Info[1] == currentColor or node4Info[2] == currentPath) and (node4Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node4Info[0]]
            currentColor = node4Info[1]
            currentPath = node4Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)

    if len(currentNode) == 6:

        node1Info = currentNode[0].split(' ')
        node2Info = currentNode[1].split(' ')
        node3Info = currentNode[2].split(' ')
        node4Info = currentNode[3].split(' ')
        node5Info = currentNode[4].split(' ')
        currentNodeName = currentNode[5]

        if(node1Info[1] == currentColor or node1Info[2] == currentPath) and (node1Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node1Info[0]]
            currentColor = node1Info[1]
            currentPath = node1Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)

        if(node2Info[1] == currentColor or node2Info[2] == currentPath) and (node2Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node2Info[0]]
            currentColor = node2Info[1]
            currentPath = node2Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)

        if(node3Info[1] == currentColor or node3Info[2] == currentPath) and (node3Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node3Info[0]]
            currentColor = node3Info[1]
            currentPath = node3Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)

        if(node4Info[1] == currentColor or node4Info[2] == currentPath) and (node4Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node4Info[0]]
            currentColor = node4Info[1]
            currentPath = node4Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)

        if(node5Info[1] == currentColor or node5Info[2] == currentPath) and (node5Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node5Info[0]]
            currentColor = node5Info[1]
            currentPath = node5Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)

    if len(currentNode) == 7:

        node1Info = currentNode[0].split(' ')
        node2Info = currentNode[1].split(' ')
        node3Info = currentNode[2].split(' ')
        node4Info = currentNode[3].split(' ')
        node5Info = currentNode[4].split(' ')
        node6Info = currentNode[5].split(' ')
        currentNodeName = currentNode[6]

        if(node1Info[1] == currentColor or node1Info[2] == currentPath) and (node1Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node1Info[0]]
            currentColor = node1Info[1]
            currentPath = node1Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)

        if(node2Info[1] == currentColor or node2Info[2] == currentPath) and (node2Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node2Info[0]]
            currentColor = node2Info[1]
            currentPath = node2Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)

        if(node3Info[1] == currentColor or node3Info[2] == currentPath) and (node3Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node3Info[0]]
            currentColor = node3Info[1]
            currentPath = node3Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)

        if(node4Info[1] == currentColor or node4Info[2] == currentPath) and (node4Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node4Info[0]]
            currentColor = node4Info[1]
            currentPath = node4Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)

        if(node5Info[1] == currentColor or node5Info[2] == currentPath) and (node5Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node5Info[0]]
            currentColor = node5Info[1]
            currentPath = node5Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)

        if(node6Info[1] == currentColor or node6Info[2] == currentPath) and (node6Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node6Info[0]]
            currentColor = node6Info[1]
            currentPath = node6Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)

    if len(currentNode) == 8:

        node1Info = currentNode[0].split(' ')
        node2Info = currentNode[1].split(' ')
        node3Info = currentNode[2].split(' ')
        node4Info = currentNode[3].split(' ')
        node5Info = currentNode[4].split(' ')
        node6Info = currentNode[5].split(' ')
        node7Info = currentNode[6].split(' ')
        currentNodeName = currentNode[7]

        if(node1Info[1] == currentColor or node1Info[2] == currentPath) and (node1Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node1Info[0]]
            currentColor = node1Info[1]
            currentPath = node1Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)

        if(node2Info[1] == currentColor or node2Info[2] == currentPath) and (node2Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node2Info[0]]
            currentColor = node2Info[1]
            currentPath = node2Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)

        if(node3Info[1] == currentColor or node3Info[2] == currentPath) and (node3Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node3Info[0]]
            currentColor = node3Info[1]
            currentPath = node3Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)

        if(node4Info[1] == currentColor or node4Info[2] == currentPath) and (node4Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node4Info[0]]
            currentColor = node4Info[1]
            currentPath = node4Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)

        if(node5Info[1] == currentColor or node5Info[2] == currentPath) and (node5Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node5Info[0]]
            currentColor = node5Info[1]
            currentPath = node5Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)

        if(node6Info[1] == currentColor or node6Info[2] == currentPath) and (node6Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node6Info[0]]
            currentColor = node6Info[1]
            currentPath = node6Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)

        if(node7Info[1] == currentColor or node7Info[2] == currentPath) and (node7Info[0] != prevNode):
            prevNode = currentNodeName
            currentNode = dictNodes[node7Info[0]]
            currentColor = node7Info[1]
            currentPath = node7Info[2]
            path.append(currentNode[len(currentNode)-1])
            nextNode(currentNode, currentColor, currentPath, prevNode)


def main():
    
    currentNode = A
    currentColor = 'RED'
    currentPath = 'CCL'
    prevNode = ''
    
    nextNode(currentNode, currentColor ,currentPath, prevNode)

A = ['B RED CCL','A']
B = ['C BLUE TL','A RED CCL','E BLUE CCL','F RED TL','B']
C = ['B BLUE TL','D GREEN TL','G RED CCL','C']
D = ['G BLUE BL','C GREEN TL','J RED TL','I GREEN BL','D']
E = ['B BLUE CCL','F GREEN HCL','K GREEN BL','O RED CCL','E']
F = ['G GREEN HCL','B RED TL','E GREEN HCL','K RED HCL','F']
G = ['C RED CCL','D BLUE BL','F GREEN HCL','H RED CCL','K BLUE BL','L GREEN TL','G']
H = ['G RED CCL','I RED HCL','L RED BL','H']
I = ['D GREEN BL','H RED HCL','J BLUE HCL','M GREEN TL','N GREEN HCL','I']
J = ['D RED TL','I BLUE HCL','N RED BL','J']
K = ['O BLUE TL','E GREEN BL','F RED HCL','G BLUE BL','P RED CCL','K']
L = ['G GREEN TL','H RED BL','M BLUE BL','Q GREEN TL','R RED HCL','L']
M = ['I GREEN TL','L BLUE BL','N BLUE HCL','S RED TL','M']
N = ['I GREEN HCL','J RED BL','M BLUE HCL','T RED BL','N']
O = ['E RED CCL','K BLUE TL','V BLUE HCL','U RED BL','O']
P = ['K RED CCL','Q GREEN CCL','V GREEN HCL','P']
Q = ['L GREEN TL','W RED TL','P GREEN CCL','R BLUE CCL','Q']
R = ['Q BLUE CCL','L RED HCL','S BLUE HCL','X RED TL','R']
S = ['Y GREEN CCL','M RED TL','R BLUE HCL','T BLUE BL','X GREEN BL','d RED HCL','S']
T = ['N RED BL','S BLUE BL','Y GREEN TL','T']
U = ['O RED BL','V GREEN BL','Z BLUE BL','U']
V = ['O BLUE HCL','a GREEN BL','b BLUE TL','P GREEN HCL','U GREEN BL','W RED CCL','Z RED CCL','V']
W = ['X GREEN CCL','Q RED TL','b RED TL','V RED CCL','W']
X = ['R RED TL','S GREEN BL','W GREEN CCL','c RED HCL','X']
Y = ['S GREEN CCL','e GREEN TL','T GREEN TL','Y']
Z = ['U BLUE BL','V RED CCL','a RED TL','f BLUE HCL','Z']
a = ['V GREEN BL','Z RED TL','b RED CCL','f GREEN HCL','a']
b = ['a RED CCL','h BLUE BL','V BLUE TL','W RED TL','c GREEN TL','g RED TL','b']
c = ['X RED HCL','b GREEN TL','d GREEN BL','h RED CCL','c']
d = ['S RED HCL','c GREEN BL','e GREEN HCL','i RED HCL','d']
e = ['Y GREEN TL','d GREEN HCL','i RED BL','e']
f = ['Z BLUE HCL','a GREEN HCL','g BLUE CCL','f']
g = ['b RED TL','f BLUE CCL','h GREEN CCL','g']
h = ['b BLUE BL','c RED CCL','g GREEN CCL','i RED BL','h']
i = ['j BLUE BL','d RED HCL','e RED BL','h RED BL','i']
j = ['i BLUE BL','j']

path = ['A']
dictNodes = {'A': A ,'B':B,'C':C,'D':D,'E':E,'F':F,'G':G,'H':H,'I':I,'J':J,'K':K,'L':L,'M':M,'N':N,'O':O,'P':P,'Q':Q,'R':R,'S':S,'T':T,'U':U,'V':V,'W':W,'X':X,'Y':Y,'Z':Z,'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'i':i,'j': j}
main()


