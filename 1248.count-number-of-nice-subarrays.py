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
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nice_sub_arrays = 0
        odd_num_idx = deque()
        start = -1

        i = 0
        while i < len(nums):
            if nums[i] & 1:
                odd_num_idx.append(i)
            i += 1

            if len(odd_num_idx) == k:
                nice_sub_arrays += odd_num_idx[0] - start
                break

        while i < len(nums):
            if nums[i] & 1:
                odd_num_idx.append(i)
                start = odd_num_idx.popleft()

            nice_sub_arrays += odd_num_idx[0] - start
            i += 1

        return nice_sub_arrays


# @leet end
