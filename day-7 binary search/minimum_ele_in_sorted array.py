a = [450, 500, 610, 720, 850, 920, 3, 80, 120, 200, 310]

left = 0
right = len(a) - 1

while left < right:
    mid = (left + right) // 2

    if a[mid] > a[right]:
        left = mid + 1
    else:
        right = mid

print("Minimum element:", a[left])