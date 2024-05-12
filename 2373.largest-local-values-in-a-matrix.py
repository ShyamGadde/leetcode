from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *
import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import statistics
import itertools
import functools
import operator
import io
import sys
import json
from typing import *

# @leet start
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0] * (n - 2) for _ in range(n - 2)]
        
        for i in range(n - 2):
            for j in range(n - 2):
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        res[i][j] = max(
                            res[i][j],
                            grid[r][c]
                        )

        return res
# @leet end
