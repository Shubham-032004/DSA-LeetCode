class Solution(object):
    def areAlmostEqual(self, s1, s2):

        if len(s1) != len(s2):
            return False

        # Step 1: Frequency check
        freq = {}

        for i in range(len(s1)):
            freq[s1[i]] = freq.get(s1[i], 0) + 1

        for j in range(len(s2)):
            freq[s2[j]] = freq.get(s2[j], 0) - 1

        for value in freq.values():
            if value != 0:
                return False

        # Step 2: Mismatch check
        mismatch = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                mismatch.append(i)

        # Already equal
        if len(mismatch) == 0:
            return True

        # One swap can create maximum 2 mismatches
        if len(mismatch) != 2:
            return False

        i = mismatch[0]
        j = mismatch[1]

        # Check if swapping these two makes them equal
        if s1[i] == s2[j] and s1[j] == s2[i]:
            return True

        return False

                
        