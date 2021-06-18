import random
import matplotlib.pyplot as plt



maxiScores = []
# This is our training data INPUT
trainInput = [[1,1], [9.4,6.4], [2.5,2.1], [8,7.7], [0.5, 2.2], [7.9, 8.4], [7,7],
             [2.8, 0.8], [1.2,3], [7.8, 6.1]]
# This is out training data OUTPUT
trainOutput = [1,-1,1,-1,-1,1,-1,1,-1,-1]
epocs = 50
weightsList = []
successRate = { }
popSize = 50

def genRandomWeigths():
    for i in range(popSize):
        w = random.sample(range(-10, 10), 9)
        weightsList.append(w)
   
    return weightsList

def getNeuronOutput(i, w, L1, L2):
    n1Out = L1.N1(1, i[0], i[1], w[0], w[1], w[2]) # Input into Neuron-1
    n2Out = L1.N2(1, i[0], i[1], w[3], w[4], w[5]) # Input into Neuron-2

    # Now feed the output into final neuron

    finalOut = L2.N1(1, n1Out, n2Out, w[6], w[7], w[8])

    return finalOut

def DecToBin(n):
    neg = False
    if n < 0:
        neg = True
        n = n * -1
    a=[]
    while(n>0):
        dig=n%2
        a.append(dig)
        n=n//2
    a.reverse()
    if len(a) == 0:
        a.append(0)
    
    if neg == True:
        a.insert(0,1) # Singed Bit
    else:
        a.insert(0,0) # signedBit
    return a

def BinToDec(binNum):
    signedBit = 0

    if binNum[0] == 1:
        binNum[0] = 0
        signedBit = 1

    res = int("".join(str(x) for x in binNum), 2)

    if signedBit == 1:
        res = res * -1
    
    return res 

