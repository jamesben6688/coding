1. 反向coin exchange, 给了coin exchange的setup, 然后问题是现在给你dp table
https://github.com/jamesben6688/coding/blob/main/dp/reverse_coin.py

2. 和in memory file system那道比较像 感觉考的主要是ood. 主要是完成ls，mkdir，addContentToFile， readContentFromFile这些功能

3. 会议室II, meeting room II

4. Our goal is to truncate a list of messages down to size max_log_messages. For the sake of this problem, 
our "fair" truncation algorithm is as follows: Let X be the max log messages maintained per client. 
For each client: If the client has emitted > X messages, truncate the log messages for that client to X 
messages. If the client has emitted <= X messages, do not truncate the log messages for that client.
The goal of this problem is to figure out the maximum value of x which causes the total number of messages 
retained across all clients to be <= max_log_messages.
Write Findx, which takes the input list and max_log_messages and returns X.
Example: Suppose there are 5 log clients, and their number of messages is: (A, 50), (B, 20), (C, 1000), (D, 50). (E, 400). 
Suppose we want to have no more than 300 total messages after truncation.
https://github.com/jamesben6688/coding/blob/main/binary_search/truncate_message.py

5. 设计一个restaurant wait list system，要求满足以下三个功能：
	1. 把新顾客加入list
	2. 任何时候把正在排队的顾客移出list （如果客人突然不想等了）
	3. 有桌子空出来的时候把下一桌客人安排进去
整个题非常灵活，第三个部分可以自己定义怎样安排客人，可以严格按照桌子的容客量也可以只要小于桌子size就安排。
   
餐厅waitlist系统，客户会随时到来并且填写party人数，也可能随时会走。任意时刻如果有空桌，需要确定serve哪一队客人。
其实写代码的部分很简单，讨论了下不同结构的复杂度。主要是在讨论这个系统到底要怎么实现：
优先serve先来的客人？优先serve刚好能坐下的big party？
展开比较多，针对每个展开的问题讨论了下使用什么样的数据结构和细节的处理。

Restaurant waiting list
Build a data structure to perform three operations (Restaurant is full initially):
1) waitList (string customer_name, int table_size):
Add customer with given name and table size they want to book into the waitlist
2) leave (string customer_name):
Customer wants to leave the waitlist so remove them.
3) serve (int table_size):
This means restaurant now has a free table of size equal to table_size. Find the best customer to serve from waitlist
Best Customer: Customer whose required size is less than or equal to the table_size. If multiple customers are matching use first come first serve.
For e.g. if waitlist has customers with these table requirements => [2, 3, 4, 5, 5, 7] and restaurant is serving table_size = 6 then best customer is index 3 (0-based indexing).

https://github.com/jamesben6688/coding/blob/main/linklist/restaurant_wait_list.py

6. 给你一个bookshelf 里面有 不同的书 每本书有 name，author 等， name不是唯一的 可能会重复
	还有个需求是 整个bookshelf 包含一个bookmark，这个bookmark只指向一本书 在 removeFromShelf 和 moveFromShelf的同时 
	也需要同时移除 或者 移动到新的位置
	让你设计一个class 里面需要实现一些基本的功能实现
	1. addToShelf(toIndex, list)把当前的list的书加到bookshelf的list里面 从toIndex的位置开始
	2. removeFromShelf(index) 把当前的index的书移除
	3. moveFromShelf(fromIndex， toIndex， number) 例子 list里面有10本书 number等于2. fromIndex等于0.toIndex等于5 
	你需要把 0-1的书移到 5-6的位置
	4. getBooks() 把当前的已在bookshelf的全部返回
	5. getBookmark() 返回bookmark值
	值得讲一下 bookmark 可以主动的去设置某本书 想象自己主动加个功能去做这个事 比如 
	6. setBookmark(index)
https://github.com/jamesben6688/coding/blob/main/linklist/book_shelf.py

7. 判断str1是否可以映射到str2，比如abc -> XYZ 是true但 aaa-> XYZ是false， 
follow up是如果给一个list，可以映射的merge起来
https://github.com/jamesben6688/coding/blob/main/str/str_map.py

8. router 的range问题，比如router是 Router A [0,0] , Router B[0,8], Router C[10,8], Router D [0,28] R = 10, 
输入start router和end router，返回是否能从start传递到end，每次传递只能在range内，这里这个distance大叔说manhattan distance就可以。 
follow up是 比如router会优先传递给最近的

有个startRouter, 有个endRouter，有个RouterLocation Array，有每个Router可以connect的range。
看是否可以从start connect to end
https://github.com/jamesben6688/coding/blob/main/bfs/my_router.py
https://github.com/jamesben6688/coding/blob/main/bfs/router.py

given a couple routers (list of coordinates), and sender , receiver. 
determine if a message from sender can be received by receiver. A message can be sent to the neighbors 
within 10 feets

9. 一个一维数组[3,10,2,12] 判断从起始点0到最后终点的最大分数，每次跳跃格数任意（1格或者直接跳到最后），
score = 目的地的 score * distance，比如直接跳到最后分数是 12*3 = 36， 如果一格格跳是10+2+12 = 24。
用dp做的，发现greedy也可以
（10，8）是坐标
它和范围10以内的其他router是connected
问从start能不能走到end
https://github.com/jamesben6688/coding/blob/main/dp/jump_score.py

10. 跟meeting room 类似，不记得具体了。
	input:
	1. a list of lists with three elements representing person_number，start_day, and end_day inclusively.
	2. 最大天数
	3.人数
	参数 1 代表有哪些人在哪段时间不在
	Output：
	输出能够凑齐所有人的天数
	四个follow-up，follow up没写code。
	
11. Given an array of meeting blocks for each person, each person has a range of days they are unavailable,
	The following is a block structure:
	It was given :
	class block:
	int personId;
	int startDay;
	int endDay;
Find all the days where everyone is available.
Follow up : How would you find all the days where at least P people are available.
Second follow up : find all the periods where P people are available for atleast X consective days.

有空, 空闲时间
https://github.com/jamesben6688/coding/blob/main/interval/people_available_days.py
https://github.com/jamesben6688/coding/blob/main/swipe_line/people_available_days.py


12. 给你一个地址簿存着一系列地址，大致是 (街道号码，街道名称，城市名称，所在州) 这样的格式， 
e.g.,[(“1”, “Main”, “San Jose”, “CA”), ("1", "Main", "Austin", "TX")]。
	要考虑不同的城市可能存在一样的街道， 不同的州存在同样的城市等等等等的情况
	问题是有一系列query（很多很多), 判断有没有match.
	query的格式可能存在以下几种情况。 有些elem可能存在NULL，这个时候如果其它的匹配上也认为是找到了match
	query = (“1”, “Main”, “San Jose”, “CA”) --> found match
	query = (“1”, “Main”, “San Jose”, None) --> found match
	query = (“1”, “Main”, None, None) --> found match
	query = (“22”, “Main”, “San Jose”, “CA”) --> no match
	
https://github.com/jamesben6688/coding/blob/main/tire/street_match.py
	
13. Given an array representing run-length encoded values, write an iterator to unpack it.
Sample: Given array [1,2,3,4,1,5], expected unpacked output [2,4,4,4,5] (1个2， 3个4，1个5)
Follow up:
设计一个class可以记录乱序接受的chunk，并记录从开始到哪一个chunk中间没有未收到的chunk。
Follow up:
怎么降低上一问中class的memory footprint 以及最糟情况，平均情况；哪些地方可能应用这样的算法（tcp 收包）
https://github.com/jamesben6688/coding/blob/main/array/unpack.py

14. 给一个表，表里有人名，shift 开始时间，结束时间，输出一个表格显示开始时间，结束时间，还有on shift的所有人。
Follow up:
一人有多个shift怎么处理；如何保持输入表格里人名字显示的顺序。
这一轮楼主也是正常发挥，但是在做的时候assume输出人名的顺序不重要，但是challenge我例子里是按shift开始顺序输出的，

15. 给一个没有运算符的等式，填入(,),+,*四种符号使等式成立（任意解），或返回不成立，第一问只有3个数在等式左侧如：
输入2 3 4 = 20 输出 （2+3)*4=20
Follow up:
如果等式左侧的数字有多个（任意个）怎么解。
https://github.com/jamesben6688/coding/blob/main/dfs/add_operators.py
https://github.com/jamesben6688/coding/blob/main/dfs/%E8%AE%A1%E7%AE%97%E6%9C%BA%E6%B7%BB%E5%8A%A0%E7%AC%A6%E5%8F%B7%E7%94%9F%E6%88%90%E7%AD%89%E5%BC%8F.py

16. tree，找到所有满足条件的node

17. 01矩阵求最大长方形面积
https://github.com/jamesben6688/coding/blob/main/mono_stack/max_rect_area.py

19. Consider a bank with some intial amount of money. Consider an array which represents list of transactions 
which are going to come through customers. + means deposit - means withdrawl. Bank can choose from which customer 
they want to start serving the customers and they can refuse any number of customers. But once they start they 
have to serve till the time its impossible to serve the customers. Maximize the total customers bank can serve.
Example :
Bank has 1 unit of money intially.
Customer transactions : [1, -3, 5, -2, 1]  # find the longest subarray, such that the sum of the subarray+init>=0
answer = 3
Bank starts with customer with deposit of 5
1+ 5 = 6
6 - 2 = 4
4 + 1 =5
If bank starts at in index 0 can only serve 1 customer
1+1 =2
2-3 = -1 not possible

https://github.com/jamesben6688/coding/blob/main/array/max_customers_serve.py

20. 行的显示宽度不得超过 70 个字符。
需要写一个方法可以自动将代码格式化为指定的格式。
从数组中读取数据生成 table list。
每列均左对齐，以便于阅读。即每个单元格都包含一个字符串。
当然，字符串保持原始顺序。
例子：
W = 70 (characters)
S = [IsAudioBuffer, GetTimestamp, SetTimestamp, GetSampleRate, GetSampleSize, GetNumberOfChannels,
GetNumberOfSamples, GetDataBuffer, GetChannel]
我们可以将其格式化如下：
IsAudioBuffer GetTimestamp SetTimestamp GetSampleRate |
GetSampleSize GetNumberOfChannels GetNumberOfSamples GetDataBuffer |
GetChannel |
给定字符串列表和每行的最大字符数，使用最大字符数格式化表格,并且不能违宽度的限制。

21. find all files in a tree-shape directory. how to optimize. how to find top 10 largest subdirectories.

22. given n tasks. 1-n. there is a pair of tasks that will result in unit test failure. 
find the pair in fastest way. (3 methods in total, need to make assumption about how to run test)
比如有1 -- n 个task，有一个pair比如1,2一起跑会挂，然后给你这n个task，你要最快的找到这个pair
https://github.com/jamesben6688/coding/blob/main/divide_conquer/min_tests.py

23. 用户在点开搜索框后，提供最近的K个搜索输入作为关键词推荐。然后这次的输入也将用于下次的推荐。例子：
search history:
paris
tokyo
seattle
K= 2， 那么应该给出的就是：
paris
tokyo
注意：需要按时间排序，最近的搜索历史应该排在前面。如果历史里有重复的，就只记最近的一次。
follow-up: 如何k是一百万怎么办。
https://github.com/jamesben6688/coding/blob/main/linklist/user_word_recommendatoin.py

24. Takes in a number n and returns the nth Fib. number
int fibonacci(int n) {
}
NOTE: DO NOT USE RECURSION
USE CONSTANT O(1) STORAGE

25. Given the following implementation of a stack:
class Stack {
bool isEmpty();
void push(int n);
int pop();
}
Use it (and NOTHING else) to implement the following specification of a queue:
class Queue {
void enqueue(int n);
int dequeue();
}

26. Given the same stack class as above, implement the following class using ONLY the given Stack class:
Stack:
Push, pop, peek
class MinimumStack {
void push(int n);
int pop();
int minimumValue(); // Returns smallest value in the Stack but does not pop it.
}
CONDITION: All three methods should be O(1) time worst case.

27. Given a binary search tree with the size of the subtree for each node stored in that node, 
and given a number i, find the ith smallest element in the tree.
EXAMPLE:
search value subtree size
			44, 9
			/	\
		20,3 	61,5
		/  \    / 	\
	12,1  31,1 55,1 70,3
					/   \ 
				  65,1  71,1

For i=1, the answer is 12
For i=3, the answer is 31
For i=5, the answer is 55
struct Node {
	Node* left, right, parent;
	int search_value, subtree_size; // Current node is counted in subtree_size so for leaf = 1.
}

28. 你从A出发要去B城市，途中可能经过CDE城市
你有所有的火车时刻表 ex: 10:00->20:00 A C

29. 给一段string文字和行宽，要求多少lines，考虑要下一个词放不下的时候换行。
然后一个follow up是有两个如上的string和一个公用的行宽。问怎么求并排放置时候的最小行数。

30. 给一大堆jigsaw puzzle pieces, 假设它们都是正方形的, 每一个有四个面, 每个面有一个数字 (从 -50...0...50), 
然后如果要拼好, 每两个面的数字和都需要为0.
如果一共有很多个pieces, 但不需要那么多, 怎样优化筛选出尽量少的pieces来去让电脑去组装拼图.

31. 找interval intersection 比较简单， 就是找left 最大和right最小
follow up是给定 和 Sn的interval 集合，找到 一个Q(数字集合）， 让Q满足 Q中的元素可以落在S的每一个interval中， 求Q size的最小值是多少

32. 给一个chat group， 统计每一个message中用户和单词的数量， 返回发的message中用词最多的n个用户

33. 输入一堆数，返回给定window size的平均数
follow up，返回平均数的时候，忽略最大的k个数

34. 给两个list，一组人的出生年份，和他们的死亡年份，然后找出一定范围内的年份中间哪个年份的人口最多。当然了，出生年份和死亡年份有重叠。

35. 23复杂版本,每个元素是(time, value),表示当前时刻当前list的值变成value, 要求结果是所有list 里value和的时刻变化

36. BFS,要求记录路径

37. number of island二叉树版本

38. list1 list2（长度不定）给定值K，返回一个list为删除最少元素的list2，使得list1与list2中前K个elements没有交集。
e.g.: list1=[3,2,4,5,2], list2=[2,1,3,4], K=2----return [1, 4]
[3, 2]与[2, 1] 删掉2 => [3, 2]与[1, 3] 删掉3=> [3, 2]与[1, 4]
follow up: 优化复杂度

39. 有个停车场，门禁记录每辆车的进出时间，时间为整数。给定时间t，返回从0到t每一时刻停车场有多少车。
e.g.: 三辆车进出时间[[1,3], [2,5], [4,5]], t=4----return [0, 1, 2, 1, 2]
follow up如果进出时间不是整数怎么改code

40. 17电话号码组合以及lc139单词拆分的合体，给input 一串数字，判断是否存在一个对应的字符串可以被拆成已知单词组合。

41. 合并K个升序排序的item数组，item有id和 数值大小，一个数组里没有重复id，但是不同数组里可能有重复，需要自己主动考虑去重的问题。

42. 1825可以TreeMap和Heap两个方法解决，都是要维护两组数据。更新的时候顺便算出sum。

43. dfs 二分图， 给了两个pos 和 一个grid， grid 的给的数字代表是 elevation, 找到能流淌去两个position 的 最大值的 position
follow up：如果pos 有多个的话 全部找出来

44. 给一个数字 和 一个number，找出这个数字的number 有效数字
例子: "124.23" , 2 --> 输出'120"

45. 在一个array 里面 找出 ascending 和 descending array （后面的数字和之前数字只能差一）
然后找出所有subarray 的 所有数字的和
例子[1,2,3] --> [1], [2], [3], [1, 2] , [2,3], [1, 2, 3] 最后return 1+ 2 + 3 + （ 1 + 2） + （2 + 3） + （1 + 2 + 3）

46. variation of top K

47. course schedule ii； parse csv file into a certain data structure

48. maximum weight matching for biparite graph。转化成maximum flow然后用ford fulkerson求解。

49. 一个公司有mangers，每个manager可能会direct管理一些人；然后这些人又可能管理其他一些员工，形成一个树状管理结构。问题：1）算出来有多少manager的工资是低于他direct or indirect管理的所有员工的平均工资（underpaid managers)？2）计算最小需要的budget给underpaid managers提高工资，使得没有公司任何underpaid员工？3）算出来有多少manager的工资是低于他direct or indirect管理的所有员工的median salary？
Sol: bfs+merge sort

50. 给你一个租车公司最近一个月的租车记录，每个记录包含字段RentalRecord (id, picktime, returntime)。问题：至少需要多少车，并且返回每个record的assignment关系（指：哪个RentalRecord分配了哪辆车）
Sol:sweep line+queue

51. 系统api会一直接收到返回的pin值， 给个int k， 返回过去k个pin值的average， 先确认了可以assume 返回average的call会在有k个值后发生， 收到的pin值是现实中的pin值大小一般0-1000， 所以不会overflow
就2个function 一个add pin 一个 average ， average过了一遍queue算。。能不能更快 才反应过来 直接存一个total 每次add pin的时候更新， 这样average就变成O（1）
第二问 有时候pin值会不稳定 所以现在计算average需要去掉一个最低值和一个最高值
2个priorityQueue 最高最低值 加上一个hashmap保存现在在最近k个pin值及个数， 计算average的时候保证最高最低值还在现有的k pin值，不在了就弹出直到map里存在这个数字

52. Given a text separated by spaces and a certain margin
How many minimal lines do you need to print everything
Follow-up: If you have 2 texts that should be fitted into the same file and given maxwidth, return
Example Follow-up:
Text1 = “I have eaten”
Text2 = “I am”
max_width = 10
[
I have | I
eaten | am
]
return 2

53. Check whether 2 integers have common digits=> num_a = 9919, num_b = 2212=> Return True due to 1 in both numbers
Follow-up: given an array of n integers, check whenether there is a path from integer a to integer b
Example:
Start = 1 end = 20 list =[1, 20, 40, 41]
Path = [1, 41, 40, 20]

54. summation timeseries:
Example:
T1 [[0, 0], [1,2], [8, 10], [15, 0] ] # at time 0, serie value becomes 0; at time 1 serie value become 2; at time 8 serie value 10 etc…
T2 [[0, 0], [3,5], [10,4], [12, 0]]
Output: [[0,0] [1,2] [3, 5] [8, 10] [10, 14], [12, 10], [15, 0]]

55. Logic
Example:
a > b
b > c
d < e
Return True

a > b
b > c
c > a
Return False because third inequality cannot be done.

56. sort an array但这个array满足一个条件, the absolute difference between the index of an element in the sorted array and the original array is less than k, k << len(arr)
然后要求你leverage this information to speed up the sorting to outperform a general algo like quicksort

57. 给了一个two-dim array，有三种点，wall，empty和customer table，要求find an empty cell to place a service table so that the sum of the distance from this table to all other customer tables is shortest

58. Assuming that each task has {id, priority}, you will receive three types of requests as a stream:
1. New task, meaning that task {id, priority} is newly generated.
2. Pick task, meaning that the task handler can handle the next task, so you have to return the highest priority task and remove it.
3. Change priority of task, meaning that specific task’s priority is changed, so you have to update the priority of the task.
For example,
New task {3, 2}// id = 3, priority = 2
New task {5, 4}
New task {2, 3}
Pick → you should return task {3, 2} // if a task has a lower number for the priority, it is a higher priority.
Update priority {5, 1} // We changed the priority of task whose id is 5 from 4 to 1
Pick → you should return task {5, 1}
New task {1, 0}
New task {4, 6}
Update priority {2, 7}
New task {6, 5}
Pick → you should return task {1, 0}
Pick → you should return task {6, 5}
Pick → you should return task {4, 6}

59. //! The electronics shop near me is creating an ecommerce site. They have a
//! bunch of different `Item`s for sale; each item has a `Category`. These
//! `Categories` are related to each other with is-a relationships. In this
//! example graph, each `Category` is a node, and each directed edge represents
//! an 'is-a' relationship.
// Here is an example graph:
// ┌─┐   ┌─┐
// │1│   │2│  1 = electronic device
// └┬┘   └┬┘  2 = communications device
//│   │ 3 = wireless device
//│   │ 4 = telephone
//├────┐  │ 5 = smartphone
//│  │  │ 6 = landline phone
//│  │  │
// ┌▼┐ │ ┌▼┐
// │3│ └──►│4│
// └┬┘   └┬┘
//│   │
//│   │
//│  ┌────┤
//│  │  │
//│  │  │
// ┌▼┐ │ ┌▼┐
// │5│◄──┘ │6│
// └─┘   └─┘
// Available API:
class Category {
public:
int id() const;
// elements non-null, non-owning, unique
std::vector<const Category*> children() const;
// elements non-null, non-owning, unique
std::vector<const Category*> parents() const;
};
class Item {
public:
std::string_view name() const;
const Category& category() const;
// Finds all categories that this item is a part of.
// elements are non-null, non-owning, unique
std::vector<const Category*> TransitiveCategories() const;
};
//! So an `Item` that is marked as a smartphone (Category 5), is also a wireless
//! device, a telephone, an electronic device, and a communication device.
//! {1, 2, 3, 4, 5}
Part1: Design an algorithm to find all trnasitive categories of an item.
Part2:
//! This Ecommerce site wants to mark down some `Item`s on their website,
//! depending on the `Category` it's in. The admin of this website wants this
//! filter to be rule-based, e.g.: "Mark down all telephones, except if it is a
//! wireless device".
//!
//! The `Catagory` graph might be arbitrarily large (maybe millions of
//! categories). Filter rules can be arbitrarily complex.
// Examples:
// 1. Mark down all electronic devices.category == 1
// 2. Markdown all items that are smartphone or landlines.
// 2a. Mark down all items that are () or ().
// 3. Mark down all items that are telephones and wireless devices.
// 4. Mark down all non-smartphone telephones.
// 5. Mark down all communication devices unless they're non-smartphone telephones.
// 6. Mark down items that are part of Sale #1, but not Sale #3.
// 6. Mark down items that are (electronic devices), but not (telephones and wireless devices).
// 8. Mark down items that are (electronic devices), but not (telephones but not communication devices unless they're non-smartphone telephones).
Design a data structure to represent an arbitrary filter.

60. Given a vector of sorted string, and a prefix, find the number of strings has the prefix

61. An image is stored in a 2D byte array byte[][] image. Your task is to mirror (or reverse) this image.

Example 1:

Input: [[11110000]]
Output: [[00001111]]
Example 2:

Input: [[11010100, 00101010]]
Output: [[01010100, 00101011]]
Example 3:

Input:
[[11110100, 10101010, 00111010],
 [11000000, 10111010, 00100011],
 [10010001, 11100111, 00111010]]
Output:
[[01011100, 01010101, 00101111],
 [11000100, 01011101, 00000011],
 [01011100, 11100111, 10001001]]
 
follow-up 1.如果把array flatten一个1d array时怎么办；
	2. time complexity怎么优化。
	
62. 给一个键盘，一个最大距离（相邻字母在键盘上的距离），一个词，问是否可以用键盘在不超过最大距离的情况下输入这个词。
具体：
jump_distance: 2
keyboard：
[
['Q', 'X', 'P', 'L', 'E'],
['W', 'A', 'C', 'I', 'N'],
]
word: PENCIL
P ->(2) -> E ->(1) -> N ->(2) -> C ->(2) -> I  ->(1) -> L 可以输入return true
word: PACE
P ->(2) -> A ->(1) -> C ->(3) -> E 不可以输入return false

Follow up问如果按键有重复的怎么做，BFS DFS

63. 写一个21点的小游戏，两1个玩家，一个庄家轮流抽牌。rule就是典型的21点的rule。超过21点立刻输，没超过就谁接近21点谁赢，玩家们可以在任何时间停止继续抽牌。
一个玩家，一个庄家轮流抽牌。rule就是典型的21点的rule。超过21点立刻输，没超过就谁接近21点谁赢，玩家们可以在任何时间停止继续抽牌。

64. 湖泊数量。起點一定是在land上，把海水也看成湖，用了2個BFS，每次找到水再count，最後返回count-1；
followup: 如果海水面積很大就很浪費算力, 如何优化

65. To determine if the paths of two robots in a 2-dimensional space intersect based on the given instructions (F for forward, L for turn left, R for turn right), and then check whether their paths overlap at any point.
每次L和R需要check当前机器人的朝向

66. 给数字PI ， 找到 digit与index相同的index number 并返回这个list of indices
例如 3 1 4 1 5 对应index 1 2 3 4 5， 5 和5 相同 所以list里要包含5
给的exmaple只有前9个数字 并没有多位数的index的exmaple 所以我先问了那多位数如何compare 总不能就比较前9个数字就完事了吧
例如index 123， 对比个位数与pi的第123个digit 然后对比123中的2 和pi的第122个digit 以此类推 必须所有的digit相同才算在return list
followup: time complexity和memory complexity 还问了如果数字太长 一个server 存不下 如何处理

