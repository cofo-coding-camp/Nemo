class Solution:
    def validIPAddress(self, IP: str) -> str:
        def checktype(IP):
            if '.' in IP:
                return 4
            elif ':' in IP:
                return 8
            else:
                return 0
        
        def _split(IP):
            if checktype(IP) == 4:
                return IP.split('.')
            elif checktype(IP) == 8:
                IP = IP.lower()
                return IP.split(':')
        
        def checklength(IP):
            l = _split(IP)
            if '' in l:
                return False
            return len(l) == checktype(IP)
        
        if not checktype(IP) or not checklength(IP):
            return "Neither"
        
        l = _split(IP)
        if checktype(IP) == 4:
            if '0' in [l[i][0] for i in range(len(l)) if len(l[i]) > 1]:
                return "Neither"
            for val in l:
                if not val.isdigit():
                    return "Neither"
                if int(val) > 255:
                    return "Neither"
            return "IPv4"
        else:
            for val in l:
                counter = 0
                for i in val:
                    counter += 1
                    if counter > 4:
                        return "Neither"
                    if i.isdigit():
                        continue
                    if i < 'a' or i > 'f':
                        return "Neither"
            return "IPv6"