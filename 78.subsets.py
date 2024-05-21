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
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def generate_subsets(start=0, current=[]):
            if start == len(nums):
                res.append(current.copy())
            else:
                current.append(nums[start])
                generate_subsets(start + 1, current)

                # Backtrack
                current.pop()
                generate_subsets(start + 1, current)

        generate_subsets()

        return res


# @leet end