67. 有一堆stack和，每个stack上都有blocks。 给出一个状态和结束状态，每一次只能移动一个block，可以移到其它stack上，或桌面上。
问用最少steps将initial state 移到final state. 输出每一个steps的状态。
[goal-stack-planning-for-blocks-world-problem](https://apoorvdixit619.medium.com/goal-stack-planning-for-blocks-world-problem-41779d090f29)
Example
initail state
1
2
final state
2
1
最少 4 steps
2 1
-----
 1 2
------
2 1
-----
2
1
------

68. 一维空间下，有颜色分别是红蓝两种点的集合，然后有个query的点，只需要在这两个集合里找离这个点最近的点，然后赋予他相应的颜色
Follow up： 二维, 高维怎么写

69. 有一个由（N-1）条连接的N个城市网络，类似于一棵树。在两个直接相连的城市（Ci，Cj）之间旅行需要固定的小时数Tij。
对于从源城市S到每个其他城市Ck的最短路径，有多少个城市会在H小时内访问。
输入：
第一个变量将包含城市数量：N
接下来的每行都包含一对城市，表示双向道路，以及旅行所需的小时数：Ci Cj Tij
接下来一行将包含源城市：S
接下来的N行中，每行都包含城市和在源城市到城市Ck的路径上要计数的小时数：Ck Hk
输出：对于最后一组输入行中的每个城市和相应的小时数，Ck Hk，打印从源城市到城市Ck的最短路径上在Hk小时内访问的城市数量。
input:
N = 4
0 1 10
1 2 5
2 3 2
S:0
0 2
1 8
2 15
3 10

70. 假设有 N 堆卡片 每堆卡片都有很多张 现在对每堆卡片进行一些清理 确保在一定程度上每堆卡片都有其独特之处 想要确保在每堆卡片的前 K 张卡片中 没有与前面几堆卡片的前 K 张卡片重复的
参数解释：
N 是卡片堆的数量。
K 是每次比较的卡片数量，ex: 每次只看每堆的前 10 张卡片。
D 是想要回顾的前几堆卡片的数量 比如只想比较最近的 3 堆卡片 以确保没有重复
例子: 按照这个规则 第一堆卡片不需要做任何改变 因为它是第一堆 但从第二堆开始 检查每堆卡片的前 K 张卡片 如果发现有重复的，就把重复的卡片拿掉
通过这种套路确保每堆卡片在一定程度上有其独特性至少在每堆的前 K 张卡片中不会有重复 .

71. 给你个N（他给的是650），然后问这中间（0 - N-1）哪些数字是可能会up side down 被看错的，例如169 就可能会被调个头看成691。但是1被看错了还是1，69被看错了还是69。return所有可能被看错的数字。

72. Trie，file system
两个input，
第一个 file names：
[a/b/c/d/somefile.txt, c/d/e/f/anotherfile.txt, /a/b/c/d/somefile2.txt, ...]
第二个selected files：
[a/b/c/d/somefile.txt, /a/b/c/d/somefile2.txt]
然后return所有被选择的文件，如果这个directory下面的所有文件都被选中了，那么直接return这个directory就行，比如上面给的这两个input，返回的就应该是：[a] ，因为a下面所有文件都被选中了
trie的children的时候，应该用hashmap

73. longest repeating substring, 这个substring里面必须都是同样的字母 
aaaaabc > aaa
aaabc > a
O(N)

74. 分配公寓
公寓是数据结构是{apt_number: 房间数}
{
apt1: 1
apt2: 3
apt4: 1
apt5: 10
}
然后有人名{name: 是否愿意share apt}
{
herry: yes
bob: no
eric: yes
}
一个人能占一个room
问最佳的分配方案，最后返回 {name: apt_number}
https://github.com/jamesben6688/coding/blob/main/dfs/%E5%AE%89%E6%8E%92%E5%85%AC%E5%AF%93%E9%97%AE%E9%A2%98.py

75. Suit: C as Clubs, H as Hearts, S as Spades, D as Diamonds
Rank: A, 1,2 ... 10, J, Q, K
Given a list of cards as ["AS", "3H", "3C"], detect whether the cards can be considered as valid sets.
Valid sets at least have 3 cards.
1 : all cards are having the same suit with consecutive ranks
2: OR all cards are having the same rank.
Note: the input cards are all valid card from the standard 52 card deck.
def isValidSet(cards: list):

76. A server is processing the request, write a solution to get the current high water mark request id.
for example: initial high water mark is 0, the request is processed in the following order [1,2, 5, 3, 4], highWatermark = [1, 2, 2, 3, 5]
Note: the current high water mark H is the highest number requestId, where H -1, H-2, H-3 ....  H-initial is processed by the server.
class Solution:
def __init__(self, initialHighWaterMark):
pass
def processRequest(self, requestId: int): # request Id can have duplicates
pass
def getCurrentHighWaterMark(self):
pass
需要自己define 数据结构， 要求 processRequest 和 getCurrentHighWaterMark， Time complexity为 O（1）

77. 生成 unique id，
要求：
1. 只能从给定的字符集中选择可用的字符
2. 对于同一个id, 同一个字符不能连着出现 k 次。
3. id 要 unique（废话）
举例：
字符集：{a, b, c}， k = 3,
valid ids: aabbccbbaa, ababc, cbcba,
invalid ids: aaabbbccc, ddeeff

78. input: N,
generate sequences such that for each sequence's sum of digits are equals to N. Each digit has only two options: "1" or "2".
for example:
N = 1， 1
N = 2, 11, 2
N = 3, 111, 12, 21

79. give an maze, how to find path from a to A
for example, "." is a cell that can be passed. "#" is barrier
. . A
. # .
. a #
follow up:
how to move a to A and b to B
# # . #
a B b B

81. 构建霍夫曼树

  *
 / \
 e *
  / \
  b  z

{'b': 2, 'e': 1, 'z': 2}

82. 按权重随机选择, followup:如果删除选中的元素，重复上述过程 直到list为空，

83. 给一些sentenses作为training data, 写一个predict method - 给一个word，return出现在这个word之后频率最高的词。
例如：sentenses: [“today is sunny.” “this problem is hard.” “california is sunny.”] predict(“is”) -> “sunny”.
followup: fuzzyPredict(word) -> return word based on propability.

84. You are given a list of boxes with 2 dimensions, width and height. Return the maximum number of boxes you can stack on each other. You can rotate the box so basically if you have a box with dimensions [3,2] you can turn it into [2,3]. You can only put the box on the top of the pile if the width is less than the width of the current box on the pile.

Ex:
input is [width,height]
[2,2],[3,2],[3,4],[4,3]: result=3, start with either of the boxes that have a 4, then take the [3,2] width 3, then take the [2,2] on top. Cannot use both the [3,4] and [4,3] regardless of rotation.

Don't think I did that well on this one. Initially I thought I should do a greedy type solution where you sort by both dimensions to create 2 sorted lists, then try to always put the biggest box you find. Solution I eventually came up with is based on the intuition that you just need to create a set to record the widths that have been used. Do not need to start from bottom up because for the purposes of this problem, you can just insert into the stack as if you laid it perfectly. So in above example, say I start with [2,2], record width 2 into seen stack, proceed to [3,2]. Witdh 3 has not been used, record seen 3. Proceed to [3,4], width 3 has been used. But I can rotate, and width 4 has not been used.

Something like this

seen=set()
res=0
for i in range(len(stack)):
	width,height=stack[i]
	if width in seen and height in seen: continue
	if width in seen:
		seen.add(height)
	else:
		seen.add(width)
		
	res+=1
return res

85. 假设有string "AABBCCDDEE"， 注意所有的char如果出现的话一定是连续出现的，假设有一个数k是他们的partition num，如果k = 3, 刚刚string的partition效果是 AAB BCC DDE E, 我们称一个char为valid char如果他仅存在于他的partition里面，并且在partition里面是连续存在的。
那么刚刚这个例子，返回的valid char应该是A, C, D。现在告诉你input不是整个string直接给你，而是以stream的形式一个char一个char的让你读，请你设计你的数据结构能够有 void getNextChar(char c) 和 int getNumberOfValidChars() 这两个函数。
基础的 O(n) 的space 复杂度，有比O(n)更好的不需要set的方法

86. string replacement
比如说
string: "%X%_%Y%"
map:
{
	X => "123"
	Y => "456"
}
需要output “123_456"
两个followup：
1. 如果variable 名字 不只是1个char怎么办？
2. 如果variable 可以reference 另一个variable 怎么做
map = {USER=>admin, HOME=>/%USER%/home}
string = "I am %USER% My home is %HOME%"
output = "I am admin My home is /admin/home"

https://github.com/jamesben6688/coding/blob/main/dfs/%E6%9B%BF%E6%8D%A2%E5%AD%97%E7%AC%A6%E4%B8%B2.py

87. 给一个forest，node只有parent idx，怎么delete 一个tree node

88. 一个word list，怎么build efficient prefix trie search。large scale 怎么distributed index和query

89. 找graph里有几个组，可以用dfs也可以union find

90. 矩阵里有陆地有水，找路径，区别是有个猫，返回离猫最远的路，你可以看成耗子着离猫最远的路逃跑

91. 给一个服务器的聊天消息日志文件，格式如下：
[YYYY-MM-DD HH-mm-ss] <user_name> message_text
给定了一个读取日志文件的函数（自己不用写文件IO），读出一个list of tuples，每个tuple是用户名和他这条消息里的单词数。
写一个函数来求出整个log文件中所有user里，谁说的单词数最多，给出top-k最多的user的username

Follow-up quetion：
写出处理log给出list of tuples的函数，假设文件已经读取成一个list of log strings形式。

92. There's a game you play with tiles which each can + be represented by a number within the (1, 9) - range.*
You are given a list of 13 tiles. Now you try to pick another tile to make it a winning hand.*
* We call this tile a winning tile.
A winning hand is when the 14 tiles can be grouped + into 4 valid triples and 1 pair, where a valid triple
* is either 3 of a kind, or 3 consecutive numbers.
* Some examples of winning states:
11223344555999 -> 123|123|555 |999|44
•11122345678999 -> 111|345|678|999|22
22455666777889 -> 456|567|678|789|22
# The task is to print out all such winning tiles.
# Example:
Input: "1116667788899"
•Output: [7, 8, 9]
Explanation:
1116667788899 + 7--> 11166677788899 -> 111|666|777|888|99
1116667788899 + 8 -> 11166677888899 - 111|666|789|789|88
1116667788899 + 9 -> 11166677888999 -> 111|666|888|999|77

93. 一共有N个房间，给每个会议的起始和终止时间，求所有会议都安排完后被预定次数最多的房间号。

94. 给一个integer stream(latency)，让你只记录前N个integer，然后去除里面最大的K个，算剩下(N - K)个数字的平均值
sample：5，2，3，3，5，1，5，7 ....
如果 N = 5， K = 2,当7进来时，call getAverage(int latency) 返回 3 -> （3 + 5 + 1）/ 3

95. unidirected graph查环
followup： min spanning tree，用kruskal(edge排序再union find)来解

96. 矩阵里面有很多 1 -1 0 然后把所有的1(可能有多个 more than 2) 连接起来 连的路线只能经过0 不能经过-1
然后输出所有经过的点的坐标in a list

97. 实现一个class，支持两个API
一个是add一个range
另一个是query输入的int是否在这个class的某个range里，返回true/false即可，不要求找到具体的range

98. 给一些长方形，找出来有多少是交叉的。

99. data stream 每次给定start, end, odd/even, 判断是否valid
代表 一个未知数组nums中 nums[start] + nums[start+1] + nums[start+2] .... + nums[end] 为奇数或偶数
3, 5, odd 返回true
6, 8, even 返回true
3, 8, even 返回false
input有可能overlap, 可以先不考虑负数

100. Given a list of elements, each element with an Id and 3 (guaranteed 3, valid input) string properties. If any of the 2 elements have an overlap of the properties, they are considered duplicates, group the duplicated element ids together and show in the output. If no duplicates for a particular element, output its own id.
Example:
Input:
Element1, id1, properties: P1, P2, P3
Element2, id2, properties: P1, P4, P5
Element3, id3, properties: P6, P7, P8
Expected output: { {id1, id2}, {id3} }

-> graph

101. 如何evaluate model hallucination

102. 写KMeans

103. 有一个mergedword 是两个单词通过merge sort的方式 得到的。 给你一个dictionary（word list）, 把这两个单词找出来。 举个例子：
wordDictionary: [alpha, apple, aalph, alaph, beta, banana], merged word: abelphata, 结果是alpha, beta. 因为你merge了alpha, beta， 结果是abelphata。
用的trie做
follow up 是： 如果这个dictionary 非常大， 怎么办？ 如果是由n个word 得到的， 怎么做。

104. 写一个找出最小index的api，需要implement addOrReplace(index, number)和find(number)，要求o(1)

105. 设计一个text prediction API，图论题

106. 有个Tree Node
包含 getText(), isText(), getParent(), getChildren()
下面是一个 tree 的例子，节点是有顺学的，按照网页元素的顺序
<b>This</b> is very <i> funny</i>
 <span>
\
 <b>is very<i>
/
"This"
之后给你这个tree的root，和一段字符串，比如 very funny，让你返回是哪几个node包含这个字符串

107. 一个n-array tree，node如果有children就视为manager。
问整个tree中收入低于下属收入平均值的manager个数。Follow up是问的是低于下属中位数应该怎么做。

108. 给定一个字符串要求把字符串扩展开，例如：
input: "a3"
output: "aaa"
复制代码
input: "(abc)2"
output: "abcabc"

109. 给两个XML文件，判断两个文件是否是相同内容。XML文件内容是否相同跟节点的先后顺序无关。
Follow-up: 有多个XML文件，把内容相同的归在同一类。

110. 给一段文字，如果把文字印在一张A4纸上，求印出来的文字高度是多少。
Follow-up: 现在A4上有一个1行2列的表格，列宽可自由调整。给两段文字分别放在第一列和第二列，
请问如何调整列宽让总体的高度最小。总体的高度即是两段文字高度的较大者。

111. 给定两个字符串source和target，你可以无限复制source。请问target是否可以成为复制的source的子序列（注意：不是子字符串）？
Follow-up: 如果上一个问题是肯定的，求最小的复制次数。

112. 假设已经有一个API可以给你调用。这个API的作用是读取一个文件中第i个区块（假设一个区块是5Mb）的内容，返回值是实际读取了多少字节。
API示例： int read(string fileName, int chunkNo, int[] buffer)

要求实现一个FileReader类型，需要支持下列操作：
读取一个文件的全部内容
读取一个文件中的前n个字节内容
Follow up: 如果现在文件特别大，要怎样做才可以加快文件的读取速度？

113. 有一堆task需要在VM上run, 每个task有相应的资源需求（memory, CPU），问最多需要多少memory和CPU (类似LC meeting room)。
扫描线写完之后又让用heap/pq写一遍
每个task有个project id。返回最烧钱的project。给定了基于CPU, memory的价格。每个task有自己的start/end timestamps

114. 2^N个选手实力排名1到2^N，一个good draw是说实力最强对最弱，次强对次弱以此类推; 并且需要满足每一轮都是good draw。 
比如如果只有8个选手，[1, 8, 4, 5, 3, 6, 2, 7]是good draw。[1, 8, 4, 5, 3, 6, 2, 7] -> [1, 4, 3, 2] -> [1, 2] -> [1] 写程序1）
给定N，输出any good draw 2）给定N，一共多少种good draw
https://github.com/jamesben6688/coding/blob/main/recursive/good_draw.py

115. Given a set of cards to play, input as a collection of cards with rank and suit to play
The play of the card is valid when meeting the following 2 options
1. 3 or more consectuive rank regardless of the suit, to be noted rotated rank doesn't count 
e.g."QC", "KD", "AC" is not consectuive
2.3 or more same ranks with the same suit
Any play less than 2 cars is invalid
Example
"2D","4H", "6S", "3C" --> valid
"3D", "3C","3H", "6S" --> invalid
"3D", "4D", "7S", "6C", "10D", "9S" --> invalid
"3D", "3D", "4S", "9D","9D" --> Invalid
"3D", "3D", "9D", "4S", "9D","9D" --> valid

116. 实现字符串转换，例子如下：
A3B2 -> (A,3), (B,2)
(A3B2)2 -> (A,6), (B,4)
A2(A3B2)2 -> (A,8), (B,4)

117. 写一个删除文件或directory的功能，如果是删除directory，下面的文件和directory都要一个个删除，
也有可能会有很多删除的request，所以可能有大量的删除工作，怎么最大化利用电脑的资源（thread），并且不会block other work。

118. 给一个数据流，找到里面的loose median。
loose median的定义应该是 2^a <= number <= 2^(a+1)
返回区间中的一个即可 如果median是5那返回[4, 8]之间任意一个都行
https://github.com/jamesben6688/coding/blob/main/heap/loose_median.py

119. 最大的10个files in a filesystem. 标准的heap题目，用了两种解法遍历 filesystem，讨论了各种复杂度，performance。
https://github.com/jamesben6688/coding/blob/main/heap/%E6%9C%80%E5%A4%A7%E7%9A%8410%E4%B8%AA%E6%96%87%E4%BB%B6.py

120. 给定一些字符串
abbaaaa
hello
hola
ho
输入相同长度的前缀和后缀，求符合前缀后缀的单词数。

121. You are given a map with 2 colors of lands - red and blue. The map looks like below where R represents a land of red, 
B represents a land of blue and . represents the sea.
We want to build a bridge between blue and red lands at minimum cost. The cost of a bridge is proportional to its length.
Write a function to return the shortest distance between the two lands.
Please note that the bridge must be connected in 4-directions; up, right, down and left.
Example 1:
[input]
.RR...
R....B
R....B
RR....
[output]
3
Example 2:
[input]
.RB...
R....B
..B...
R.....
[output]
0
https://github.com/jamesben6688/coding/blob/main/bfs/%E6%9C%80%E7%9F%AD%E7%9A%84%E6%A1%A5.py

122. 给两个list, l1, l2。 返回两个list，第一个list是l1里的有但l2里没有的元素，第二个list是l2有但是l1没有的元素。
（元素可以是数字，也可以是string）
Followup是如果l1和l2只有一个元素不一样，该怎么找

123. 假设有一个function可以返回给定start,end time内的所有vote信息, getVotes(start, end) (这个不需要实现)，
每一条vote信息是一个（image_id, vote_time, user_id)的tuple, 实现一个function来return 
当前时间之前24h内最高vote的image_id以及它成为最高的vote image的时间
Example:
QueryResult: [(A, 00:00, u1), (A, 00:01, u2), (B, 00:03. u3)]
Output: (A, 00:00)
QueryResult: [(A, 00:00, u1), (A, 00:01, u2), (B, 00:03, u3), (C, 01:02, u1), (C, 02:04, u3), (C, 05:20, u4), (C, 10:01, u10)]
Output: (C, 05:20)

124. 定义一个一个list的K-window 表示为前K个元素的distinct element set。给两个list, l1, l2和k, 
从l2中移除最少的元素使得l2的k-window中不包括l1的k-window中的元素，返回移除元素后的l2是什么？
Example:
l1 = [1,2,3,4,5,6], l2 = [3,1,1,2,4,1], k = 2
Output [3,4,1]
Followup是如果给一堆list，l1, l2, ..., ln, k 和 m, m是指当前list，li的k-window不能包含它之前的m个list的k-window中的元素，

125. 解optimization推导, linear regression的问题及如何改进，normalization，神经网络某一层gradients数学推导，
以及推导optimal weights。如何做optimization。

126. overfit, dropout；贝叶斯：给定一些samples，
求概率。然后问design question：同时给一些病人图片和相关metadata，怎么做分类

127. 有两种人 一种是想合住 一种是不想合住
有不同房间数量的房子
怎么安排住宿？

128. 给一个数组。 需要提供3个功能
1. set 数组中一个index 的value
2. take snapshot。
3. 提取那个snapshot 时候的某一index 的value
要求节省空间。
https://github.com/jamesben6688/coding/blob/main/hash/%E5%BF%AB%E7%85%A7%E6%95%B0%E7%BB%84.py

129. prefix sum有关的 记不清楚了。 就是给一个0-1 array 然后一个range, return 里面1的个数 很简单

130. 给两个矩阵， 1 是石头0 是水。判断你能否从第一行走到最后一行（可以4各方向上下左右走）
例子:
[[0, 1, 0, 1, 1],
[0, 1, 1, 0, 1],
[0, 0, 1, 1, 0],
[0, 0, 0, 1, 1]] True

[[0, 1, 0, 1, 1],
[0, 1, 1, 0, 1],
[0, 0, 0, 1, 0],
[0, 0, 0, 1, 1]] False
Follow up:
- 具体怎么走？
- 多少走法.
https://github.com/jamesben6688/coding/blob/main/dfs/%E7%9F%A9%E9%98%B5%E4%BB%8E%E7%AC%AC%E4%B8%80%E8%A1%8C%E8%B5%B0%E5%88%B0%E6%9C%80%E5%90%8E%E4%B8%80%E8%A1%8C.py

131. Given a list of strings and a character budget N, use at most N characters to make substrings from the list of strings 
such that as many characters are used as possible AND the absolute difference between the length of any two substrings 
is minimized.
Eg strings = ["Embarcadero", "Ember", "SFO", "Montgomery"], N = 7
return ["Em", "Em", "SF", "M"]
A wrong answer is ["Emb", "E", "S", "Mo"] because abs(len("Emb") - len("E")) is 2, which is more than 1 as above.
https://github.com/jamesben6688/coding/blob/main/str/%E5%AD%97%E7%AC%A6%E4%B8%B2%E9%95%BF%E5%BA%A6%E5%9D%87%E8%A1%A1.py

132. A circle is define by x-axis position, y-axis position, and a radius. 
A circle group is a collection of circles that overlap. Given a list of circles, figure out if they belong to 
a single circle group. Formula for calculating distance between two points: sqrt((x2-x1)^2 + (y2-y1)^2)

133. 给一串数组 找到任意一个重复出现的数字 数字的范围是[1 - N], array的size是 N + 1,
eg: [1, 2, 3, 3, 2] , N = 4 return 2 或者3都可以 写了hashmap, two pointer, binary search 3种做法

134. 给一个period和oncall schedule 返回在period oncall的engineer name list
[Alex, 1, 9] [Ben, 2, 5], [Jeff, 15, 17]
period = [1, 10]
return [Alex, Ben]

follow up: 还是给一个schedule list 返回 所有interval的 oncall的 name list
[Alex, 1, 9] [Ben, 2, 5], [Jeff, 15, 17]
1 - 2 -> Alex
2 - 5 -> Alex, Ben
5 - 9 -> Alex
15 - 17 -> Jeff

135. 一堆人出去旅行，每个人都有付钱买东西，有人付的多，有人付的少给了两个class
class Person{
	int id
	double payment
}
class Transfer{
	int fromId;
	int toId;
	double payment
}
写一个function 可以split everything evenly between people and settle the balance.
Eg: input [person1,10],[person2, 12] outPut[person 1, person 2, 1];
https://github.com/jamesben6688/coding/blob/main/greedy/%E6%97%85%E6%B8%B8%E8%B4%B9%E7%94%A8%E5%B9%B3%E6%91%8A.py

136. 给定一个长度为n的binary array， 求the number of subarrays containing all 1s.
 给定一个n*n的binary matrix，求the number of submatrices containing all 1s.
 
137. 一片房子有三个社区，{{8, 2, 7}, {3, 1, 5}, {4, 8, 9}} 排序所有的社区 并且每个社区不能有同样的门牌号（每个数字代表一个门牌号）

138. 排序以下table:
name start end
abc 3 8
bcd 7 10
cde 3 6
output:
3 - 6 abc, cde
6 - 7 bcd
7 - 8 bcd, cde
8 - 10 bcd

139. 给一个 log file[('John', 1), ('Mary' ,3), ('John', 8), ('joe' 7)]
名字后面是每条消息的word count, 请找出word count最多的前N个user
parse log 这个helper是已提供的
follow up: 是把这个helper function写完。

140. 给一个N面的骰子 一个小人 一段无限长的一维坐标 给一段范围[a,b] 小人从0点出发 根据骰子走x步 骰子可以掷无数次 
小人走到[a, b]这个范围内包括a和b就算获胜
求小人获胜的概率

141. 给一个 string，返回第一个不重复的字母。 "abcrabc". --> 'r'

141. in-order traverse tree:检查给定的一个数字序列是否是in-order traversal sequence的subsequence.
 follow-up 1:怎么修改这个tree可以让给定序列成为subsequence.
 follow-up 2:怎样最小化改动的步骤(overwrite existing node value or insert node都记为1).
 
142. 给N个会议室安排会议,每个会议有开始时间和时长,选取最早空闲的会议室安排,有同样早空闲的会议室选index最小的,
 会议可以延后(在所有房间都被占时)但时长不能变,求问最后哪间会议室安排了最多的会议.
 
143. Wordle game, 5-letter密码,用户输入猜测,对每一个位置都判断是否对上了密码(标绿,'G'),
 还是没对上但这个用户的字符在别的位置有(标黄,'Y'),还是这个字符压根没在密码中出现(标红,'R').
 实现一个函数来校验密码和用户输入并返回5-letter结果.
 
144. 给定一个二维点列表，如果任何两个点的距离（直线）<= k，则将它们组合在一起。例如。 
[P1,P2,P3]，P1 到 P2 <=k，P2 到 p3<=k，p1 到 p3>k。他们仍然在同一组中。 （距离关系是可链接的）请问你能找到多少组？
follow up讨论了一下优化

145. get permutation based on range list.
e.g: [[2, 3], [3, 5]]
return ['23', '24', '25', '33', '34', '35']
follow up是会不会有repeated number，不会有

146. 给一个chat log file[('John', 1), ('Mary' ,3), ('John', 8), ('joe' 7)], 
名字后面是每条消息的word count, 请找出word count最多的前N个user
Heap

147. 给个m x n matrix， 0 可以走 1是wall, 要求robot从左上走到右下，问在最多可以打破一面墙前提下能否走到终点。

148. 有三个array：source，destination，operations。ops array里面存的是 [['COPY', i, j], ['COPY', i, j], ['WRITE', x, i], ...] 这样子
如果遇见COPY指令，就将 source[ i ] 复制到 destination[ j ] 里
如果遇见WRITE，就将x这个数值复制到 destination[ i ] 里
follow up是，假如source和destination是同一个数组该怎么办？[['COPY', 1, 2], ['COPY', 2, 1]] 
需要达到的是同一个数组里俩数值swap的效果
时间空间复杂度，然后继续优化

149. 自己写一个class define一个Item，每个item带一个编号和一个重量，input是两个lists of this items，output输出一个list of this items，
要求按重量从小到大排，遇到编号一致的把重量相加合并成一个。

150. 一个v shape的Int array，类似【4，4，4，3，2，1， 1，2，2，3】这种，数值先下坡再上坡，有重复数字可能，找出最小的值返回。

