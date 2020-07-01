class Find:

    def find_sum(self, n):
        i = 0
        d = []
        n.sort()
        while i < len(n)-2:
            j = i+1
            k = len(n)-1
            while j < k:
                if n[i]+n[j]+n[k] < 0:
                    j += 1
                elif n[i]+n[j]+n[k] > 0:
                    k -= 1
                else:
                    d.append([n[i], n[j], n[k]])
                    j += 1
                    k -= 1
                    while j < k and n[j] == n[j+1]:
                        j += 1
                    while j < k and n[k] == n[k-1]:
                        k -= 1
            i += 1
        return d


f = Find()
print(f.find_sum([-25, -10, -7, -3, 2, 4, 8, 10]))
