from padic import *


class Matrix(object):

    def __init__(self, n, m, init=True):
        if init:
            self.rows = [[PAdic("0", 2)] * n for x in range(m)]
        else:
            self.rows = []
        self.m = m
        self.n = n

    def __str__(self):
        s = '\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
        return s + '\n'

    def __repr__(self):
        s = str(self.rows)
        rank = str(self.get_rank())
        rep = "Matrix: \"%s\", rank: \"%s\"" % (s, rank)
        return rep

    def __getitem__(self, idx):
        return self.rows[idx]

    def __setitem__(self, idx, item):
        self.rows[idx] = item

    def get_rank(self):
        return self.m, self.n

    def reset(self):
        """ Reset the matrix data """
        self.rows = [[] for x in range(self.m)]

    def transpose(self):
        """ Transpose the matrix. Changes the current matrix """

        self.m, self.n = self.n, self.m
        self.rows = [list(item) for item in zip(*self.rows)]

    def get_transpose(self):
        """ Return a transpose of the matrix without
        modifying the matrix itself """

        m, n = self.n, self.m
        mat = Matrix(m, n)
        mat.rows = [list(item) for item in zip(*self.rows)]

        return mat

    def __add__(self, other):
        """ Add a matrix to this matrix and
          return the new matrix. Doesn't modify
          the current matrix """

        if self.get_rank() != other.get_rank():
            raise Exception("Trying to add matrixes of varying rank!")

        ret = Matrix(self.m, self.n)

        for x in range(self.m):
            row = [item[0] + item[1] for item in zip(self.rows[x], other[x])]
            ret[x] = row
        return ret

    def __sub__(self, other):
        """ Subtract a matrix from this matrix and
        return the new matrix. Doesn't modify
        the current matrix """

        if self.get_rank() != other.get_rank():
            raise Exception("Trying to add matrixes of varying rank!")

        ret = Matrix(self.m, self.n)

        for x in range(self.m):
            row = [item[0] - item[1] for item in zip(self.rows[x], other[x])]
            ret[x] = row

        return ret

    def __mul__(self, other):
        """ Multiple a matrix with this matrix and
        return the new matrix. Doesn't modify
        the current matrix """

        matm, matn = other.get_rank()

        if self.n != matm:
            raise Exception("Matrices cannot be multipled!")

        mat_t = other.get_transpose()
        mulmat = Matrix(self.m, matn)

        for x in range(self.m):
            for y in range(mat_t.m):
                sum_list = [item[0] * item[1] for item in zip(self.rows[x], mat_t[y])]
                for item in sum_list:
                    mulmat[x][y] += item

        return mulmat