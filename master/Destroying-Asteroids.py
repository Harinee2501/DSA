1class Solution(object):
2    def asteroidsDestroyed(self, mass, asteroids):
3        asteroids.sort()
4        for i in asteroids:
5            if i<=mass:
6                mass+=i
7            else:
8                return False
9        return True