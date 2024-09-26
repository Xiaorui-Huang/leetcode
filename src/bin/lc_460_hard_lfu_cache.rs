/*
* @lc app=leetcode id=460 lang=rust
*
* [460] LFU Cache
*
* https://leetcode.com/problems/lfu-cache/description/
*
* algorithms
* Hard (40.47%)
* Likes:    4338
* Dislikes: 268
* Total Accepted:    188.7K
* Total Submissions: 455.7K
* Testcase Example:  '["LFUCache","put","put","get","put","get","get","put","get","get","get"]\n' +
 '[[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]'
*
* Design and implement a data structure for a Least Frequently Used (LFU)
* cache.
*
* Implement the LFUCache class:
*
*
* LFUCache(int capacity) Initializes the object with the capacity of the data
* structure.
* int get(int key) Gets the value of the key if the key exists in the cache.
* Otherwise, returns -1.
* void put(int key, int value) Update the value of the key if present, or
* inserts the key if not already present. When the cache reaches its capacity,
* it should invalidate and remove the least frequently used key before
* inserting a new item. For this problem, when there is a tie (i.e., two or
* more keys with the same frequency), the least recently used key would be
* invalidated.
*
*
* To determine the least frequently used key, a use counter is maintained for
* each key in the cache. The key with the smallest use counter is the least
* frequently used key.
*
* When a key is first inserted into the cache, its use counter is set to 1
* (due to the put operation). The use counter for a key in the cache is
* incremented either a get or put operation is called on it.
*
* The functions get and put must each run in O(1) average time complexity.
*
*
* Example 1:
*
*
* Input
* ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get",
* "get"]
* [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
* Output
* [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
*
* Explanation
* // cnt(x) = the use counter for key x
* // cache=[] will show the last used order for tiebreakers (leftmost element
* is  most recent)
* LFUCache lfu = new LFUCache(2);
* lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
* lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
* lfu.get(1);      // return 1
* ⁠                // cache=[1,2], cnt(2)=1, cnt(1)=2
* lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest,
* invalidate 2.
* // cache=[3,1], cnt(3)=1, cnt(1)=2
* lfu.get(2);      // return -1 (not found)
* lfu.get(3);      // return 3
* ⁠                // cache=[3,1], cnt(3)=2, cnt(1)=2
* lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate
* 1.
* ⁠                // cache=[4,3], cnt(4)=1, cnt(3)=2
* lfu.get(1);      // return -1 (not found)
* lfu.get(3);      // return 3
* ⁠                // cache=[3,4], cnt(4)=1, cnt(3)=3
* lfu.get(4);      // return 4
* ⁠                // cache=[4,3], cnt(4)=2, cnt(3)=3
*
*
*
* Constraints:
*
*
* 0 <= capacity <= 10^4
* 0 <= key <= 10^5
* 0 <= value <= 10^9
* At most 2 * 10^5 calls will be made to get and put.
*
*
*
*
*/

// @lc code=start
/// There are several approaches to this question.
/// most important aspect is to return the LRU is the frequency of use when evicting has a tie.
/// to achieve this, the most natural way to do this is using a LinkedHashSet, which keeps track of
/// the order of insertion, giving O(1) time for both front and last element access and hashed access.
///
/// However, there is no std library in rust that achieve's this easily, We only have BTreeSet, taking O(log n) time for access
///
/// This can alternatively be implemented with a doubly linked-list and storing a reference in the cache hashset to reference the frequency hashset.
///
use std::collections::{btree_map::Entry, BTreeMap, BTreeSet};

struct Node {
    frequency: i32,
    call_counter: u32,
    value: i32,
}

pub struct LFUCache {
    capacity: usize,
    call_counter: u32,
    // key: original key, Node values
    nodes: BTreeMap<i32, Node>,
    // frequency, call_counter, key
    frequencies: BTreeSet<(i32, u32, i32)>,
}

impl LFUCache {
    pub fn new(capacity: i32) -> Self {
        Self {
            capacity: capacity as usize,
            call_counter: 0,
            nodes: BTreeMap::new(),
            frequencies: BTreeSet::new(),
        }
    }

    pub fn get(&mut self, key: i32) -> i32 {
        self.call_counter += 1;
        if let Entry::Occupied(mut entry) = self.nodes.entry(key) {
            let value = entry.get().value;
            let mut node = entry.get_mut();

            self.frequencies
                .remove(&(node.frequency, node.call_counter, key));

            node.frequency += 1;
            node.call_counter = self.call_counter;

            self.frequencies
                .insert((node.frequency, node.call_counter, key));

            return value;
        }

        return -1;
    }

    pub fn put(&mut self, key: i32, value: i32) {
        self.call_counter += 1;
        if self.capacity == 0 {
            return;
        }

        if let Entry::Occupied(mut entry) = self.nodes.entry(key) {
            let mut node = entry.get_mut();

            node.value = value;
            self.get(key);
            return;
        }

        let new_node = Node {
            value,
            frequency: 1,
            call_counter: self.call_counter,
        };

        if self.nodes.len() >= self.capacity {
            // let least_frequent_group_by_lru = self.hash.pop_first().unwrap();
            let least_frequent_group_by_lru = self.frequencies.iter().next().unwrap().clone();
            self.frequencies.remove(&least_frequent_group_by_lru);
            let (_, _, eviction_target) = least_frequent_group_by_lru;
            self.nodes.remove(&eviction_target);
        }

        self.frequencies
            .insert((new_node.frequency, new_node.call_counter, key));
        self.nodes.insert(key, new_node);
    }
}

