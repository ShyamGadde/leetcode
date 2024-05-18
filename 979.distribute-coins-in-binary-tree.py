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
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        min_moves = 0

        def dfs(node):
            nonlocal min_moves

            if not node:
                return 0

            # "node.val - 1": We need that node to have exactly one coin.
            # The dfs() function returns either the number of extra coins in the
            # child node or the number of coins needed in the child node to make them have
            # exactly one coin in them. This overflow/underflow at this node also
            # equals to the number of moves we need to make so that all the nodes have
            # exactly one coin in each.
            extra_coins = (node.val - 1) + dfs(node.left) + dfs(node.right)
            min_moves += abs(extra_coins)
            return extra_coins

        dfs(root)

        return min_moves


# @leet end

