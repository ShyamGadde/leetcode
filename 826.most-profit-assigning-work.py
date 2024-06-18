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
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        jobs = sorted(zip(profit, difficulty), key=lambda x: x[0], reverse=True)
        worker.sort(reverse=True)

        max_profit = 0
        i = 0
        for ability in worker:
            while jobs[i][1] > ability:
                i += 1

                if i == len(jobs):
                    return max_profit

            max_profit += jobs[i][0]

        return max_profit


# @leet end