// @lc code=end
fn main() {
    let mut c = LFUCache::new(10);

    c.put(3, 17);
    c.put(6, 11);
    c.put(10, 5);
    c.put(9, 10);
    println!("{}", c.get(13)); // returns -1
    c.put(2, 19);
    println!("{}", c.get(2)); // returns 19
    println!("{}", c.get(3)); // returns 17
    c.put(5, 25);
    println!("{}", c.get(8)); // returns -1
                              //let mut c = LFUCache::new(2);
                              //c.put(1, 1);
                              //c.put(2, 2);
                              //println!("{}", c.get(1)); // returns 1
                              //c.put(3, 3); // evicts key 2
                              //println!("{}", c.get(2)); // returns -1 (not found)
                              //println!("{}", c.get(3)); // returns 3
                              //c.put(4, 4); // evicts key 1
                              //println!("{}", c.get(1)); // returns -1 (not found)
                              //println!("{}", c.get(3)); // returns 3
                              //println!("{}", c.get(4)); // returns 4
    println!("{}", c.get(9)); // returns 3
    println!("{}", c.get(10)); // returns 5
    println!("{}", c.get(10)); // returns 5
    c.put(6, 14);
    // with expected answers:
    //[null,null,null,null,null,null,-1,null,19,17,null,-1,null,null,null,-1,null,-1,5,-1,12,null,null,3,5,5,null,null,1,null,-1,null,30,5,30,null,null,null,-1,null,-1,24,null,null,18,null,null,null,null,14,null,null,18,null,null,11,null,null,null,null,null,18,null,null,-1,null,4,29,30,null,12,11,null,null,null,null,29,null,null,null,null,17,-1,18,null,null,null,-1,null,null,null,20,null,null,null,29,18,18,null,null,null,null,20,null,null,null,null,null,null,null]

    let mut c = LFUCache::new(10);
    c.put(10, 13);
    c.put(3, 17);
    c.put(6, 11);
    c.put(10, 5);
    c.put(9, 10);
    println!("{}", c.get(13)); // returns -1
    c.put(2, 19);
    println!("{}", c.get(2)); // returns 19
    println!("{}", c.get(3)); // returns 17
    c.put(5, 25);
    println!("{}", c.get(8)); // returns -1
    c.put(9, 22);
    c.put(5, 5);
    c.put(1, 30);
    println!("{}", c.get(11)); // returns -1
    c.put(9, 12);
    println!("{}", c.get(7)); // returns -1
    println!("{}", c.get(5)); // returns 5
    println!("{}", c.get(8)); // returns -1
    println!("{}", c.get(9)); // returns 12
    c.put(4, 30);
    c.put(9, 3);
    println!("{}", c.get(9)); // returns 3
    println!("{}", c.get(10)); // returns 5
    println!("{}", c.get(10)); // returns 5
    c.put(6, 14);
    c.put(3, 1);
    println!("{}", c.get(3)); // returns 1
    c.put(10, 11);
    println!("{}", c.get(8)); // returns -1
    c.put(2, 14);
    println!("{}", c.get(1)); // returns 30
    println!("{}", c.get(5)); // returns 5
    println!("{}", c.get(4)); // returns 30
    c.put(11, 4);
    c.put(12, 24);
    c.put(5, 18);
    println!("{}", c.get(13)); // returns -1
    c.put(7, 23);
    println!("{}", c.get(8)); // returns -1
    println!("{}", c.get(12)); // returns 24
    c.put(3, 27);
    c.put(2, 12);
    println!("{}", c.get(5)); // returns 18
    c.put(2, 9);
    c.put(13, 4);
    c.put(8, 18);
    c.put(1, 7);
    println!("{}", c.get(6)); // returns 14
    c.put(9, 29);
    c.put(8, 21);
    println!("{}", c.get(5)); // returns 18
    c.put(6, 30);
    c.put(1, 12);
    println!("{}", c.get(10)); // returns 11
    c.put(4, 15);
    c.put(7, 22);
    c.put(11, 26);
    c.put(8, 17);
    c.put(9, 29);
    println!("{}", c.get(5)); // returns 18
    c.put(3, 4);
    c.put(11, 30);
    println!("{}", c.get(12)); // returns -1
    c.put(4, 29);
    println!("{}", c.get(3)); // returns 4
    println!("{}", c.get(9)); // returns 29
    println!("{}", c.get(6)); // returns 30
    c.put(3, 4);
    println!("{}", c.get(1)); // returns 12
    println!("{}", c.get(10)); // returns 11
    c.put(3, 29);
    c.put(10, 28);
    c.put(1, 20);
    c.put(11, 13);
    println!("{}", c.get(3)); // returns 29
    c.put(3, 12);
    c.put(3, 8);
    c.put(10, 9);
    c.put(3, 26);
    println!("{}", c.get(8)); // returns 17
    println!("{}", c.get(7)); // returns -1
    println!("{}", c.get(5)); // returns 18
    c.put(13, 17);
    c.put(2, 27);
    c.put(11, 15);
    println!("{}", c.get(12)); // returns -1
    c.put(9, 19);
    c.put(2, 15);
    c.put(3, 16);
    println!("{}", c.get(1)); // returns 20
    c.put(12, 17);
    c.put(9, 1);
    c.put(6, 19);
    println!("{}", c.get(4)); // returns 29
    println!("{}", c.get(5)); // returns 18
    println!("{}", c.get(5)); // returns 18
    c.put(8, 1);
    c.put(11, 7);
    c.put(5, 2);
    c.put(9, 28);
    println!("{}", c.get(1)); // returns 20
    c.put(2, 2);
    c.put(7, 4);
    c.put(4, 22);
    c.put(7, 24);
    c.put(9, 26);
    c.put(13, 28);
    c.put(11, 26);
}