def crossover_mutation():

    # Step-1 sort the Dictionary
    sortedDict = sorted(successRate.items(), key=lambda x: x[1], reverse=True)
    
    # Step-2 Convert the list into dictionary // (as Sorted func return List)
    newDict = dict(sortedDict) 
    # Step-3 Now store the Keys in List //
    sortedWeightList = []

    temp = []
    oo = 0
    for key in newDict.keys():
        if oo < 1:
            temp = key
        sortedWeightList.append(list(key))
        oo += 1
    #print(newDict[tuple(temp)])  
    # maxiScores.append(newDict[tuple(temp)])  
    if len(sortedWeightList) < popSize:
        for heh in range(0, (popSize-len(sortedWeightList))):
            randLis = []
            for i in range(popSize):
                rnd = random.randint(-10, 10)
                randLis.append(rnd)
            sortedWeightList.append(randLis)
    iteri = 0
    weightsList.clear()
    # print(sortedWeightList)
    while iteri < popSize:
        neu_11 =[]
        neu_12 =[]
        neu_13 =[]
        neu_21 =[]
        neu_22 =[]
        neu_23 =[]
            # print(sortedList[iteri][0])
        w111 = sortedWeightList[iteri][0]
        w112 = sortedWeightList[iteri][1]
        w113 = sortedWeightList[iteri][2]
        w121 = sortedWeightList[iteri][3]
        w122 = sortedWeightList[iteri][4]
        w123 = sortedWeightList[iteri][5]
        w131 = sortedWeightList[iteri][6]
        w132 = sortedWeightList[iteri][7]
        w133 = sortedWeightList[iteri][8]
            # weights of second list
        w211 = sortedWeightList[iteri+1][0]
        w212 = sortedWeightList[iteri+1][1]
        w213 = sortedWeightList[iteri+1][2]
        w221 = sortedWeightList[iteri+1][3]
        w222 = sortedWeightList[iteri+1][4]
        w223 = sortedWeightList[iteri+1][5]
        w231 = sortedWeightList[iteri+1][6]
        w232 = sortedWeightList[iteri+1][7]
        w233 = sortedWeightList[iteri+1][8]
            # incer the iter
        
        w111Bin = DecToBin(w111)
        w112Bin = DecToBin(w112)
        w113Bin = DecToBin(w113)
        w121Bin = DecToBin(w121)
        w122Bin = DecToBin(w122)
        w123Bin = DecToBin(w123)
        w131Bin = DecToBin(w131)
        w132Bin = DecToBin(w132)
        w133Bin = DecToBin(w133)
        w211Bin = DecToBin(w211)
        w212Bin = DecToBin(w212)
        w213Bin = DecToBin(w213)
        w221Bin = DecToBin(w221)
        w222Bin = DecToBin(w222)
        w223Bin = DecToBin(w223)
        w231Bin = DecToBin(w231)
        w232Bin = DecToBin(w232)
        w233Bin = DecToBin(w233)
        l111 = len(w111Bin)
        l112 = len(w112Bin)
        l113 = len(w113Bin)
        l121 = len(w121Bin)
        l122 = len(w122Bin)
        l123 = len(w123Bin)
        l131 = len(w131Bin)
        l132 = len(w132Bin)
        l133 = len(w133Bin)
        l211 = len(w211Bin)
        l212 = len(w212Bin)
        l213 = len(w213Bin)
        l221 = len(w221Bin)
        l222 = len(w222Bin)
        l223 = len(w223Bin)
        l231 = len(w231Bin)
        l232 = len(w232Bin)
        l233 = len(w233Bin)
            # Now Joining
            # print(w111Bin)
            # print(w112)
            # print(w111, w112, w113,w111Bin, w112Bin, w113Bin)
        neu_11.extend(w111Bin)
        neu_11.extend(w112Bin)
        neu_11.extend(w113Bin)
            # print(neu_11)
        neu_12.extend(w121Bin)
        neu_12.extend(w122Bin)
        neu_12.extend(w123Bin)
        neu_13.extend(w131Bin)
        neu_13.extend(w132Bin)
        neu_13.extend(w133Bin)
            
        neu_21.extend(w111Bin)
        neu_21.extend(w212Bin)
        neu_21.extend(w213Bin)
        neu_22.extend(w221Bin)
        neu_22.extend(w222Bin)
        neu_22.extend(w223Bin)
        neu_23.extend(w231Bin)
        neu_23.extend(w232Bin)
        neu_23.extend(w233Bin)
            # neuron 1 balancing
        if len(neu_11) > len(neu_21):
            for i in range(len(neu_11) - len(neu_21)):
                neu_21.insert(0,0)
        else:
            for i in range(len(neu_21) - len(neu_11)):
                neu_11.insert(0,0)
            # neuron 2 balancing
        if len(neu_12) > len(neu_22):
            for i in range(len(neu_12) - len(neu_22)):
                neu_22.insert(0,0)
        else:
            for i in range(len(neu_22) - len(neu_12)):
                neu_12.insert(0,0)
            # neuron 3 balancing
        if len(neu_13) > len(neu_23):
            for i in range(len(neu_13) - len(neu_23)):
                neu_23.insert(0,0)
        else:
            for i in range(len(neu_23) - len(neu_13)):
                neu_13.insert(0,0)    
            # print("before crossover--------")
            # print(neu_11)
            # print(neu_12)
            # print (neu_13)                                    
            # now crossover neuron 1
        neu_11.reverse()
        neu_21.reverse()
        rand_cut = random.randint(0, (len(neu_11) -1))
        for i in range(0, rand_cut):
            neu_11[i], neu_21[i] = neu_21[i], neu_11[i]
        neu_11.reverse()
        neu_21.reverse()    
            # now crossover of neuron 2 
        neu_12.reverse()
        neu_22.reverse()
        rand_cut = random.randint(0, (len(neu_12) -1))
        for i in range(0, rand_cut):
            neu_12[i], neu_22[i] = neu_22[i], neu_12[i]
        neu_12.reverse()
        neu_22.reverse()    
            # now crossover of neuron 2 
        neu_13.reverse()
        neu_23.reverse()
        rand_cut = random.randint(0, (len(neu_23) -1))
        for i in range(0, rand_cut):
            neu_13[i], neu_23[i] = neu_23[i], neu_13[i] 
        neu_13.reverse()
        neu_23.reverse()           
            # print("after crossover--------")
            # print(neu_11)
            # print(neu_12)
            # print (neu_13)
            # Now mutation
        rand_mut = random.randint(0, (len(neu_11) - 1))
        if neu_11[rand_mut] == 1:
            neu_11[rand_mut] == 0
        else:
            neu_11[rand_mut]=0
        rand_mut = random.randint(0, (len(neu_12) - 1))    
        if neu_12[rand_mut] == 1:
            neu_12[rand_mut] == 0
        else:
            neu_12[rand_mut]=0
        rand_mut = random.randint(0, (len(neu_13) - 1))    
        if neu_13[rand_mut] == 1:
            neu_13[rand_mut] == 0
        else:
            neu_13[rand_mut]=0
            # ...
        rand_mut = random.randint(0, (len(neu_11) - 1))
        if neu_21[rand_mut] == 1:
            neu_21[rand_mut] == 0
        else:
            neu_21[rand_mut]=0
        rand_mut = random.randint(0, (len(neu_22) - 1))    
        if neu_22[rand_mut] == 1:
            neu_22[rand_mut] == 0
        else:
            neu_22[rand_mut]=0
        rand_mut = random.randint(0, (len(neu_23) - 1))    
        if neu_23[rand_mut] == 1:
            neu_23[rand_mut] == 0
        else:
            neu_13[rand_mut]=0

            # now converting numbers back to decimal weights
            # print(neu_11)
            # print(neu_22)
        w111Bin.clear()
        w112Bin.clear()
        w113Bin.clear()
        w121Bin.clear()
        w122Bin.clear()
        w123Bin.clear()
        w131Bin.clear()
        w132Bin.clear()
        w133Bin.clear()
        w211Bin.clear()
        w212Bin.clear()
        w213Bin.clear()
        w221Bin.clear()
        w222Bin.clear()
        w223Bin.clear()
        w231Bin.clear()
        w232Bin.clear()
        w233Bin.clear()
            # print(neu_11)
            # print(neu_22)
        for i in range(l113):
            popi = neu_11.pop()
            w113Bin.append(popi)
        for i in range(l112):
            popi = neu_11.pop()
            w112Bin.append(popi)
        w111Bin = neu_11
        for i in range(l123):
            popi = neu_12.pop()
            w123Bin.append(popi)
        for i in range(l122):
            popi = neu_12.pop()
            w122Bin.append(popi)
        w121Bin = neu_12 
        for i in range(l133):
            popi = neu_13.pop()
            w133Bin.append(popi)
        for i in range(l132):
            popi = neu_13.pop()
            w132Bin.append(popi)
        w131Bin = neu_13
            # ..
        for i in range(l213):
            popi = neu_21.pop()
            w213Bin.append(popi)
        for i in range(l212):
            popi = neu_21.pop()
            w212Bin.append(popi)
        w211Bin = neu_21
        for i in range(l223):
            popi = neu_22.pop()
            w223Bin.append(popi)
        for i in range(l222):
            popi = neu_22.pop()
            w222Bin.append(popi)
        w221Bin = neu_22 
        for i in range(l233):
            popi = neu_23.pop()
            w233Bin.append(popi)
        for i in range(l232):
            popi = neu_23.pop()
            w232Bin.append(popi)
        w231Bin = neu_23
            # converting binary digits back to decimal
        w111 = BinToDec(w111Bin)
        w112 = BinToDec(w112Bin)
        w113 = BinToDec(w113Bin)
        w121 = BinToDec(w121Bin)
        w122 = BinToDec(w122Bin)
        w123 = BinToDec(w123Bin)
        w131 = BinToDec(w131Bin)
        w132 = BinToDec(w132Bin)
        w133 = BinToDec(w133Bin)
        w211 = BinToDec(w211Bin)
        w212 = BinToDec(w212Bin)
        w213 = BinToDec(w213Bin)
        w221 = BinToDec(w221Bin)
        w222 = BinToDec(w222Bin)
        w223 = BinToDec(w223Bin)
        w231 = BinToDec(w231Bin)
        w232 = BinToDec(w232Bin)
        w233 = BinToDec(w233Bin)
            # print(w111Bin)
        new_weights = []
        new_weights2 = []
        new_weights = [w111, w112, w113, w121, w122, w123, w131, w132, w133]
        new_weights2 = [w211, w212, w213, w221, w222, w223, w231, w232, w233]
            # print('new weights are below')
            # print(new_weights2, new_weights)
            # print('new wegh above=--------')

        weightsList.append(new_weights)
        weightsList.append(new_weights2)

        # print(weightsList[iteri])
        # print(weightsList[iteri+1])
        iteri += 2
    

