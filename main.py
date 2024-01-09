

# 2x2 matrix

matrix2 = [
    [1,2],
    [3,1]
]

def determinant2(matrix2):
    return((matrix2[0][0] * matrix2[1][1]) - (matrix2[0][1] * matrix2[1][0]))

det2 = determinant2(matrix2)
print(det2)

def inverse2(matrix2,det2):
    matrix2i = [
        [matrix2[1][1]/det2,-matrix2[0][1]/det2],
        [-matrix2[1][0]/det2,matrix2[0][0]/det2]
    ]
    return(matrix2i)

mi2 = inverse2(matrix2,det2)
for fila in mi2:
    print(fila)

# 3x3 matrix

matrix3 = [
    [1,1,1],
    [0,1,1],
    [1,0,1]
]

def determinant3(matrix3):
    return((matrix3[0][0]*matrix3[1][1]*matrix3[2][2])+(matrix3[0][1]*matrix3[1][2]*matrix3[2][0])+(matrix3[0][2]*matrix3[1][0]*matrix3[2][1])-(matrix3[0][2]*matrix3[1][1]*matrix3[2][0])-(matrix3[0][0]*matrix3[1][2]*matrix3[2][1])-(matrix3[0][1]*matrix3[1][0]*matrix3[2][2]))

det3 = determinant3(matrix3)
print(det3)

def inverse3(matrix3,det3):
    matrix3iaux=[
        [(matrix3[1][1]*matrix3[2][2]-matrix3[1][2]*matrix3[2][1])/det3,-(matrix3[1][0]*matrix3[2][2]-matrix3[2][0]*matrix3[1][2])/det3,(matrix3[1][0]*matrix3[2][1]-matrix3[1][2]*matrix3[2][0])/det3],
        [-(matrix3[0][1]*matrix3[2][2]-matrix3[2][1]*matrix3[0][2])/det3,(matrix3[0][0]*matrix3[2][2]-matrix3[0][2]*matrix3[2][0])/det3,-(matrix3[0][0]*matrix3[2][1]-matrix3[0][1]*matrix3[2][0])/det3],
        [(matrix3[0][1]*matrix3[1][2]-matrix3[1][1]*matrix3[0][2])/det3,-(matrix3[0][0]*matrix3[1][2]-matrix3[1][0]*matrix3[0][2])/det3,(matrix3[0][0]*matrix3[1][1]-matrix3[0][1]*matrix3[1][0])/det3]
    ]
    matrix3i =[
        [matrix3iaux[0][0],matrix3iaux[1][0],matrix3iaux[2][0]],
        [matrix3iaux[0][1],matrix3iaux[1][1],matrix3iaux[2][1]],
        [matrix3iaux[0][2],matrix3iaux[1][2],matrix3iaux[2][2]]
    ]
    return(matrix3i)

mi3 = inverse3(matrix3,det3)
for fila in mi3:
    print(fila)



# 4x4 matrix

matrix4 = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

#def determinant4(matrix4):
#   return()
#det4 = determinant4(matrix4)