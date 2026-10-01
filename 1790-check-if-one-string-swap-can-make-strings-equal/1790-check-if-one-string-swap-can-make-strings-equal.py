class Solution(object):
    def areAlmostEqual(self, s1, s2):

        if len(s1) != len(s2):
            return False

        mismatch = []

        for i in range(len(s1)):

            if s1[i] != s2[i]:
                mismatch.append(i)

        if len(mismatch) == 0:
            return True

        if len(mismatch) != 2:
            return False

        i = mismatch[0]
        j = mismatch[1]

        if s1[i] == s2[j] and s1[j] == s2[i]:
            return True

        return False

                
        