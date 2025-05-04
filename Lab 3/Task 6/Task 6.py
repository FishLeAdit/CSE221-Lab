


def kthquickSort(arr,left,right,k):
  if k == left == right:
    return arr[k]
  if left<right:
    partition_pos = partition(arr,left,right)
    if k == partition_pos:
      return arr[k]
    if k < partition_pos:
    
      return kthquickSort(arr,left,partition_pos-1,k)
    if k > partition_pos:
      return kthquickSort(arr,partition_pos+1,right,k)
def partition(arr,left,right):
  i = left
  j = right - 1
  pivot = arr[right]
  while i<j:
    while i < right and arr[i] < pivot:
      i += 1
    while j > left and arr[j] >= pivot:
      j -= 1
    if i < j:
      arr[i], arr[j] = arr[j], arr[i]
  if arr[i] > pivot:
    arr[i], arr[right] = arr[right], arr[i]
  return i


num = 9
lst = [10, 11, 10, 6, 7, 9, 8, 15, 2]
Q = 4
q = [4,2,1,6]


for i in q:
  x = kthquickSort(lst,0,num-1,i)
  print(x)