def doCross_and_mutations():
    
    # Step-1 sort the Dictionary
    sortedDict = sorted(successRate.items(), key=lambda x: x[1], reverse=True)
    
    # Step-2 Convert the list into dictionary // (as Sorted func return List)
    newDict = dict(sortedDict) 
    # Step-3 Now store the Keys in List //
    sortedWeightList = []

    temp = []
    for key in newDict.keys():
        temp.append(key[0])
        temp.append(key[1])
        sortedWeightList.append(temp)

    print(len(sortedWeightList))
    
    # Step-4 Now Crossover //
    i = 0
    ind = 0

    while i < len(weightsList):
        ind = i 
        w0 = DecToBin( sortedWeightList[i][0] )
        w1 = DecToBin( sortedWeightList[i][1] )
        w2 = DecToBin( sortedWeightList[i][2] )
        w3 = DecToBin( sortedWeightList[i][3] )
        w4 = DecToBin( sortedWeightList[i][4] )
        w5 = DecToBin( sortedWeightList[i][5] )
        w6 = DecToBin( sortedWeightList[i][6] )
        w7 = DecToBin( sortedWeightList[i][7] )
        w8 = DecToBin( sortedWeightList[i][8] )
   
        w00 = DecToBin( sortedWeightList[i+1][0] )
        w11 = DecToBin( sortedWeightList[i+1][1] )
        w22 = DecToBin( sortedWeightList[i+1][2] )
        w33 = DecToBin( sortedWeightList[i+1][3] )
        w44 = DecToBin( sortedWeightList[i+1][4] )
        w55 = DecToBin( sortedWeightList[i+1][5] )
        w66 = DecToBin( sortedWeightList[i+1][6] )
        w77 = DecToBin( sortedWeightList[i+1][7] )
        w88 = DecToBin( sortedWeightList[i+1][8] )
   
        p1 = []
        p2 = []
        
        for i in w0:
            p1.append(i)
        for i in w1:
            p1.append(i)
        for i in w2:
            p1.append(i)
        for i in w3:
            p1.append(i)
        for i in w4:
            p1.append(i)
        for i in w5:
            p1.append(i)
        for i in w6:
            p1.append(i)
        for i in w7:
            p1.append(i)
        for i in w8:
            p1.append(i)

        for i in w00:
            p2.append(i)
        for i in w11:
            p2.append(i)
        for i in w22:
            p2.append(i)
        for i in w33:
            p2.append(i)
        for i in w44:
            p2.append(i)
        for i in w55:
            p2.append(i)
        for i in w66:
            p2.append(i)
        for i in w77:
            p2.append(i)
        for i in w88:
            p2.append(i)

        l1 = len(p1)
        l2 = len(p2)

        if l1 > l2:
            for i in range(0, (l1-l2)):
                p2.insert(0,0)
        else:
            for i in range(0, (l2-l1)):
                p1.insert(0,0)

        rand = random.randint(0, len(p1)-1)

        p1.reverse()
        p2.reverse()

        for i in range(0, rand):
            p1[i], p2[i] = p2[i], p1[i]

        p1.reverse()
        p2.reverse()

 # Now Mutation
        rand = random.randint(0, len(p1)-1) 
        if p1[rand] == 0:
            p1[rand] = 1
        else:
            p1[rand] = 0

        if p2[rand] == 0:
            p2[rand] = 1
        else:
            p2[rand] = 0
   

        #################################
        n_w0 = []
        n_w1 = []
        n_w2 = []
        n_w3 = []
        n_w4 = []
        n_w5 = []
        n_w6 = []
        n_w7 = []
        n_w8 = []

        n_w00 = []
        n_w11 = []
        n_w22 = []
        n_w33 = []
        n_w44 = []
        n_w55 = []
        n_w66 = []
        n_w77 = []
        n_w88 = []
        
        
        
        for i in range(len(w8)):
            n_w8.append(p1.pop())


        for i in range(len(w7)):
            n_w7.append(p1.pop())

        for i in range(len(w6)):
            n_w6.append(p1.pop())

        for i in range(len(w5)):
            n_w5.append(p1.pop())

        for i in range(len(w4)):
            n_w4.append(p1.pop())

        for i in range(len(w3)):
            n_w3.append(p1.pop())

        for i in range(len(w2)):
            n_w2.append(p1.pop())
        
        for i in range(len(w1)):
            n_w1.append(p1.pop())
    
        n_w0 = p1

        ###############################
        ###############################
    
        for i in range(len(w88)):
            n_w88.append(p2.pop())

        for i in range(len(w77)):
            n_w77.append(p2.pop())

        for i in range(len(w66)):
            n_w66.append(p2.pop())

        for i in range(len(w55)):
            n_w55.append(p2.pop())

        for i in range(len(w44)):
            n_w44.append(p2.pop())

        for i in range(len(w33)):
            n_w33.append(p2.pop())

        for i in range(len(w22)):
            n_w22.append(p2.pop())
        
        for i in range(len(w11)):
            n_w11.append(p2.pop())
    
        n_w00 = p2
    
        i = ind 
        weightsList[i][0] = BinToDec(n_w0)
        weightsList[i][1] = BinToDec(n_w1)
        weightsList[i][2] = BinToDec(n_w2)
        weightsList[i][3] = BinToDec(n_w3)
        weightsList[i][4] = BinToDec(n_w4)
        weightsList[i][5] = BinToDec(n_w5)
        weightsList[i][6] = BinToDec(n_w6)
        weightsList[i][7] = BinToDec(n_w7)
        weightsList[i][8] = BinToDec(n_w8)


        weightsList[i+1][0] = BinToDec(n_w00)
        weightsList[i+1][1] = BinToDec(n_w11)
        weightsList[i+1][2] = BinToDec(n_w22)
        weightsList[i+1][3] = BinToDec(n_w33)
        weightsList[i+1][4] = BinToDec(n_w44)
        weightsList[i+1][5] = BinToDec(n_w55)
        weightsList[i+1][6] = BinToDec(n_w66)
        weightsList[i+1][7] = BinToDec(n_w77)
        weightsList[i+1][8] = BinToDec(n_w88)

        # print("WEIGHTS AFTER MUTATIONS")
        # print(weightsList[i])
        # print(weightsList[i+1])
        




        i += 2

        



