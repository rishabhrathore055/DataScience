# word = dict()
# word['Web Dev'] = 1
# word['Andriod'] = 1
# word['Data Science'] = 1
# word['Web Dev'] = word['Web Dev'] + 1
# # print(word['Andriod'])
# counts = dict()
# domain = ['Web Dev','Andriod','Data Science']
# for jobs in domain:
#     counts[jobs] = counts.get(jobs,0) + 1
# print(counts)
# Q1 - Write a program to count the number of times each word occurs in an array
# arr = [2,7,9,31,7,8,9,2,7]
# hmap = {}
# for i in arr:
#     if i in hmap:
#         hmap[i]+=1
#     else:
#         hmap[i]=1
# for k,v in hmap.items():
#     print(k,v)
# print(len(hmap))

# Q2 - Write a program to displat the first non-repeating character in an array

# nums = [20,1,7,6,1,20,3,8,20,3,8,7]
# hmap = {}
# for i in nums:
#     if i in hmap:
#         hmap[i]+=1
#     else:
#         hmap[i]= 1
# for k,v in hmap.items():
#     if v == 1:
#         print(k)
#         break

# Q3 - Write a program to  find the common elements between two arrays
# a =[ 3,2,15,4,7,8,2]
# b =[4,9,11,6,2]
# hmap = {}
# res = []
# for i in a:
#     if i in hmap:
#         hmap[i]+=1
#     else:
#         hmap[i] = 1
# for j in b:
#     if j in hmap:
#         res.append(j)
#         del hmap[j]
# print(res)
# nums1 = set(a) # Use set to remove duplicates
# ans = []
# for num in b:
#     if num in nums1:
#         ans.append(num)
#         nums1.remove(num)
# print(ans)

# Q4 - Write a program to check if arr[i] + arr[j] = k and i != j
arr = [1,3,2,3,8,9]
k = 4
# for i in range(len(arr)): ## tc = O(n^2)
#     for j in range(i,len(arr)):
#         if arr[i] + arr[j] == k and i != j:
#             print(arr[i],arr[j])
# print(-1)
# hset = set() ## tc = O(n) using hashset
# for i in arr:
#     r = k - i
#     if r in hset:
#         print(i,r)
#         break
#     else:
#         hset.add(i)
# hmap = {} ## tc = O(n) using hashmap
# for i in arr:
#     print(i)
#     r = k - i
#     if r in hmap:
#         print(i,r)
#         break
#     else:
#         hmap[i] = 1
