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
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        i = 0

        def swap(nums, x, y):
            nums[x], nums[y] = nums[y], nums[x]

        while i <= right:
            if nums[i] == 0:
                swap(nums, i, left)
                left += 1
            elif nums[i] == 2:
                swap(nums, i, right)
                right -= 1
                i -= 1  # Because we don't the pointer to move forward in this case

            i += 1


# @leet end
