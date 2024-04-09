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
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time_taken = 0
        kth_tickets = tickets[k]

        # The people before the kth position, add a max time required to buy kth_tickets
        for i in range(k + 1):
            time_taken += min(tickets[i], kth_tickets)

        # The people after the kth position, add a max time required to buy kth_tickets - 1
        for i in range(k + 1, len(tickets)):
            time_taken += min(tickets[i], kth_tickets - 1)

        return time_taken
# @leet end
