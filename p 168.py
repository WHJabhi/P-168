class Bookshelf:
    def __init__(self,name,author,price,publishing_year):
        self.book_name = name
        self.book_author= author
        self.book_price = price
        self.book_publishing_year = publishing_year
        
    def add_book(self):
        print("book name :"+ self.book_name)
        print("book author:"+ self.book_author)
        print("book price :"+ str(self.book_price))
        print("book publishing year:"+ str(self.book_publishing_year))
        print("book added :")
        
    def years_since_published(self):
        years_ago_published = 2020-self.book_publishing_year
        print("book was published "+ str(years_ago_published)+"years ago")

book1 = Bookshelf("Harry poter", "Jk rowleing", 289, 1997)
book1.add_book()
book1.years_since_published()

book2 = Bookshelf("I want to eat your pancreas", "Yoru sumino", 750, 1981)
book2.add_book()
book2.years_since_published()