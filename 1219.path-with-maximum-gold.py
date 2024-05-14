import bisect
import collections
import copy
import datetime
import functools
import heapq
import io
import itertools
import json
import math
import operator
import random
import re
import statistics
import string
import sys
from bisect import *
from builtins import *
from collections import *
from copy import *
from datetime import *
from functools import *
from heapq import *
from io import *
from itertools import *
from json import *
from math import *
from operator import *
from random import *
from re import *
from statistics import *
from string import *
from sys import *
from typing import *


# @leet start
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)  # rows
        n = len(grid[0])  # cols
        directions = (
            (1, 0),  # right
            (-1, 0),  # left
            (0, 1),  # up
            (0, -1),  # down
        )
        visited = [[False] * n for _ in range(m)]
        max_gold = 0

        def dfs(r, c):
            visited[r][c] = True
            gold = grid[r][c]
            max_gold = 0

            for dr, dc in directions:
                x = r + dr
                y = c + dc

                if 0 <= x < m and 0 <= y < n and not visited[x][y] and grid[x][y] != 0:
                    max_gold = max(max_gold, gold + dfs(x, y))

            visited[r][c] = False

            return max_gold

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                max_gold = max(max_gold, dfs(i, j))

        return max_gold


# @leet end