151. 给你个String Array，比如【“AC” “2B”, “3D”, “4F”...“10B”“11A”】，概念是扑克牌的感觉，判断他是否是个valid的卡组。
条件首先至少要3张，然后要么是同数字的卡牌可以不用管后面字母，比如【“2C”,"2E","2G“】符合。或者是数字是consecutive的并且字母要一样
比如【"10A","9A""11A"】（乱序也算consecutive）符合。
follow up question是还是给你String Array，
比如【"1A",“2C”,"2E","2G“,“3G","4G","5B"】返回所有可能组成valid卡牌的List，比如{【“2C”,"2E","2G“】，【"2G","3G""4G"】}。

152. 写一个user（friends） class 这个class里面完成三个func。
判断你跟另一个user是不是直接或者间接的朋友
返回top k priority

153. GOOGLE CEO 要给全体员工发邮件邀请 用什么data structure？- 
TreeNode 然后让我自己define TreeNode - Narry Tree 怎么get total count？DFS/BFS - 
写了 DFS 问了两种 search 区别 Big O

154. 任意相同character都是group在一起的， 例如： “AAAABCCCCDEEEFFG” 非法的就是“ABBA”；
同时定义一种对于character的label叫“contained”，问：given partition number let us say N. 
那么分割一个grouped string into N parts. (没整除没关系， 最后分割的string可以是余数 “AABC” N：
3， 那么就是 “A” “A” “BC” )求分割后的每个partition里的character是不是“contained”？ 
（contained 定义 当前char有且只在本partition出现）拿“AABC” partition number=3 
举例， 答案return false， 因为 char：A 出现在两个partition group

155. Find the longest beginning substring of target without any characters in reject string.
https://github.com/jamesben6688/coding/blob/main/str/%E4%B8%8D%E5%8C%85%E5%90%ABreject%E7%9A%84%E6%9C%80%E9%95%BF%E5%AD%90%E4%B8%B2.py

156. Create a function to return a function that can only function once, if called multiple times, 
the latter times will only return the value of the first return.

157. 员工salary tree，find all underpaid managers。 Underpaid manager的定义：薪资低于子树中所有节点的平均值。
A[100]
-B[200]
-C[100]
-D[60]
-E[400]
Follow up: Compensation to underpaid; median instead of mean.

158. non-decreasing contiguous array那道题，
followup: 你可以改变其中一个数字 比如原本[1,0,0,0,0,3,4] 你可以改掉0变成1 
然后找到最长contiguous non decreasing array


159. 有一个list，
[( 'John',5), ('Mary',4), ('Sherry',10), ('John',3),('Mary',3),...........]
这个list里有重复的人名，每个人名对应是他们短信里的字数。 给你这样一个list和特定数字N，要求你返回前N个最活跃的用户量。

160. a+b+c 只有+/-，有很多valid的括号 a+(b-(c+d-(f+e))) => a+b-c-d+f+e
a → maximum nested ()
a+(b+(c+d+e)) O(N^2)

161. 拿金币，最多能拿多少？
001010
001010
000000
000000
only when the row of col has more than 1 coin, than you can take one
O(MN)
Union Find

171. input:
		10 example input
		11 low water level
		12 error: low battery
		13 example input
		14 low water level
		25 information received
		30 information received
	output:
		10 example input
		11 low water level
		12 error: low battery
		25 information received

172. 假设你知道每个点之间的距离
cities -> [city1, city2, city3....citym]
destination cities -> [d1, d2, d3.....dn]
time也可以当作是时间 -> [t1, t2, t3......]
n<=m
返回一个城市可以到别的城市的最短时间

173. 两个input，一个list的地址作为字典（比如 “31, abc, Los Angeles, CA”，“32, abc, Los Angeles, CA”），
一个list的地址作为原文件（比如 “31, abc, Los Angeles, CA”）。返回list是原文件存在字典中的地址（map解决）。
followup就是如果null算个百搭

174. 找一个string里第一个non-alphabetical order的char的index(遇见非字母的字符直接跳过，不分大小写)
followup: 找一共有几个这样的char （讨论了两分钟，觉得题目意思不明确，move on to the next followup）
followup2: 求最少移除几个char后是字符串变为aplhabatical (最基础的dp问题，为了简单，假设都是小写字母) 最长递增子序列

175. 给出 item - date - price的文本，输出top n 贵的物品
比如 cloth - 03/09 - $19.9

176. 第一个函数是找到字符串中前缀匹配到元素，然后返回true or false；
第二个函数就是基于前一个子函数的基础之上去排除掉不符合条件的字符串子串。

177. 给你很多圆的x,y, r坐标（对应圆在坐标轴上的位置和半径），让你先完成一个connected函数的判断，
然后是判断一大群圆他们是否全部连接。

178. give you some buckets , you know the capacity of each bucket, return if you can use the buckets 
to get target gallon of water.assume you have infinity buckets of each size.
for example , target is 11, buckets [7, 4],true (7 + 4)
target 8, buckets[7, 5]. return true, 7-5 = 2 do 4 rounds. follow up, how to make the operate times minum.
https://github.com/jamesben6688/coding/blob/main/bfs/%E6%B0%B4%E6%A1%B6%E5%80%92%E6%B0%B4.py

179. if you have an array of submarine A,
and K person, try to find a way to accomodate people into submarines make the the person who 
have the least unit of air maxmium
for example,
A = [10, 6, 4, 3, 2], k = 4
P = [2, 1, 1, 0, 0]
第一个潜水艇每人占5unit， 第二个潜水艇每人占6unit，第三个占4unit，
这样最少人占4个unit空气。
https://github.com/jamesben6688/coding/blob/main/binary_search/%E6%BD%9C%E6%B0%B4%E8%89%87%E7%A9%BA%E6%B0%94%E5%88%86%E9%85%8D%E9%97%AE%E9%A2%98.py

180. you have a organization tree, if a manager's salary is lower than the avarage of it's reports 
( direct reports and indirect reports), then it's underpaid
find out the count of underpaid manager

follow up: if pay extra money to make all underpaid manager not underpaied, what's the minum money will spend.
for example:
A(100)
- B(200)
	- C(100)
	- D(60)
then A is underpaid : B + C + D / 3 = (200 + 100 + 60)/3 = 120 > 100
B is not underpaied since no reports

181. 1. ApkVersions是一个三元组的list，ApkVersions[i] = (ApkVer, minOSVersion, maxOSVersion)，
描述了当前的Apk Version, 以及它支持的OS的最低和最高version
2. OSVersions是一个单纯的数组，OSVersions[j] 描述一个OS version
输出是为每一个OSVersions中的元素OSVersions[j]，找到最新(最大)的ApkVer满足 minOSVerion <= OSVersion[i] <= maxOSversion.
Solution是，先过一遍ApkVersions，合并可以合并的range，保持这个range中最大的ApkVer，然后按照range排序。
接着为每一个OSversions[j], 用binary search找到满足条件的range，取出对应的ApkVer.
https://github.com/jamesben6688/coding/blob/main/binary_search/%E6%B1%82%E6%94%AF%E6%8C%81%E7%9A%84%E6%9C%80%E5%A4%A7apk%E7%89%88%E6%9C%AC.py

182. 给你一组括号，比如 "( ("，然后你可以add delete或者replace三种操作，然后用最少的操作得到一个平衡的括号string，输入是一个string，
输出是一个list of string。前面这个例子显然是replace一次最优，输出 "( )"。
再举个例子："( ( ) ( )"，这个输出是 "( ) ( ) ( )", "( ( ) ( ) )", "( ) ( )"。
https://github.com/jamesben6688/coding/blob/main/dfs/%E6%9C%80%E5%B0%91%E7%9A%84%E6%AC%A1%E6%95%B0%E7%94%9F%E6%88%90%E6%8B%AC%E5%8F%B7.py

183. 给你一个function，call这个function会返回两个节点的 排序如 a -> b，b -> c。
但是这个function不保证每次返回都是unique的，就是可能返复call 5次，返回的都是 a -> b。
给你总共character的个数n，要求输出character之间的顺序。
https://github.com/jamesben6688/coding/blob/main/topo_sort/%E5%87%BD%E6%95%B0%E8%B0%83%E7%94%A8%E7%A1%AE%E5%AE%9A%E5%AD%97%E7%AC%A6%E9%A1%BA%E5%BA%8F.py

184. 2034  write 99.99%, read只有0.01%的解法 和read 99.99%, write只有0.01%的解法

185. 给 x [1, 2) 上，y在[2,5), z 在[1, 4), 让输出各个区间上的character，如[1,2) -> [x, z], [2, 4) -> [y, z), [4,5) -> [y]

186. 题目是给一个 binary tree, 问最下边那个level的width。第一个1之前的null不算，最后一个1之后的null也不算。例如
      1
    1    1
     1 1  1
答案就是 3
      1
    1    1
      1   1
答案也是3

187. 一堆路由器问你一个路由器发出的message能不能被第二个路由器收到
如果转发完一个message，
这个路由器就会被shut down怎么搞
follow up是如果路由器太多了，内存装不下怎么搞
https://github.com/jamesben6688/coding/blob/main/bfs/%E8%B7%AF%E7%94%B1%E5%99%A8.py

188. 给你一棵树的root，问你这棵树的同一层有没有相同value的节点

189. 两台用很慢的网络连接的电脑上面有两个文件，怎么样用最短的时间判断出这两个文件有哪些位不一样。
最短的时间不是big o notation，而是要你自己估算disk的速度和网络的速度，然后算多少秒

190.  给出一定规律 写出第N个5位数车牌号，follow up是 车牌有k位

191. 一个奇怪的sorting算法 要挂就是这一轮 sorting需要交换swap数字 要求是数字不能向左移动超过2位，求最优的sorting结果 
https://github.com/jamesben6688/coding/blob/main/sort/%E9%99%90%E5%88%B6%E4%BA%A4%E6%8D%A2%E6%AC%A1%E6%95%B0%E7%9A%84%E6%8E%92%E5%BA%8F.py

192. 给一个list of cards with rank & suit, 找出最大的5张牌顺子（straight flush）

193. 相似字符串。改成任意String 输入

194. 给一个二维黑白图，0，1表示，用Array存储，要求写一个function对图像进行flip，就是左右对换。follow up如果是分布式系统该怎么改进

195. 给一个二维黑白图，0，1表示，用四叉树存储，如何进行压缩？用树存储的话一定比二维数组更优么？
什么情况下用树存储更优化？写一个function，给定树中的一个node，求该node以下黑色pixel的比例。
follow up 写一个function随机返回图中一个黑色的pixel，既x，y，必须完全随机
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/%E7%BF%BB%E8%BD%AC%E5%9B%BE%E5%83%8F.py

196. 用一个Array表示一个树，已知子节点肯定比父节点的index大，每个节点的值是父节点的index，比如
  0
1 2
表示方式是【-1， 0， 0】
写一个function，给定target node，删除target node
Follow up，写一个function删除给定节点的sub tree

197. 你有n个server和m个task，每个task用startTime和endTime表示，每个server每次只能处理一个task，先到先得，
如果没有availble server，就pending直到有一个server available，求哪个server 处理的任务最多

198. 给一个2D matrix，每个元素都是int。可以从矩阵任何一个元素出发进行游走，游走规则：
（1）可以去所在row中strictly比它大的元素
（2）可以去所在col中strictly比它大的元素
如果没有符合游走规则的选项，视为path终止；path中遍历到的所有元素的int的和，视为pathSum
要求从所有path中选择pathSum最大的path，将其pathSum返回
follow up： 不单单是返回pathSum，同时也要返回path是什么
https://github.com/jamesben6688/coding/blob/main/dfs/%E6%9C%80%E9%95%BF%E8%B7%AF%E5%BE%84.py

199. 不同android apk 有最低支持SDK版本，最高支持SDK版本
   Min SDK version    Max SDK version
APK 1:   4            -
APK 2:   7            10
APK 3:   -            16
APK .....
(- 代表没有上下限）
Input: (4, max), (7, 10), (min, 16)           -> 所有APK所支持版本的区间
Output: (min, 3], (3, 7), [7, 11), [11, 17), [17, max)  -> 所有SDK 区间，要求相邻区间被支持的APK 不能完全一样
Clarification:
(min, 3) -> APK 3   // 问：为什么第一个区间不能用(min, 4] 。 答：(min, 4] 和 相邻的 (4, 7) 被支持的APK 完全一样
[3, 7) -> APK 1, 3 // 问: (min, 3) 和 [3, 7) 能合并吗。 答：不能
[7, 11)  -> APK 1, 2, 3
[11, 17) -> APK 1, 3
[17, max) -> APK 1

200. Given a alphabetic string, 判断它能否用元素周期表里的元素表示，如PrAcTiCe。Ignore cases。return true or false.
由于元素符号只能是一位或两位字母，可以DP。递推式:
DP(i) = (DP(i - 1) and word in chemElements) or (DP(i - 2) and word[i - 1: i + 1] in chemElements)
https://github.com/jamesben6688/coding/blob/main/dp/%E5%85%83%E7%B4%A0%E5%91%A8%E6%9C%9F%E8%A1%A8%E5%87%AD%E5%80%9F%E5%AD%97%E7%AC%A6%E4%B8%B2.py

201. 给一个矩阵，其中0代表空地，1代表墙。又给一个起点一个终点坐标，要把球踢从起点踢到终点，每一次踢球的方向可以是上下左右，
踢一次以后球会一直运动到碰墙或者边界。球只要滚过终点就算结束。
return shortest sequence of ball movement(like [right, down, right, up])

202. Given list of N nodes, node object has (id, value, label). return K largest node by value, which satisfy 
that no more than M nodes having the same label.
https://github.com/jamesben6688/coding/blob/main/topk/%E6%89%BE%E7%AC%ACk%E5%A4%A7%E7%9A%84node.py

203. 假设你去一个镇上做survey，需要收集一个街区的每户人家的名字。你有一个本子，里面写上一些instruction，
然后把本子传给第一户人家。每户人家会按照你写的instruction来完成一系列动作，最终把本子返回到你手上。问，
本上应该写什么instruction。

204. 给一个data steam，和一个d，返回stream里面出现过的triplet，这个triplet里的每两个数的差值都小于d。
比如[1, 2, 5, 10], d=4, 返回(1, 2, 5)

205. 给你一堆大小比较表达式，判断是否合法。
类似于 图里找环， DFS
输入是类似 “a > b”“b > c” "c > a"， 输出false
follow up是表达式里会加入数字，比如“a > b”“b > 2” "a < 2"

206. 给一个无限的board，board上有一些点，输入是这些点的坐标，输出是离这些点最近的空格子的坐标。

207. 输入是一些时间点和每个时间点的hit count，求哪30min的range count最高。
比如 [0, 1][1, 2][30, 3][60, 70]
那么就是 30- 60这个时间段hit count最多，有73个

208. merge interval,

void insert(int[] range)  --> 每次insert了要处理一下merge，我这里脑残了选了个list自己写了个comparator，
然后写之前还说treeset跟list都行
boolean getValue(int i) ---> 看这个数字是不是在range里 比如已有range [1,5] [7,9]getValue(4) return true
follow up:
1. 如果数据超级大是个数据流之类的你怎么办？答可以分成几个bucket 分别按bucket的range处理 这样sort的时候不会太痛苦，
最后合并一下比如mapreduce一下。。
如果只在乎1-1000的数字怎么办？能不能更快的处理getValue 答直接用int[1000] 然后在每个index++

209. 输入： [2,3,5]target = 25
你可以往数字里添加 + - × ÷（ ）
输出：运算式
比如上面 要求输出一个String (2+3) × 5

210. 找下一个permutation的变体
要加小数点
原规律大家肯定都知道，然后加点我这么处理的，比如432.1的下一个是1234 
就是当排序在最后一个的时候，小数点才向右移动。然后如果是4321. 下一个就把点向左移动 .1234
followup。。问我String x = "a"然后String x = x+x 是怎么work的。。。可能因为我code里写到了这些
str不可变。每次会创建新的str, 所以id会变
然后问了如果有相同数字，怎么break code 之类的

211. 一个tree里，一个节点如果不是leaf node也不是有两个child的节点就算chain node，
从上到下这样的节点串起来不中断就是一个chain，数最长的chain
https://github.com/jamesben6688/coding/blob/main/tree/tree_chain.py


212. A Beautiful value means that the maximum streak of the specific item in the array.
Input:
1. an array with items.
2. target item
Output:
return the maximum streak
Follow up:
an array of targets items, please find its respective maximum streak.
https://github.com/jamesben6688/coding/blob/main/hash/%E6%9C%80%E9%95%BF%E8%BF%9E%E7%BB%AD.py

213. Text justification，但是只要置左

214. Given a positive integer,
divided by two if the number is even.
if not even, increment one.
what is minimum stpes to reduce to one.

215. 818 输入是sequence of instructions，输出是target

216. 查找列表里的字母是不是按字母表排序

217. 62. 从左下角到右下角有几条路可以走到，只能左，左上，或者下左

218. 关于python generator的问题。如何随机返回一个数字，概率一定要unformly distributed。
暴力解法，把generator转list, 
follow up: 如何优化

219. 给一个array a[], 称满足a[i] - a[j] = i - j的（i，j）为一个good pair, 找出一共有多少对good pair：
需要clarify的问题有： 1.(i, j) 和(j, i )是否算两对2. 是否考虑 i =j的情况
https://github.com/jamesben6688/coding/blob/main/hash/%E6%95%B0%E7%BB%84pair%E5%B7%AE%E7%AD%89%E4%BA%8Eindex%E5%B7%AE.py

220. 一个迷宫从左上角走到右下角有几种路径 （只有下或者右两个方向）
一个小tricky是迷宫中有一些障碍

221. 值更新, 给一个数, 返回最小的idx 比如[idx, num]
[1, 10],[2, 10], [1, 20]
现在问num = 10, 返回2, 因为idx 1 被20用掉了, 

222. 彼此相识的最早时间
Follow up感觉答得比较差，也确实比较难。问的是除了Union 加好友之外，又多了一个Unfriend动作，
撤销好友关系，那么最早时间所有人都成为朋友会如何变。
https://github.com/jamesben6688/coding/blob/main/union_find/%E5%8F%AF%E6%92%A4%E9%94%80%E7%9A%84%E5%B9%B6%E6%9F%A5%E9%9B%86.py

223. 怎么判断回文Valid. 找到数列第K大的数，quick select写了五分钟写完了。然后他又说能不能写个iterative的方法，我只要找到第二大的数。

224. 568. 要求print 每周去哪个城市的itinary list，而不是最长假期日

225. 207的变式 最后我记得是需要求最短的学期数

226. 46的原题
follow up要求优化这个算法
如果有duplication需要怎么处

227. 一个nested list，里面包了很多个children，每一个children是一个区间，然后要在这里面找所有children区间不重叠的部分，
https://github.com/jamesben6688/coding/blob/main/swipe_line/%E4%B8%8D%E9%87%8D%E5%8F%A0%E7%9A%84%E5%8C%BA%E9%97%B4.py

228. 经典top K frequent, bucket sort

229. 366，但是这个树所有的节点都没有child指针，只有parent指针，然后给你一个deleted node，
让你在这个树上找deleted node，然后delete subtree，要求空间必须是O1的，

230. 简化表达式。 例如 a + (b - (c -d)) -> a + b - d + d
解法应该就是stack，然后只保留开括号之前的符号， 比括号就pop出符号，字母就直接加到答案。

231. 一个教室里的学生传纸条，从第一排开始 横向传，被抓住的几率是 90%，纵向传被抓住的几率是50%，每往后一排被抓住的几率要减少一半，
横向纵向都减少。最后要计算的是从学生A 到B，被抓的最小几率是多少。
https://github.com/jamesben6688/coding/blob/main/dijstra/%E6%95%99%E5%AE%A4%E4%BC%A0%E7%BA%B8%E6%9D%A1.py

232. 一块圆形石头，已知半径，天上下雨，假设雨点也是圆形的，已知半径，求问要下多少雨点才能覆盖整个石头表面， 其中雨点是不均匀的下的。
雨点不均匀的下，可能一千滴都落在同一地点。

233. 921 返回值改成 生成的新valid string

234. input是一个 Integer array和一个 Integer K, 求返回 k个non-overlapping subarray，他们的总和最大。
eg：  
[1,2,3,-10, 5, -1, 20] , k = 1: subarray 是[5, -1, 20]，return 24，  DP
[1,2,3,-10, 5, -1, 20]k = 2: subarrays是 [1,2,3], [5, -1, 20]，return 30，
[1,2,3,-10, 5, -1, 20] k = 3: subarrays是 [1,2,3], [5], [20], return 31

235. api rate limiter，区别是滑动窗口时间里，被call次数不能超过10次
一个runnable interface，里面有run方法，
一个 service implement runnable，
要实现 RateLimit class，和一个apply方法，要求apply被call到的时候检查规定时间内超过1次/10次，超过了报错，没超过call runnable

236. 给一条带子，里面有n个segment涂成红色，另外给一个长度是L的蓝色带子，问放上蓝色带子之后剩余红色部分最少是多少。
segment之间没有重复，sorted input, index可以是负数
example [[0,2], [4,9], [10,12]] L=7

237. 给一个string，需要满足password 条件，条件1:len在6到10之间，条件2:包含字母至少2个，条件3:包含数字至少2个，返回满足条件的所有substring个数

238. 会议室booking system， 输入start time, end time， 返回有没有available spot 就是查overlap

239. 给了一串数组，int[] 要我deduplicate. 
follow up如果是100TB你要咋做。 
用2**32-1个桶。
答案拿十来台台机子做hashset, 另外拿几百台台机子线性处理，hashcode每个数看你要去哪台机子去重

240. 给你调用一个api,得到流数据group单词，return 单词频率
follow up会断开来，eg wo wo ni wo ni ni ta 要返回 wo 2, ni 1, wo 1 ni 2 ta 1
followup: 设置一个 string pre, int frequency =1,每次喊下api, 拿到单词，若是等于pre， frequency++, 如果不等于， list. 
add new Pairs(pre, frequency).pre = thisword, frequency重制成1。

241. train一个list of sentences来预测一个string后面最有可能出现哪个单词。
时间复杂度 如何优化
如果一个单词有1/3可能性出现另外一个2/3可能性出现 如何保证出现概率

242. 单向列表删除奇数index的node。 followup问的如果要删除每k个位置的node怎么办 followup时间复杂度 如何优化

243. 设计一个数据结构保存时间段  比如06/30/2022 - 07/01/2022. 要求可以方便insert和search。
search一个日期是否在已存的时间段里面

244. 在一位坐标上，有pawns，有很多空格，只允许左边 L, 和右边 R 移动。 给予两种input，判断是否能match。比如
s1: R _ _ L 
s2: _ _ _ R L
从s1 能到s2， 因为r可以右移动。
s1: _ L _ _ R
s2: _ _ _ L R
从s1 不能到s2， 因为 l 只能向左。 所以是false。

245. 给一个 array of building height, 要求把 所有building都trim一样的高度，或者把某些夷为平地，
求最少需要remove多少个floor，
题目读了一会才弄懂
比如 input: [1,3,5]， after remove:

prefix_sum[i-1] + prefix_sum[n]-prefix_sum[i]
1. [0,0,0] -> remove 9层floor
2. [1,1,1] -> remove 6层floor
3. [0,3,3] -> remove 3层floor （返回这个3）
4. [0,0,5] -> remove 4层floor
推房子, 推倒房子
https://github.com/jamesben6688/coding/blob/main/prefix_sum/trim%E6%88%BF%E5%AD%90.py


246. 一个教授给学生pass or fail，有两门课 math and bio, 教授要尽可能多地pass 学生，
但是不能让学生complain，a student complains only when students worse than him passed. 
WORSE : math1<math2 and bio1 < bio2, then student 1 is worse than student 2
input : a list of pair of scores
output: for each student, it pass or fail.
https://github.com/jamesben6688/coding/blob/main/sort/%E6%95%99%E6%8E%88%E7%BB%99%E5%AD%A6%E7%94%9F%E6%89%93%E5%88%86.py

247. 去掉树的所有叶子节点，按照删去的顺序返回一个列表
followup: 366, 按照树的高度来收集。叶子节点的高度为0,

248. 几个朋友在校园里约在咖啡馆见面，已知朋友们的位置，咖啡馆和各类建筑的位置，只能通过咖啡馆或其他建筑到达其他位置，
各建筑之间的连接情况已知，
求所有朋友到达其中一个咖啡馆的最短路径，若没有符合要求的咖啡馆，则返回空

249. 求list中第二大的数，不要用heap。 follow-up: 求第k大的数

250. 57. 看能不能预定到房间。改成设计题。
例如：
add(10, 20) 返回对
add(20, 25) 返回对
add(22,24) 返回错
add(1, 5)返回对

251. Input是timestamp + string, 例如 {1, abc}, {3, abc}, {9, efg}, {12, abc}, {24, abc}
第一小问是，如果相同的string在10s内再次出现，那么只放入result list中一次，
即上面的input应该输出 {1, abc}, {9, efg}, {24, abc}。无论如何都更新string的timestamp。
followup: 如果相同的string在10内再次出现，那么要在result list中把之前出现那次也删掉， 即上面的input应该输出 {9, efg}, {24, abc}
timestamp可能duplicate，还有prev为null的情况也应该输出

252. design一个class来实现 insert(int[][] ranges) 和 query(int time)来返回时间是否在之前给的ranges中。
例如：ranges = [[2, 5], [9, 13]], 然后query(2) 返回True, query(6) 返回 False。

253. 给一个csv file，类似：
product_id, product_name, stock_remaining
1, books, 50
2, pencils, 30
需要我Parse这个file，然后自己找一个合适的data structure来output所有的信息
有哪些invalid input可能导致程序出错

254. 监控 RPC 的执行时长给一些log 和 timeout threshold。找出第一次 timeout 的log id。 可以理解为是stream data Input
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/%E5%8E%BB%E6%8E%89timeout%E7%9A%84RPC.py

255. 判断是否是contradiction ，只有 ==， != :例如 a == b, b == c, c != a--> false. a== b, b== c, c == a--> true
followup: operator 加上了 < :a == b, b == a, b < a --> false,a < b, b == c, a < c--> true

a-0->c
a-0->b -1->c
a<-1->b
operator 加上了 <=

256. erge interval， 给定一个区域的左右边界，不断有interval进来，判断什么时候这些interval可以cover整个区域。

257. input: binary tree with InternalNode (with sum of length from children) and 
LeaveNode (contains string and length of string). 一个String被分成了substring存在tree里面
问：return第n个char.
follow up: remove(idx, length) -> 从idx开始删除length个char

258. 给一个directed graph和target，find shortest cycle contains target。 
第一问return length, 用的BFS解，
第二问要求return cycle path，用的DFS with depth，但是因为有overlapped 
cycle所以不能用visited，最后runtime是m^D, 
m是edge count, D是depth。

259. [[0, 3], [1, 4], [5, 6]]
1.1给一些interval，问在某个点有多少interval，比如上面，在2的时候就是2个，
对于边界面试官这时候还不在意。
1.2问如果最多只能有k个interval overlapping，让判断给的intervals满足否返回True or False，
然后这时候如果在边界就不算
[[1,2],[2,3]] 这时候2就是没有overlapping

260. merge 两个list，context和操作略复杂一点，实际就是merge 两个list
 然后follow up是k个list，就扯了扯heap or divide and conquer
 
261. AAAABBBDDDCCCC 一个string，所有相同的字符都在一起的
  然后求最多的一个，先写了个O(N)然后 space complexity O(1)的
  然后问怎么优化，就说binary search
  
262. 求水位低于seaLevel 的数组, 海平面容器
给定一组表示地形高度的正整数(在二维中，比如《超级马里奥》)和一个表示平坦海平面的整数，
返回一个表示每个独特水体体积的整数容器。
input:
int[] arr = {1, 5, 1, 3, 4, 3, 1, 2, 7, 5, 6};
[3, 0, 3, 0, 1, 3, 2, 0, 0, 0]
int seaLevel = 4;
output: [3, 4,6]
如果有高于海平面的跳过，output 是 4-1 =3， 7是后面因为中间没有海平面挡着 
就会将低于海平面的相加。
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/%E6%B5%B7%E5%B9%B3%E9%9D%A2%E5%AE%B9%E5%99%A8.py

263. Count number of words within a list (sorted) with prefix
[a, ac, bb, bbc, c, cc, dd, de] prefix = “bb”
Brute force的方法是Use foor loop and startswith to get the count
Follow up: improve time complexity by using binary search to find the range of words 
(start and end)

264. two D array，有障碍找最短路径 1293

265. 2096 follow up是node是sort的，要用logn方法实现

266. 给两个二维数组，各存一组pair，key是int，value是double，把两个数组merge成一个数组，
相同key的value相加，如果key只在一个数组里则删除该pair。提示，两个数组key都是sorted。
例：input：[[1, 2.5], [2, 2.7], [3, 5.5], [4, 2.3], [5, 2.4]]
[[3, 2.5], [4, 1.7], [5, 9.5], [6, 8.3], [7, 6.4]]
output: [[3,8], [4, 4], [5,11.9]]
Two pointer

267. 有一个蛋糕，上面有一些长方形的奶油块。现在你要切这个蛋糕，
每一刀或平行或竖直（无斜刀）。并且贯穿，从一端到另外一端，也就是每一刀必定把你切的那块蛋糕
变成两块。不可以破坏奶油块。最终要求切出来的每块蛋糕上面都最多有一个奶油块，
求问能否有切法满足要求，如果有valid的切法最少几刀。
https://github.com/jamesben6688/coding/blob/main/divide_conquer/%E5%88%87%E8%9B%8B%E7%B3%95%E5%A5%B6%E6%B2%B9.py

268. 子数组和子序列啊，条件是non-decreasing，长度为一的子数组和子序列也符合条件。
数组：1 2 3 4
符合条件的子数组数量：1+2+3+4 = 10
数组：1 3 2 4
1 3
1 2
1 4
3 4
2 4
1 2 4
1 3 4

dp[i] = 1 + sum(dp[j]), s.t. arr[j] <arr[i]

dp[0]=1
dp[1]=1+dp[1]=2
dp[2]=1+dp[1]=2
dp[3]=1+dp[1]+dp[2]+dp[3]=6
符合条件的子序列数量：1+2+2+6 = 11

269. tree的题，用parent array来表示，node从0—n-1，root一直是0， 
然后给一个toDelete array，true表示要删除。
删除的规则：删除这个node和他的children node。
tree的特性：parent node一定小于children node。
返回 删除后的parent array。
Follow up：不用dfs或者bfs

270. 返回数组中non-decreasing subarrays的数量，time and space compleixty
Follow up：返回non-decreasing subsequence的数量。

271. check if the given 20 cards can be divided into 4 hands (Texas Holdem) 
which are either royal flush or 4 of a kind. Follow up to check if it will work by 
followup: replacing only one card
非常慢: https://github.com/jamesben6688/coding/blob/main/dfs/%E5%BE%B7%E5%B7%9E%E6%89%91%E5%85%8B%E5%90%8C%E8%8A%B1%E9%A1%BA%E6%88%96%E8%80%85%E7%82%B8_%E9%9D%9E%E5%B8%B8%E6%85%A2.py

快速版: https://github.com/jamesben6688/coding/blob/main/dfs/%E5%BE%B7%E5%B7%9E%E6%89%91%E5%85%8B%E5%BF%AB%E9%80%9F%E7%89%88.py
正常版本: https://github.com/jamesben6688/coding/blob/main/dfs/%E5%BE%B7%E5%B7%9E%E6%89%91%E5%85%8B%E6%AD%A3%E5%B8%B8%E7%89%88%E6%9C%AC.py
替换一张: https://github.com/jamesben6688/coding/blob/main/dfs/%E5%BE%B7%E5%B7%9E%E6%89%91%E5%85%8B%E6%9B%BF%E6%8D%A2%E4%B8%80%E5%BC%A0.py

272. given a dictionary of file tree, find entire size of the given file or
 directory(sum of the files in it). Follow up to implement a directory-delete function.
 
273. coding -- [3,4,2,5,1,6,7,9] to find longest sublist strictly increasing by one, 
e.g. [3,4,5,6,7]. Follow up to find longest sublist strictly increasing e.g. 
[3,4,5,6,7,9].
https://github.com/jamesben6688/coding/blob/main/dp/%E6%9C%80%E9%95%BF%E9%80%92%E5%A2%9E%E4%B8%BA1%E7%9A%84%E5%AD%90%E5%BA%8F%E5%88%97.py

274. 一个停车场的车票上记录了车子进入时间和离开时间，记录n时间内，停车场内每个时间点的车的数量
ex:tickets = {[1,3],[2,4]}
n = 5;
output:[0,1,2,2,1]
ps：虽然第一辆车是3点离开的，但是在3点这一时刻还是有两辆车，3-4点到一辆车离开

275. 有一个party，只有被邀请或者是host才能参加，一个人可以邀请一个或多个人，
但每个人只能被邀请一次，我要找出那些人是最开始发出邀请的人（host）。
题目给的input是list of tuple (inviter, invitee)，output得是a list of string (host)。
具体例子如下：
input  Output:
[A,B] [A, F]
[B,C]
[C,D]
[C,E]
[F,G]

建两个
set (inviter, invitee), 扫一遍input并将tuple里的人放入对应的set，最后两个set不一样的
部分放到list里就是output。
followup: 如何得出每个人之间
的common link（e.g. C同时邀请了D和E，所以他们的commmon link就是C）。
common link可以是他们
本身（e.g. A和B的common link就是A）。
找链表的交点

276. 给出一个文件目录，每个文件节点下面可能会有subfolder，每一个文件节点如果有多个
sub节点则应该在该节点有一个icon。给出这样一个目录，要求验证每个这样的节点是否
有这样的icon。

277. multi-language translator
就是设计一个翻译系统，这个翻译系统可以有两个方法
add(String inputLanguage, String inputWord, String outputLanguage, 
String outputWord)
get(String inputLanguage, String inputWord, String outputLanguage)
比如
add: English hello -> Spanish hola
｛1： ｛english: hello, spanish: hola｝｝
{hello: 1}
{hola: 1}
add: Spanish hola -> French Bon jour
｛1： ｛english: hello, French: Bon jour｝｝
{hello: 1}
{Bon jour: 1}
那get(English, hello, French)的时候需要直接输出Bon jour，
总之需要实现已有词汇的间接查询，
间接查询跳转次数不超过1次。

278. 有一个2D array，作为training data, 例如[['I', 'like', 'apple'],
['You', 'like', 'orange'],
['apple', 'orange', 'like']],
求写一个function 来 predict 一个string后边最有可能会出现的下一个string。

279. 两个dictionary，每个dictionary 都是key 然后套一个或多个dictionary
要求找到两个dictionary相同的key 和独立的key（要把所有的dictionary展开到最里
层去比较）
https://github.com/jamesben6688/coding/blob/main/dfs/%E4%B8%A4%E4%B8%AA%E5%B5%8C%E5%A5%97dict%E6%89%BE%E7%9B%B8%E5%90%8C%E7%9A%84key.py


280. 给了一个list的人，
每个人
都有一个相对应的开始和结束工作时间。要求写一个function，output结果是列出所
有可能的时间interval，
并且在每个interval里面写出这个时间段在工作的人。

281. 写一个class，里面要实现两个method去做以下的query set
一个是接收一个tuple的input。该tuple是[startNumber, endNumber]
另一个是传进一个任一整数的参数，return这个整数是否存在set。
也就是根据前面所有input过的range去找是否有在里面。
eg.
input [1,8]
input [10,18]
query 9 -> False
query 2 -> True
query 1 -> True

282. 给你一个relationship list， 以及一个pattern, 以及starting person和
ending person, 需要回答有没有可能output一个符合pattern的person的list
例子：
relationships: [0,1,'F'], [1,2,'E'],[2,3,'E'](是bidirectional的)
pattern: "FEE" (F是friend的意思，E是enemy的意思)
0<-F->1<-E->2<-E->3
starting person:0
ending person:3
expected output: true (因为[0, 1, 2, 3] 符合 "FEE")

283. Jessica wants to get auto insurance. When arriving at the insurance company, there are N agents (number 1 to N) serving nobody, and M people have already arrived with the same demand.
The company follows the rule of first arrived first served, and if more than 2 agents can serve a customer at the same time, the customer will always choose the one with the smallest number.
For agents, each of them has a constant serving time that the ith agent will take T[i] minutes to serve a customer. Assume Jessica arrived at time 0, and all the agents are idle and start to serve the customers.
The question is how many minutes will Jessica needs to wait before meeting with an agent?

284. russian envelope

285. find the best swimmer relay for the 4 x 4 freestyle. 
The swimmers cannot repeat in one single game.
Swimmer {
double free;
double fly;
double back;
double breast;
String name;
}
follow up: what about the mixed relay?

286. given an ArrayList and reference, remove all elements that do not 
match the reference. require the minor data movement.
Example:  array: [apple, banana, foo, string]
  reference: [foo, apple, pineapple] 
 result: [apple, foo]
follow up:keep the order? the realization of ArrayList, 
the difference with LinkedList.

287. given a number N, output all sequences of '1's and '2's in which 
the sum is N. Require recursion solver.

288. given a list of IP ranges and cities, manage a query of a set of 
IP addresses, and output the list of cities in which the query IP locate. (IP ranges are not overlapping)
Example： 1.0.1.0  1.0.1.10
NYC 1.0.1.20 1.0.1.30  LA
 query: ["1.0.1.3", "1.0.1.30"]  -> ["NYC", "LA"]
 
289. given a 2D matrix of '0' and '1', '0' represents the water while '1' 
represents the land. find the size of the largest island.
follow up: if the lake also counts as the island area?

290. given an array of words, find the longest word that maintains the 
following condition: remove one character in the word, and the 
remaining part can still be found in the array, until down to 
the single character word.
Example: ["a", "at", "sin", "si", "s", "eat"]
 ->eat  
 Since the longest word chain is "a" -> "at" -> "eat"
 
291. 329 改了一下说是下一个格子可以同行同列任意一个

292. 猜密码 每次给一个三个字母的snippet 是密码的subsequence 
然后给一串snippet 问能不能确定密码是什么 并输出密码 拓扑排序

293. given N number of nodes, what's the maximum amount of edges you can 
add and make sure of no cycles.
如果是有向图?
followup: 判断两个图一样
判断两个图是否一样: https://github.com/jamesben6688/coding/blob/main/graph/%E5%88%A4%E6%96%AD%E5%9B%BE%E4%BC%9A%E5%90%A6%E4%B8%80%E6%A0%B7.py
图同构问题: https://github.com/jamesben6688/coding/blob/main/graph/%E5%9B%BE%E5%90%8C%E6%9E%84%E9%97%AE%E9%A2%98.py

294. 有K 种不同的宝石， 每个无限多， 把这些宝石放在一个 M*N 的格板上， 要求不能有三个连续的格子是一样的宝石。 写一个函数随机生成一种放置方式。

295. 你有10+T 的数据， 你有1T 的磁盘和8个cpu 的资源。 怎么取出最热门的100 条数据。

296. graph. 给一些街道(edges), 
自己建graph. 建好后写个func判断能不能从一条街道到另一个vertex而不经过任何
的intersection. Intersection就是有多于两条边的vertex. 
Follow up是计算路程长度

297. fill color, 填充图形. 给一个matrix, 起始坐标, 
和new color. 把起始坐标以及相连的same color的cells填充new color. 像画
图工具里的填充图形.
Follow-up: the current function is just 
handling a chunk of a very big image that doesn’t fit into the memory.
 There is another function to get another chunk. Design the higher 
 level that handles filling color across multiple chunks. Follow up
 上升了一个维度, 当前fill color的可能只是一个巨大的image中的一部分, 
 所以fill到边界的时候有可能有bleeding, 就是相邻的另一部分可能有和当前正
 在fill的形状相连的.
 
298. 给一个sorted array, 删除重复的元素in place, 并且删除后的空位要
挪到array后面.

299.  Given an unsorted array of integers and a target integer A,
 return the indexes of all A in the array as if the array is sorted. 
 Follow-up: A is not given, instead, it is the number that shows up 
 the most in the array. So you need to figure out this target A first,
 and solve the first question.
 
300. Sample Input:
1 2 0 3
4 6 5 1
9 2 5 7
5 4 2 2
Sample Output:
5
Explanation: The best route is
1 2 0
    5
    5
  2 2
1 2 0 3
  1
  7
  2
  output 7
给你一个 2d array
从左上角 到右下角
哪个path 里面 最大值最小
就是选一个 最短的path path的大小取决于 里面的最大值

301. 找intervals的题，一开始先从判断two intervals 
overlap做起，很简单，
两个follow up，一个是判断multiple intervals overlap，
然后是find number of overlap intervals

302. 类file system的
Map （key: entityId, value: entityObject）给你了。两种entity 
一种directory 一种file 都有Id。directory会有children, file会有size。
先问给定一个entity Id 怎么计算他的size （包括children的）。
follow up: 给一个List of entity，return list of entity size。
follow up2: 给一个entity id 怎么absolute print entity path。

303. graph path compression。leetcode上无这题 不过有老外的面经。
Input给一个list 里面有所有的start node，它跟它们的children组成了一个graph，
compress 里面的path, 然后return compress之后的start node。 这个讲真一
开始挺懵的，大姐一开始有点没说明白那些需要compress的path如何定义为相同的。
给的例子是
A -> B -> C -> END
A -> B -> C- > D -> END
A -> H -> END
可以compress成
A -> BC -> END
A ->   -> D -> END
A -> H - END
当一个Node的child只有一个 而且它的child只有它一个parent的时候 
可以compress

304. 给一个数组，和一个target number，返回target所在排序后数组的index。
比如{2,4,3,1,5}，target=3，返回2。不允许用排序。

305. 给一个binary tree，返回叶子节点。写个不更改树的方法

306. 预定房间问题。给n个房间，index 0-n-1。给一个访客的二维数组：
{{0,3}，{0,5}，{1，6}，{5,8}，{10,12}}，第一个人0时来，3时走，优先住index
小的房间，每人只能住一间，问访客都住完后，哪个房间住过的人最多，并返回人数。

307. 給許多長度為3的 code list and N
code list中的code是有按照順序排的
求能不能找出長度為N的唯一解
ex.
N = 5 codeList = ["abc", "bcd", "cde"] return "abcde"
N = 6 codeList = ["abc", "def"] 
return [] since it could be "abcdef" or "defabc"

309. recipes = ["bread"], ingredients = [["yeast","flour"]], 
supplies = ["yeast","flour","corn"]
we can now draw the graph first. (Consider the graph directed from 
upper nodes to downwards)
 yeast   flour
   \ /
 meat  Bread
 \  /
 SandWhich
For each recipe, count its non-available ingredients as in degree; 
Store (non-available ingredient, dependent recipes) as HashMap;
a
Store all 0-in-degree recipes into a list as the starting points of 
topological sort;
Use topogical sort to decrease the in degree of recipes, whenever 
the in-degree reaches 0, add it to return list.

310. 一个array of numbers，求升序sort 之后的 targeting number 的所有 
positions 的index
比如arr= [11,22,33,11,22]，targetingNumber = 22， sorted 之后是 
[11,11,22,22,33]， 那返回 22的index 的array 所以return [2,3]
O(N), O(1) space

311. 给一个很长的字符串，然后一个map，里面的key value分别是keyword和
score，就是说给的string里面能找到0-n个keyword，问最多能得多少分。
follow up是说要我给出都有哪些keyword。

312. 给一个二叉树，每个节点有个value，然后再给两个value，问从value1
的那个节点怎么走到value2. 
Follow up是这个树每个节点变得有规律，比如当前点
是i，那左孩子变成i*2，右孩子i*2 + 1.问这样怎么找刚刚的节点。

313. 有个movie class，每个object都有相似movie和评分，还有title。
然后给你一个movie，给一个integer N，请你返回top rated movies similar 
to the given movie，其中间接相似movie也算的.
follow up是万一很多movie rating一样，你怎么返回？万一movie很多，
一台机器放不下，你怎么办？

314. 随机生成迷宫

315. 给了一个list of 每个学生两次考试的成绩。 比如 [50, 60], [70, 80]. 
然后你作为教授，可以给学生pass 或者fail。 要求尽可能pass学生。给的限制是，
对于两个学生来说，如果其中一人的两门成绩都高于另一人，不能两个人都pass，
不然成绩好的同学会complain.

316. 给一个带字母的转动锁， 有很多圈，每一圈都有n个字母。问你如何比较快的找
出这个锁可以组成的单词。这个题其实是要你先用trie建一个字典，这样lookup单词
的时候，只要发现不在trie里面，就可以直接跳过。

317. 286. Follow up是门不在交点上怎么处理
https://github.com/jamesben6688/coding/blob/main/bfs/%E5%A2%99%E4%B8%8E%E9%97%A8.py

318. 给一个text（一堆word用一个或多个空格隔开），然后说屏幕每行可以占用X个字符，
需要多少行来装下这个text。题目给的非常模糊，需要自己clarify，比如断行时怎么处理之类的。Follow up是，想象你在分屏操作，
并且可以自行分配左右屏幕的比例，左边屏幕在处理text1，右边屏幕处理text2，问最少需要多少行装下。
binary search

319. family tree。 找两个人最近的祖先。比较trick的地方就是，一个的祖先是颗倒挂树，会指数增长。
https://github.com/jamesben6688/coding/blob/main/bfs/family_tree%E6%89%BE%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.py

320. 593 写一个class，可以不停加点，然后找到里面的所有valid的正方形，
followup是有一个误差范围，
比如delta = 0.1, [1,1], [1, 0], [0, 1], [0.01, 0.02]也valid。

321. 如何打开一个文件，然后打印出文件里只出现过一次的行。

322. 一串字符1010*10*10， 里面*可以表示0或者1，请把所有可能性都输出。

323. 一个数列，[1,2,0,3,1,3,0], 如何把所有的0都移动到数列的一边。

324. 有binary tree, we want to remove leaf node one by one. immediately remove the newly exposed leaf node. output the removal order. 
follow up 1是prioritize remove other leaf node rather than the newly exposed one. 366
follow up 2是，不管什么顺序了，请输出所有可能的remove leaf node的顺序。

325. 输入一个两位数字，然后每步取这个数的个位和十位相乘，贴到这个数后面。问第一个开始循环的位数是多少。比如 12248326 1224....，开始循环的是8位，需要输出8.
follow up 1. 用两个variable代替。
follow up 2. 如何找到这个最长的可能的循环长度
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/%E6%9C%80%E9%95%BF%E5%BE%AA%E7%8E%AF%E9%95%BF%E5%BA%A6.py

326. 在画板涂色。BFS。 
followup 是如果整个画板 放不下内存。有API 可以getFixSizeBoardByPoint(x, y) 从大返回固定size 的画板一部分。
怎么涂色。要求写代码实现

327. 直线的高速公路上有N 个检查站（checkpoint）。每次有车通过就会charge 此处到这个车经过的上个检查站的距离算出来的钱。
给一个检查站的数组然后给车从哪里进哪里出算钱。
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/%E6%B1%BD%E8%BD%A6%E8%BF%87%E6%94%B6%E8%B4%B9%E7%AB%99.py

328. 一个n * n的int matrix, 找一条从upper left 到lower right 的路径（minWeight）其实就是找sum最小的路径但不得出值需要return这个路径。

329.  8*8 的board，四个player，randomly and evenly assign cells to players。就每个人给16个格子。
Follow up： 8 * 8 的board， randomly and evenly assign cells to players。
就每个人给16个格子， 但每个人的cells 必须连续。

330. 有一个board，有'W' 'B' '-'， 你是否能capture 'B' capture的条件是
如果black和他连着的black们其中有adjacent to ‘-’就不能capture。
Follow up1: same same，但是你capture后要把颜色换成white
Follow up2： same same， 但是不是capture black是输入一个要capture的颜色但还是限定于‘B''W'

331. 给定背包size，和list of物品的weight和value，求出最大的value组合，返回这个最大组合和最大值。
followup如何优化

332. 1101  followup是如果允许friend之间cancel relationship 怎么做。

333. 给定一个餐厅的list 以及餐厅的category，类似 fast food，pasta，sushi，pizza，noodle等。
再给一个uber driver的list以及每个driver愿意送餐的category，比如司机1只愿意配送sushi和noodle；
司机2只愿意配送fast food，只能在对应的category里选餐厅配送。
每个餐厅和司机都允许有多个category，只要有一个match就可以送。
求怎么样能最大化餐厅的送餐数量。

334. 用一个3 * 3的刷子 可以把 0变1 问可以用这个特殊的刷子刷完某个矩阵嘛 比如中间有一个 x的可能就不行
x代表钉子
0 代表未刷区域
1 代表着 涂色的部分

335. employee 到 manager的扫描 一颗树 从某个manager 到 employee的路径

336. Given some bigrams, and with an input word, try to predict the best next word (criteria: frequency)
[[“I”, “am”, “Sam”]
[“Sam”, “am”]
[“I”, “am”, “a”, “Sam”, “am”, “I”, “like”]]
预测下一个单词
follow up： 如果给的是权重，怎么办？
https://github.com/jamesben6688/coding/blob/main/hash/%E9%A2%84%E6%B5%8B%E4%B8%8B%E4%B8%80%E4%B8%AA%E5%8D%95%E8%AF%8D.py

337. 给一个binary tree，输出vertical order

338. 传送带有一些不同重量的包裹，要把包裹按顺序打包总重量不超过k的箱子，并将箱子装进飞机。求飞机上行李的顺序。
包裹打包是先进后出，装飞机是先进先出。如果有行李重量大于k，直接跳过。
eg. input = [10, 5, 6, 3], k = 20, output = [6, 3, 10, 5], 
input = [10, 5, 5, 3], k = 20, output =[3, 10, 5, 5]

339. 输入一组array，每个element包括两个货币和换算的实时汇率，
判断给定的两种货币是否存在换算路径，以及换算结果。

340. waitlist server

341. 输入一组object，每一个object需要call function runTest() 得到测试结果，
如果某一个runtest是false，后面的object全都为false，问我如何设计函数找到first object which runtest()== False。
followup: binary search优化

342. given a list [0,3,5,8], k=4, calculate shortest distance of the path from first to last 0->8.
path can be [0,3,8], then distance = (3-0-k)^2 + (8-3-k)^2 = 2
path can also be [0,8], distance = (8-0-k)^2 = 16
path can also be [0,3,8], distance=(3-0-k)^2 + (8-3-k)^2 = 2

dp[i] = for j in 0 to i - 1, min of dp[j] + (i - j - k) ^ 2

343. 给个json
{"user": [{"A":12, "B":"test"}], "id":123}
给你 fields [("user", "A"), ("user", "id")]
写function来delete这些field。注意value可能是list，也可能是dict，或者int/string.
follow up，how to make it more efficient。答案是先处理fields,比如("A", "B", "C")和("A", "B")，你先处理后者就行了

344. Given a map from letter to interval as input, 要求return的很复杂, 
select any subset of letters, 
return the overlapped part for all selected intervals, while at the same they don't contain 
any other unselected interval.
e.g.
Input:
{A: [1 8)
B: 3 16
C: 5 7
}
[1 1, 3 2, 5 3, 7 2, 8 1, 16 0]
Output:
example, for {A,B}, return [3,8) without [5,7), so [3,5) and [7, 8)
final answer is a map where key is all combination of letters, value is the partial overlapped interval

345. Given String "abcdefffgabcde...", encode/compress it, use ".start.end" substitue the repetitve part of substring
output: "abcdefffg.0.4" (s[0] = a, s[4] = e),
开个List<>[26], 每个list 放同首字母所有出现过的substring, 似乎是比我的解法更快

346. Given a array, merge every two numbers each time, cost is the sum of two numbers, minimize the total cost.
Solution1 : priority queue + greedy
Solution2:array 很大, say 5000, 且sorted, 怎么处理, but array element max 1000
bucket sort 开个 arr[5000000], greedy, e.g. a[10] = 11, 10of them and cost is 100, a[20]+=5, 
merge last 10 with next smallest element, ...分奇偶处理

347. Generate a sequence that adds up to a given sum. Which is a map question.
I made one mistake: the key of the map is a number, but the object's key is a string.
const paires = {
1: [1, 2, 3],
2: [2, 3],
3: [1],
};

348. treenode 题 一个follow up找leafnode 然后remove直到没有

349. 有n个integer代表不同的core，设计schedule函数，每次分配一个core，
设计isfree函数判断某个core是否空闲，设计release函数释放某个core。

350. 判断arr中某个数字连续出现最长的子串的长度；
followup是：再给一个target arr，
判断所有在target array中每个元素联系出现最长的子串的长度，

351. 一个目录结构，就是有文件夹，有文件，这个类中有getDirectory方法，isDirectory方法，
delete方法。设计一个方法来删除某个目录。
followup：递归会出现什么问题，改为非递归的话应该怎么写，

352. 类似于｛｛ab ｛c｝d｛｛e｝｝f｝的字符串，要求输出删除最少的括号可以使得表达式有效。
stack

353. html
<html>This <I> is a <font>student</font></I></html>
对应的dom tree是
      <html>（1）
  this（2）   <I >(3）
        is a (4）  font>(5）
              student(6）
如果target string 是a student的话，则返回节点4和6，如果target string是is的话，则返回第一个出现的节点2

followup是问我，如果这个html文档在你处理的过程中被修改了怎么办，
回答用多线程的synchronized机制来进行domtree的锁定。

354. 一堆time blocks （person_id， start_day, end_day），代表一个人在这个time block里unavailable。
第一问求有哪些天是所有人都available的， return list of days。
第二问，现在不用所有人了，只要有K个人available就行，return list of days for K people。
第三问，现在要相同的K个人，在连续的d天里都available，return list of day ranges for a same K people。

355. 一个 total num of questions，和三个bucket的比例，每个bucket里面是题目, 实现不放回随机抽样生成一份考卷。
给的例子是
total 13， ratio 0.5， 0.3， 0.2
total 5， ratio 2， 1， 1
注意ratio并不一定add up to something。

356. 一个BST的root node，return all node values in BST in ascending order.
Recursive DFS + follow-up with the Iterative approach

357. 两位玩家，桌上一共有12张卡片 - 3绿3白3黄3黑。
玩家每轮需要进行一次combine把两摞卡牌叠在一起，两位玩家交替操作。
combine的两个条件： 
  a. 如果两摞卡片高度一致，可以combine
  b. 如果两摞卡片顶端的卡片颜色一致，可以combine
如果当前玩家无法进行combine操作，则另一名玩家获胜。
Perfect play：100%的玩家获胜概率，即在这条路线中不存在另一名玩家获胜的结果
题目需要写一个function，输入为player 1或player 2并默认此player是先手，输出为bool判断此player能否有perfect play。

358. Meeting Room III，follow-up如果有2个meeting room可以预约

359. 1090 Given an array of data, data有value和label两种属性，给出前k大的数据，要求其中不同label种类不超过m。
列了不同种解法

360. 一个2d空间中，有一些Vampire和mirror，input是这些vampire和镜子的row, column 坐标和镜子方向（东南西北），
设定是vampire在同一行或同一列面对自己的镜子中看到自己会embarrassed。 要求return 所有embarrassed vampire的
坐标以及embarrassed的方向。比如如果vampire在左边的镜子中看到自己，embarrassed方向就是西边。
vampire对同类来说是透明的。如果面向vampire的镜子被另一面相反方向的镜子挡住vampire就不会看到自己。
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/mirrow_vampire.py

361. 1820 一堆人回答一堆问题。每个问题有一堆标签，每个人有一堆感兴趣的标签，每个人只能回答包含至少一个自己感兴趣的标签的问题，
人和问题需要1对1匹配。返回a list of 人和问题 pairs。
比如 person1的tag是["java", "python"], question1的tag是["python","javascript"]就可以匹配。
follow up问了如果人和问题变成stream怎么scale。
要求用greedy写

362. 给一个聊天记录文件，每一行的格式是
something（人名@）word1...word2 word3
人名后面的东西全是message。要求parse这个文件并返回top k word count by person.
follow up问了文件很大放不进memory怎么办。

363. 给n个文件和一个non-blocking的API countWord(fileId, machineId)，会把一个文件发到一个machine上计算并返回word count。
这个API call完会立刻返回一个object。这个object有两个method：
int getCount() - 返回word count
boolean isFinished() - 返回这个task是否完成了。也就是说getCount()必须在isFinished()返回true之后才能call。
如果machine的数量没有限制怎么做？
follow up 1: machine的数量是m个, m可能小于n
follow up 2: 每次countWord call有1%的概率返回错误结果，也就是每个文件需要count r次然后取majority。


364. 有一个disk list，有一系列的snapshot，每一个snapshot属于一个disk 同时也有可能包含child disk 问如果我们想要依次删除disk，
删除的顺序是怎么样的，对于一个snapshot来说 我们需要先删除它的child disk 然后再才能删除它属于的disk; child disk 可能有多个
List<Character> disks = {'A','E','H'...}
snapShot = [
{	name: bingo
	source_disk: 'A'
	child_disk: ['B','E','H']
}
{	name: mongo
	source_disk: 'B'
}
]

365. 有一个input matrix 每一个值表示由红灯转为绿灯的秒数 问从matrix的左上角出发到右下角需要的最少时间是多少
有一些assumption：一旦转换为绿灯，就不会再变红；汽车在信号灯之间的形式速度非常快，这一部分时间可以忽略不计
Input:
2 3 0 5
1 4 5 5
9 8 2 7
6 5 4 3
Output: 5
2 3 0
    5
	2
	4 3
	
366. 设计一个combination lock, 类似有很多圈的密码锁
1. 支持的功能: 给定某一个圈的index 以及旋转的次数 如何获得对应的combination；
2. 给定一个input string 判断能不能用密码锁转出相同的string
1  2  3
--------------
'a' | 'q' | 'm'
'b' | 'a' | 'n'
'm' | 'c' | 'n'	

367. longest word chain: given a dictionary and start, find the longest word chain, 
In this problem we will extend Longest Word in Dictionary by allowing insertion of a new character in any position not only at the end. Return the construction path of the longest word.

Example 1:

Input: words = ["o", "or", "ord", "word", "world"]
Output: ["o", "or", "ord", "word", "world"]
Example 2:

Input: ["o", "or", "ord", "word", "world", "p", "ap", "ape", "appe", "apple", "apples"]
Output: ["p", "ap", "ape", "appe", "apple", "apples"]
follow up: without start,

369. file system, 要求实现一个function getEntitySizeByEntityId(id). 给了一个json格式的Entity例子，可以是folder，
可以是文件，如果是folder，会有child的filed，如果是文件，会有文件大小，先问如果parse这个json，有什么exception是需要考虑的，
然后实现这个function，如果给定的id是文件夹的，返回这个文件夹下所有文件的大小，如果id是文件的，直接返回这个文件的大小
https://github.com/jamesben6688/coding/blob/main/dfs/%E8%8E%B7%E5%8F%96%E6%96%87%E4%BB%B6%E5%A4%B9%E5%A4%A7%E5%B0%8F.py

370. flight costs, flightCosts[from][day] = c, if c != 0, we can flight, find the schedule with minimum 
cost that covers all cities, optimize the searching

371. Given an array arr. Return True if it is an almost sorted array, and False if it's not.
arr is almost sorted if there is an element arr[i] such that the rest of the array are sorted.
i.e. arr[0] <= arr[1] <= ... <= arr[i-2] <= arr[i-1] <= arr[i+1] <= arr[i+2] <= ... <= arr[n-2] <= arr[n-1]

372. 题目是给一串数组，里面是[[a, b], [b, x], ...] 类似，a和b以及b和x视为alliance，a和x视为union

373. jump game, 用DP，follow up是jump game ii

374. 2034 设计一个NumContainer Class，用于保存一系列数字，其中包括两个方程：
  InsertOrReplace(Index, Number)，就是在given index 的位置插入或替换数字
  findMinimumIndex(Number)，找到现在container里面given number出现的第一个index
  
375. 设计一个记录天气温度的class（只需要记录过去24小时每秒的温度），其中包括两个方程：
  找到过去24小时的平均值
  找到过去24小时的最大值
  
376. 给一个list of integers，我们改变这个list，只保证留下想要的，删掉不想要的（比如只留下偶数，不要奇数之类的）
 但是我们希望尝试以最小化移动次数（data movement）来改变这个list，保证只留下我们想要的，删掉我们不想要的

377. 用川麻的规则，给14张麻将牌，让设计一个算法，判断这手14张麻将牌胡了没有
比如 1 1 1 2 3 4 6 6 7 7 8 8 9 9 胡了
  1 1 1 1 2 3 4 5 6 7 8 8 9 9 没胡
   1 1 2 2 3 3 4 4 5 5 6 6 7 7 七小对 胡了

378. follow up加入花色以及翻倍   

379. 假设你是chef，你要准备menu上的几道courses，你知道每个course的raw ingredients和intermediate ingredients，
给你list of courses，output是list of raw ingredient。
例子：
Course Name: Pizza
intermediate ingredients: N/A
raw ingredients: flour，cheese， ketchup，suger
Course Name: Steak
intermediate ingredients: Bread, Salad
raw ingredients: Beef, Oil
Course Name: Salad
intermediate ingredients: N/A
raw ingredients: veg, egg, sauce
Course Name: Bread
intermediate ingredients: N/A
raw ingredients: flour, Suger, oil
Course Name: sandwich
intermediate ingredients: N/A
raw ingredients: flour, Suger, oil， beef
假设input是【Pizza，Steak】，output是【flour，cheese， ketchup，suger，Beef，Oil，veg，egg，sauce】

380. 给你一个string set，比如：（den，dent，dents，dew，det，bet，bent），找到最长的递增string list，递增的规则是前一个string尾部
增加一个字母变成后一个string。
例子的output是：den-》dent-》dents
https://github.com/jamesben6688/coding/blob/main/hash/%E6%9C%80%E9%95%BF%E5%8D%95%E8%AF%8D%E9%93%BE%E7%AE%80%E5%8D%95%E7%89%88.py

381. 给你一个string list和int width，比如：【foo，bar，a，b，cdefg，h，i，j，k】width = 14
输出一个另外一个string list：
“foo   bar a b ”
”cdefg h   i j “
“k”
（注释：foo后面有三个空格，bar、a、b后面有一个空格，cdefg后面一个空格，h后三个空格，i、j后面一个空格，k后面没有空格）
规则：
1. 把输出的string list的每个element按列打印，就会得到一个类似table的东西。比如例子里，除了最后一行，就是一个2x4的table。
2. 这个table的每一列打印出来后，要纵向对齐，而且要比前一列的最长的单词纵向多一个空格(第一列除外)。
这就是为什么cdefg后面只有一个空格，但是foo后面需要三个空格。
3. table的每行不能超过width。
4. table的每列的宽度是确定的，不同列宽度可以不同。
假设上面的例子变成了【foo，bar，a，b，cdefg，h，i，j，k，abcdefghich】width = 14，那结果是：
"foo         "
"bar      	 "
"a       	 "
"b       	 "
"cdefg    	 "
"h       	 "
"i        	 "
"j           "
"k           "
"abcdefghich "
Binary Search + Check
我们可以把左边界设置成1 右边界设置成string list的长度 跑BS
如果可以装下当前数量的words 也就可以装下比当前数量少的words
如果不能装下 就尝试更小的值
现在问题转换成了: 给定每行可以装下的words的数量，判断它是不是valid
因为每列都需要对齐 所以对于每一列来说 我们需要找到这一列最长的word
同样的方法 把所有列的最长的word找到，相加补上空格后看是不是超过了width
从而判断当前数量的word是不是valid

382. input 是 List<Employee> 每个employee 有unique id & List<Employee> directReporters
Basic Question:给一个 targetEmployee 求从CEO到target Employee 路径（每个Employee 确保只有一个manager）
思路： build tree 之后 find node from source to targetNoderecursive function
Follow up 1: 如果每个employee 可能有多个manager 找从CEO 到 target Employee 的最短路径
思路： 这时候结构从tree变成了 graph， build graph 之后 bfs 可解
Follow up 2: 接着follow up 1 如果每个manager 通知自己的direct report 需要1s， 那么从CEO开始 通知到全部员工的最短时间是多少

383. (medium)设计一个 WordStoreService
实现两个 method： addWord(String word) requestWord()
addWord 很简单 把word 加到 Word Store里面存储起来
requestWord（）从wordStore 中pop 一个word出来
Constraint： 同一个首字母开头的单词不能在1s内同时出现两次
example：
addWord(Apple)
requestWord() return apple
addWord(banana)
addWord(Apple)
requestWord() return banana
requestWord() return null (已经return 过 word starts with A， 可以理解为前三个requestWord 是synchronized calls)
// after 1s
requestWord() return Apple

384. Maze Generation Algorithm
步骤是这样
Step 1: 生成一个sides box length = N， 每条边XO 交叉排列， 每条边X的数量=N
Step 2: 随机选择一个有效的X
Step 3: 对step 2 选择的X 随机选择一个有效的方向 （4 directions）
Step 4: 对随机选择的X 随机选择的方向 延伸标记O 和 X
Step 5: 如果还有可以选择的X， 那么重复Step 2
https://github.com/jamesben6688/coding/blob/main/maze/dfs_generate_maze.py
https://github.com/jamesben6688/coding/blob/main/maze/prim_maze_generation.py
https://github.com/jamesben6688/coding/blob/main/maze/prim_maze_gene_2.py

385. string substitution,
input是一个string 比如%HOME%/usr/1， 然后一个map HOME -> /home/%USER% USER -> abc
输出需要是/home/abc/usr/1。 map里的string也带%%算是一个follow up了
大致就是讨论了一下在这个case里是写function好还是设计成一个class，然后做format的异常检测，用memo来提高效率，
有nested的情况还要考虑会有loop

386. Maze problem 从一个点到另一个点的最短路径
follow up返回path
再followup是maze中间有portal，最后一个是如果使用portal如果有额外cost

387. 1200变种，给的数组里是时间点，求最短间隔

388. 每个TreeNode会存储本身的index和parent的index还有本身的值
输入是一个树节点类型的数组，
求输出一个映射，键是点的id, 值是这个点和它所有下面链接到的节点的值

389. Given two strings, check if they are permutations of each other.

390. Split a binary search tree by a pivot

391. 给-一个list of城市和对应的value，和一个list of
城市之间的 connections，找出4个城市，
value 之和最大，并且4个城市之问要连在•
起，比如 ABCD，就至少需要 A-B B-C, C-D
之间有连线

392. 523 Follow up需要O(n)完成。

393. 747，Follow up 需要O(n)完成

394. 给一个matrics(m*n)，只能走straigt，计算所有可能的数字。

395. input一个长度为偶数的数组，odd位置是重复次数，even位置是数字，设计一个iterator 的next() 
function，return 下一个应该print的数字比如[1,2,3,4] 用iterator遍历完应该输出 2,2,4,4,4
时间空间复杂度要求constant
follow up是当遇到次数为0的时候，next()要返回上一个遇到的数字

396. 前提每个graph node 分布在不同server, 不能用global memory，要求写算法每个node遍历一次

397. 给一组数A，问能不能找到俩数，满足index |i-j| <= a, value |A - A[j]| <= b

398. 给一个scheduler，可以设置t时间之后运行程序a，但是会被覆盖，比如设置10s后运行a，在第5s又设置8s后运行b，
之前的a就不会运行了，要求写一个新的scheduler解决覆盖问题，可以调用给定的schedule。

399. 658 给一个matrix，把每个0所在的行和列都转化成0

400. Check Directions
N, S, E, W表示东南西北, 1N2表示1在2的北边 1NW2 表示1 在2的西南 给一个序列，检查是否合法["1N2", "3N4", "4NW5"]
以南北和东西分两个Topological sort解决

401. 有一群好朋友要在学校里找个距离所有人最近的咖啡厅，前提是必须让所有的好朋友都能到达。Friends array: [1,2] Cafe array: [4,5]. 
给一个二维数组代表图里面连接的边：( (1,2) , (1,5) , (2,4) ), 返回距离最近的咖啡厅。
以每个咖啡店为起点bfs，记录下距离，最后选取距离最短的咖啡店
https://github.com/jamesben6688/coding/blob/main/bfs/%E6%9C%8B%E5%8F%8B%E5%88%B0%E5%92%96%E5%95%A1%E5%8E%85%E6%9C%80%E7%9F%AD%E8%B7%9D%E7%A6%BB.py

403. Given a Temperature Manager class, with functions recordTemp(int temp); and getMaxTemp(); 
You need to record the temperature when a new temp comes in, and get the max within the last 24 hours.

404. 2242 fun city1

405. Manager Employee Management
Design a class organization
setManager(manager, employee) => 将employee的直属上司设为manager
setPeer(personA, personB) => 把person A和person B设为peer，代表着这两人将有相同的上司
reportsTo(personA, personB) => 给定两个人，返回person B是否是person A的上司，注意不一定是直属上司
注意更新一个员工的上司的时候要更新他所有的peer的上司

406. Given some bigrams, and with an input word, try to predict the best next word (criteria: frequency)
[[“I”, “am”, “Sam”]
[“Sam”, “am”]
[“I”, “am”, “a”, “Sam”, “am”, “I”, “like”]]

407. Cycle Group
Given a list of circles (x, y, radius), determine whether they belong to the same group. Two circles are in the same group if they overlap: dist <= r1 + r2.

408. 定义一个add(x, y) 添加一个点到平面上，返回是否有其余三个点能与之组成正方形。

409. 给你一个 Clock object， 里面有一个method return当前时钟的时间， 
以及把时钟往后调1， 5 ，15,60 分钟的add method。 让设计一个function 输入一个新时间， 
并用最少次数的add 来快进到新时间（时间格式是[Hour, Minute, "AM/PM"]）。
Follow up 是现在 add button 的数量是不定的了，要怎么写。
E.g 有两个button[23, 59], [0, 2]。 要快进三分钟的话就是按两下第二个按钮再按一下第一个按钮。
可以用BFS 最多只有24*60= 1440的node需要visit
栗子的话23:59 = 1439， 00:02 = 2
从0开始
step = 0: { 0 }
step = 1: { 1439, 2 }
step = 2: { 1438, 1, 4}
step = 3: { 1437, 3, 6}

410. 307 不过不更新，找最大，一线段树，用array实现，被问优缺点

411. 给一组log有任务id，时间，开始或者结束，再给一个timeout，找第一个timeout的任务，log里不是所有开始的id都有结束log，
follow up是timeout不是constant和输入是数据流怎么办

411. 给一串floder，有它的id，名字，parent，打印从folder到根的路径，需要检测环和memorization优化复杂度还有各种edge case

412. 有一个forest，以数组的形式存储，-1代表根节点，然后要求是删除某一个结点，输出删除后的数组表示。
比如[-1,0,0, 2, 3, 1]表示的是index为1和2的结点与根节点相连，index为3的结点与index为index为2的结点相连，
总之就是数组的数值表示的是当前index的结点连接的父结点，比如删除index = 3的结点，返回结果应该是[-1,0,0,1]
又比如[-1,0,0,2,2,3,4]删除index=3返回[-1,0,0,2,3]
两个注意的点: 删除所有与删除结点连接的点，同时还要注意更新index

413. 数组[0,1,2,3,3,3,4,5]删除最大的k个数后返回数组长度，比如k是3，返回3，因为3，4，5是最大的三个数。
follow up是k远远小于n，怎么提升，

414. 给一个target单词，一个guess单词，如果位置完全匹配是G，字母匹配但是位置不匹配是Y，否则是R。如果有多个可以匹配为Y的，则把index最小的匹配成Y，其他的还是R，然后输出结果的string。比如BACD和CAGE，就输出YGRR。follow up是如果给一个target和一堆guess，每一步要求前一步的guess是G的地方需要保持，前一步如果是Y的地方这一步必须要
包含这个单词。输出这一堆guesses是不是全部valid。

415. 给了一个值d，一个数据流stream = [-10, 4, 3, 10, 5, ...]，最后要return一个array，里面只有三个元素（可重复），
使得每个元素之间的差都 <= d
例如这里就return [4,3,5] （顺序无所谓）
用Bucket

416. 给一个数字，输入进计算器，倒过来会找到一堆单词 比如 1=I， 8=B 等等 600637就对应gOOgLE 给一个word list 判断word在不在这串数字中

417. 给一个shuttle bus 到达时间 列表，给shuttle bus的容量，给乘客到站的时间，问你最晚到站的时间是多晚，才能赶上最后一般列车
比如 shuttles[5,10] capacity =2 arrivals=[3,8,8,9] return 7
shuttles[5,10] capacity =2 arrivals=[3,8,12,12] return 9

418. 给一个2-d 列表，每个cell代表一个城市，每个城市有一个红绿灯，一开始都是红灯，每个cell的数字代表红灯变绿的时间，
也说明你可以离开这个城市，红灯说明不能离开城市，返回最快从左上到右下的时间
比如 [1, 2, 0],[4,6,5],[9,6,5] return 5 两个方向（右和下），用dp就可以了，
follow up是四个方向，

419. 进行gmail和其他邮箱系统数据导入，其他系统的邮箱系统是用
folder {id: 27, parentId: 15, name: 'projects'},表示的。
而gmail采用的是 label {displayName: 'projects', path: 'personal/projects'}
sample data:
/**
*
* // Sample input:
*
* folders = [
* {id: 27, parentId: 15, name: 'projects'},
* {id: 81, parentId: 27, name: 'novel'},
* {id: 15, parentId: -1, name: 'personal'}, // a parentId of -1 means root, some of the variant using 0 to represent root.
* {id: 35, parentId: 27, name: 'blog'},
* ]
*
* // Sample output:
*
* labels = [
* displayName: 'projects', path: 'personal/projects',
* displayName: 'novel', path:'personal/projects/novel',
* displayName: 'personal', path:'personal',
* displayName: 'blog', path: 'personal/projects/blog',
* ]
* */
//要求实现数据的导入
List<Label> folderToLabels(List<Folder> folders){
// write your excellent code here
}

420. source， target两个string，把source变成target，只能在同一个index delete一次，insert一次，在保证delete的数量最小的情况下，
return哪个index开始delete，要delete多少个，要insert哪些个char进去才能变成target。
example：input: source: '12345', target: '45'
output: 0, 3, ''

421. add and remove points from the matrix and print out the boundary box to encompass all points

422. Flip row or column to close all lights.
Given a binary 2D grid (each element can either be a 1 or a 0). You have the ability to choose any element and flip its value. The only condition is that when you choose to flip any element at index (r, c), the 4 neighbors of that element also get flipped. Find the minimum number of flips that you need to do in order to set all the elements in the matrix equal to 0. If it's not possible, return -1.
NP Hard. 用暴力法

423. 给一串字符串，要求实现csv的parse功能，比如给“name，gender n/ jack， male n/ marry female”， 
要求能快速返回第几列第几个。
如果字符串很长怎么办

424. 两个手机截图，判断有多少部分是重叠的 套kmp或者字符串哈希实现O（n）

425. 给一个timeout和一个log list，看在执行这个log list的时候会不会出现timeout
example:
input: id, timestamp, status
["id1", 0, "Start",
"id2", 0, "Start",
"id2", 1, "End",
"id3", 1, "Start",
"id1", 2, "End",
"id3", 5, "End",
...
]

如果timeout = 3，可以看出id3 被timeout了。所以function就是return true（要timeout），不然就是return false。
注意给的timestamp是已经sorted需要被利用上。如果得出o（n）的solution。

426. calculate the result for the mutiplication for two big numbers

427. Given a 2D array as dimensions for several boxes, find the max number stack of boxes. 
这题类似俄罗斯套娃，就是给你一个二维数组，每个数组是由box的长和宽组成 could be like this：[[10, 6], [6, 4], [5, 3], [5, 1], 
[3, 2], [3, 2], [2, 1]]. 每个大箱子里只能套一个小箱子，箱子dimension不是unique的，可以有一样的箱子。
问你最多总共能有几个箱子套娃？

428. 给两个2D数组，S and T，比方说 
S = [[2,3],[4,5]], T = [[1,2,3,4], [2,5,4,6],[4,3,2,7]], 问你在T中能找个几个和S相同的pattern，
楼主的理解是就是在T中找S的permutaion（要把S和T写成一行一行的形式会比较好看出来）如果用楼主举的栗子，
结果就是3，分别是：[2,3,5,4], [5,4,3,2],[2,5,4,3].

429. 给了一个list，里面有一堆String，例如{carandcar,carand,plane,trainorcar}，
用这些构建pattern，写一个构建pattern函数。再写一个是否match的函数，是否在pattern中有match的string，
函数输入是一个string，但是这个string有个特点，可能含有*，*可以match 0-n个字母，
例如match(carandcar)-->True, match(plan)-->false, match(cara*d)-->True, match(trainor*)-->True

430. 给一个list例如[a,a,a,a,b,b,b,b,c,c,c,c]，保证相同的字母一定在一块儿，即相邻，问是否在list中有字母出现次数超过总次数的15%，
如果有，输出来它是谁，如果有多个，可以输出任意一个。

431. 不放回随机抽样. 需要设计时间和空间复杂度最优的方法.

432. 278 简单来说，input是两个integer，low和high，代表的是一开始的commit和最后的commit。你还有一个API isWorse(a, b) 
可以比较两个commit a和b是不是恶化了。简单来说，就是给你一个数值单调递减的array（e.g. 999887776555322211），
然后找出所有比前一个数字小的下标，只是这个下标不是0开始，而是low，然后最后是high，中间的下标数字连续。
用binary search即可，如果binary search里右边没有比左边差，那么这个区间必定没有worse commit，直接返回，
否则取中点，看中点是不是worse commit, 是的话加到answer里，再两边binary search

433. 给一串数字（不连续，可大可小，可重复，可负数），写一个API生成这串数字的一个random permutation，生成过的不可再用，

434. 计算一个64 bit unsigned int的每一位数字之和，秒了，然后三姐问给你1mb的内存，如何优化

435. 首先input还是一个有障碍的matrix，要找出最短到终点的路径，但是没有炸弹可以炸障碍，取而代之的是有些格子是大写字母（A- Z），
代表的是宝藏。宝藏的字母可以不连续出现（就是matrix里有A，C但没有B），但是宝藏是unique的。你需要收集所有的宝藏然后到达终点。
如果无法到达终点，或者有宝藏无法collect，返回-1
followup是宝藏被上锁了，有小写，小写是钥匙，大小写是对应的，譬如钥匙a可以解锁宝藏A。还是求到达终点的最短路径，
还是要求收集所有的宝藏，但是要收集宝藏意味着先找到钥匙

436. 12个 tile， 4 个color，3 each
两组tile可以摞到一起的条件：1. 两组一样高；或者 2. 两摞最上面的颜色一样。
两个player轮流走，无路可走的时候输。假设两个player每次都可以走perfect的move
input： 一个tiles的分组状态，和一个player
output： winner

437. 给三种二维brick, Width x Length分别是 3x1, 3x2, 3x3, 问有多少种方法建一个二维的tower, 
tower的width is 3, height is x. 不改变砖的方向。比如一个 3x4的塔，1+1+1+1是一种，2+1+1是一种。
follow up是如果可以改变砖的方向的话那是几种。比如 1x3 和2x3 并在一起组成一个3x3的塔是一种，3x1 和3x2一起是一种。

438. 实现平方根，但是特别注重code reusability。只需写1+的平方根，0-1 invert即可。
还问了binary search有比取mid更好的方法么

439. 逆波兰 跟进问，加一个操作，要求支持assignement, 要求处理各种exception
比如 a b 5 = = a 1 + 要求最终结果返回 6
b 等于 5
a 等于 b
所以 a + 1 等于 6
https://github.com/jamesben6688/coding/blob/main/stack/%E9%80%86%E6%B3%A2%E5%85%B0%E8%A1%A8%E8%BE%BE%E5%BC%8F.py

440. 战舰游戏，给一个二维矩阵，初始值只包含0或1,0代表水，1代表舰，舰只能是一条横或一条竖，并且舰跟舰不会相邻
实现两个操作
isShot， 检查某个格子是否被射击过，如果是返回 true; 反之，false
shoot，向某个各自射击，返回值要求 water | shot | sank
一个格子只能被射击一次，重复射击需要报错
water = 射击的格子是水，shot = 射击打在了船上， sank = 这次射击之后船沉了
跟进问是如果优化 shoot function 要求O(1)时间复杂度

441. 给一个JSON array 如下
const data = [
{
  name: 'John',
  company: 'Google',
  position: 'Software Engineer',
  level: 'Entry',
  ...,
  ...
},
{
  name: 'Ann',
  company: 'Waymo',
  position: 'Product Manager',
  level: 'Senior',
  ...,
  ...
},
...,
...
];

然后给一个match pattern， 比如
const match = {
name: 'John',
level: 'Entry',
...
};

要求根据match pattern找到data里边相对应的item。

442. 给一个array，其中包含了api url, 根据以下规则实现
array order代表了每一个api的优先级
找到优先级最高的success result
如果所有的api 都reject，那就handle reject

443. 给一堆jobs，有start time，duration，number of cpu needed，然后有一个cpu数量为n的机器，问能不能把jobs跑完。
follow up是实现一个类，
有一堆jobs，然后给一个新的job，判断这个job加进去之后cpu数会不会超，如果不会超，就把这个new job加进去。

444. 给一个target单词，一个guess单词，如果位置完全匹配是G，字母匹配但是位置不匹配是Y，否则是R。如果有多个可以匹配为Y的，
则把index最小的匹配成Y，其他的还是R，然后输出结果的string。比如BACD和CAGE，就输出YGRR。follow up是
如果给一个target和一堆guess，每一步要求前一步的guess是G的地方需要保持，前一步如果是Y的地方这一步必须要
包含这个单词。输出这一堆guesses是不是全部valid。

445. word break I/II

446. 判断一棵树是不是有多余的edge

447. Given a keyboard (2d-grid, each cell is a key), from a position, you can jump at most k distance (Manhatten distance) 
to another position. Given a word, determine whether you can type the word on the keyboard.
You can always start at the index where the first letter is.
大概题目就是，从一个key开始往外走，你最多能走k的距离（abs(x1 - x2) + abs(y1 - y2) <= k），看看能不能顺利把词打出来。
比如“late”，"l" -> "a" -> "t" -> "e"，如果距离太远就return False。刚开始很简单，说key都是unique的，
Follow up：现在键盘上的key不是unique的怎么办

448. 银行有n个agent给客户做service，客户需要一个一个来做service，每个service的时长是由客户决定的，
目前前面有m个客户(m个客户的service时长作为输入)，你是第m+_1个到的，求需要等多长时间轮到你去service.

449. Given a string, each consecutive identical vowels accounts for 1 score, implement a method to get the score of the string.
Example: "abc": 0, "foo": 1, "fooo": 2, "ofo": 0
Follow up:
Given number N, output the number of the strings that is length of N and scores zero. 
DP[i][c] 来做当初为i, 尾字母c的个数

450. 213 换个壳。附加题：如果不是每隔一个，而是隔k个，怎么写？space & time complexity

451. 货车过桥。 货车有重量，桥有长度 一共可以容纳k个车。然后就是算每来一个新的车，桥长最重的车是多重。 

452. 往grid里加入和删除点的坐标，每次加入和删除return最小的能cover 所有点的方形。

453. 输入1. node，里面有string也可能是一堆children node，输入2. String，输出所有可能包含这个string单词的node

454. 坐标系加减点，用矩形框住所有的点，返回此矩形左上和右下的坐标

455. 给一组 TESTS， 还有一个 api runTests(test[] tests)。 如果tests 中有一个pair 有问题, 这个 runTests api 会return false, 
没有这样的pairs 的话就return true. 要我们找出所有那些fail test pairs. 举个例子：
TESTS: 1 2 3 4 5 6 7 8
Fail test pairs (我们要找的):[ [2,7], [ 5,6]]
runTests([1,2,5]) => true (因为[1,2], [1,5], [2,5] 都不在我们要找的pairs 里面）
runTests([1,2,3,5,7]) => false (因为[2,7] 在我们要找的pairs 里面)
我们要做得就是怎么用这个 api 找到所有这些pairs.

456. 一個無限大的board, 給定0的位置, 其他皆為1, 找出各個點到1的最短距離

457. binary tree, 找p 到 q的 path

458. 给了基本的function框架，让写一个translator，要实现添加单词功能，两个语言之间的互相翻译功能，
follow up，corner case的处理之类的，比较简单。 第二题是第一题的follow up，让把刚才双语translator拓展成多语言translator。
如果两个语言之间没有直翻，但是有间接翻译（比如，a语言和b语言互翻，b和c互翻，但是a和c不互翻，那也算a和c互翻，可以找得到解）。

459. N(Rooms) = 2,
Customers' appointments =
[
{start: 1, duration: 1}, -> 0
{start: 1, duration: 1}, -> 1
],
Ans: 0
PriorityQueue(heap) 就可以了

460. 给定string a, string b, 一个map（可假设所有节点联通），能否用map将a转换成b。
 a："aba"b:"cdc" map: "a -> c", "b->d" true
 a："aba"b:"bab" map: "a -> b", "b->a" false, 有环
 
 只给a 和 b，问是否存在一个环使a可转成b。
 followup是只给a 和 b，问是否存在一个map使a可转成b。
 
461.  huffman tree哈夫曼
https://github.com/jamesben6688/coding/blob/main/tree/%E6%9E%84%E9%80%A0%E5%93%88%E5%A4%AB%E6%9B%BC%E6%A0%91.py

462.  LRU，就是如果保存log 每次来新的要更新下ttl。最后followup的时候要用LRU

463. 一个排序数组，找离t最近的k个值

464. 528，implement一个weighted random number generator
follow up没有原题，大致内容是：
take random numbers and add to total
try to get as close to 100 without going over
my friend will take numbers until he reaches 95, but will stop at or above 95
what is the probability that my friend will go over 100 based on the int n used to create our 
random generator and the current total my friend has

465. Find path from 'CEO' to an Employee: 楼主用BFS解的

466. 对每个朋友同时进行BFS并记录下第一个所有朋友都去过的餐厅，需要注意的是图里可能有cycle，

467. 用三个数字玩24点，可以用 括号+ 和*，求是否可以算出24
直接暴力解，followup是如果数字数量可变该怎么办

468. 给一个grid，每个格子是一个0到7的数字，其中有一格是-1，代表终点。起点是(0, 0)。要求返回一套指令，
把每个0到7的数字映射到上下左右其中一个，使得按照这套指令能够从起点走到终点。后续是返回最短路径的指令。

469. 给一个compact的图邻接矩阵，以及一个std::set<int>, 
表示无法达到的节点（原题的context是travel，从一个街区到另一个街区，这个std::set指的是堵车的街区。
就算graph的topology上可到达，在只要这个表里也不能去），然后求从任意节点到另一个节点的最小步数。用层序遍历可以解决。
然后follow on问的是，如果那个不可达表(std::set)现在变得可达了，但是要付过桥费，让找从一个节点到另一个节点的最小过桥费。
大概就是调整下cost的计算。

470. 第一个是给一个 0-n 的数字序列，生成一个随机的permutation，

471. 给了一个用tree表达的 四则运算，让展开成表达式

472. 470 recursive, Iterative

473. 找出 在一串字符当中 X, Y 的最小距离。'XX00XY'
 follow up是 在2D的char array里面 找出X,Y 之间的最小距离
 
474. compare string 和 一个 char array, 检查是否能够用提供的 char array来组成目标 string.

475. 第一part: char array里面的字符可以无限使用
第二part: char array里面的字符不可以无限使用
第三part: 设计class。把前两个part 分别放到自己设计的 class 里面, 达到user friendly, 模拟user使用不同的class

476. board game. 两个硬币, 都是正面跳两个格子, 否则跳一个格子. 问到N的时候 一共有多少种可能

477. iterate through all the nodes in the tree. follow up: 找出parent node.
class node{
  int val;
  List<node> children;
}

478. if there is a file system that contains files and dirctorys.like this
{1, {type: "Directory", Name:"Direcroy1", Children[2, 3]}
2, {type: "Directory", Name:"Direcroy2", Children[4, 5]}
3, {type: "File", Name:"File1", Size: "100"}
4, {type: "File", Name:"File2", Size: "200"}
5, {type: "File", Name:"File3", Size: "300"}
}
Type emum{
  Directory
  File
}
Entity{
  EntityId
  Type,
  Name,
  Size,
  Children<Integer>
}
public int findSize(int entityId){}
Follow up what if you want to findSize within O(1) if you already calculated the size.

479. Give a list of integer, find the length of longest sublist that one number is 1 bigger than previous one
[2,1,3,2,4,1,3,4,5] -> return 5
[2,3,4,5]
[1,2,3,4,5]
[3,4,5]
Follow up: what if it is m bigger than previous one.
*/
public int longestSubString(int[] arr){
  HashMap<Integer, Integer> map = new HashMap<>();
  int res = 0;
  for(int i= 0 ; i < arr.lenght; i++){
  map.set(arr, getOrDefault(arr[i]-1 , 0)+1);
  res = Math.max(res, map.get(arr[i]));
  }
  return res;
}

480. Assume you have a map of cities with these cities' adjacent cities. There are also cities where the 
traffic is very bad and we want to avoid it.Find the shortest path from the start city to the destination city.
A -> "New York"
B -> "Chicago"
map: ["New York" ["Philidopha", "Boston"]]
Heavy Traffic: ["Bostion"]
Follow up: return the path list instead of the shortest path.

481. 给一个robot and a 2D array of int, 0~7代表8种颜色 -1代表target start position = 0,0
   给每一种颜色一个direction让robot能到达target0
方向只有四種 不包含對角線方向
   
482. 给两个string 找出shortest superstring
follow-up 给multiple strings find shortest superstring

483. 给rook and pawn position, rook could not jump off obstacles. 求shortest move to get pawn
BFS 遍历寻找更新数值，问我能不能optimize to O(n^2) 但一时之间没想到

484. Jessica serveing server time.
follow up了一下以数学题的角度来说怎么解决, 最小公倍数之类的.

485. 给一个计算机屏幕, 比如左上角是(0,0), 右下角是(1920, 1080).
这其中有一些窗口, 给的也是这些窗口的左上角和右下角坐标(都是长方形), 比如 A:[(10,10), (50,50), 3], 
最后那个参数3 是指这个窗口的相对位置, 也就是说数字越大代表这个窗口在更靠前的位置. 比如 B:[(25,25), (100,100), 4]. 
B这个长方形盖在A的上方.
求每一个window露出来的面积是多少.
https://github.com/jamesben6688/coding/blob/main/swipe_line/%E7%AA%97%E5%8F%A3%E9%9D%A2%E7%A7%AF.py

496. 315, 但是反过来找, count the smaller element before self.

497. There are K check up room in sequence (indexed 0 - K-1)in a long corridor and you are given the entry time of different patients and duration of check up in order.
The check up room is assigned on the basis of closest check up room available to incoming patient.
Once check up is finished it can be assigned again.
Find the check up rooms which catered to maximum number of patients.

498. 一个搜索引擎然后用户搜索很多字符串，找出most recent N words user searched for.
LRU Cache 146

499. 假设有一个stream, 每个元素是(time, price)，实现一个类支持下面的操作
(1) add(time, price) (2) update(time, price) (3) remove(time) (4) getMaxPrice() 5getMinPrice() 6.getMaxPriceTimestamp() 7.getMaxTimePrice()
(1) what if a lot of read, only small ammount of write -> update max, min, maxTime at write
(2) what if in multithread -> lock, queue with multithread, get local max from each thread and get glocal max from all local max

500. find max area of land-locked islands, 如果water 被island包围，也算做结果里面
0 0 0 0
1 1 1 1
1 0 0 1
1 1 1 1

501. binary tree的leaf node的 delete。
Followup1 要求新产生的leafnode最先被去
除 （移除一个leaf他的parent变成leaf必须紧接着移除）
Followup2 要求新产生的leafnode最后被去除

502. 283. Move Zeroes. 要求minimize the total number of operations

503. 968. Binary Tree Cameras

504. 实现两个方法一个add()一个query()，add往结构里加数,query取第k个最小值

505. 2128一个二维数组 灯泡 有1有0 ，问能不能都turn off，就是都变成0

506. 一个record温度的方法，要实现registerTemp()和getMaxTemp(),返回24小时内温度最大值。
Follow up: 想取最小值

507. 1856

508. 密码锁破解。一共五个数字，每次可以按一个或多个数字，穷举所有的密码输入。例如"1-2-3-45"表示第一下按1，第二下按2，第三下按3，第四下45同时按，同时按的几个数字不考虑先后顺序，
搜索+二进制状压。
follow up估计是用二进制优化搜索中的状态。

509. 判断能否用全部的字符串组成一个对称的字符串序列，例如["ab", "c", "ab"]可以，但["ab", "bc", "cd"]不行。
followup是在判断后的基础上输出全部的组合，搜索+回溯。

510. 猜词给反馈。给一个目标字符串，含无重复乱序英文大写字母，再给一个用户猜测的等长字符串。要求我们写算法来给用户的猜测做反馈。
规则是如果猜的字在目标里且下标也正确则为对，
在目标里但下标不正确则为中，
followup：目标字符串有重复字母，且规则发生变动，
（猜测的字和目标的字从左往右最近的字匹配），

511. 计算beauty value，一开始没看懂题目，其实就是给一个list, 表示每个block的颜色，再给你颜色c，让你计算list里这个颜色的最长连续的长度；
follow up1，如果是给一个很长的list of c，怎么做；
followup 2，如果可以repaint其中m个block，那么最长连续的长度是多少；
follow up3, 如果这个block list是一个circle，怎么处理。

512. Reverse linkedlist odd & even; Maximum path sum from leaf to leaf

513. 找到几个朋友之间最近的cafeteria，给int[] friendsPos，int[] cafeterias, int[][] edges，用的BFS，follow up, 如果cafeterias特别多，怎么办

514. 种board game，只有0，1, 每次用 boolean next(int val)，就会从board[0][0] 插入val, 并且剩下的数都会z字移动，这时候如果任意row或者col全都是1，就winning, 返回true。
101
010 -> insert 1 ->
111

101
010
111
插入1后变成
110
101
011
插入1后变成
111
010
101

515. interval insert， 稍微有点不同就是他需要你输出每次插入一个区间之后的需要画的长度， 比如一个stream[[4,10], [7, 13], [20, 30], [1, 40]] 那输出就分别是6， 3， 10， 20， 
因为一开始你画了4~10 长度是6， 然后7-13的时候因为7~10这一部分你不需要画了所以只有10~13所以长度为3 

516. 岛的那道题变形，其实用DFS做也一样。就是click 一个点，如果是1就不变，如果是0就把周围所有0变成1，染色的这么一个概念。而且也没有follow up。
直接出了 一个排序好的数组去重，要求On时间O1空间，双指针即可。唯一要注意的是他是用的Integer 数组不是int数组 比较的时候以及有需要填入null的时候。

517. 比如dir（id=1）-node1（id=2）-file1（id5）（100B）
                   -file2（id6）（200B）
         -node2（id3）- file3（id7） 400B
        -file4（200B）
然后说id5的size就是100B，node1因为包含了file1，file2所以id=2的时候size是300B。以此类推id=1的时候size就是900B，类似于叶子结点都是实际的file有实际的大小，
而中间节点就是他的子节点的size的和。其实结构很简单，他就让实现这个东西，当给一个targetId要返回对应的size。但是On不行OlogN也不行，我看他的意思是要O1

518. 给一组replacements<beginIndex,replaceString,replacedString> 和原字符串str，
先判断原字符串str从beginIndex开始的substring为replacedString，如果存在，把它replace成replaceString。
833。想问问下面这样的写法时间复杂度多大，不包括sorting?

519.  给一个dict，包含很多string，找出类似于这样的abc->ab->a 或者erfg->erg->rg->g这样的chain并且返回最大开始string例如这个例子就是erfg。
follow up是万一删除某个word怎么样。1048

520. 给定一组request，形式是startTime,url,status code,duration，求每个时间节点（每个request的startTime）对应要处理的request
10001 url1 404 10
10002 url2 500 1
10010 url3 300 10
10009 url4 200 100
返回10001->1 10002->2 10010->1 10009->2

521. 给一个文件系统，python的字典形式（面试官用的hashmap），里边的key有文件的类别（文件夹/文件）和大小，
文件夹类型里有一个list里边存了属于它的文件/文件夹，文件直接给出size，文件夹没有，现在随意给出一个文件/文件夹号，求size。

followup 说如果每次计算文件夹size都要重复所有的计算过程，比如文件夹1中包含文件夹2，但基于我写出来的代码，
如果要分别知道文件夹1和文件夹2的大小，要计算一遍1，又要计算一遍2，问有没有什么优化。

522. 给一个多叉树的root, 让删除这个树。dfs bfs 遍历挨个删秒出，time 是O(N), memory O(logN), 
followup是怎么O(1) memory,

523. 有一堆机器，一字排开，可以给左右两边的机器发消息，每个机器上有6个function, 给了 hasLeft(), hasRight(), sendLeft(msg), sendRight(msg), 
让你implement receiveLeft(msg), receiveRight(msg), 和main(), 然后在main里面利用这6个函数，让每个机器print出来整个network里有多少机器

524. 写一个Classifier class, 里面有三个function让你写，前两个简单，is_above_threshold(x, threshold), x >= threshold就返回1， 
不然就返回-1， has_error(label, should_be_label), 如果label == should_be_label, 那就是对的，反之就是有error，然后input是一个x (list) 和 y (list),
 让你写一个train(x, y), 返回threshold让他的error最少，举个例子，x=[1,2,3,4], y=[1, -1, 1, 1], 
train()出来的threshold 应该是1， 这样只有2是错的，error count是1。 让我先用brutal force做，很快写出来了，然后讨论怎么improve time complexity O(N)

525. 366 写完recursion写iteration

526. 写一个class，要求时间复杂度O(1) 实现 1. ack(int n), 可以不断ack已经收到的number;
2. 可以getH, 可以return出来第一个从1开始的连续ack的interval的右边界
比如ack(1), ack(4)， 此时getH，需要return 1
继续ack(2), 此时getH，需要return 2
继续ack(5), 此时getH，需要return 2
继续ack(3), 此时getH，需要return 5
Follow up 3.1：ack过的那些数，memory可能存不下， 怎么优化我的代码
Follow up 3.2：实现一个getUnack function，return目前没ack的东西
Follow up 3.3：假如1-9被ack了，10没有被ack了，但是如果11-110（共100个）被ack了，那么我们就说，放弃10，此时再getH这试需要return110

527. 实现一个英语西班牙语单词翻译机：1. addTranslation(English, hello, Spanish, hola)
2. getTranslation(Spanish, hola), return hello
Follow up: 实现一个多种语言单词翻译机（多种语言之间没有重复词汇，即hello只可能出现在英语里，不可能出现在其他语言里）:
addTranslation(English, hello, Spanish, hola)
addTranslation(Spanish, hola, French, bonjour)
getTranslation(English, hello, French) --> return bonjour


528. 给一个path string比如说“asdfghjkloiujkjhsgfrert” 再给a list of 世界上所有的 English words (有1000k左右)， 返回能被这个path cover的所有words. 一个word被path string cover的意思是 这个word是path的一部分但是不需要连续 
比如说给的这个例子里的path string就可以cover ["ghost" , "alert" ...] 其中"ghost" 是因为 "asdfghjkloiujkjhsgfrert"; "alert"是因为 “asdfghjkloiujkjhsgfrert”。

529. 给一个array, in place删掉里面所有的'a'， 第二问是 删掉里面所有的'a' 同时如果遇到一个'b'就把这个 'b'替换成 'bee' 都是要in place 做。

530. 给一个word和a list of strings，判断是否match。 match条件是word的每一个char 都存在于list的一个string里 而且顺序不能错. 
比如 word = "cat", list = ["cathy" "caught" "a" "cat" "ye!"] 返回True。
第二问是 如果word一个char连续mismatch了k个string 那就返回False。 (个recursive的方法 类似backtracking，
第一问有什么更简单的solution

531. 设计个数据结构，给一堆 ip 网址的pair 例如(1.2.3.4, "googlevideo.com")，要求能查找 某个ip 访问过的所有网址
如果每个访问有expiration time (1.2.3.4, "googlevideo.com"， 60) 表示60秒过期，要求查找返回的 网址是没过期的

532. 有一台机器不停的在记录 当前温度，
要求实现getMax 返回24小时内数据的最大温度

533. 设计个数据结构储存文件，要求能够根据id 返回文件夹或者文件的大小
root (id=1)
  dir (id=2)
   file1 (id=4): 3Mb
   file2 (id=5): 6Mb
  file3 (id=3):(1Mb)
  
534. Graph is stored in dictionary with keys as nodes and values as neighboring nodes. Guaranteed to be a ring, return the path either 
counterclockwise or clockwise following the ring until you get all nodes in the ring.
follow up is how to modify code to catch invalid inputs

535. ，实现一个Clock类的advance方法，从当前时间advance到目标时间且advance次数最少。提供的API是Advance 1hr 15mins 5mins 1min，用greedy可解
follow up是假设advance的API也是input，可能有任意多个API去advance任意时间，也可能有重复，这种情况greedy就不行了，我dp的方法

536. unique subtree，508的思路，就是key需要变成subtree的结构而不是sum，后来想到可以只写到每一个叶节点下面的两个null也是唯一的，说了思路但是没来得及证明为什么是一一对应

537. 1937 n^3的dp然后说可以简化到n^2

538. 输入: matrix (字母和.表示的空), words=["HELLO", "EGG", "HI"]
matrix 举例:
. . . . . . . .
. HELLO .
. . E . . . . .
. . G . . . HI
判断所有的字(横排和竖排)是否在words里面, 以及是否所有的字母都相连: True/False.

539. find bad commits，假设给定n个commit id(从0 到 n-1）和一个API worse_commit(commit_id1, commit_id2)。
这个API return True if commit_id1 导致performace regression，return False if the performance stays neutual。 
问如何找到所有的bad commit ids。follow up是，如果只有k（k << n) 个bad commits，time complexity是多少。

540. 实现一个Tree class。要求support any number of children，并且每个node 的 depth 不能超过一个给定的值（max_depth). 
要求实现一下methods：
insert(parent_id, node_id) -> 添加一个新的node作为parent_id 的child
raise exception if parent_id doesn't exist in the tree or node_id already exists
raise expcetion if the new depth of the node exceeds max_depth
move(sub_root_id, parent_id) -> 移动subtree 到新的parent下
raise exception if sub_root_id or parent_id doesn't exist.
raise exception if the move leads to a cycle
raise exception if the new depth of any node under sub_root exceeds max_depth
delete(node_id) -> 删除一个node
raise exception if node_id doesn't exist
find(node_id) -> 返回True如果node在tree里，否则False
所有这些method除了delete最好是O(max_depth)实现

541. 实现一个interface，支持两个function：
addOrReplace(index, number) -> 在index的位置存放 number，如果index已有数据则覆盖原来的值
findSmallestIndex(number) -> 返回存放number最小的index，如果number不存在则返回-1

542. 2115 follow up是判断环和invalid input

543. 给一个matrix，里面是红蓝两种颜色的方块，只flip（颜色红蓝换）最左上角那个方块，规则是，所以与其相邻的相同颜色的方块都翻转，
连锁反转，比如
[0, 0, 1, 0] 翻转一次得到 [1, 1, 1, 0]
[0, 0, 0, 1]             [1, 1, 1, 1]
问最少几次翻转可以让所有颜色统一

544. 涂篱笆，给一串intervals，每个interval是涂篱笆的范围，每次返回实际涂色的长度，比如[1, 5], [3, 7], 返回 4, 2，第一次涂色长度4，
第二次有重叠，只涂了[5, 7]

545. 课程表，不过给的是task以及每个task运行的时间和dependencies，tasks可以同时运行，问完成全部task最短多久，
比如A depends on B和C，B，C分别花费3和5单位时间, 所以A运行前要5单位，因为B,C可以同时运行

546. 504，不过底为3，直接用二进制的解法

547. 二维矩阵0是海水1是岛，
求打印岛的边界（可以把四个方向都是陆地的点flood掉）DFS秒了。follow up是在第一问的基础上求每个点到最近边界的距离，
317

548. 465

549. 给一个list of coordinates作为occupied，return每个coordinate最近的unoccupied的点，一样近的任选，order随意

550. 给一个list of Folder objects，return每个folder的absolute path。Folder object 有parent和name。

551. Design a class which implements following functions:

func insertOrReplace(_ item: Int, at index: Int)
func getMinIndex(of element: Int) -> Int

552. word compress， 给一个array 然后在遇到一个符号，比如 255 的时候开始back reference，距离是255 后一位， 长度是255 后两位，
 直接scan array 就好了 读到255 的同时 再check下接下来的2 位。 
然后follow up 就是 各种corner case， 为负数怎么办

553. 1610

554. matrix最大路径

555. 设计一个温度tracker，只保留24小时温度。需要加温度和查询最大问题

556. 给一个无向图，给一个wrong path among different citie，然后想办法用最少的change去update 这个wrong path里面不正确的city名字，
使得它valid。
可以理解这样的图
ACC - ABB - ABD
这几个city名字不一样，而且相连，然后给一个invalid path 是 ACC-ABD, 但这两个不是直接相连的，所以invalid。
为了找到一个valid path，可以把这个invalid path里面的ABD变成ABB（ACC-ABB)或者ACC变成ABB(ABB-ABD)，但第一个solution变动最少，所以取第一个变动之后的path
https://github.com/jamesben6688/coding/blob/main/dp/%E4%BF%AE%E6%94%B9%E5%9F%8E%E5%B8%82%E5%90%8D%E5%AD%97%E4%BD%BF%E5%BE%97%E8%B7%AF%E5%BE%84%E5%90%88%E6%B3%95.py

557. 屋留变了一下，给一个排过序的intervals和一个单独的interval，把第二个merge进去返回排过序的list

558. cord Tree
https://github.com/jamesben6688/coding/blob/main/tree/cord_tree.py

559. 有几个city,有分别的fun values, 然后也有一个各别的班机资料,可以知道从哪个城市到哪个城市有班机,不限定起点,
求走四个城市可以让fun Value最大.

560. 在tree上要陆续删除leaf, 1)第一小题是问, 如果删除leaf后, 某些node变成leaf,这些node要立刻成为下个删除的目标, 
2)第二小题是问, 这些node（刚变成leaf的）不能立刻成为删除的目标.

561. 77

562. 问一个网络上，一个节点可以对其相邻节点广播，广播完他就关机了，然后问是否从J点出发能够到K点？
非常典型的BFS题。follow-up是
假设有多个点（>=2）同时往一个节点广播，这个点就失效了。本质上是在BFS维护一个map<Node, 步数>，如果发现有这样的对存在了，
证明有另外一个点会向该点广播，直接返回零。
207。
映射到这道题的话，第一问就是假如有一门课J和一门课K，问是否能从课J上到课K？
第二问就是假如有两门前置课程指向同一门课，那么这么课就直接置为无效课，问是否能从课J上到课K？

563. 2034

564. 把一个bit array翻过来，比方说10110101 --> 10101101，这个bit array是按Byte array的方式给的，每个Byte是8个bits，

565. 打印多叉树的所有路径，写完dfs recursive后问怎么能减少memory usage，不知道怎么答，写了iterative的方法

566. 一个平面上有多个平行于x轴或者y轴的线段，问这些线段能构成的最大矩形
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/%E7%BA%BF%E6%AE%B5%E7%BB%84%E6%88%90%E7%9A%84%E6%9C%80%E5%A4%A7%E7%9F%A9%E5%BD%A2.py

567. 写一个list的push_front，remove nth node，insert nth node，其中的node是
class Node {int val, Node * next, int hashVal;}; 
hashVal是根据node后面所有node计算出来的，Hash(Node * nd)能算出这个val值，不用管这个Hash怎么实现的，

568. one user adding num to a stack in order: 1, 2, 3, ...n
Another person pops num from the stack at any time and prints the number out.
Given a list, determine if the list is valid.
Example: input[1,2,3,4,5] true
input [2,5,1,4,3] false

569. 一块空地和一个api，api中有getWidth(), getDepth(), stop(), nextTower()。
nextTower()会在图中空地位置随机生成一个楼（保证只有空地生成新楼），当左边界和有边界被连通就call stop()结束。
边nextTower()边bfs判断。

570. Suppose you have an input string s and a list of strings. You can delete a character in the string (one at a time) if the resulting string after deletion is in the given list of strings. Is it possible to turn s into a single character string (note that single character must be present in the list of strings)?
bfs/dfs+mem，但小哥一直问哪里可以优化

571. 流散留，输入形式是File，要求输出特定task的period，很强调细节，不停地提出用不同数据结构
（比如一开始用arr，要求新建一个Pair class），follow up：如果有很多嵌套task会有什么问题（stack过长），
如果内存有限无法使用stack的情况下有什么方法？可以无限次read file，然后定位到指定task数start和end，
数量对应则可知道start和end。

572. 1048
Follow up是问如果去掉某一个string以后chain的长度会有什么变化

573. 在一个grid里面有好多路由器，（每个路由器在一个坐标的位置）， 然后两个路由器相距10以内被视为相连，
然后路由器可以通过相连的路由器到达新的路由器，给两个路由器看是否能够相连， 蛮简单的graph， 
follow up 问如果只有最近的路由器被视为相连要怎么改，还有如果grid太大怎么改，

574. 是给两个数组，比如说[B, C, A, D]和[A, D, C, B]，后面的数组是这些字母的新order， 
问使用bubble sort的话需要最少多少步能够从第一个array变成第二个，同样建了给图。。。然后之前忘了bubble sort是啥。。。

575. 给一个friend的数组，一个食堂的数组，一些edge，最后问所有friend都能去到的最近的食堂

576. 给一个有向连接图表示不同service state 之间的转变方向，只有其中一个是healthy state。问给定途中的其中一个state， 
如何知道是否一定能self recover道healthy state。

577. 实现一个data structure，来满足每次enqueue entry 都只process10秒内没有出现过的entry

578 2128 给一个矩阵表示灯泡开关，每次操作都会flip一整排或者行，判断能否关掉所有灯

579. 347 你有一組聊天對話log，找出 username of top K word count
log 格式為 <username> saying
word 為連續的 a-z A-Z 0-9 字符
Ex.
<ABC> Hello~ my friend!
<XYZ> Hi ~~yo!!!!
<ABC> Are..you.. there?
<XYZ> I'm here~~~~
ABC 之 word count 為6 (Hello my friend, Are, you, there)
XYZ 之 word count 為 5 (Hi, yo, I, m, here)
假若 K 為1, 則 output為 ["ABC"]
Follow up:
如果今天有非常非常多不同的username
但我們需要找的K很小的時候
你會如何處理

580. 小数点相乘运算
input: an array of float, output: float number

581 input: interge of 2-d matrix, output: a maximun number of a path
问题是从0,0走到n-1,n-1,路径找小的那个数字，然后回传最大的数字，有点近似leetcode的path-with-maximum-minimum-value

582. 有12个size为1的tile stack，共有4种颜色，每种颜色的tile为3个
游戏规则是A、B两个player轮流merge stack
一次只能merge两个stack，merge的条件是（两个stack的顶部tile颜色相同）或（两个stack的高度相同）；
一次merge只能把一个stack整体堆到另一个stack上（不能中间插入）；可以merge任意两个stack，不需要它们相邻
如果轮到A或B其中一方时无法再merge stack，那另一方就获胜

583. 就是给几个x,y坐标。x,y坐标被占领了。 求最近的没被占领的坐标。
 给一组坐标 Points{ int x, int y}
List<Points> Input;
input.add(new Points(0,1));
input.add(new Points(1,0));
input.add(new Points(-1,0));
input.add(new Points(0,0));
input.add(new Points(0,-1));
这些点就是被在 xy图上被占的点。求 离他们最近没被占的点。
所以答案也是List<Points> res应该也有5个

584. 给用户和网址和时间的边，第一问是建图，第二问是有多少unique路径。

585. 写一个csv parser，后续问题是csv中的某个单元格可能包含“，”如何处理。
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/csv_parse.py

586. 盗贼[] 和战士[] 两个数组， 盗贼属性有名字(String)和坐标(row, col)，战士属性有朝向(char)和坐标(row, col)。
盗贼有两个属性，1， 潜行，盗贼看不见其他盗贼， 2， 战士会一直朝自己的朝向怒吼，如果战士朝着盗贼方向怒吼，盗贼就会显形。
要求返回显形的盗贼[], 显形的盗贼有朝向(char)和名字(String)两个属性。
需要考虑一行或一列中有两个战士，或者两个盗贼的情况。

587. 一个矩阵里面只有两种值，'是'和'否'，有的'是'有的'否'，你控制一个开关，这个开关可以翻转任一行或者任一列，
让'否'变'是'，让'是'变'否'，而且你可以使用任意次开关。
问，给你一个上述类型的矩阵，判断这个矩阵 能否通过你的骚操作，最后变成全是'是'。返回是或否。

588. 设计一个自动联想的类，包含自动联想方法，添加和删除库中字串的方法。要求根据首字母提示用户字库中已添加的所有字串，
没要求字典排序，但你可以问。

589. 给你树的数组，树可能存在这种情况，有些树的根节点是有些树的叶节点。要求你铺平所有树，输出成一个数组，
要求先输出叶节点，在输出相对根节点。

590. design a postfix expression calculator. For example, input: 1 5 +, output: 6.
follow up1: how do you handle invalid input cases.
follow up2: what if we want to handle variable assignments calculations. 
For example, input: a 2 =, b 3=, a b +; ouput is 5

591 design a class where you have a 2d array as a map to the city. 
given two APIs: 1) void buildABuilding(); randomly pick an empty space to build a building in the city 
2) boolean hasPathFromLeftToRight(); return true if there’s a path of connected buildings from the first 
column to the most right column. Implement a method to call the first API until the second API return true. 
follow up: how to optimize and calculate the shortest path

592. given a very large keyboard and limitation k as the Manhattan distance next key to reach. 
input: a random word output: return true if the given word is able to be typed with the keyboard.

593. 有n个m位的id，请问最少需要遮住其中多少位，才能让他们看上去相同
第一题的基础上，最少需要遮住其中多少位，才能只剩下2种

594. 一个电影院买票, 实现2个功能： search（）和 book( )

595. test engineer 面的， 给一个温度系统， 可以拿到logs, 这里面存了最近5天内的所有温度数据。
设计一个Algorithms， 拿到最高温度数据。

596. Test engineer ： give a stream data(***you don't known the length)
e..g "ahjsagsjj  bcgds  asbjbjkiuasuhiajsnasnjkjahshhsajjasnnsj……."
have an exist method : nextChar() ---> it only can get one char each time
give any string: e.g. "bcgds",
do 2 things:
return true/false if string exit in stream
find all existing position(return start index)

597. 有一个datastream, 不停收到到transaction price, 23.21， 44.67 这种数据。
建一个object， 两个function: insert(), getPercentile(percentile: float).
insert拿来 insert price to data stream,
getPercentile用来算percentile, 比如 getPercentile(0.75). return P75 price

bucket sort

598. merge interval ood 版本，2个function, insert interval, get(int) -> return if int is in the interval list

599. 设计一个 暴力解锁器， 假设有一个 锁，你可以通过 turn(idx)来旋转它的值，比如 turn(1)， 会把 0010 变成0020. 
然后写个程序走完所有的 可能性。

600. 346 followup，问说能不能找最大数，概念上就像 239 ，但是是要求像上题一样以“数具流”的形式
问了时间複杂度

601. 833

602. 有一个grid里面有blocker, 有一个机器人,给定一个位置, 这个机器人只能往右走,每走一步effort=1,
这个机器人也可以上下走(可以跳跃,例如越过blocker,可以去同一列的任何位置) 不管跳多远effort都是1. 
求抵达最后一列任意位置的最小effort

603. Google有很多campus 然后你的小伙伴在不同的campus, 中午约饭, 约到cafe, 找到最早能集合的时间的时间(所有的小伙伴都到了那个cafe). 
input: List<campus>, List<cafe>, List<int[]>edges(例如 postionA-PostionC)代表A到C之间有路, 假设每一次移动的时间都是=1min

604. 两个时间点之间最短的时间差 539

605. 有一堆product,每个product有个ID, 每个product他会有一堆offerID, 每个offerID对应的一个price
1. add Offer(pID, offerID, price)
2. remove Offer(offerID)
3. queryClosetPrice(productId, price) return offerID

606. One of the TTY command tools got updated, its input/output has changed
A: tool在一个chain里, how to make sure the TTY command is backward-compatible (A: use wrapper)
B: you got several call chains, a->b->c->f, d->c, e->b->c->g, create a structure to store these call chain, and if updated c, find which tool need to be noticed to update

607. 150

608. 56 1254

609. 给一大堆unsorted时间点，每个时间都有人进进出出求最多人数，follow up就是某个时间点大量发生
2128

610. 建一个MyIter class。假设已经建好了trie(ABC → “he”, DE → “llo”), 。trie的leaf是一个string。MyIter class的constructor 
input是一个javaioreader和一个已经建好的Node root
Answer:
弄一个buildStr method，给你一个ABCDE这种String，返回在tire里面的leaf的string的concandinate → “Hello”
Iter class还要写出hasNext和next method。这里可以把之前建好的string在class里面存下来，然后用一个index去做。
follow up：因为给的Node的children 是个node array，如果换成hashmap会怎么样
follow up：如果换成换hashMap的down side是什么
follow up：在memory层面还能如何优化？

612. A function which takes text and a width (int) and returns the number of lines that the text would take on the page.
Example:
text = "asdf asdf asdf asdf asdf asdf"
width = 7
answer: 6
Example:
text = "asdf asdf asdf asdf asdf asdf"
width = 8
answer: 6
Example:
text = "abcdabcdaabcdabcda \n\t   asdf asdf(1) asdf asdf(1) asdf(1)"
width = 9
answer: 5
text = "asdf asdf asdff asdf asdf asdf"
width = 14
asdf asdf
asd   asdsadsd
asdf asdf
text = "a a a a  a a a a a a a a"
width = 16
answer = 2
a a a a  a a
a a a a a a
text = "a    a  a a"
width = 12
s = s.trim();
split("\\s+")
After split
for each single string, we need to use it and width to get how many lines it take

Follow up: Assume Part 1 getLines works perfectly.
Write a new function:
int getColumnTextSplit(String s, int width, int col);
if width = 10, col = 5
then we have two columns of width 5
width = 10, col = 2
two columns, width 2 and 8
returns the split point in s
text = "asdf1 asdf2 asdf3 asdf4 asdf5 asdf6"
width = 12
col = 6
asdf1 | asdf4
asdf2 | asdf5
asdf3 | asdf6
asdf1 | asdf2
| asdf3
| asdf4
| asdf5
| asdf6


613. secret & guess 有点像 蠡口的二舅舅
secret：CHALK
guess: AGBLC
output:YRRGY
就是 如果字符存在且位置正确，G；字符存在但是位置不对，Y；否则 R
（a）secret 每个字符是unique，guess 也没有重复字符
（b）secret 每个字符是unique，guess 有重复字符 ， 比如说 guess=“AGAIN”, output="RRGRR"
（c）secret 有重复，guess 有重复字符，我用了dictionary 记录count
（d）有一系列 guess 输入，让你比较每次的guess 是否有比上一次的guess 更好，没有implementation

614. filesystem, 也是个树结构，多叉树, 有dir, 有file, 然后file 有对应的filesize, 让你计算这个目录下的filesize 总和
（a）DFS 写了一个
（b）某些目录被多次访问，如何提高计算效率。用一个dict 记录
（c）BFS 又写了一个
（d）如果有cycle 怎么办，变成一个图的问题，用一个visited set 记录已经访问的节点

615. 实现一个class，在xy平面上，一开始没有点，不断add和remove点，点用坐标(x,y)表示，每一步return一个最小box把所有的点框住，box平行于x/y轴

616. 一个class，一开始为空，有三个method，setManager(M, E), M是E的direct manager，setPeers(E1, E2), E1和E2是peers，E1的direct manager不是E2的，queryManager(MM, E)，
问MM是否是E的manager，可以是很多层的manager。这三个method被call的顺序是随机的。
我的解法：dag表示manager-employee关系，udg表示peers关系，另外一个e2m字典，记录直接mgr
setPeers（E1，E2），E1的direct manager是E2的，如果E1是C的manager，E2不是C的manager

617. top K items变种 对应的item是一种特别的class, 增加了另一个维度, 限制top k每一类不能超过m. 
follow-up是用四种解法写这道题 同时分析复杂度bq: 各种假如你是org的leader, 你要干什么 有什么conflict .etc

618. 问top n user的名字和wordCnt。楼主刚开始走了弯路用了sorting，后来面试官问有没有更快的方法，改成了Priority Queue

619. fun city question 给一个city list，每一个list有一个fun value，还有一个list是双向的机票, 比如 A <=> B 代表可以从A飞到B也可以从B飞到A，找一条unique path，由 4 个distint cities组成，使得fun value 最大，输出这个最大值
City fun value
A. 1000
B. 2000
C. 3000
D. 4000
E. 5000
Tickets: A <=> B, C <=> D, B <=> C, A <=> E, E <=> B
output E => B => C => D 所以是14000
做法的话大概是固定中间的两个city然后找一头一尾


620. 1011、410

621. input是好多log string ex："1+3+5=9",其中1，3，5是三台机器的运行结果，9是expected结果总和，如果出现"1+3+4=9"那就是有一台了（这里假设只有一台机器出错），
问怎么查有没有机器出错，如何查是哪台机器出错，然后思路就是把这个string两部分parse一下看前面的和是不是等于后面的数

622. 一个2D array，里面0是空地，1是墙，问从左上到右下，最多拆一堵墙，能否到达
Follow up是不问你能不能到了，问你最少拆几堵墙能到

623. Job Scheduler, 拓扑排序解决， follow up： 如果跑在实际场景中会遇到什么corner case

624. Friend Host,Union Find 解决， follow up: 怎么优化 time complexity

625. 2034

626. 给几个cd命令，返回正确的directory
eg:  cd a/b/c
     cd a/e/f
     cd a/b/h  
	 cd x/y
return a
       - b
         - c
         - h
       - e
         - f
      x
      - y
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/cd%E5%91%BD%E4%BB%A4%E8%BE%93%E5%87%BA%E5%AD%97%E7%AC%A6%E4%B8%B2.py	  
	  
627. 类似phonetool的一个公司结构，每一个人都有read email time, reporter(下属的员工)，
问：当一个leader（root node）发一封邮件出去（只发给自己的reporter，在由reporter给再下一级的人转发，以此类推），需要多少时间全公司的人才能都读到邮件

628. stream一辆车在每一秒的速度, eg: 第一秒60mile/h 第二秒65mile/h，问： 在每60秒的window里（0-60，1-61，2-62，3-63….）最低的车速是多少

629. 366 要求从最底层子节点开始remove整个tree。 
follow up： 1.移除顺序变为移除了某个叶子的子节点后立即移除该节点
2.如果给定了移除顺序 判断是否valid （valid定义是必须先移除该所有子节点再移除母节点）

630：269变种 比原题简单 给定字母顺序判断string valid与否。 follow up：分布式，多个机器怎么做这道题，机器之间transfer什么变量，如果字符串长度少于机器数量怎么办，runtime
631. Manager chain，给一些 {index， 员工邮箱，经理邮箱} 然后输入一个员工输出manage chain，follow up就是判断环

632. 从巨简单的一维presum [1,2,3,4,5] => [1,3,6,10,15]
到二维presum [1,1,1] =>[1,2,3]
        [1,1,1]   [2,4,6]
        [1,1,1]   [3,6,9]
到实现1.update其中某坐标的值 2.get2dSum返回加和后的某坐标的值
讨论怎么节省时间复杂度，怎么保证concurrency一致性



633. 给一个n叉树，返回每条从根到叶的最大值
输入是root
follow up：如果输入是所有的edge，怎么改
可以改成tree的结构，也可以用adj list

634. 给一很多组tuple {A, B, TEAMMATE} （A和B是队友）, {B, C, MANAGER} （B是C的老板） 然后给{A, B, Query} 
问A是不是B的manager。用了Union Find变体，小哥说以前听人说过用Union Find但是没人用过很吃惊。
Follow Up是 给一堆 Query 和 中途老板switch换来换去怎么搞。

635 国人小哥 人很好 问题是给一堆DISK，有些DISK有child DISK。要删除DISK必须得先删CHILD DISK，给一个删除的顺序。
Follow是分批怎么解决，在BFS里面用一个for loop把当前的disk一次性都跑完再跑下一个level的就行。

636. 国人小哥 人不错 问题是给一个list，求问一个范围内最大的数字。刚开始惊讶住了，for loop做了一下这么简单的吗，
follow up是数据很长很长，query范围的次数也很多次。
问怎么办，我就用了segment tree。写完了表示可以。

637. 国人小哥 人不错 问题是 给一个string 比如 a-(b+c+b) 输出 a-2b-c。聊了半天给了口述了两个解法。
用for loop走recursion和用stack。小哥内心的标准答案是stack。但是我用了for loop。sample run后表示可以，

638. 有四个工作，分配个两个worker，每个workēr对应每个task的cost记录在数组中.求将工作平均分配，最小的cost是多少。
https://github.com/jamesben6688/coding/blob/main/dp/%E5%B9%B3%E5%9D%87%E5%88%86%E9%85%8D%E5%B7%A5%E4%BD%9C%E7%9A%84%E6%9C%80%E5%B0%8F%E6%97%B6%E9%97%B4.py

639. 给一个2d矩阵，0和1分别代表水和地，求最大地的面积。
第二问：如果一个水被周围8个地环着，那么这个水就变成湖了，湖也算做一块地的面积，求最大地的面积。

640. 140

641. 各种sort和算法的time complexity, 矩阵相乘的时候

642. design一个类似
excel sheet可以compute function的功能。比如说A1可以输入MAX(B1, B2, B3),然后B1可能是另一个func，
比如 AVG(C1, C2) etc。设计这个，写model和这个function的impl。

643. 比较简单，给一付牌，不是传统的牌，但是类似的是有suit和rank，输入是一个list的string，类似S1R3，意思是suit 1， rank 3，
实现一个输出最大flush的func。

644. 也比较简单，56 和 921

645. 一个mapping F, 对于非负整数 x1 > x2, 有F(x1)>F(x2). 给定F 和 y，找到整数x使得|F(x) - y| 最小。
follow up是 非负整数扩展到所有整数。F 没有具体形式，直接F表示

646. 微波炉 10%误差

647. 给定两个list [‘ac’, ‘ed’, ‘cc’], [‘cba’, ‘def’, ‘ccc’] 求第二个list中满足以下条件的数量：能通过第一个list的string加上任意字符
后shuffle得到。

648. Given a binary tree, return the node to root map in any orderGaps to clarify: 
the data structure of tree node, whether the value of each node is unique.
Ex:
      5
      /\
     3  2
     /\/\
   1 4 6 8
Return {5 : [5], 3 : [3, 5], 2 : [2, 5], 1 : [1, 3, 5], 4 : [4, 3, 5], 6 : [6, 2, 5], 8: [8, 2, 5]}
Follow up: what if it’s an n-ary tree?

649. Given an array of integers representing the error rate (0 - 100) during that hour, a certain time and a threshold, 
determine whether or not the weighted error rate that includes the given time exceeds the threshold.
The weighted error rate is calculated by multiplying the minimum error rate within the hour duration by the duration itself.
Ex:
Error rates = [5, 10, 15, 20, 70, 70, 65, 10, 10], threshold = 16, time = 3
Return false
Explain: Starting from time 3 (error rate 20), we can’t find the time frame that’s under the threshold. 
The minimum weighted error rate is 5 * 3 = 15.
Ex2:
Error rates = [5, 5, 5, 20, 70, 70, 65, 10, 10], threshold = 15, time = 3
Return true
Explain: start from time 3 (error rate 20), if we choose the error rate before it, 5, the result becomes 5 * 2 
since we want to include the given time. This gives us 10 which is below the threshold.

650 Design a data structure that represents a hand of cards and implement a method to return the biggest flush straight.

651 string replacement

652. 给一堆log， log有requestID， timestamp，和type， type有start OR end。 log按照时间顺序排序。还有一个time-out时间。
如果发现一个request没有在timeout内收到response， flag it。

653. 有一个third party的API 问如何integrate到自己的service里。感觉他是想问cache的相关问题。说要加个cache之后，
让写简单的代码如何call这个API并且check CACHE。

654. 给了一个图，途中有一堆线段，问有多少个正方形。没有给input, . 需要讨论。最后面试官说input是一堆node就是线段的焦点， 
每个node有相应四个邻居的reference。 应该就是backtracking的问题。


655. two pointer 给一个 array 和一个index ， 然后对这个index 两边进行two pointer

656. 241 就是给你一个string 和一个数，然后对string Add Parentheses问能不能得到 这个数
eg： String: 2+2 *3 数是12 return yes as （2+2）*3 = 12

657. 150- 一个简单的stack， 很多followup 比如 invalid input 然后是如何scale

658. 1293

659. 给一个matrix，里面每一个element都是一个字母，完成isInMatrix(matrix, word) function。
follow up是给1.isWord(str) -> bool 和2.isWordPrefix(str) -> bool, 完成findAllWords(matrix) function。

660. 如果正确的词是"system"，你猜的是"absent"，则返回"RRGYRY" 
(R：没有这个字母, G：有这个字母且位置正确，Y：有这个字母但位置错误)。第二问给定第一问的function(guessWord(word) -> result)
和一个巨大的包含所有六字词的wordDictionary，implement一个function，在6次之内猜出结果。

661. 两个intervals有没有intersection，n个intervals有没有intersection，n个intervals共有几个intersection

662. 给黄绿两种颜色的布，给定黄色布的位置，比如[1,3], [5,8], [9,15]，剩下所有位置都可以认为是绿色的布。input：黄色布的位置list，
一块绿色布的长度。问：把绿色布放到任意位置，最多能剩多少黄色布。

663. 匹配足球比赛，给定1.国家和足球队的dict（e.g. {'Italy': [c1, c2], 'Spain': [c3], 'France': [c4, c5, c6]) 2. 
之前踢过比赛的队[c3, c6], [c4, c2], [c5, c1]，要求匹配下一轮的n场比赛（任意一种组合），要求同一个国家的不能一起比，
之前踢过比赛的队也不能一起比。

664. 767不过需要空两个

665. 写个func input是list of events 返回list of coordinators for 
rendering those events in calendar.
具体input和output什么结构需要自己定义 我这么写的
type Event struct {
  StartTime time.Time
  EndTiem time.Time
}
type Coordinator strut {
  Top int
  Left int
  Height int
  Width int
}
func ScheduleEvent(events []Event) []Coordinator {
  // sort events by event.StartTime in ascending order
  ....
 // loop events slice to calculate coordinator
  ....
}
需要注意的就是如果两个events有overlap 每个event的width就是max width / number of overlapped events

666. Historical log,会不断更新某个string的值，然后问你相应时间值， 要求写test

667. 杨辉三角，二维数组和滚动数组解法

668. 大数据浮点数乘法， （1） 加法（2） 乘法

669. 逆波兰， 要求处理各种exception

670. 给N 张扑克牌，不同的suit 和rank组成一个输入数组， 返回最大的一组同一suit中5张连续的牌， 
follow up，如果suit更多怎么办。

671. Tree （不是binary）， 树叶上有value， 树枝结点没有value， 但有所有子叶value 的range。
叶的value是sorted所以不同path 的branch 
没有overlap。
给一个value，返回从root开始的path。

672. There are N kinds of gems in a mine.
Each gem has a weight of 1.
Their count and price (per gem) is given as follows:
c[0], c[1], .... c[N-1]
p[0], p[1], .... p[N-1]

You have a knapsack of weight W.
Maximize the total price of gems that you can keep in the knapsack.

Solution: Simple Greedy approach. Sort the gems w.r.t. price from highest to lowest and keep them in the knapsack until it is full.

Follow-up:

If c and p are given in the form of running queries, maximize the total price after each query.

673. 给一个tree，删除里面的leaf node，输出删除的顺序
  follow up是，如果一个node没有任何leaf node，这个node就必须马上删除，no matter还有没有其他leaf node
  
674. 给一个string，类似aaabbc的形式，就是相同的char都放在一起，不会有aba这种形式的，输出出现次数最多的那个char
  用tow pointer
 follow up是怎么优化space和time complexity
 
675. 写两个function，第一个function是插入一段interval和相应的一个operator name，判断能不能插入，
可以的话分配一个不重复的id并且返回这个id，第二个function是用id找一个operator，如果存在这个id，就把相应interval删除，
如果存在这个interval，删除成功，返回true，如果不存在，返回false

676. 给一个integer array，找到一个subsequence，在这个subsequence里，后一个element总比前一个大1，输出它的长度
  follow up是，如果要求的是在subsequence里，后一个element比前一个大的范围是1 ~ N，给出最长的subsequence

677. 150，follow up是如何判断input valid

678. Nary-tree的先序遍历变体并打印。一开始说回溯做但面试官表示用不着太麻烦了用递归遍历...总之思路想出来了但代码写不完，
后面问时间复杂度

679. 200 第一部分给包含0、1的2d数组找boudnary pixel
(满足两个条件，本身是1且上下左右邻居至少一个是0)，暴力法双层loop解决。
第二部分找给的2D数组每个点到boundary pixel距离，

680. T[N] , 表示N 个服务员和 他们服务一个人的时间（每个服务员只能同时服务一个顾客）。
店刚开门，前面有M 个人在等着，这个时候来一个新顾客， 问他要等多长时间

681. 636， 但是不太一样，要格式化打印出每一步正在运行的函数。 当一个函数A start之后，如果没结束，
再start另一个函数B，那么B就是A的子函数。如果再来个C，D，E类似的，这时候要打印：
A(运行时间)
B(运行时间)
  C(运行时间)
D(运行时间)
E(运行时间)
要用空格排好
682. 就是给一堆坐标点，找里面面积最大的一条边平行于X轴的平行四边形。

683. 给两个树，输出diff。 Follow up 修改第一个树变成第二个树

684. 410

685. 1167

686. 1143+44

687. 460

688. 给出一些时间戳让找相邻最近的两个时间，要求constant，因为一天内时间戳数量固定

689. 给一个每个人的进出时间输出每段时间有哪些人
A，1，5
B，2，4
输出
1，2，A
2，4，AB
4，5，B

690. 是给一串String和dictionary，String是一句话，里面有错的词，正确的词在dictionary里，让你correct
input: Todxy is a god day.
dictionary: today, good
output: Today is a good day
先开始说dictionary是map有一一对应，之后问没有对应只有正确的单词的话怎么办，这里用edit distance

691. 2096，给树里的两个值让你找到从开始到结束的走法

692. Graph 问题，找cost最小的path

693. 跟merge intervals 相似，不过他要我用 o(n) 的时间写出来

694. find all bad versions.
给定input数组，相邻的version只能一样bad，或者右侧的version比左侧的version更bad。同时给定一个helper function，
input两个不同的version number ，假定为v1，v2，output是两个version时候一样bad，或者v2比v1更bad（假定v1 < v2）。

695. 给一个二叉树，每个节点都有一个value值，求二叉树中相邻的K个节点所有value可以构成的maximum sum。

696. 1153. 大概是给定两个长度一致的字符串，找出一个one to one mapping可以把第一个字符串转成第二个字符串。

697. matrix上各个点，可以是墙（*）玩家（p）火焰（f）终点（d）或者空地（.），玩家只可以在空地上移动，
不可以移动到墙或者火焰上，火焰会每轮向四周的空地上蔓延，问能不能到达终点

698. 1244

699. 715，需要update range但是不需要delete

700. 560 然后拓展到二维，也就是1074

701. Input 是一个csv文件，output是计算出他们的median number。
最后会问你edge caes。

702. 已知有一个类， 有两个function可以调用， hasNext(), 和 getNext() 分别输出是否有下一个， 和得到下一个char.
假设已知这个类的两个实例， it1，和it2， 让我们来比较两个类的大小。
例子： it1 = 34.12345789
    it2 = 34.12346
如果 it1 < it2: return 1
或者 it1 == it2: return 0
或者 it1 > it2: return -1

703. There is a ball on the nth stairs, and it wants to get to the ground(level 0).
During odd time, you can jump down 1, 2 stairs.During even time, you can jump down 2, 3 stairs.
Return the number of ways you can get to ground.

704.253变体。不让返回一个需要几间room，而是返回这些room同时开会的那个时间段。如果有好几个时间段满足 
返回最长的那个

705. string substitution
Input:
Text = "num foo"
Replacement (4,"foo","bar")
Replacement (0,"num","String")
Output:
"String bar"

按照replacement idx进行排序后递推replace, 

706. Design a system to keep track of all temperatures in the past 24 hours, 
you need to implement two methods below
int getMaxTemperature() return the maximum temperatures in the past 24 hours
void storeTemperature(int temperature) record the temperature

使用monotonic stack 和priority queue两种方法解决, follow up "What is space benefits using priority queue or monotonic queue ?"

707. 849，follow up是要安排n个人

708. 给了一个matrix int[][], value代表村庄的海拔，水只能从高处流到低处，给定村庄a和b，
请问在哪里修建水井，水井的海拔最高 对a和b分别作bfs/dfs 看看能到哪些点，都能到的点里面取最高的。
follow up path min cost 用dijkstra
https://github.com/jamesben6688/coding/blob/main/dijstra/%E6%9D%91%E5%BA%84%E6%8C%96%E4%BA%95.py

709. 366 794

710. 在一个平面上给起点，终点，一堆点的排列和规定距离，如果两点（a,b) 在规定的距离内就可以从a跳到b，
问从起点开始，经过任何一个所给的点，能不能到达终点

711. 散令令变种，我一开头就提议用空间 O(n)的dp, 不要用dp改用暴力解

712. 200 253 google运行网络服务器

713. 636 追问 必须逐层去掉叶节点

714. 设计api，追踪过去固定时间内数据流的最大值

715. 给一个树，也可以说是图，每次删除这个图上的一个叶子节点，并把跟这个叶子节点相连的父节点放到一个数组中去，
直到这个图只剩下两个节点，就不再删除。问题是给这个数组，反向推导出图的结构。
prufer
https://github.com/jamesben6688/coding/blob/main/graph/prufer%20Code%E7%BC%96%E7%A0%81.py
构建prufer序列： https://github.com/jamesben6688/coding/blob/main/graph/%E6%9E%84%E5%BB%BAprufer%E5%BA%8F%E5%88%97.py

310 的反向版本

716. 1554 给一个数组，每个元素是等长的单词，问这个数组中，是否存在两个单词，其中一个可以由另外一个替换一个字母得到。数组内可以有重复的单词。

717. 317 没有obstacle。直接用BFS写了，时间复杂度，还聊了DFS跟BFS的区别，简单分析DFS的表现。
Follow up是如果这个grid很大memory放不下怎么办， divide and conquer或者map reduce

718. 一堆timestamp，精确到分钟，比如[23:11], [10:55]...
让找出两个时间最小差值。

719. 一条直线表示路，路上有很多加油站，每个加油站的油价不一样。给你一辆车，起点的时候油箱满的，
问到终点的最低cost是多少，邮箱还有大小限制，引入了tank size，

720. add a range, such as [1, 3], [4, 5] [2, 6].
query a point is in the range. for example, 0 is not in, but 2 is in based on the 3 ranges above.
https://leetcode.com/problems/binary-tree-coloring-game/description/
https://leetcode.com/problems/interleaving-string/description/

721. 给了一个binary tree structure里面存有一串string, tree由两种node组成：内部节点和末梢节点。末梢节点上有字符串的value和长度,
而非末梢节点（内部节点）只有它子节点的字符串总和长度。
Q1让定义这两种节点，Q2给定一个index n, 让写一个function来输出字符串的第n个字符


722. 一个alphabet set，输出所有用这个set可以组成的string的个数，且拥有如下的性质：总长度L,同时最长的不超过k个重复字母

723. 一个alphabet set，输出所有用这个set可以组成的string的个数，且拥有如下的性质：总长度L,同时最长的不超过k个重复字母

724. 需要自定义的classes,一个是单一的TreeNode，另一个是Tree,让完成一系列functions,
 包括搭建Tree的function(def initializeTree()), 在Tree里面给定parent node让产生一个新
 TreeNode的function( def createNode(parent):), 随机选择一个node（getRandomNode()), 
 还有随机选择一个末梢节点（getRandomLeafNode())
 https://github.com/jamesben6688/coding/blob/main/tree/%E8%B7%9F%E8%B8%AA%E6%A0%91%E7%9A%84%E6%89%80%E6%9C%89%E8%8A%82%E7%82%B9%E5%92%8C%E5%8F%B6%E5%AD%90%E8%8A%82%E7%82%B9.py
 
