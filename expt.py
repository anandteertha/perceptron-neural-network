def activationFunction(yin):
    if yin > 0:
        return 1
    return -1
while True:
    for i in range(4):
        if i == 0:
            print(str(i+1)+') AND bipolar' )
        elif i == 1:
            print(str(i+1)+') OR bipolar' )
        elif i == 2:
            print(str(i+1)+') NAND bipolar' )
        else:
            print(str(i+1)+') NOR bipolar' )
    option = int(input('enter the option\n'))
    if option not in [1,2,3,4]:
        break
    weights = input('enter the initial weights and bias (ex:w1 w2 b) space seperated\n').split()
    weights = [int(m) for m in weights]
    learningRate = int(input('enter the alpha (learningRate)\n'))
    epochs = int(input('enter the number of epochs you want to execute\n'))
    if option == 1:
        '''
        x1  x2 = t
        -1 -1 = -1
        -1  1 = -1
         1 -1 = -1
         1  1 =  1
        '''
        x = [-1,1]
        cur = []
        for i in x:
            for j in x:
                if i == -1 or j == -1:
                    t = -1
                else:
                    t = 1
                cur.append([i,j,t])
        print('AND with bipolar =',cur[::-1])
    elif option == 2:
        x = [-1,1]
        cur = []
        for i in x:
            for j in x:
                if i == -1 and j == -1:
                    t = -1
                else:
                    t = 1
                cur.append([i,j,t])
        print('OR with bipolar =',cur[::-1])
    elif option == 3:
        x = [-1,1]
        cur = []
        for i in x:
            for j in x:
                if i == -1 or j == -1:
                    t = 1
                else:
                    t = -1
                cur.append([i,j,t])
        print('NAND with bipolar =',cur[::-1])
    elif option == 4:
        x = [-1,1]
        cur = []
        for i in x:
            for j in x:
                if i == -1 and j == -1:
                    t = 1
                else:
                    t = -1
                cur.append([i,j,t])
        print('NOR with bipolar =',cur[::-1])
    else:
        break


    cur = cur[::-1]
    finalTable = []
    i = 0
    while i < epochs:
        d = {}
        d['epochs'] = i+1
        j = 0
        while j < len(cur):
            yin = cur[j][0]*weights[0] + cur[j][1]*weights[1] + weights[2]
            netOP = activationFunction(yin)
            if netOP == cur[j][2]:
                d['x1'] = cur[j][0]
                d['x2'] = cur[j][1]
                d['t'] = cur[j][2]
                d['w1'] = weights[0]
                d['w2'] = weights[1]
                d['b'] = weights[2]
                finalTable.append(d)
                #print('d =',d)
                d = {}
                d['epochs'] = i+1
                j += 1
            else:
                weights[0] += learningRate*cur[j][2]*cur[j][0]
                weights[1] += learningRate*cur[j][2]*cur[j][1]
                weights[2] += learningRate*cur[j][2]
                d['x1'] = cur[j][0]
                d['x2'] = cur[j][1]
                d['t'] = cur[j][2]
                d['w1'] = weights[0]
                d['w2'] = weights[1]
                d['b'] = weights[2]
                finalTable.append(d)
                #print('d =',d)
                d = {}
                d['epochs'] = i+1
                j += 1
        i += 1
    for d in finalTable:
        print('************')
        for (key,value) in d.items():
            print(str(key)+' : '+str(value))
