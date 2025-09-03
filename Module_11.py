# Inheritance
class Publication:
    """
    Task 1:
        A publication can be either a book or a magazine.
        Each publication has a name.
    """
    def __init__(self, name: str):
        self.name = name

class Book(Publication):
    """
    Task 1:
        Each book also has an author and a page count.
        Also write the required initializers to both classes.
        Create a print_information method to both subclasses for printing out all information of the publication in question.
    """
    def __init__(self, name: str, author: str, page_count: int):
        Publication.__init__(self, name)
        self.author = author
        self.page_count = page_count

    def print_information(self) -> None:
        print(f"Book: {self.name}")
        print(f"Author: {self.author}")
        print(f"Page count: {self.page_count}")

class Magazine(Publication):
    """
    Task 1:
        Each magazine has a chief editor.
        Also write the required initializers to both classes.
        Create a print_information method to both subclasses for printing out all information of the publication in question.
    """
    def __init__(self, name: str, chief_editor: str):
        Publication.__init__(self, name)
        self.chief_editor = chief_editor

    def print_information(self) -> None:
        print(f"Magazine: {self.name}")
        print(f"Chief Editor: {self.chief_editor}")

class Task_1:
    """
    In the main program, create publications Donald Duck (chief editor Aki Hyyppä) and Compartment No. 6 (author Rosa Liksom, 192 pages).
    Print out all information of both publications using the methods you implemented.
    """
    @staticmethod
    def main() -> None:
        print("Module 11, Task 1.\n")
        donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
        compartment_no_6 = Book("Compartment No. 6", "Rosa Liksom", 192)
        print("------------------------")
        donald_duck.print_information()
        print("------------------------")
        compartment_no_6.print_information()
        print("------------------------")

class Task_2:
    """
    This Task is done in module 9
    """
    pass