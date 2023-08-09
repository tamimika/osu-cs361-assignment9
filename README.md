# osu-cs361-assignment9

# Microservice Data Request Guide
This README provides detailed instructions on how to programmatically request data from the microservice, which sorts a list of books based on the specified criteria in a file named sort.txt. The sorted results will be saved in a file called sorted.txt.

Requirements:
Before proceeding, ensure that you have the following components installed and set up on your system:

Python (version 3.6 or higher)
A text editor of your choice
Access to the sort.txt file containing the unsorted list of books

Usage:
Follow these steps to programmatically request data from the microservice:
Prepare the sort.txt file:

The sort.txt file should be structured as follows:

Sort by [Sorting Criteria]
[[1, “Title”, “Author”], [2, “Title”, “Author”], [3, “Title”, “Author”]]...

The first line represents the sorting criteria, which can be one of the following:

Sort by Title: Sort the books by their titles in alphabetical order.
Sort by Author: Sort the books by their authors in alphabetical order.
Sort by Order_a: Sort the books by their original order in the list.
Sort by Order_d: Sort the books by their original order in reverse.
The subsequent lines contain the list of books.

Request data from the microservice:

You can interact with the microservice programmatically using Python. Here's a sample Python script that demonstrates how to request data from the microservice:
# Write contents to the 'sort.txt' file
user_input = "Sort by Title"
data = str([[1, 'Little Women', 'Louisa May Alcott'], [2, 'Pride and Prejudice', 'Jane Austen'], [5, "The Handmaid’s Tale", 'Margaret Atwood'], [3, 'The Hunger Games', 'Suzanne Collins'], [4, 'Where the Crawdads Sing', 'Delia Owens']])
with open("sort.txt", 'w') as sort_file:
    sort_file.write(user_input + "\n")
    sort_file.write(data)
time.sleep(5)

# Read the contents of the 'sort.txt' file
with open('sorted.txt', 'r') as file:
    data = file.read()

Run the Python script:
An example of the above interface is located in interface_micro.py). Save it and execute it in your terminal to interact with book_micro.py (the sorting microservice).

python interface_micro.py
The script will send the contents of sort.txt to the microservice, and upon successful sorting, it will save the results to sorted.txt.

UML Diagram:
![image](https://github.com/tamimika/osu-cs361-assignment9/assets/97025553/1b9f22cb-26b3-4423-b822-275a3167e648)

