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
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0

        for char in s:
            if char == t[i]:
                i += 1
                if i == len(t):
                    return 0

        return len(t) - i


# @leet end

