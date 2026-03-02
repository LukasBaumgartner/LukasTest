a = 5
a *= 2
# Assuming this means a=2a? so a should be 10
print(a)

# /	division
# //	integer division
# %	remainder
# **	power
print(9 % 2)
# 1 as you get 4 reminder 1

print(7 // 3)     # 2      (int)
print(7 // 3.0)   # 2.0    (float)
# But ussually // removes the last number

print(7/3)
# 2.33333
print(7//3)
# 2
print(9//2.0)
# 4.0

# Python rounds down, however, so
print(-7//3)
# =-3, as -2.333333 rounded down is -3