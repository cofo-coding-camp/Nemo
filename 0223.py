class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        l1 = (A, C)
        l2 = (B, D)
        l3 = (E, G)
        l4 = (F, H)

        def helper(L1, L2):
            if L1[0] > L2[0]:
                return helper(L2, L1)
            if L1[0] < L2[1] < L1[1]:
                return L2[1] - L2[0]
            elif L1[1] < L2[0]:
                return 0
            else:
                return L1[1] - L2[0]
        s = (C - A) * (D - B) + (G - E) * (H - F)
        return s - helper(l1, l3) * helper(l2, l4)