#########################################################################
#########################################################################
class LayerOne: #Input Nuerons Layer
    def N1(self, x1, x2, x3, w1, w2, w3):
        s = (x1*w1) + (x2*w2) + (x3*w3)
        return s
    
    def N2(self, x1, x2, x3, w1, w2, w3):
        s = (x1*w1) + (x2*w2) + (x3*w3)
        return s

#########################################################################
#########################################################################

class LayerTwo: #Final Neuron Layer
    def N1(self, x1, x2, x3, w1, w2, w3):
        s = (x1*w1) + (x2*w2) + (x3*w3)
        return -1 if s < 0 else 1
        


#########################################################################
#########################################################################



# Main function
L1 = LayerOne()
L2 = LayerTwo()

# Now generate random populations of weights 
weightsList = genRandomWeigths()

currentInput = []
currentWeights = []
desiredOutput = 0

status = 'fail'
bestWeights = []
errorCount = 0

inpIndex = 0
g = 0
while(epocs > 0):
    successRate.clear()
    print("Generation : ", g)
    g+=1
    ## Loop on weights
    for i in range(len(weightsList)):

        currentWeights = weightsList[i]
        errorCount = 0
        ## Loop in training data inputs

        for inpIndex in range (len(trainInput)):
        
            currentInput = trainInput[inpIndex]
            desiredOutput = trainOutput[inpIndex]
            

            actualOutput = getNeuronOutput(currentInput, currentWeights, L1, L2)
            if actualOutput == desiredOutput:
                pass
            else:
                errorCount += 1
           
            
            # Save the best weights
            if errorCount == 1 and inpIndex == 9:
                bestWeights = currentWeights

            #####################################################
            ##################################################### Training data input loop ENDS


        ########################################################## Weights Loop ENDS
        ########################################################## 
        # Check if we found the best weights //
        if errorCount == 0:
            status = 'success'
            bestWeights = currentWeights
            break

        # Store the success rate for every weight populations //)
        sr = 1 - (errorCount/len(trainInput))
        successRate[currentWeights[0],currentWeights[1],currentWeights[2],
                    currentWeights[3],currentWeights[4],currentWeights[5],
                    currentWeights[6],currentWeights[7],currentWeights[8]] = 1 - (errorCount/len(trainInput))


    sortedDict2 = sorted(successRate.items(), key=lambda x: x[1], reverse=True)
    sortedDict2 = dict(sortedDict2)
    best_weigh = []
    for xo in sortedDict2.keys():
        best_weigh = xo
        break
    best_fit = sortedDict2[tuple(best_weigh)]
    maxiScores.append(best_fit)
    # Break the main loop if SUCCESS //
    if status == 'success':
        print("SUCCESS")
        break
    else:
        #doCross_and_mutations()
        crossover_mutation()
        # print(weightsList)


    epocs -= 1

x = []
y = []

x1 = []
y1 = []


for i in range(len(trainInput)):
    if trainOutput[i] == 1:
        x.append(trainInput[i][0])
        y.append(trainInput[i][1])
    else:
        x1.append(trainInput[i][0])
        y1.append(trainInput[i][1])


generationsTot = []
for xo in range(0, len(maxiScores)):
    generationsTot.append(xo)
plt.figure()
plot1 = plt.plot(generationsTot, maxiScores)
plt.title('Classification Figure')
plt.xlabel('Generations')
plt.ylabel('MaxScore')
plt.show()
