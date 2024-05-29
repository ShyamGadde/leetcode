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
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cur_cost = max_len = left = 0

        for right in range(len(s)):
            cur_cost += abs(ord(s[right]) - ord(t[right]))

            while cur_cost > maxCost:
                cur_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


# @leet end

