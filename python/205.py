class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def get_mapping(x):
            mapping = {}
            mapped_str = []
            idx = 0
            for char in x:
                if char not in mapping:
                    idx += 1
                    mapping[char] = idx
                mapped_str.append(mapping[char])
            return mapped_str
        return get_mapping(s)==get_mapping(t)