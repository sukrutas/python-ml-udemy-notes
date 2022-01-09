# WORKING WITH SET_UNION-INTERSECT-DIFF-S_DIFF


seta = {1,2,3,4,5}
setb = {1,3,4,6,7,8}

# union (to combine)
print(seta | setb)
print(seta.union(setb))
print(setb.union(seta))

# intersect (to get common items)
print(seta & setb)
print(seta.intersection(setb))
print(setb.intersection(seta))

# difference
print(seta - setb)
print(seta.difference(setb))
print(setb.difference(seta))

# symetric_difference (to get not intersect part)
print(seta ^ setb)
print(seta.symmetric_difference(setb))
print(setb.symmetric_difference(seta))


