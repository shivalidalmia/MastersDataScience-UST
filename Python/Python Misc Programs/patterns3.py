# Shivali Dalmia
# patterns3.py

import numpy as np

def checkerboard(N):
    for row in range(N):
        for col in range(N):
            if row%2==0 and col%2==0:
                print("*",end="")
            elif row%2==0 and col%2!=0:
                print("_",end="")
            elif row%2!=0 and col%2!=0:
                print("*",end="")
            elif row%2!=0 and col%2==0:
                print("_",end="")
        print()
    print()

def caret(N):
    for row in range(N):
        for col in range(2*(N-1)+1):
            if abs(row+col) == N-1 or abs(row-col) == N-1:
                print("*",end="")
            else:
                print(" ",end="")
        print()

    print()

def aitch(N):
    for row in range(2*N-1):
        print("*",end="")
        if row == (2*N-1)//2:
            print("*"*(N-1),end="")
        else:
            print(" "*(N-1),end="")
        print("*")
    print()

def solid_diamond(N):
    no_of_stars = 1
    for row in range(N+1):
        for col in range(2*N+1):
            if row+col==N:
                print("*"*no_of_stars,end='')
                col = col + no_of_stars
            else:
                print(" ", end='')
        if no_of_stars<2*N+1:
            no_of_stars = no_of_stars + 2
        print()

    for row in range(N+1,2*N+1):
        no_of_stars = no_of_stars - 2
        for col in range(2*N):
            if row-col==N:
                print("*"*no_of_stars,end='')
                col = col + no_of_stars
            else:
                print(" ", end='')
        print()
    print()

def hollow_diamond(N):

    for row in range(N + 1):
        for col in range(2 * N + 1):
            if row + col == N or abs(row-col)==N:
                print("*",end='')
            else:
                print(" ", end='')
        print()

    for row in range(N + 1, 2 * N + 1):
        for col in range(2 * N):
            row_x = row-(N+1)
            if row - col == N or abs(row_x+col)==2*N-1:
                print("*", end='')
            else:
                print(" ", end='')
        print()
    print()

def num_diag(N):

    if 0 < N < 10:
        for row in range(0,N):
            for col in range(row,-1,-1):
                print(col,end="")
            for col_x in range(col+1,N-row):
                print(col_x,end="")
            print()
    print()

def print_sq(sq):
  if sq is None:
    return
  m,n = sq.shape
  for i in range(0, m):
    row = ''
    for j in range(0, n):
      if sq[i][j] == 1:
        row += '*'
      else:
        row += (' ')
    print(row)

def nested_squares(N):
  if(N < 0):
    return None
  sq = np.zeros((2*N+1, 2*N+1))
  n = N
  top_ctr = 0
  bottom_ctr = -1
  left_ctr = 0
  right_ctr = -1
  lr = 0
  ur = 2*n+1
  while(n >= 0):
    for i in range(lr, ur):
      sq[top_ctr][i] = 1
      sq[bottom_ctr][i] = 1
      sq[i][left_ctr] = 1
      sq[i][right_ctr] = 1
    top_ctr += 2
    bottom_ctr -= 2
    left_ctr += 2
    right_ctr -= 2
    n -= 2
    lr += 2
    ur -= 2
  print_sq(sq)

def nested_triangles(N):
    pass

def main():
    N = int(input("Enter an int for N: "))
    checkerboard(N)
    caret(N)
    aitch(N)
    solid_diamond(N)
    hollow_diamond(N)
    num_diag(N)
    nested_squares(N)
    nested_triangles(N)

main()