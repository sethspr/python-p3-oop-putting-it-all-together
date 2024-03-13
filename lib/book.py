#!/usr/bin/env python3

class Book:
    #test 1
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = page_count

    def __repr__(self):
         return f"<Book: {self.title}, Pages: {self._page_count}>"
    #test 2
    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count_int):
        if type(page_count_int) == int:
            self._page_count = page_count_int
        print("page_count must be an integer")

    #to convert a string into an integer. this works, but it's not what the test is looking for. 
    def int_page_count(self): 
        page_int = int(self.page_count)
        print(type(page_int))
        return page_int
        # for this to work, on line 9, 'Pages:' needs to be {self.int_page_count()}
    
    #test 3
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

my_book = Book("And Then There Were None", 272)

print(my_book)
