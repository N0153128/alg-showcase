def make_matrix(l, w, char):
    length = [char for i in range(l)]
    scroll = [length for i in range(w)]
    return scroll

def mod_matrix(matrix):
     matrix[0][0] = '|'
     matrix[-1][-1] = '|'
    #  matrix[0][0][0][0] = 9
     return matrix

def pretty_out(matrix):
        out = ''.join([str(i) for i in matrix])
        print(out.replace(',','').replace('\'', '').replace('[', '').replace(']','').replace(' ',''))


pretty_out(mod_matrix(make_matrix(133, 30, 'W')))