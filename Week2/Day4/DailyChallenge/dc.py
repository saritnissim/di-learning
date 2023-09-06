matrix_str =  '''
7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!
'''
matrix = []
rows = matrix_str.strip().split("\n")
for row in rows:
    matrix.append(list(row))
print(matrix)
secret_str = ''
isAlpha = False
for row_num in range(len(matrix[0])): 
    for col_num in range(len(matrix)):
        # [0][0] -> [1][0] -> [2][0]
        char = matrix[col_num][row_num]
        if char.isalpha():
            secret_str += char
            isAlpha = True
        else:
            if isAlpha:
                secret_str += ' '
                isAlpha = False
            
print(secret_str)