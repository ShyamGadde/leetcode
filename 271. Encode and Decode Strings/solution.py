class Solution:
    def encode(self, strs):
        """
        @param: strs: a list of strings
        @return: encodes a list of strings to a single string.
        """
        return "\0".join(strs)

    def decode(self, string):
        """
        @param: string: A string
        @return: decodes a single string to a list of strings
        """
        return string.split("\0")
