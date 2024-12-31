def sort_map_by_value(map1):
    return dict(sorted(map1.items(),key=lambda item: item[1]))

map1={101:"John Doe",102:"Jane Smith",103:"Peter Johnson"}
print("Input Map:")
print(map1)
sorted_map=sort_map_by_value(map1)
print("Sorted Map:")
print(sorted_map)