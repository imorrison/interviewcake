
def merge_arrays(arr1, arr2, output=[]):
  print arr1, arr2, output
  if len(arr1) < 1:
    return output + arr2
  if len(arr2) < 1:
    return output + arr1

  if arr1[0] > arr2[0]:
    output.append(arr2[0])
    return merge_arrays(arr1, arr2[1:], output)
  else:
    output.append(arr1[0])
    return merge_arrays(arr1[1:], arr2, output)



my_array     = [3,4,6,7,10,11,15]
alices_array = [1,5,8,12,14,19,20,30]

print merge_arrays(my_array, alices_array)
