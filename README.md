# Introduction

in this readme file you will find all the documentation that has been done over all the labs that have something to do about the development in networking. screenshots will have an explanation if needed.

## LAB 1 - Python Experiments

### 1.1 task preperation and implementation

I would have to do research on how to install all these tools/packages
sources: <br>
https://docs.python-guide.org/starting/install3/linux/ <br>
https://jupyter.org/install <br>
https://www.python.org/downloads/

### 1.1 task troubleshooting:

at first there were some problems with the dependencies that python requires, so I would have to start from scratch so to be able to fix the issues.

### 1.1 task verification
![image](https://github.com/DennisRomeijnPXL/master/assets/73332330/243abfdc-e251-436f-8f8e-c24340883a67)
![image](https://github.com/DennisRomeijnPXL/master/assets/73332330/aebe1789-1c7c-482c-a3d6-437ab5528b3b)
![image](https://github.com/DennisRomeijnPXL/master/assets/73332330/6bbe6664-75f5-4b36-a5a9-c222ddafda18)
![image](https://github.com/DennisRomeijnPXL/master/assets/73332330/28e63db3-d2e8-46f6-9839-3dc6c8fcddb6)

### 1.2 task preperation and implementation

At the beginning we would have to get the code from the github repository and place it in a file on our DEVASC machine. After that we use python3 (file) to activate said file.

### 1.2 Task troubleshooting

The files worked

### 1.2 task verification
![image](https://github.com/DennisRomeijnPXL/master/assets/73332330/f3f759d2-720b-458c-9c35-3a221d090d15)
![image](https://github.com/DennisRomeijnPXL/master/assets/73332330/7f8e93e2-b6b5-4b30-be3d-fa44f4cea1df)
![image](https://github.com/DennisRomeijnPXL/master/assets/73332330/1615ee7b-1ade-483c-a6f8-81627fd9c125)

## Lab 2 - Explore rest APIs with API-simulator and postman

### 2.1 task preperation and implementation

Open the website library.demo.local

### 2.1 task troubleshooting

no problems have occured.

### 2.1 task verification
![image](https://github.com/DennisRomeijnPXL/master/assets/73332330/ecbeed52-c07c-4a6a-ad37-b75a6c88815b)
![image](https://github.com/DennisRomeijnPXL/master/assets/73332330/8d7bb564-6502-4d6e-a0ec-f983a9e2fd09)
change IncludeISBN value to true. 
![image](https://github.com/DennisRomeijnPXL/master/assets/73332330/0f447eda-2383-4db7-9bd4-6d3d387cb73e)
You will get these responses
![image](https://github.com/DennisRomeijnPXL/master/assets/73332330/1c843781-7580-4ca0-84c2-ca42b3106588)

You have to sign in when doing the POST/LoginViaBasic
![image](https://github.com/DennisRomeijnPXL/master/assets/73332330/fa2252aa-1544-4e87-afa8-1a6e1421f7a4)
![image](https://github.com/DennisRomeijnPXL/master/assets/73332330/a1f7bc70-c735-4c16-87f1-ec08e09e061a)
after receiving this token you can login with that token in the top right using the "Authorize" button 

to add a new book you do this:
![image](https://github.com/DennisRomeijnPXL/master/assets/73332330/1f9110dc-b99f-4928-919c-03e8a444902a)

When you want to get a specific book and you know the id, you do this
![image](https://github.com/DennisRomeijnPXL/master/assets/73332330/9ea5754e-5434-42cc-a511-e81ef562a753)

and this is how you remove that book:
![image](https://github.com/DennisRomeijnPXL/master/assets/73332330/30875325-b3fa-4cbd-a1f3-c01038bf8242)

### 2.2 task preperation and implementation

open school library API in the chromium broswer and postman

### 2.2 task troubleshooting

no errors were found

### 2.2 task verification

by using the given link we click send to get a reply in the bottom tab.
![image](https://github.com/DennisRomeijnPXL/master/assets/73332330/e8706b32-da2a-40a0-b7c9-5f21ec8bf1a5)

putting a username and password you can do a POST
![image](https://github.com/DennisRomeijnPXL/master/assets/73332330/69c5ae11-a8eb-4056-8fa8-1e3369593cfa)

after putting in the right values in the authorization tab and clicking raw in the body tab. you can click send and see that it worked.
![image](https://github.com/DennisRomeijnPXL/master/assets/73332330/6b7e67bc-0e5e-409c-870d-f557138b998d)

![image](https://github.com/DennisRomeijnPXL/master/assets/73332330/5766c49c-3252-4b4d-aa88-30ccdd9175ca)

after doing a GET request with the given link you can see that it's sorted in the way we wanted
![image](https://github.com/DennisRomeijnPXL/master/assets/73332330/ecd2fba0-dc84-4f76-8e2b-e1d1f8ef5963)

### 2.3 task preperation and implementation

open visual studio code and have python updated

### 2.3 task troubleshooting

none

### 2.3 task verification

we have to open python3 in the terminal and then type 
  ```sh
  import fake from Faker
  fake = Faker()
```
![image](https://github.com/DennisRomeijnPXL/master/assets/73332330/ff154c95-7378-451f-832b-dc44db79d994)
  
the second exersice:
![image](https://github.com/DennisRomeijnPXL/master/assets/73332330/e84afb99-fd3b-4da4-895e-08da4820ec0c)

![image](https://github.com/DennisRomeijnPXL/master/assets/73332330/8c6fd550-b730-40e9-a6fb-3b0588aac460)

on the library.demo.local site you go back to get/books to check if they're added:
![image](https://github.com/DennisRomeijnPXL/master/assets/73332330/dea5acd0-b69a-4a4a-9a17-e58c5dea336d)

to add another 100:

![image](https://github.com/DennisRomeijnPXL/master/assets/73332330/8631800e-f592-450d-9b71-941d095e164e)

## Lab 3 

### 3 task preperation and implementation

all I needed to prepare was have python3 and visual studio installed.

### 3 task troubleshooting

///

### 3 task verification

all the python files are put in the lab 3 folder and they can be tested out.

## Lab 4

an entire document has been placed in the lab 4 folder that has all the information needed

## lab 5 

### 5.2 task preperation and implementation

the unittest framework had to be on the machine.

### 5.2 task task troubleshooting

there were a lot of problems with the indendations of the code, so I had to manually fix that.

### 5.2 task verification

after putting the code in unittest/recursive_json_search.py
![image](https://github.com/DennisRomeijnPXL/master/assets/73332330/0cb85a9a-94b7-49d7-aab8-7853e5bfedf6)

