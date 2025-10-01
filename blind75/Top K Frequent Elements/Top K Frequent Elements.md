# Question

Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Example 2:
Input: nums = [7,7], k = 1
Output: [7]

Constraints:
1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.

## Solution

What are the edge cases that we should consider?

- What if the array is empty?

  - Array cannot be empty as per constraints.

- What if k is 0?

  - k cannot be 0 as per constraints.

- What if k is greater than the number of unique elements in the array?

  - k cannot be greater than the number of unique elements as per constraints.

One quick solution is to use a counter (or a hash map) to store the frequency of each element in the array, then sort the elements (keys) by their frequency (values) and return the top k elements.

In this case, the time complexity is O(N log N) due to the sorting step, where N is the number of unique elements in the array. And the time complexity is O(N) for counting the frequencies. Making the overall time complexity O(N log N).

The space complexity is O(N) for storing the frequencies in the counter.

But we can do better than this with the bucket sort algorithm.

### Using a Max Heap

We can use a max heap to store the elements by their frequency. We can then pop the top k elements from the heap to get the k most frequent elements.

In this case, a max heap is a binary tree where the value of each node is greater than or equal to the values of its children. This way, the root node always contains the maximum value.

Here is an example of a max heap:

```
        10
       /  \
      9    8
     / \  / \
    7  6 5   4
   / \
  3   2
 /
1
```

We can store the elements in a max heap in a list where the `parent node` is at `index i`, the `left child` is at `index 2*i + 1`, and the `right child` is at `index 2*i + 2`.

For example, the above max heap can be represented as a list: `[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]`.

Notice that the root node, `10` is at index `0`

- The left child, `9` is at index `1` (2*0 + 1)
- The right child, `8` is at index `2` (2*0 + 2)

For the node `9` at index `1`

- The left child, `7` is at index `3` (2*1 + 1)
- The right child, `6` is at index `4` (2*1 + 2)

And so on...

See implementation here: [Max Heap Data Structure](https://www.geeksforgeeks.org/dsa/introduction-to-max-heap-data-structure/), [Binary Min/Max Heap Overview](https://www.youtube.com/watch?v=IjPZc9zpn7Y)

Python docs for [heapq module](https://docs.python.org/3/library/heapq.html), and more reading [Heap queue or heapq in Python](https://www.geeksforgeeks.org/python/heap-queue-or-heapq-in-python/).

Using a max heap to solve this problem, we can follow these steps:

1. Count the frequency of each element in the array using a counter (or a hash map).
2. Create a max heap and insert each element along with its frequency (key) into the heap.
3. Pop the top k elements from the heap and store them in a result list.
4. Return the result list.

For time complexity:

- Counting the frequency of each element takes O(N) time.
- Adding N elements to the heap (using heapify) takes O(N) time.
- Popping one element from the heap takes O(log N) time, and we do this k times, so it takes O(K log N) time.
- Hence, the overall time complexity is O(N + K log N). This is a little bit better than the previous solution.

### Bucket Sort Algorithm

[Bucket sort](https://www.geeksforgeeks.org/dsa/bucket-sort-2/)

In Bucket Sort, we divide the element in an array into several bin or buckets. Each bucket is then sorted individually, either using a different sorting algorithm, or by recursively applying the bucket sort algorithm.

Generally, the number of buckets is chosen to be equal to the number of elements in the array. This way, we can ensure that the elements are distributed evenly across the buckets.

In the best case, the time complexity of bucket sort is O(N) when the elements are uniformly distributed across the buckets. In the average case, the time complexity is O(N + K) where K is the number of buckets. In the worst case, the time complexity is O(N^2) when all elements are placed in a single bucket.

if the element in the array are not integers, we can use a scaling function to map the elements to integers or to another standard that we can use to define the buckets.

Here is an example of using bucket sort to sort and array:

- We have an array of integers: [4, 2, 2, 8, 3, 3, 1]

- We create an array of buckets, where each bucket is an empty list. The number of buckets is equal to the maximum value in the array plus one (to account for the zero index). In this case, we have 9 buckets (0 to 8).

  Buckets: [[], [], [], [], [], [], [], [], []]

- We iterate through the array and place each element in its corresponding bucket based on its value.
  - Place 4 in bucket 4: Buckets: [[], [], [], [], [4], [], [], [], []]
  - Place 2 in bucket 2: Buckets: [[], [], [2], [], [4], [], [], [], []]
  - Place another 2 in bucket 2: Buckets: [[], [], [2, 2], [], [4], [], [], [], []]
  - Place 8 in bucket 8: Buckets: [[], [], [2, 2], [], [4], [], [], [], [8]]
  - Place 3 in bucket 3: Buckets: [[], [], [2, 2], [3], [4], [], [], [], [8]]
  - Place another 3 in bucket 3: Buckets: [[], [], [2, 2], [3, 3], [4], [], [], [], [8]]
  - Place 1 in bucket 1: Buckets: [[], [1], [2, 2], [3, 3], [4], [], [], [], [8]]
  
- After placing all elements in their respective buckets, the buckets look like this:

  Buckets: [[1], [2, 2], [3, 3], [4], [], [], [], [], [8]]

- In this case the buckets are already sorted, but if they were not, we would sort each bucket individually.

- Finally, we concatenate the buckets to get the sorted array: [1, 2, 2, 3, 3, 4, 8]

### Bucket Sort for Top K Frequent Elements

We create an array of buckets, where the index of each bucket represents the frequency of the elements in that bucket. The value at each index is a list of elements that have that frequency.

The size of the buckets array is equal to the length of the input array plus one (to account for the zero index). This is because the maximum frequency of any element in the array can be equal to the length of the array (if all elements are the same).

We then iterate through the frequency counter and place each element in its corresponding bucket based on its frequency.

Finally, we iterate through the buckets array in reverse order (from highest frequency to lowest frequency) and collect the top k elements until we have k elements in our result list.

The time complexity of this approach is O(N) for counting the frequencies and O(N) for placing the elements in the buckets, making the overall time complexity O(N). The space complexity is also O(N) for storing the frequencies and the buckets.