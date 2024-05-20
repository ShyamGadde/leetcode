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
    def subsetXORSum(self, nums: List[int]) -> int:
        out = 0

        def generate_subsets(i=0, cur=0):
            nonlocal out

            if i == len(nums):
                out += cur
                return

            generate_subsets(i + 1, cur ^ nums[i])
            generate_subsets(i + 1, cur)

        generate_subsets()

        return out


# @leet end

