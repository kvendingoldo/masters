# -*- coding: utf-8 -*-
# @Author: Alexander Sharov

from padic.padic import *

import random
import copy


class Matrix(object):

    def __init__(self, n, m, init=True):
        if init:
            self.rows = [[PAdic("0", 2)] * n for x in range(m)]
        else:
            self.rows = []
        self.m = m
        self.n = n

    def __copy__(self):
        m = Matrix(self.n, self.m, init=False)
        m.rows = copy.copy(self.rows)
        return m

    def __deepcopy__(self):
        m = Matrix(self.n, self.m, init=False)
        m.rows = copy.deepcopy(self.rows)
        return m

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

    def get_size(self):
        if self.m == self.n:
            return self.m
        else:
            return 0

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

    def __iadd__(self, other):
        """ Add a matrix to this matrix.
        This modifies the current matrix """

        tempmat = self + other
        self.rows = tempmat.rows[:]
        return self

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

    def __isub__(self, other):
        """ Add a matrix to this matrix.
        This modifies the current matrix """

        tempmat = self - other
        self.rows = tempmat.rows[:]
        return self

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

    def __imul__(self, other):
        """ Add a matrix to this matrix.
        This modifies the current matrix """

        # Possibly not a proper operation
        # since this changes the current matrix
        # rank as well...

        tempmat = self * other
        self.rows = tempmat.rows[:]
        self.m, self.n = tempmat.getRank()
        return self

    def __eq__(self, other):
        """ Test equality """
        return other.rows == self.rows

    @staticmethod
    def determinant(A, total=PAdic("0", 5)):
        dim = len(A.rows)
        indices = list(range(dim))

        if dim == 2 and len(A[0]) == 2:
            val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
            return val

        for fc in indices:
            As = copy.copy(A)
            As = As[1:]
            height = len(As)

            for i in range(height):
                As[i] = As[i][0:fc] + As[i][fc + 1:]

            sign_val = (-1) ** (fc % 2)
            sign = PAdic(str(sign_val), 5)

            m_size = A.get_size() - 1
            m = Matrix(m_size, m_size)
            m[0] = As[0]
            m[1] = As[1]

            sub_det_val = Matrix.determinant(m)
            sub_det = PAdic(str(sub_det_val), 5)

            total = total + sign * A[0][fc] * sub_det
        return total

    @classmethod
    def make_matrix(cls, rows):

        m = len(rows)
        n = len(rows[0])
        # Validity check
        if any([len(row) != n for row in rows[1:]]):
            raise Exception("inconsistent row length")
        mat = Matrix(m, n, init=False)
        mat.rows = rows

    @classmethod
    def make_random(cls, m, n, low=0, high=10):
        """ Make a random matrix with elements in range (low-high) """

        obj = Matrix(m, n, init=False)
        for x in range(m):
            obj.rows.append([random.randrange(low, high) for i in range(obj.n)])

        return obj

    @classmethod
    def make_zero(cls, m, n):
        """ Make a zero-matrix of rank (mxn) """

        rows = [[0] * n for x in range(m)]
        return cls.fromList(rows)

    @classmethod
    def make_id(cls, m):
        """ Make identity matrix of rank (mxm) """

        rows = [[0] * m for x in range(m)]
        idx = 0

        for row in rows:
            row[idx] = 1
            idx += 1

        return cls.fromList(rows)