725. 十进制的数改成一个六进制的表达

726. 57 + followup 类似 253，后半部分open ended test design question，怎么测试gmail

727. 394

728. 二叉搜索树, 让你实现两个function
1. 最左边的节点。
2. next node， 就是下个比你大的节点。

729. 计算器 + 2128/2428? 而已儿吧

730, 假设queue只有isEmpty 和poll两个method, 现在有list of queue，怎么call 最少来找出 1. 最小size 2. 最小queue 数字的sum

731，定义一个纸牌游戏，数值相同的可以叠起来，或者高度相同的也可以叠起来；
两个人同时采取最佳策略，问给定一个初始纸牌序列，先手能否获胜
给出了基础解法之后接着问如何优化，打出来每个纸牌序列转成string，
记录cache result,

732. 一个二维矩阵，从左上到右下走的所有路径中最大值的最小值，每次方向只能向右或者向下走，
  接着拓展可以上下左右四个方向走，从dp改成pq就行了
  第三问给定一个string的iterator，实现新的iterator,比如s='aaabbbccddd'
 next: [a, 3]
 next: [b, 3]
 next: [c, 2]
 next: [d, 3]

733. GeoHash，给定两个数据结构Node表示GeoHash的一个位置，他可以有四个children，表示他分成四份，或者他只有一个Point表示一个饭店
 Node 和 Point这两个类都有getDistance方法，来计算他们到某一个Point的距离，对于Node 就是表示Point到他的四条边的最短距离
 需要实现的是给定GeoHash的root，和一个Point表示一个人当前的位置，如何返回下一个离他最近的饭店。lc没有类似的题目，
 Node可以看成是一个QuadTree之类的
 https://github.com/jamesben6688/coding/blob/main/tree/%E5%9C%B0%E7%90%86%E4%BD%8D%E7%BD%AEgeo_hash%E6%A0%91.py
 
