import numpy as np

class Difference:

    def difference(self,string1, string2):
        # Split both strings into list items
        self.string1 = string1
        self.string2 = string2
        non_match_a = []
        non_match_b = []

        list_a = [*string1]
        list_b = [*string2]

        count = 0
        for i in list_a:
            count = count + 1
            if i not in list_b[count-1]:
                non_match_a.append(i)
                non_match_b.append(list_b[count-1])
        
        return non_match_a,non_match_b

