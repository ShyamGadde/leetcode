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
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = collections.Counter(students)

        for i in range(len(sandwiches)):
            if not counter[sandwiches[i]]:
                return len(sandwiches) - i
            counter[sandwiches[i]] -= 1

        return 0
# @leet end