734. 机器人扫房间 489; 问题：房间大的时候程序哪里会最先出问题，怎么解决？

735. 号塔只能接收到10m距离内的别的信号塔的信息，给一堆信号塔的坐标，一个起点和一个终点信号塔，
输出是否信息能从起点传到终点；follow up 1：只能传送给10m以内离它最近的信号塔的信息；
follow up 2：假设一个信号塔接收到2个信息，第二个会cancel掉第一个（双数就不发送)

736.  给一个最多带一个*的字符串格式，比如a*b, 再给一个字符串数组，比如["ab", "acdb", "ba"]，
输出数组里面所以符合格式的字符。（["ab", "acdb"]是符合"a*b"的）

737. merge interval，从最简单的merge两个interval开始，
follow up到很多个interval，再follow up
到最后生成一个两两interval之间的Adjacency matrix，[i][j] - 1 (代表两个interval直接或者间接相连)，- 
0（代表两个interval不直接也不间接相连）

738. 给一堆图和一张画布，图有些pixel透明有些不透明，可以叠起来覆盖底下的，问最后叠完之后是什么样的。

739. 给你n个球员，每个球员有编号和weight。然后组队比赛，
两支队伍组成一个比赛，每个队k人，要求公平竞争，即队里的球员weight要么相同，要么相近。最后要求返回n/（k*2）个比赛。
每个队员只需要存在一个队伍里就可以了，不需要排列组合。
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/%E7%90%83%E5%91%98%E6%AF%94%E8%B5%9B.py

