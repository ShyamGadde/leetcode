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
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:  # len(hand) % groupSize != 0
            return False

        count = Counter(hand)

        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            min_ = min_heap[0]

            for i in range(min_, min_ + groupSize):
                if i not in count:
                    return False

                count[i] -= 1

                if not count[i]:
                    # If the element being removed in not the minimum,
                    # then grouping is not possible for the given constraints.
                    # E.g., there are two 1s left and zero 2s. Hence exit early
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)

        return True


# @leet end

