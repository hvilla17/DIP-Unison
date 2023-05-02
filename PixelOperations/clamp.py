def clamp(value, min, max):
    if value < min:
        return min
    elif value > max:
        return max
    else:
        return value


print(clamp(-10, 0, 255))  # 0
print(clamp(400, 0, 255))  # 255
print(clamp(190, 0, 255))  # 190
