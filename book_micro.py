# Name:         Tamarah Binek
# OSU Email:    binekt@oregonstate.edu
# Course:       CS361 - Software Engineering I
# Assignment:   9 - Microservice for Book App
# Due Date:     31 July 2023
# Description:  A program that, given a descriptive string ("Sort by Title", "Sort by Author", "Sort by Order_a", "Sort by Order_d"), returns
#               the set of books sorted (Sort Service)

import time

while True:
    time.sleep(5)

    print("sorting...")

    with open("sort.txt", 'r') as file:
        contents = file.readlines()
    
    # check ig the file is not empty and has the sorting option
    if contents:
        sort_by = contents[0].strip() #get the sorting option in file

        # Skip the first line and join the remaining lines into a single string
        book_contents = "".join(contents[1:])
        # convert the lines back into a list of books
        books = []
        books = eval(book_contents)

        # Sort the books based on the ascending book order (index 0 in each sublist)
        if sort_by == "Sort by Order_a":
            sorted_books = sorted(books, key=lambda x: x[0])
            print("Sorting in by Order - ascending.")

        # Sort the books based on the ascending book order (index 0 in each sublist)
        elif sort_by == "Sort by Order_d":
            sorted_books = sorted(books, key=lambda x: x[0], reverse=True)
            print("Sorting in by Order - descending.")

        # Sort the books based on the book titles (index 1 in each sublist)
        elif sort_by == "Sort by Title":
            sorted_books = sorted(books, key=lambda x: x[1])
            print("Sorting by Title.")

        # Sort the books based on the book authors (index 2 in each sublist)
        elif sort_by == "Sort by Author":
            sorted_books = sorted(books, key=lambda x: x[2])
            print("Sorting by Author.")
        # if txt blank or doesnt have one of the sort options then pring this line and exit
        else:
            print("Incorrect file sort option.")
            break

        # write the sorted_books list to the sort.txt file
        with open("sorted.txt", "w") as file:
            file.writelines(str(sorted_books))

        print("Books sorted and written to sort.txt.")
    else:
        print("File is empty.")
        break