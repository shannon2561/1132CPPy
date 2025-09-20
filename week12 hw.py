class BooksInformation:
    def __init__(self,title,authors,publication_year,edition):
        self.title=title
        self.authors=sorted(authors)
        self.publication_year=publication_year
        self.edition=edition

    def add_author(self,author):
        if author not in self.authors:
            self.authors.append(author)
            self.authors=sorted(self.authors)
        # self.authors.append(author)
        # self.authors=sorted(self.authors)

    def remove_author(self,author):
        if author in self.authors:
            self.authors.remove(author)
        #self.authors.remove(author)

    def update_edition(self,edition):
        self.edition=edition

    def update_publication_year(self,publication_year):
        self.publication_year=publication_year

    def update_title(self,title):
        self.title=title

    def __str__(self):
        return f"Title: {self.title}; Authors: {', '.join(self.authors)}; Year: {self.publication_year}; Edition: {self.edition}"
        #Title: Linear Algebra; Authors: Andrew Waldron, David Cherney, Rohit Thomas, Tom Denton; Year: 2013; Edition: Second


if __name__=="__main__":
    Testcase=int(input())
    input()
    for i in range(Testcase):
        BookName=input()
        Authors_List=input().split(", ")
        Publication_Year=int(input())
        Edition=input()
        input()
        s=BooksInformation(BookName,Authors_List,Publication_Year,Edition)
        while True:
            Input=input()

            if Input=="---":
                break

            if Input=="print":
                print(s)
                continue

            Command=Input.split(" ")
            Operation=Command[0]
            New_Info=Command[1:]   #List

            if Operation=="add_author":
                s.add_author(" ".join(New_Info))

            elif Operation=="rm_author":
                s.remove_author(" ".join(New_Info))

            elif Operation=="update_edition":
                s.update_edition(" ".join(New_Info))
            
            elif Operation=="update_pubyear":
                s.update_publication_year(int(New_Info[0]))
            
            elif Operation=="update_title":
                s.update_title(" ".join(New_Info))