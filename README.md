# Stock Market Database Application
Basic GUI application for stock market database, created as a part of the database management course. Frontend used: Tkinter GUI, Backend: MySQL database

This project involves the implementation of a stock exchange database containing
information about some of the top-performing stocks in India (For our project, we
have chosen the NIFTY 50 index). The project consists of a graphical user
interface that has been developed using the tkinter package in python. The database
contains some of the major information required to identify a stock such as its
symbol, share price, total no of shares, net market capitalization, daily percentage
change and industry to which it belongs. The GUI enables the end-user to easily
make modifications in the share details, and also graphs have been implemented
along with the GUI that enables the user to clearly visualize the key-components of
the data, in a clear and precise manner.

![alt text](https://github.com/bharathbabu68/Stock-Market-Database-Application/blob/master/Picture1.png)

## Tools Used
- Tkinter for GUI (Frontend)
- SQLite3 for database(backend)
- MatPlotLib for plotting Graphs
- Python 3.7

## Functionalities
The project involves implementation of basic functionalities such as insert, update ,
delete operations on the stocks database, and provides the user with an interactive
GUI to easily make changes in it. The project also has functionalities like
username and password implemented for login functionality, allows the end-user to
purchase shares by entering his credentials, and also has a log table, which
describes the various operations that have been made in the database. The project
also has triggers to ensure the integrity of the database, and also lets the user, view
all his past transactions and analyze the data before making another purchase. The
output screenshots have been detailed and attached in the following pages.

## Login Window

The login details of the user logging in are stored in a database, and the user is allowed to login upon entering his correct credentials, if the user does not possess an account to login, then he can easily create a new account by clicking the create account button. The login details of the user are stored in a secure manner, and the passwords are encrypted and stored in the database via a secure algorithm.



## **Create Account Window**

The create account window asks the user for some basic information such as choice of username, some registered form of ID, age, emaild and password, which are stored in a table, in the database. Once an account, is created then the user will be allowed to login to the stock exchange GUI to perform his tasks.



## **Stock Exchange Window**

The stock exchange window comprises of many functionalities. The functionalities along with their output screenshots have been listed. The stocks database contains information about the top 50 performing companies during the financial year of 2019, in the NIFTY index.

1. Inserting, Updating and Deleting of data in stocks table


1) Required data can be inserted onto the table by typing the data about the stock onto the respective entry boxes, and then pressing the &#39;+&#39; image on the top.

2) Required data can be updated in the table by selecting the stock to update, and then pressing the &#39;update&#39; image on the top.

3) Required data can be deleted from the table by selecting the stock to delete, and then pressing the &#39;delete&#39; image on the top.


2) Searching for data in the stocks database

We can search for any stock in the database by making use of any of its characteristics such as company name, market cap, industry, share price, % change. The backend then sends a query to the database to retrieve the required data from the database.


We can also search using any of the other characteristics of a stock. Once you have filled the entries, make use of the &#39;search&#39; button on the top, to search.

Use clear all button, to clear all entries in the entry boxes.

![alt text](https://github.com/bharathbabu68/Stock-Market-Database-Application/blob/master/Picture2.png)

## **Graphs to analyze data**

Graphs have also been implemented to analyze the data in the stocks database. By conducting an analysis of the data between the various companies, we can determine which stock we want to buy, in this program we have implemented 3 graphs: company vs share price, share price vs market cap, and percent change vs the stock price.

They have been implemented using the matplotlib package, and the required type of graph can be chosen using the dropdown menu and clicking generate graph.

1 ) Share Price vs Market Cap

- We make use of a line graph to compare market cap and share price because we are tracking the differences between various companies&#39; market cap and share price.
- Graph is updated whenever a new value is inserted, updated or deleted via a trigger that links the graph&#39;s function with the database.

2 ) Percent change vs Stock Index Price

- We make use of a scatter graph to percent change and stock price because we are trying to use the correlation between a company&#39;s stock price change and its stock price to visualize the data.
- Graph is updated whenever a new value is inserted, updated or deleted via a trigger that links the graph&#39;s function with the database.

3 ) Company vs Share Price

- We make use of a bar graph to compare the company name, and the share price, so that we can visualize the earnings of the company
- X axis contains the company names, and y axes denotes the share prices of the company.

4)Market Domination of Companies

The button &#39;view greater cost companies&#39; contains information about various companies&#39; participation and domination in a particular industry. For ex: If we chose finance, then we get a list of all non-finance companies that have a higher share price than all that of the finance companies, hence showing market domination of the company.

A dropdown menu consisting of various industry sectors is present, and after choosing the sector, click &#39;view greater companies&#39; and the list of the dominating companies appears in the listbox.


Here , the listbox displays companies that have a higher share price than all companies belonging to the computer industry

## **Logs Window**

The &#39;view logs&#39; button when clicked opens a new window displaying the log table of the database. It displays the changes made in the database, along with the date and time of the change. Contains a refresh button, to update the log table after performing the changes such as insert, update, delete, etc.

Refresh button updates the log table.

**Code:**

Frontend: ltfrontend.py

Backend: ltbackend.py

## **Buy Stocks Window**

The buy stocks window is opened upon pressing the &#39;buy stocks&#39; button. The buy stocks window allows the user to purchase stocks onto his user account. He can then view his stocks by clicking the &#39;view cart&#39; button.

![alt text](https://github.com/bharathbabu68/Stock-Market-Database-Application/blob/master/Picture3.png)

**Output Screenshot:**


View all button when clicked displays all the details about the stocks available for sale, which are retrieved from the database.

**Buy Now Button:**

When the &#39;buy now&#39; button is clicked, the window extends itself prompting the user to enter the no of shares required to be bought. Also, the details of the stock is presented to the user, and upon clicking the confirm purchase button, the transaction is complete.

**Code:** frontend: &#39;buystockfrontend.py&#39; backend: &#39;buystockbackend.py&#39;
