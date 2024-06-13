# Test case 1
# n=int(input(("n = ")))
# arr = []
# missing = []
# if n>=1 and n<=1000000:
#     print("arr[] = ",end=' ')
#     for i in range(1,n):
#         num=int(input())
#         if num>=1 and num<=1000000:
#             arr.append(num)
#         else:
#             print("Enter Valid Number!!")
# else:
#     print("Try Again!!")
#     exit(1)
# for i in range(1,n+1):
#     if i not in arr:
#         missing.append(i)
# if len(missing)>1:
#     print("Numbers must range from 1 to n")
# elif len(missing)==1:
#     print(arr)
# else:
#     print("All Present")

# arr = []
# repeat = []
# n=int(input("n = "))
# print("arr[] = ")
# for i in range(n):
#     num=int(input())
#     if num>=0 and num<n:
#         arr.append(num)

# for i in range(n):
#     for j in range(n-1):
#         if arr[j]>arr[j+1]:
#             temp=arr[j]
#             arr[j]=arr[j+1]
#             arr[j+1]=temp

# for i in range(n):
#     for j in range(i+1,n):
#         if arr[i] == arr[j]:
#             if arr[i] not in repeat:
#                 repeat.append(arr[i])

# if len(repeat)>0:
#     print(repeat)
# else:
#     print("-1")

# arr = []
# repeat = []
# n=int(input("n = "))
# print("arr[] = ")
# for i in range(n):
#     num=int(input())
#     if num>=0 and num<n:
#         arr.append(num)

# for i in range(n):
#     for j in range(n-1):
#         if arr[j]>arr[j+1]:
#             temp=arr[j]
#             arr[j]=arr[j+1]
#             arr[j+1]=temp

# for i in range(n):
#     for j in range(i+1,n):
#         if arr[i] == arr[j]:
#             if arr[i] not in repeat:
#                 repeat.append(arr[i])

# if len(repeat)>0:
#     print(repeat)
# else:
#     print("-1")

# n=int(input("n = "))
# if(n<=1):
#     print("Invalid!!")
#     exit(1)
# else:
#     for i in range(1,n+1):
#         f=i+i
#     print(f)


def find_second_largest_sorted(arr):

  if len(arr) < 2:
    return None

  arr.sort(reverse=True)
  return arr[1]

n=int(input("n = "))
arr=[10,5,10]
print("The array elements are:\n",arr)
find_second_largest_sorted(arr)
print("After sorting the elements are:\n",arr[0])