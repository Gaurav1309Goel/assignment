d1 = {1:200, 2:400, 3:600}
d2 = {2:800, 5:1000}
d3 = {}
for i in d1:
    for j in d2:
        if i == j:
            d3[i] = [d1[i],d2[j]]
        if not i in d3:
            d3[i] = d1[i]
        if not j in d3:
            d3[j] = d2[j]
print d3            
