if __name__ == "__main__":
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    son1 = 0
    son1_index = 0
    son2_index = len(mat)-1
    son = len(mat)%2
    for i in range(len(mat)):
            mantiq = True
            son1+= mat[i][son1_index]
            if son == 1 and i == len(mat)//2:
                mantiq = False
            if mantiq == True:
                son1+= mat[i][son2_index]
            son1_index+=1
            son2_index-=1
    print(son1)