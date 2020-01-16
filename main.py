import threading
import time
import planeX
import planeY
import planeZ
import P1
import P2
import P3
import random

class main:
    rows = 8
    columns = 7
    bufferA = [[0 for x in range(7)] for y in range(8)]

    # Coordinates for X Y Z randomly generated
    x_xCoor = random.randint(0,rows-1)
    x_yCoor = random.randint(0,columns-1)
    y_xCoor = random.randint(0,rows-1)
    y_yCoor = random.randint(0,columns-1)
    z_xCoor = random.randint(0, rows-1)
    z_yCoor = random.randint(0, columns-1)
    # generate coordinates again if same coordinates
    if((x_xCoor==y_xCoor or x_xCoor==z_xCoor or y_xCoor==z_xCoor) and (x_yCoor==y_yCoor or x_yCoor==z_yCoor or y_xCoor==z_xCoor)):
        x_xCoor = random.randint(0, rows - 1)
        x_yCoor = random.randint(0, columns - 1)
        y_xCoor = random.randint(0, rows - 1)
        y_yCoor = random.randint(0, columns - 1)
        z_xCoor = random.randint(0, rows - 1)
        z_yCoor = random.randint(0, columns - 1)

    bufferA[x_xCoor][x_yCoor] = 'X'
    bufferA[y_xCoor][y_yCoor] = 'Y'
    bufferA[z_xCoor][z_yCoor] = 'Z'

    bufferB = [[0 for x in range(7)] for y in range(8)]
    bufferC = [[0 for x in range(3)] for y in range (3)]
    bufferD = [[0 for x in range(3)] for y in range (3)]
    bufferC[0][0] = 'X'
    bufferC[0][1] = 'Y'
    bufferC[0][2] = 'Z'
    bufferD[0][0] = 'X'
    bufferD[0][1] = 'Y'
    bufferD[0][2] = 'Z'
    time_interval = 1
    iterations = 20
    semA = threading.Semaphore()
    semB = threading.Semaphore()
    semC = threading.Semaphore()
    semD = threading.Semaphore()
   

    plane_X = planeX.planeX(x_xCoor,x_yCoor)
    plane_Y = planeY.planeY(y_xCoor,y_yCoor)
    plane_Z = planeZ.planeZ(z_xCoor,z_yCoor)

    p1 = P1.P1(0, plane_X, plane_Y, plane_Z, bufferA, bufferB, semA, semB)
    p2 = P2.P2(0, bufferC, bufferD, semA, semB, semC, semD)
    p3 = P3.P3(bufferC, bufferD, plane_X, plane_Y, plane_Z, z_xCoor, y_yCoor)
    

    #thread class declarations
    i = 0
    t1 = threading.Thread(target=p1.proc1,args=(i, plane_X, plane_Y, plane_Z, bufferA, bufferB, semA, semB,semC, semD, time_interval, iterations))
    t2 = threading.Thread(target=p2.proc, args=(i,bufferA,bufferB, bufferC, bufferD, semA, semB, semC, semD, time_interval, iterations))
    t3 = threading.Thread(target=p3.check, args=(i, bufferC, bufferD, semC, semD, plane_X, plane_Y, plane_Z, semA, semB, time_interval, iterations))
   
    t1.start()

    t2.start()
    
    t3.start()
