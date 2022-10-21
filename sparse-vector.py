"""
Q1: 設計⼀個 sparse vector class. Throw an error if the index is larger than the size.
sparseVector v = new sparseVector(100); //size constructor; size is 100.
v.set(0, 1.0);
v.set(3, 2.0);
v.set(80,-4.5);

Q2: Add these operations to your library: Addition, dot product, and cosine. Formular for each are
provided below; we’re more interested in you writing the code than whether you’ve memorized the
formula. For each operation, your code should throw an error if the two input vectors are not
equal length.

Sample input/output:.
//Note: This is pseudocode. Your actual syntax will vary by language.
v1 = new vector(5)
v1[0] = 4.0
v1[1] = 5.0
v2 = new vector(5)
v2[1] = 2.0
v2[3] = 3.0
v3 = new vector(2)
print v1.add(v2) //should print [4.0, 7.0, 0.0, 3.0, 0.0]
print v1.add(v3) //error -- vector lengths don't match
print v1.dot(v2) //should print 10
print v1.dot(v3) //error -- vector lengths don't match
print v1.cos(v2) //should print 0.433
print v1.cos(v3) //error -- vector lengths don't match
Formular:
Addition
a.add(b) = [a[0]+b[0], a[1]+b[1], a[2]+b[2], ...]
Dot product
a.dot(b) = a[0]*b[0] + a[1]*b[1] + a[2]*b[2] + ...
Cosine
a.cos(b) = a.dot(b) / (norm(a) * norm(b))
//norm(a) = sqrt(a[0]^2 + a[1]^2 + a[2]^2 + ...).
"""

import collections
import math


class SparseVector:
    def __init__(self, size) -> None:
        self.hash = collections.defaultdict(float)
        self.size = size
    
    def set(self, index, value):
        if index > self.size:
            raise ValueError("Out of range!")
        self.hash[index] = value
    
    def add(self, vector):
        if self.size != vector.size:
            raise ValueError("Vector lengths don't match!")
        res = [0.0] * self.size
        for index, val in self.hash.items():
            res[index] += val
        for index, val in vector.hash.items():
            res[index] += val
        return res
    
    def dot(self, vector):
        if self.size != vector.size:
            raise ValueError("Vector lengths don't match!")
        res = 0
        if self.size < vector.size:
            for index, val in self.hash.items():
                res += val * vector[index]
        else:
            for index, val in vector.hash.items():
                res += val * self.hash[index]
        return res

# a.cos(b) = a.dot(b) / (norm(a) * norm(b))
# //norm(a) = sqrt(a[0]^2 + a[1]^2 + a[2]^2 + ...).

    def cos(self, vector):
        if self.size != vector.size:
            raise ValueError("Vector lengths don't match!")
        sum1 = sum([val * val for _, val in self.hash.items()])
        norm1 = math.sqrt(sum1)
        sum2 = sum([val * val for _, val in vector.hash.items()])
        norm2 = math.sqrt(sum2)
        res = self.dot(vector) / (norm1 * norm2)
        return res

v1 = SparseVector(5)
v2 = SparseVector(5)
v3 = SparseVector(2)
v1.set(0, 4.0)
v1.set(1, 5.0)
v2.set(1, 2.0)
v2.set(3, 3.0)
# v3.set(3, 1)
print(v1.add(v2)) #should print [4.0, 7.0, 0.0, 3.0, 0.0]
# print(v1.add(v3))
print(v1.dot(v2)) #should print 10
# print(v1.dot(v3)) #error -- vector lengths don't match
print(v1.cos(v2)) #should print 0.433
# print(v1.cos(v3)) #error -- vector lengths don't match