740. 判断一串数组里存不存在某个数，它比其他数都大k。
第二题是2d数组里每个格子有weight，
从左上走到右下的最大和

741. robot 从0,0 走到n-1,n-1， 碰到墙有一次复活机会，返回true or false能不能到达目的

742. 1610.

743.假设你有一个phonenumber的存储
实现
1.number insert to db
2.is number taken
3.give a new number
这个phonenumber会很大的情况下会怎么设计用什么来存储以及实现
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/%E7%94%B5%E8%AF%9D%E5%8F%B7%E7%A0%81%E5%AD%98%E5%82%A8.py

744. 有n个数,需要比几次才能选出最大值,n-1,然后怎么证明

745. 国人小哥,给个sorting array,返回平衡二叉树.sorting list?.follow-up,sorting list 
复杂度降到O(n)..

746.扫雷游戏,从随机生成雷开始写.最后又做了一个linkedlist 简单排序, 给一个target,小的在前,大的在后.

747 随机播放音乐
followup 最坏和平均时间复杂度 如何优化空间

748. basic calculator变形

749. 数字1-9 组成一个组有2种条件 一个是3个相同数字 一个是3个连续数字； 题目：第一题给3张牌 能否组成一个组 
第二题有12张牌 但是不是sorted 能否组成4个组
Follow up 时间复杂度

