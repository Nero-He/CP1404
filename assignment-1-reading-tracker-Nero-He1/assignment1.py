import csv

"""
Replace the contents of this module docstring with your own details
Name: HongZhe He
Date started: 2021/4/16
GitHub URL:
"""

""""
1. print welcome message
2. print a looping menu
3.get the optional [List/ Add/ Mark a book as complete/ Quit]
"""


def main():
    # Main function for the printing menu and get the options
    menu_text = """ 
    Reading Tracker 1.0 - by HongZhe He/ Nero
    
    Menu:
    L - List all books
    A - Add new book
    M - Mark a book as complete
    Q - Quit
    """
    print(menu_text)
    optional = input('Please select your choice for the menu: ').lower()
    while optional != 'q':
        if optional == 'l':
            show_books()
            print(menu_text)
            optional = input('Please select your choice for the menu: ').lower()
            return optional
            break
        elif optional == 'a':
            record_books()
            print(menu_text)
            optional = input('Please select your choice for the menu: ').lower()
            return optional
            break

        elif optional == 'm':
            mark_books()
            break
        else:
            print('Invalid menu choice')
            print(menu_text)
            optional = input('Please select your choice again: ').lower()


def show_books():
    data = []

    with open('books.csv', 'r') as f:
        rete = csv.reader(f)

        for row in rete:
            data.append(row)

    for item in data:
        status = item[3]
        if status == 'c':
            print(" - {} at {} for {} pages".format(item[0], item[1], item[2]))
        else:
            print("* - {} at {} for {} pages".format(item[0], item[1], item[2]))


def record_books():
    # this is for the add new books to the csv file
    new_books = []
    books_author = []
    book_pages = []
    title = input("Title: ")
    if title == '':
        print('Input can not be blank')
        title = input("Title: ")
        return title
    else:
        new_books.append(title)

    author = input('Author: ')
    if author == '':
        print(print('Input can not be blank'))
        author = input('Author: ')
        return author
    else:
        books_author.append(author)

    pages = float(input('Pages: '))
    if pages == '':
        print('Input can not be blank')
        pages = float(input('Pages: '))
        return pages
    elif pages < 0:
        print('Number must be > 0')
        pages = float(input('Pages: '))
        return pages
    elif int(pages) != pages:
        print("Invalid input; enter a valid number")
        pages = float(input('Pages: '))
        return pages
    else:
        book_pages.append(pages)

    print('{} by {}, ({} pages) added to Reading Tracker'.format(new_books, books_author, book_pages))

    with open('books.csv', 'w')as f:
        writer = csv.writer(f)
        for row in new_books:
            writer.writerow(row)

        for row in books_author:
            writer.writerow(row)

        for row in book_pages:
            writer.writerow(row)

def mark_books():
    books = []

    with open('books.csv', 'r') as f:
        rete = csv.reader(f)

        for row in rete:
            books.append(row)

    books1 = sorted(books, key=lambda author: author[1])
    for item in books1:
        status = item[3]
        if status == 'c':
            print(" - {} at {} for {} pages".format(item[0], item[1], item[2]))
        else:
            print("* - {} at {} for {} pages".format(item[0], item[1], item[2]))

    mark_the_book = int(input('Enter the number of a book to mark as completed: '))
    if mark_the_book <= 0:
        print('Number must be > 0')
        mark_the_book = int(input('Enter the number of a book to mark as completed: '))
    elif mark_the_book > len(books1):
        print('Invalid book number')
        mark_the_book = int(input('Enter the number of a book to mark as completed: '))
    elif status == 'c':
        print('That book is already completed!')
        main()
    else:
        print('The {}  by {} completed!'.format(item[0], item[1]))
        with open('books.csv', 'w')as f:
            csv_writer = csv.writer(f)
            for row in csv_writer:
                row[4] = 'r'
                csv_writer.writerow(row)




if __name__ == '__main__':
    main()
