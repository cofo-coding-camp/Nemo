class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LFUCache:

    def __init__(self, capacity: int):
        self.data = {} # key: [node, freq]
        self.freq = {} # freq: [head, tail, nums]
        self.minfreq = float('inf')
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        self.updatefreq(key)
        return self.data[key][0].value
    
    def updatefreq(self, key):
        if self.freq[self.data[key][1]][2] == 1:
            if self.minfreq == self.data[key][1]:
                self.minfreq += 1
            self.freq.pop(self.data[key][1])
        else:
            self.freq[self.data[key][1]][2] -= 1
            m = self.data[key][0].prev
            m.next = m.next.next
            m.next.prev = m
        new_freq = self.data[key][1] + 1
        if new_freq not in self.freq:
            self.freq[new_freq] = [ListNode(), ListNode(), 1]
            self.freq[new_freq][0].next = self.data[key][0]
            self.data[key][0].prev = self.freq[new_freq][0]
            self.freq[new_freq][1].prev = self.data[key][0]
            self.data[key][0].next = self.freq[new_freq][1]
        else:
            m = self.freq[new_freq][1].prev
            m.next = self.data[key][0]
            self.data[key][0].prev = m
            self.data[key][0].next = self.freq[new_freq][1]
            self.freq[new_freq][1].prev = self.data[key][0]
            self.freq[new_freq][2] += 1
        self.data[key][1] =new_freq

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return None
        if key in self.data:
            self.data[key][0].value = value
            self.updatefreq(key)
        else:
            if len(self.data) == self.capacity:
                self.data.pop(self.freq[self.minfreq][0].next.key)
                if self.freq[self.minfreq][2] == 1:
                    self.freq.pop(self.minfreq)
                else:
                    self.freq[self.minfreq][2] -= 1
                    self.freq[self.minfreq][0].next = self.freq[self.minfreq][0].next.next
                    self.freq[self.minfreq][0].next.prev = self.freq[self.minfreq][0]
                self.fill_freq_data(key, value)
            else:
                self.fill_freq_data(key, value)
    
    def fill_freq_data(self, key, value):
        self.data[key] = [ListNode(key, value), 1]
        if 1 not in self.freq:
            self.freq[1] = [ListNode(), ListNode(), 0]
            self.freq[1][0].next = self.freq[1][1]
            self.freq[1][1].prev = self.freq[1][0]
        self.freq[1][2] += 1
        self.minfreq = 1
        m = self.freq[1][1].prev
        m.next = self.data[key][0]
        self.data[key][0].prev = m
        self.data[key][0].next = self.freq[1][1]
        self.freq[1][1].prev = self.data[key][0]

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)