750. 给一个数组 然后query是一个index的range 比如[2,4) 返回这个range里最大的数 如果query多次 
如何precompute来保证effective query

751. 不难， 给你一个string，找里面distinct char 最长的substring，返回长度。例如：input： “ABCDAWERTY”, 
后面问了follow up，如果这个input 特别长

752. 给你一个string list， 里面每个元素都是一个timestamp，格式是： “hh：mm”， 例如： ["23:23","11:13","21:01","01:03"], 

753. 818

754. Imagine an office which issues license plates, in the following format and order:
00000
00001
...
99999
0000A
0001A
...
9999Z
000AA
...
ZZZZZ
Write code that returns the Nth license plate in this sequence, given N as the input.

755. Design a class organization
setManager(manager, reportee) => 将reportee的直属上司设为manager
setPeer(personA, personB) => 把personA和personB设为peer，代表着这两人将有相同的上司
reportsTo(personA, personB) => 给定两个人，返回personB是否是personA的上司，注意不一定是直属上司
Example:
setManager(A, B)
setPeer(E, D)
setManager(B, D)
reportsTo(E, A) => true

756. Given a binary image, with pixel value equal to 0 (background) or 1 (foreground), find the boundary pixels.
A pixel is a boundary pixel if
1) It's foreground (pixel value = 1) AND
2) It has at least 1 background pixel among its 4 neighbors (up, bottom, left, right)
 If the pixel doesn't have 4 neighbors(on image edge), it is a boundary pixel.
Q2: Compute the distance transform (DT) of this binary image.
For each pixel, the DT is equal to the distance to its nearest boundary pixel.
Here the distance is defined as |row1-row2| + |col1-col2| (Manhattan distance)

757. 286

758.  1293 用的三维visited数组，
follow-up迪杰斯特拉 那种dp做法，
dfs怎么实现

