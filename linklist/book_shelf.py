from sortedcontainers.sorteddict import SortedDict
from collections import defaultdict


class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __repr__(self):
        return "{" + f"name: {self.name}, author: {self.author}" + "}"


class DoubleLinkListNode:
    def __init__(self, book, prev=None, nxt=None):
        self.book = book
        self.prev = prev
        self.nxt = nxt


class BookShelf:
    def __init__(self):
        self.books_dummy = DoubleLinkListNode(None)
        # self.books_dummy.nxt = self.books_dummy

        self.book_map = SortedDict()
        # self.book_map = defaultdict(DoubleLinkListNode)
        self.book_map[0] = self.books_dummy
        self.bookmark = 0

    def update_bookmap(self, idx, book_node):
        while book_node:
            self.book_map[idx] = book_node
            book_node = book_node.nxt
            idx += 1
        for i in list(self.book_map.keys())[idx:]:
            self.book_map.pop(i)

    def add(self, book_list, to_index):
        cur_book = self.book_map[to_index]
        cur_book_bk = cur_book

        # first_added_book = book_list[0]
        for i, book in enumerate(book_list):
            book_node = DoubleLinkListNode(book)
            """
                    book_node<---
                   _
                   |             |
                   |             |
                   _             -
                cur_book  nxt
            """
            if cur_book.nxt:
                cur_book.nxt.prev = book_node
            book_node.nxt = cur_book.nxt
            cur_book.nxt = book_node
            book_node.prev = cur_book

            cur_book = cur_book.nxt

        # update the book_map
        self.update_bookmap(to_index, cur_book_bk)

    def remove_from_shelf(self, index):
        cur_book = self.book_map[index]

        """

        cur_book <----> book_1 <-------> book_2
        """
        nxt_book = cur_book.nxt

        if cur_book.nxt:
            cur_book.nxt = cur_book.nxt.nxt
        if cur_book.nxt:
            cur_book.nxt.prev = cur_book

        self.book_map.pop(index + 1)

        del nxt_book
        self.update_bookmap(index, cur_book)

    def move_from_shelf(self, from_index, to_index, number):
        if from_index + 1 >= len(self.book_map) or from_index + number + 1 >= len(self.book_map):
            raise ValueError("index out of self.book_map bound")

        from_book_start = self.book_map[from_index + 1]
        pre_from = from_book_start.prev

        from_book_end = self.book_map[from_index + number]
        after_end = from_book_end.nxt

        to_book_start = self.book_map[to_index+1]
        after_to = to_book_start.nxt
        """
         + ->  from_book_start <--------------------> from_book_end [] <--------------->to_book_start   []  +  <--------------------->
        """

        if pre_from:
            pre_from.nxt = to_book_start
        if to_book_start:
            to_book_start.prev = pre_from

        if to_book_start:
            to_book_start.nxt = from_book_start
        if from_book_start:
            from_book_start.prev = to_book_start

        if from_book_end:
            from_book_end.nxt = after_to
        if after_to:
            after_to.prev = from_book_end

        self.update_bookmap(from_index, self.book_map[from_index])

    def get_books(self):
        return [self.book_map[i].book for i in sorted(list(self.book_map.keys()))[1:]]

    def get_bookmark(self):
        return self.book_map[self.bookmark].book

    def set_bookmark(self, index):
        self.bookmark = index + 1


shelf = BookShelf()
shelf.add([Book("A", "X"), Book("B", "Y"), Book("C", "Z")], 0)
print("初始书架:", shelf.get_books())

shelf.set_bookmark(1)
print("书签指向:", shelf.get_bookmark())

shelf.add([Book("D", "W"), Book("E", "V")], 1)
print("插入后书架:", shelf.get_books())

shelf.remove_from_shelf(2)
print("删除后书架:", shelf.get_books())
print("书签现在指向:", shelf.get_bookmark())

shelf.move_from_shelf(1, 3, 2)
print("移动后书架:", shelf.get_books())

