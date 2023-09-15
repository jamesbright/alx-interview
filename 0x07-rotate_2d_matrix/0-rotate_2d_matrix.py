#!/usr/bin/python3
""" Rotate a matrix 90 degrees clockwise
"""


def rotate_2d_matrix(m):
    """Rotates elements in-place"""
    n = len(m)
    temp1, temp2 = 0, 0

    for j in range(0, len(m) // 2 + 1):
        for i in range(j, n - 1):
            # put same position in col from back
            temp1 = m[i][n - 1]
            m[i][n - 1] = m[j][i]
            # put temp1 in reverse position in row from bottom
            temp2 = m[n - 1][n - 1 - i + j]
            m[n - 1][n - 1 - i + j] = temp1
            # put temp2 in same position in col from front
            temp1 = m[n - 1 - i + j][j]
            m[n - 1 - i + j][j] = temp2
            # put temp1 in reverse position in row from top
            m[j][i] = temp1
        n -= 1
