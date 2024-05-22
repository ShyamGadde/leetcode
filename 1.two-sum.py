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
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_elems = {}

        for i, n in enumerate(nums):
            if (diff := target - n) in prev_elems:
                return [prev_elems[diff], i]
            prev_elems[n] = i


# @leet end

