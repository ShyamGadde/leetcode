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
    def heightChecker(self, heights: List[int]) -> int:
        freq = Counter(heights)
        height_mismatch = 0
        current_height = 0  # Expected height

        for i in range(len(heights)):
            while freq[current_height] == 0:
                current_height += 1

            if current_height != heights[i]:
                height_mismatch += 1

            freq[current_height] -= 1

        return height_mismatch


# @leet end

