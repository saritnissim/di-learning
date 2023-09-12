import math
class Pagination:
    
    def __init__(self, items=None, page_size=10):
        self.items = items
        self.page_size= int(page_size)
        self.total_pages = math.ceil(len(self.items)/self.page_size)
        self.current_page = 1

    def get_visible_items(self):
        start_index = self.current_page * self.page_size
        print(self.items[start_index:start_index+self.page_size])
        return self

    def prev_page(self):
        if self.current_page - 1 >= 1:
            self.current_page -=1 
            self.get_visible_items()
        return self
    
    def next_page(self):
        if self.current_page +1 <= self.total_pages:
            self.current_page +=1 
            self.get_visible_items()
        return self
    
    def first_page(self):
        print(self.items[0:self.page_size])
    
    def last_page(self):
        print(self.items[-self.page_size:])
    
    def go_to_page(self, page_num):
        page_num = int(page_num)
        if page_num <= 0:
            self.current_page = 1
        if page_num >= self.total_pages:
            self.current_page = self.total_pages
        self.get_visible_items()


alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)
p.first_page()
p.last_page()
p.get_visible_items()
p.next_page().next_page().prev_page()


