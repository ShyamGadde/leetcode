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
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem_idx = {0: -1}
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            rem = total % k

            if rem not in rem_idx:
                rem_idx[rem] = i
            elif i - rem_idx[rem] >= 2:
                return True

        return False


# @leet end

