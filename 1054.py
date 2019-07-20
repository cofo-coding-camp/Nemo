import collections
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = dict(collections.Counter(barcodes))
        sortedcounter = sorted(counter, key=lambda k: 0 - counter[k])
        barcodes = []

        for i in sortedcounter:
            barcodes += [i] * counter[i]
            
        arrangedbarcodes = [None for _ in range(len(barcodes))]

        arrangedbarcodes[::2] = barcodes[:len(arrangedbarcodes[::2])]
        arrangedbarcodes[1::2] = barcodes[len(arrangedbarcodes[::2]):]

        return arrangedbarcodes