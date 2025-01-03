# DS-project
## Team members
*- Othman Gharibeh
*- Asem Abusini
## Description

This Python application provides basic functionality for managing a bookshop's inventory and sales, it allows users to add books, update stock, process sales, and view sales data. Data is stored in CSV files 

## Features

- **Inventory Management:
    -   Add new books to the inventory
    -   View the current inventory (book ID, title, author, genre, price, stock)
    -   Update the stock of existing books
- **Sales Management:
    -   Record sales transactions
    -   View sales data (including total sales per book and genre)
- **Data :
    -   Inventory and sales data are saved to CSV files (inventory.csv and sales.csv)
    -   Data is loaded and cleaned from CSV files the moment the file is ran
      
- **Data Visualization: Basic sales data visualization using bar charts and pie charts

  ## Usage

  When you run the file the application will present a menu with the following options:

1.  Display Inventory
2.  Add Book
3.  Update Stock
4.  Process Sale
5.  View Sales Data
6.  Exit

**Display Inventory:-
  Will show the conent of the inventory.csv file(it will be shown like this{The book name by Author(ID:book_id)})

**Add book:-
  The app will ask you to enter book_id, title, author, genre, price and stock if the book alredy exsists you will receive an error messeage otherwise the book will be added to inventory.csv once you exit the app

**Update Stock:-
  The app will ask you to enter book_id once you entered the id it will ask you to enter the quantity to add to the stock

**Process sale:-
  The app will ask you to enter book_id once you entered the id it will ask you to enter the quantity to subtract from the stock and the transaction will be saved to the sales.csv once you exit the app

**View sales data:-
  the app will show two figures the first is a pie chart that will have sales by genre data, And the second is a horizontal bar chart that will have the sales by book data

**Exit:
  the app will exit and save the changes that where made during the app runtime