759. 給一個 2D array 裡面好幾個 string
ex [['i', 'like','meat'], ['i', 'like','food'], ['i', 'am','human']]
prediction function to predict the next words based on most frequent showing bigram

760. Given: Timestamp (ms) url status duration (ms)
		0001		   xx    200  150
		0002   		   yy    500  1
		0005   		   zz    200  20
		1000   		   ww    200  10
Ask: Finding the number of concurrent request at each timestamp
Sample result:
0001 -> 1
0002 -> 2
0005 -> 2
1000 -> 1

761. Replace substitution in a string (Directed Graph)
Input 1:
FIRSTNAME --> Bill
LASTNAME --> Gates
FULLNAME --> %FIRSTNAME% %LASTNAME%
Output1: This is %FULLNAME% --> This is Bill Gates
Input 2: invalid input because there is a cycle
ONE --> %TWO%
TWO --> %THREE%
THREE --> %ONE%

762. 200

763. Max profit for growing crops，给定几种庄稼的种类，grow time，profit；给定一块地，一次只能种一种庄稼，
给定一个时长，问如何最大化收益。
时长，比如总共有一年或者一个月的期限，在这个期限的最后你能拿到的最大利益，
对的每种庄稼只给出来growtime，比如10天，startTime和endTime是你要optimize的。
https://github.com/jamesben6688/coding/blob/main/dp/%E7%A7%8D%E5%BA%84%E7%A8%BC.py

764. 一个迷宫，从左上走到右下，最多可以消除一个障碍物问能否抵达。 1293，bfs加记忆化搜索

765. file system，列出想到的方法和优缺点。
hashmap之后直接开问follow up，
顺着聊完就继续实现了hashmap的解法。提出了几个follow up

766. 给一个list of time（格式是HH:MM），找到任意两个时间之间的最小值。

767. 说给定一个bitmap形式存储的黑白图像，以及图像的bit宽，左右翻转图像。
最后写了个简单的ByteArray形式的图像，一个pixel就是一个byte，存储方式是从左上到右下，方法是：byte[] 
FlipMonochromeBitmapHorizontally(byte[] imageData, int widthInPixels) {}。
一个MxN pixel的图像存成一个Byte Array里，然后知道图片宽是N pixels，
所以实质就是把Array分成M段，每段长度为N，然后对每一个N长段做一个左右的flip。

768. 233

769. given unigrams string list [new, york, hampshire, french], and bigrams string list [new york, new hampshire], 
find non match unigrams in bigrams, this example we return [french]. follow up, if no space in bigrams e.g. 
[newyork, newhampshire], I think about trie, but could not talk through clearly.

770. find point in list of intervals, if multiple queries, can we define a more generic function find<T,R>(T[] list, R point)

771. given list of strs of anagrams, find how many group we can form, a group is a list of words which one of 
them is k difference from the other.

772. given string "%a%", % is special char for mapping and a hashmap {a-abc}, return substituted string "abc", 
many corner cases, and nested situations, need a lot of communication and scoping.

773. 给了一个n x n 的matrix with unique Integer,
求sequence of swap得出一个sorted matrix.
e.g:
[[1,3,2],     [[1,2,3],
[4,5,9],  =>   [4,5,6],
[7,8,6]]       [7,8,9]]
用上面的例子就是 [[2,3],[6,9]]
每一次只能和相邻的数字swap.

774. 2007 要考虑 negative integers，注意 0 会是 special case

775. 给你一个 list，然后有 real time query 进来，每个 query 都是一个 index
range [i, j] （闭区间），返回 list 在这个 index range 里面最小的值。Brute force 是
每次都取出 list 里面的这个范围然后取最小值，这样每个 query 的平均用时会是 O(n)，
所以你的 solution 要 average 好于 brute force 解法

776. implement median pooling given an input image (matrix). followup
是如果 window 是按照 stepsize 滑动的，怎么改之前的 solution 实现

777. 1110

778. LFU 变体

779. 给一个address book [(street number, street name, city name, state name), ...], 
然后再给一个query来找是否在adress book中出现，query中可能有NULL。如果能吧非NULL的query里的内容全都match到则返回true。用字典树做。

780. 从数组中找出k个数，使得k个数组成的数最大，这k个数要保持原来的顺序

781. 给定一个有序的数组和一个数字k，表示这个数组中有k个数是乱序的，还原这个数组 
https://github.com/jamesben6688/coding/blob/main/array/k%E4%B8%AA%E6%95%B0%E5%AD%97%E4%B9%B1%E4%BA%86%E7%9A%84%E6%95%B0%E7%BB%84%E8%BF%98%E5%8E%9F.py

782. 不含重复元素的一维数组做压缩编码，使得最新的数字为1，返回压缩后的数组，压缩后的数组中每个元素的位置应与压缩前对应 
followup，包含重复元素

783. 给一个机器人和一个地板，机器人需要从入口到达出口，机器人可以向上下左右四个方向移动，地板的颜色会指导机器人的移动，
地板会有8种颜色，机器人每遇到一个颜色就会按这个颜色指定的方向走，直到遇到其他颜色的地板，请给出一种机器人可以到达出口的方案，
这个方案是指什么颜色指的是哪个方向

784. 636变形。如果输入如下：
<1,f1,enter> <2,f2,enter> <3,f2,out> <4,f2,enter><5,f2,out><6,f1,out>
那么需要输出如下：
f1,5
 - f2,1
 - f3,1
要注意的是
1.需要按函数被call的先后顺序输出
2.需要考虑函数的indent。如果f1 里面 call f2，f2 里面再call f3，那么输出f3时前面要有两个空格，
输出f2时前面有一个空格。输出f1时前面没有空格。
https://github.com/jamesben6688/coding/blob/main/dfs/%E5%87%BD%E6%95%B0%E5%B5%8C%E5%A5%97%E8%B0%83%E7%94%A8.py

785. 359/362? 數連接。 只有一個函數“能不能連接”，不 take timestamp. 要用系統的時間。
超過五百個連接後就不讓再接了。每個連接一秒鐘後自動掛斷。

786. 三张card属不属于一个set 注意每个attribute是独立的

787. 253，但是要实时统计frequncy(可以想象需要画frequency的trend line)
788. 1034，有follow-up但实在想不起来了。。

789：随机生成迷宫

790. 每张卡片有rank和suit两种attribute。相同的rank，并且suit值连续递增的卡片才算是一个valid set。
输入一个卡片数组，求问suit值最大的valid set。
需要5张卡片才能算一个set

791. 设计一个提示钓鱼网站的service，主要是判断某个 url 是否是钓鱼网站。着重讨论了更新数据的时候怎么办，用户抱怨这个service误报怎么办。

792. 一个0-1 矩阵，只能从1的 cell 跳到上下左右相邻的 1 的cell，问从第一行的值为 1 的 cell开始跳，
能跳到哪些最后一行的cell。bfs解决。

793. 设计一个 stock 类，会接收一些 Feeds
Feed(timestamp, stcokPrice) 2种情况 ，如果 timestamp 没有出现过，就add，出现过就update
Feed(timestamp) 如果timestamp出现过。就delete 那个 record
除了 add/update/delete 还要写另外3个方法，getMostRecentPrice, getLowestPrice, getHightestPrice
题目有个 前提。。。大部分情况是add，少量的 update/delete

794. 给一个N，然后有一个method getNext，等概率随机生成下一个数，而且生成过的数不再被生成。

795. 在高速公路上有N个checkpoint （1到N），每经过一个checkpoint就会有一条log，
（checkpoint number，车牌，timestamp），给一堆这样的log，而且已知每两个checkpoint之间的距离，走高速要花钱，
给出了一个公式来计算费用，要求输出每一辆车的费用

796. 2115

797. 给定 n个服务员，m个人等位，给了数组里面元素是每个服务员服务一个人的时间，当同时有多个空闲的的服务员时，
最小编号的服务员会先服务，问当你是第m+1个人的时候要等多久。
第一个followup，输出是哪个编号的服务员会服务第m+1个人。
第二个followup，当m>>n的时候，能不能对m进行优化。

798. 随机播放音乐 N 首，实现一个随机播放函数 返回一首歌 这首歌在之后的K次播放中不能出现，
而且要保证播放音乐彻底随机 O(1) 的写法，面试官非常好心地给hint才写出来，
代码量其实非常小

799. 一个dom tree 返回包含被搜索的字符串的node，不需要完全彻底match，可以横跨多个node，但是node必须相邻然后构成句子，例如
<div> ~~~node1~~~~
  <div>Thank you</div>  ~~~node2~~~~
  <div>so much.</div>  ~~~node3~~~~
<div>
你搜Thank you 返回node2， 搜so 返回node3 搜you so much 返回node 2 跟 node3

800. cord tree只不过char 换成了 weight
然后一个node 有weight 有set<Node> children,
要求 total weight under this node 简单的 recursion

801. 3个function ： constrcuter / ack(int number)/ getFirstUnAck()
eg: constrcuter(5) // 5 == starting point
ack(6),
ack(8)
ack(9)
ack(10)
ack(11)
ack(12)
（ack not comes in order）
getFirstUnAck() should return 7
要求O（1） （我个人感觉不太可能）

802. 552

803 tire tree implement + parse URL

804. 2115变种 大概的情景就是 每个package都有一些dependency，它的dependency同样也有其他的dependency。 
a) 返回有多少种unique的packages在dependency graph中. 
b) 如果需要下载某个package，并且要求先下载所有的dependency再下载parent package。
要求返回可行的下载顺序 -> topological sorting.

805. 给一个array [1,1,2,3], tell whether it's true to connect them together. 
每个element代表一个插座，大小代表连接点的个数。 element只能是1，2，3，返回true or false.
每个连接点只能用一次 input的数组顺序不重要 我们可以自由的改变array的顺序 只要能找到一种可行的连接方式 就返回true
[1,1] --> true
0- -0
[1,2,1] --> true
0- -0- -0
[1,3,1,1,] --> true
0- -0- -0
  |
  |
  0
[1,2,1,1]
0- -0- -0-0
follow up：
如果element有可能是任何postive number怎么办？
如果要求不能有空的连接点怎么办？自己能和自己连接的时候？ 自己不能和自己连接的时候？
https://github.com/jamesben6688/coding/blob/main/graph/%E7%BB%99%E5%AE%9A%E4%B8%80%E4%B8%AAdegree%E5%88%97%E8%A1%A8%E8%83%BD%E5%90%A6%E5%BD%A2%E6%88%90%E5%9B%BE.py

806. 两个list， 其中的element是id和balance： （id, balance) 每个list里面的id都是unique的 但是第二个list中可能有第一个list的id
[[1, 2], [2, 5], [3, 1]], [[1, 3], [4, 5]]]
所以最终呢要merge两个list based on id
然后返回按balance从小到大的排序？ 接着问id从小到大的排序？
如果是k个list怎么办？ 这个时候按balance从小到大的排序？ 按id从小到大的排序？

807. 给一个tree 返回nodes的个数 BFS秒
follow up: 如过这个tree是complete binary tree

808. 636 把unixdirectory 转换成Tree的结构
"name, files, dirs{}, id = 1"这种nested形式 包含customized tree structure 和string processs.
要自定义树的结构，并且处理字符串输入。

809.818， 超难题

810. You have an array of N numbers, where N is at most 32,000. The array may have duplicate entries and you do not know what N is. With only 4 Kilobytes of memory available, how would print all duplicate elements in the array ?. 

Examples:

Input : arr[] = {1, 5, 1, 10, 12, 10}
Output : 1 10
1 and 10 appear more than once in given
array.

Input : arr[] = {50, 40, 50}
Output : 50

811. Given a stream of prices from transactions: 79.20, 20.05, 96.82, ...  SortedList
Implement 2 methods:
1) insert(price)
2) query(percentile) - e.g.: query(0.2) should give a price that 20% of prices is lower than it, 

812. N cities from 1 to N, each city has either landmark A or B
return true if there is a path from x to y so that path has either A or B landmark, otherwise return false
example:
Landmarks: 1:A,2:B,3:B,4:A,5:A
Paths:
1-2
1-5
3-4
3-5
4-5
from 1 to 4 -> 1,5,4 (x) but 1,5,3,4 (y) so return true

813. stream of logs from RPC calls:
PRC ID, Timestamp, Event
1, 0, START
2, 1, START
1, 2, END
3, 5, START
2, 6, END
3, 7, END
...
现在告诉你timeout是3秒，要你写个method能尽快把timeout的RPC calls找出来

814. 有一种牌，牌面有三个信息，shape, color,count, shade.
每个信息有三个值：
shape: circle, square, triangle
color: green, red, blue
count: 1, 2, 3
shade: filled, empty, striped
刚开始问有多少种不同的牌；
后来说，有一种set的定义：给三张牌，对于这些牌的每个信息，三个都一样，或者都不一样，就说这个一个set。
问如何判断给你的三张牌是不是一个set.

815. 我们只有2种type，Wire和Torch。下面有几个规则。大概就是Torch提供能源，max是10。
Wire传输能源每走一个格子能源-1。现在给你一堆这样的简化版circuits，要求return每个node当前的能源值。
4个API可以直接用：1.判断是不是Torch；2.拿到当前node的能源值；3.set当前的node能源值；4.拿到当前node的所有neighbor。
这几个API也是clarify出来的。
，边走边update每个node的value。这轮对clarify question的要求真的很高。写完dry run，，
follow up问这个是简化版的，那么in real world每个circuit都那么复杂，咋处理给他们赋予能源值这个事情呢。

816. 给你一个range，一个值，return这个值在不在range里面。这个题看地里出现好几次了，我是用的binary search，
后面follow up问万一input很多很多是个stream咋办。

817. 给你steam of words，print if 10s内都没重复出现，optimize时间和space。
有点类似刷题网359
follow up， LRU cache的思路来remove掉10s以外的value

818. 给你一个distance, 然后一些 floating values （one by one）, 让你找到三个一组，每两个的distance 要小于given distance.

819. 股票的 status update, 可以update price, drop price. 然后 maintain low, high, mosr recent.

820. part 1: shuffle("anyString" + anyChar) => newString,判断 if we can obtain newString from `shuffle("anyString" + anyChar)`
  part 2: [oldString....] [newString....], return counter of pairs that statisfies part1 ((m*n)^2 很简单， 
part1:
“ABC” + anyChar => "BACD" (True)因为加了一个D 然后Shuffle
“ABC” + anyChar => "BADD" (False)
part2: (Strings only has 26 Chars, "A", "B"..."Z")
a = ["A", "B", ""]
b = ["AB", "AB", ""]
find total number of part1 pairs between list a and list b.
做法是将
“ABC”=> ["A:2B:1C:1D:0....Z:0"] .... ["A:1B:1C:1D:0....Z:1"] 26 of them from list a
then check with list b (b transfer 也一样， 但只需要 1-1, not 1-> 26) 这样就optimized 了

821.  - part1: 让写一个Tree, 可以return a random node (O(1))
  - part2: 让写一个Tree, 可以return a random leaf (O(1))
  
822. 900. 实现特殊iterator  [3, 8, 2, 5 ]两个数 第一个是repeat time 第二个是返回数值
  hasNext() -> True
  next() -> 8
  hasNext() -> True
 next() -> 8
 hasNext() -> True
next() -> 8
hasNext() -> True
 next() -> 5
 hasNext() -> True
 next() -> 5
 hasNext() -> False
 next() -> NullException
 
823. 2034

824. 寻找 符合 difference 的 arithmetic sequence最大长度 input是二叉树和 diff

825. 每户之间可能有双向连同的隧道
你要从起点传递一本书 给所有能访问的居民 统计完居住人数然后返回起点

826. 最优账单平衡
https://github.com/jamesben6688/coding/blob/main/dfs/%E8%B4%A6%E5%8D%95%E5%B9%B3%E8%A1%A1.py
https://github.com/jamesben6688/coding/blob/main/dfs/%E8%B4%A6%E5%8D%95%E5%B9%B3%E8%A1%A1dp.py

827. 定义了一类数，如果是质数并且去掉最后一个数位还是这类数

follow up: 找小于n的所有这一类数
https://github.com/jamesben6688/coding/blob/main/dfs/%E8%B4%A8%E6%95%B0%E5%8F%98%E7%A7%8D.py

828. 边界着色
https://github.com/jamesben6688/coding/blob/main/dfs/%E8%BE%B9%E7%95%8C%E7%9D%80%E8%89%B2.py

829. 随机生成迷宫
https://github.com/jamesben6688/coding/blob/main/dfs/%E9%9A%8F%E6%9C%BA%E7%94%9F%E6%88%90%E8%BF%B7%E5%AE%AB.py

830. 员工休假
https://github.com/jamesben6688/coding/blob/main/dp/%E5%91%98%E5%B7%A5%E4%BC%91%E5%81%87.py

831. Range Module 
https://github.com/jamesben6688/coding/blob/main/range/P710.py

832. Segment Tree
https://github.com/jamesben6688/coding/blob/main/segment_tree/segment_tree.py

833. 最大连续1的个数
https://github.com/jamesben6688/coding/blob/main/sliding_window/%E6%9C%80%E5%A4%A7%E7%9A%84%E8%BF%9E%E7%BB%AD1%E7%9A%84%E4%B8%AA%E6%95%B0.py

followup: 可以修改0为1
https://github.com/jamesben6688/coding/blob/main/sliding_window/%E6%9C%80%E5%A4%A7%E7%9A%84%E8%BF%9E%E7%BB%AD1%E7%9A%84%E4%B8%AA%E6%95%B0_follow_1.py

834. 最大可见点的数目
https://github.com/jamesben6688/coding/blob/main/sliding_window/%E8%83%BD%E7%9C%8B%E5%88%B0%E5%A4%9A%E5%B0%91%E7%82%B9.py

835. 日历区间
https://github.com/jamesben6688/coding/blob/main/sortedlist/%E6%97%A5%E5%8E%86%E5%8C%BA%E9%97%B4.py

836. 中位数x到2x的数
https://github.com/jamesben6688/coding/blob/main/sortedlist/%E8%BF%94%E5%9B%9E%E4%B8%AD%E4%BD%8D%E6%95%B0x%E5%88%B02x%E7%9A%84%E6%95%B0.py

837. 最小栈
https://github.com/jamesben6688/coding/blob/main/stack/min_stack.py

838. 函数独占时间
https://github.com/jamesben6688/coding/blob/main/stack/%E5%87%BD%E6%95%B0%E7%8B%AC%E5%8D%A0%E6%97%B6%E9%97%B4.py

839. 解码字符串
https://github.com/jamesben6688/coding/blob/main/str/%E5%AD%97%E7%AC%A6%E4%B8%B2%E8%BD%AC%E6%8D%A2.py

840. 改变字符是否存在
https://github.com/jamesben6688/coding/blob/main/str/%E6%94%B9%E5%8F%98%E4%B8%80%E4%B8%AA%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%98%AF%E5%90%A6%E5%AD%98%E5%9C%A8.py

841. 转化字符串
https://github.com/jamesben6688/coding/blob/main/str/%E8%BD%AC%E5%8C%96%E5%AD%97%E7%AC%A6%E4%B8%B2.py

842. swipe_line 矩形面积
https://github.com/jamesben6688/coding/blob/main/swipe_line/%E7%9F%A9%E5%BD%A2%E9%9D%A2%E7%A7%AF.py

843. 矩形面积 像素归属法
https://github.com/jamesben6688/coding/blob/main/swipe_line/%E7%9F%A9%E5%BD%A2%E9%9D%A2%E7%A7%AF_%E5%83%8F%E7%B4%A0%E5%BD%92%E5%B1%9E%E6%B3%95.py

844. 第i天画画
https://github.com/jamesben6688/coding/blob/main/swipe_line/%E7%AC%ACi%E5%A4%A9%E7%94%BB%E7%94%BB.py


845. 一堆圆是否是同一个group
https://github.com/jamesben6688/coding/blob/main/topo_sort/%E5%88%A4%E6%96%AD%E4%B8%80%E5%A0%86%E5%9C%86%E6%98%AF%E5%90%A6%E6%98%AF%E5%90%8C%E4%B8%80%E4%B8%AAgroup.py
https://github.com/jamesben6688/coding/blob/main/topo_sort/%E5%88%A4%E6%96%AD%E4%B8%80%E5%A0%86%E5%9C%86%E6%98%AF%E5%90%A6%E6%98%AF%E5%90%8C%E4%B8%80%E4%B8%AAgroup_dfs%E6%B3%95.py

846. 删除二叉树叶子
https://github.com/jamesben6688/coding/blob/main/tree/%E4%BA%8C%E5%8F%89%E6%A0%91%E5%8F%B6%E5%AD%90.py
https://github.com/jamesben6688/coding/blob/main/tree/%E6%89%93%E5%8D%B0%E6%A0%911.py

847.二叉树最大路径和
https://github.com/jamesben6688/coding/blob/main/tree/%E4%BA%8C%E5%8F%89%E6%A0%91%E6%9C%80%E5%A4%A7%E8%B7%AF%E5%BE%84%E5%92%8C.py

848. 二叉树迭代遍历
https://github.com/jamesben6688/coding/blob/main/tree/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E8%BF%AD%E4%BB%A3%E9%81%8D%E5%8E%86.py

849. quad tree, QUAD 存二值图片
https://github.com/jamesben6688/coding/blob/main/tree/%E5%9B%9B%E5%8F%89%E6%A0%91%E5%AD%98%E4%BA%8C%E5%80%BC%E5%9B%BE%E7%89%87.py

850. 断开叶子节点的最小cost
https://github.com/jamesben6688/coding/blob/main/tree/%E6%96%AD%E5%BC%80%E6%89%80%E6%9C%89%E5%8F%B6%E5%AD%90%E8%8A%82%E7%82%B9%E7%9A%84%E6%9C%80%E5%B0%8Fcost.py


851. 树最下面一层的宽度
https://github.com/jamesben6688/coding/blob/main/tree/%E6%A0%91%E6%9C%80%E4%B8%8B%E9%9D%A2%E4%B8%80%E5%B1%82%E7%9A%84%E5%AE%BD%E5%BA%A6.py

852. 树的中位数
https://github.com/jamesben6688/coding/blob/main/tree/%E6%A0%91%E7%9A%84%E4%B8%AD%E4%BD%8D%E6%95%B0.py

853. 第一问是从左到右删叶子节点，但是如果删完一个节点后，它的父节点也变成了叶子节点，有限删除这个父节点；第二问就是利口 要灵儿，
每轮删除都是从左到右删除所有的叶子节点；第三问是，可以删除任意叶子节点，求输出所有可能的删除顺序

第一问：从左到右删叶子节点，但一旦删除叶子后其父也变成叶子，就接着删这个父
这是一个“一口气往上删到底”的做法，但每次删除从左到右。

       1
      / \
     2   3
    /
   4
第一步删叶子：4、3（从左到右）

然后 2 变成叶子，也删掉

然后 1 变成叶子，也删掉

删除顺序：[4, 3, 2, 1]
实现思路：
每次从左到右找叶子，删掉它

如果某节点的左右子树都删了，它变成新的叶子，继续删

✅ 第二问：Leetcode 366 — 每轮删除所有叶子节点，按轮次输出
这里是一轮一轮地删叶子，而不是像第一问那样一口气删到顶。

       1
      / \
     2   3
    /
   4
第1轮删：4、3 → [[4, 3]]

第2轮删：2 → [[4, 3], [2]]

第3轮删：1 → [[4, 3], [2], [1]]

思路：
用 DFS 后序遍历，节点的“高度”决定它在哪一轮被删除（叶子是第 0 层）

LC366 原题参考代码（高度分组）：

def findLeaves(root):
    res = []
    def dfs(node):
        if not node: return -1
        level = 1 + max(dfs(node.left), dfs(node.right))
        if level == len(res):
            res.append([])
        res[level].append(node.val)
        return level
    dfs(root)
    return res
✅ 第三问：可以删除任意叶子节点，求所有可能的删除顺序
这是一个 回溯 / DFS 的全排列变种问题。


   1
  / \
 2   3
初始叶子：2, 3。你可以选择先删 2 再删 3，也可以先删 3 再删 2。

删除顺序可能是：
[2, 3, 1]

[3, 2, 1]

思路：
每一轮找所有当前的叶子

对这些叶子做全排列（可以任选一个删）

继续递归下去

def backtrack(tree, path):
    if tree is empty:
        results.append(path)
        return
    leaves = find_all_leaves(tree)
    for leaf in leaves:
        remove(leaf)
        backtrack(tree, path + [leaf.val])
        restore(leaf)
		
854. 删除排序数组重复元素
https://github.com/jamesben6688/coding/blob/main/two_pointer/%E5%88%A0%E9%99%A4%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84%E9%87%8D%E5%A4%8D%E5%85%83%E7%B4%A0.py

855. 判断两个机器人轨迹是否相交
https://github.com/jamesben6688/coding/blob/main/two_pointer/%E5%88%A4%E6%96%AD%E4%B8%A4%E4%B8%AA%E6%9C%BA%E5%99%A8%E4%BA%BA%E8%BD%A8%E8%BF%B9%E6%98%AF%E5%90%A6%E7%9B%B8%E4%BA%A4.py

856. abc 2输出 abcabc
abc2 de3 输出 abcabcdeabcabcdeabcabcde

https://github.com/jamesben6688/coding/blob/main/two_pointer/%E6%89%93%E5%8D%B0%E5%AD%97%E7%AC%A6%E4%B8%B2.py

857. 判断不等式是否合法 a>b
https://github.com/jamesben6688/coding/blob/main/union_find/%E7%AD%89%E5%BC%8F%E5%88%A4%E6%96%AD%E5%A4%A7%E5%B0%8F%E6%98%AF%E5%90%A6%E5%90%88%E6%B3%95.py

858. 能穿过矩阵的最后一天
https://github.com/jamesben6688/coding/blob/main/union_find/%E8%83%BD%E7%A9%BF%E8%BF%87%E7%9F%A9%E9%98%B5%E7%9A%84%E6%9C%80%E5%90%8E%E4%B8%80%E5%A4%A9.py

859. 合并牌, pile

860. 村庄打井的最小费用

861. 获取斐波拉契数
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/fib.py

862. jessca 保险 serve 服务 服务器 task
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/jessca%E4%BF%9D%E9%99%A9.py
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/n%E4%B8%AA%E6%9C%8D%E5%8A%A1%E5%99%A8m%E4%B8%AAtask.py

863. 工作时间summary
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/people_work_summary.py

864. utf8 utf-8
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/utf8.py

865. wordle_game
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/wordle_game.py

866. 不放回随机抽样
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/%E4%B8%8D%E6%94%BE%E5%9B%9E%E9%9A%8F%E6%9C%BA%E6%8A%BD%E6%A0%B7.py

867. 从双倍数组删除
		1. 排序法
		2. O(N)
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/%E4%BB%8E%E5%8F%8C%E5%80%8D%E6%95%B0%E7%BB%84%E5%88%A0%E9%99%A4.py

868. 出栈顺序是否合法
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/%E5%87%BA%E6%A0%88%E9%A1%BA%E5%BA%8F%E6%98%AF%E5%90%A6%E5%90%88%E6%B3%95.py

869. 正方形
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/%E5%88%A4%E6%96%AD%E6%AD%A3%E6%96%B9%E5%BD%A2.py

870. 版排序数组
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/%E5%8D%8A%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84.py

871. 压缩字符串
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%8E%8B%E7%BC%A9.py

872. 字符串链
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/%E5%AD%97%E7%AC%A6%E4%B8%B2%E9%93%BE.py

873. 微波炉
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/%E5%BE%AE%E6%B3%A2%E7%82%89cost.py

874. 把0移到一边
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/%E6%8A%8A0%E7%A7%BB%E5%8A%A8%E5%88%B0%E4%B8%80%E8%BE%B9.py

875. 服务器空闲分配
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%A9%BA%E9%97%B2%E5%88%86%E9%85%8D.py

876. 桶中抽提组成试卷
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/%E6%A1%B6%E4%B8%AD%E6%8A%BD%E6%8F%90%E7%BB%84%E6%88%90%E7%AD%94%E6%A1%88.py

877. 牌是否合法
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/%E7%89%8C%E6%98%AF%E5%90%A6%E5%90%88%E6%B3%95.py

878. 猜单词
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/%E7%8C%9C%E5%8D%95%E8%AF%8D.py


879. 重构字符串
https://github.com/jamesben6688/coding/blob/main/%E6%A8%A1%E6%8B%9F%E9%A2%98/%E9%87%8D%E6%9E%84%E5%AD%97%E7%AC%A6%E4%B8%B2.py



