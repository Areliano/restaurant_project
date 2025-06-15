Hello, this is an explanation on how to run this poject locally on your machine, i tried to deploy it but it failed. If you know how to deploy a Django project, reach out to me.
I'll upload screenshots of the website. So this is a Restaurant Management website.

# 🍽️ Restaurant Management System

This is a Django-based web application designed to help restaurant owners and managers manage menus, customer records, reservations, and more. This guide will walk you through how to set it up on your own computer — even if you're new to coding.

---

## 🧰 Step 1: Get the Project on Your Computer

There are two ways to get this project:

### Option A: Clone the Repository (Recommended if you have Git)
1. Open **Git Bash** or **Terminal**.
2. Navigate to the folder where you want to save the project.
3. Run the following command on your terminal:
   ```bash
   git clone https://github.com/Areliano/restaurant_project.git
   
### Option B: Download ZIP
1. Go to the repository page on GitHub.

2. Click the green "Code" button → "Download ZIP".

3. Unzip the downloaded folder on your computer.

### 🖥️ Step 2: Open the Project in an IDE
You can use any Python-friendly IDE or code editor. I recommend:

a. PyCharm

b. VS Code

## After opening the project, make sure your IDE uses Python 3.8 

### Step 3: Set Up a Virtual Environment (Optional but Recommended)
Using a virtual environment keeps your project dependencies isolated.

In terminal (inside the project folder), run:
    python -m venv venv

Activate the virtual environment:
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

### 📦 Step 4: Install Required Packages
The project depends on some external Python packages like Django and Pillow.
On your terminal, paste these commands, one at a time:

     pip install django
     pip install requests
     pip install Pillow  

                OR 
You can use just this one command on the terminal

       pip install django pillow requests python-decouple django-crispy-forms

### 🔐 Step 5: Create a Superuser (Admin Account)
 1. To access the Django admin dashboard and manage the restaurant system, you need to create a superuser (an admin account).

 2. In your terminal (with the virtual environment activated), run:
            python manage.py createsuperuser
You’ll be prompted to enter:

Username (e.g., admin)

Email address (optional)

Password (must be at least 8 characters)

After successful creation, you can log in to the admin panel at:   127.0.0.1:8000/admin        This should be on your browser

  ## Use the username and password you just created to log in.


### ⚙️ Step 5: Run the Project
Now that everything is installed, you can run the project.

In terminal (inside the project folder), run:

    python manage.py runserver


### after running the project successfully, this should be displayed on your terminal
![img.png](img.png)

### after seeing that on your terminal, go to your browser and type 127.0.0.1:8000 on one tab and on the next tab 127.0.0.1:8000/admin   and the following should be displayed
![img_1.png](img_1.png)    This is for  127.0.0.1:8000
![img_2.png](img_2.png)           This is the admin side of the website

### Remember the username and passwod you created in step 5: Create a Superuser (Admin Account), use those credentials to login to both the admin side and the customer side.

## NB: IF THE CREDENTIALS YOU USED DON'T WORK FOR SOME REASON, YOU CAN CREATE ANOTHER SUPER USER ACCOUNT OR USE MY CREDENTIALS:
                  username:  hussein
                  password:  hussein

###  NOW LET ME EXPLAIN HOW THE WEBSITE WORKS

![img_3.png](img_3.png)     

### This is what you see when you login on the customer side of the website, I will only explain the main parts, so i won't explain the following pages since they are obvious:
            1. Homepage
            2. Aboutpage
            3. Contactpage

![img_4.png](img_4.png) 

![img_5.png](img_5.png)

#### These are screenshots of the specialties page which basically displays the menu. This page has a real-time stock inventory system. As you can see from the screenshots, it displays when an item's stock is less than 5, and when the stock is finished, the order button is disabled.
#### That is on the customer side, Let's now look at how the admin can add the stock from the admin side. 

![img_6.png](img_6.png)

### This is what you will see first when you login to the admin side of the website.

## To add stock/inventory, click on ourmenus and the following will be displayed

![img_7.png](img_7.png)

### Click on whatever you want to stock up and the following will be displayed: 
![img_8.png](img_8.png)

### EDIT WHATEVER YOU WANT AND CLICK SAVE. iF YOU ALSO WANT TO ADD ANOTHER ITEM ON THE MENU, YOU CAN ADD IT ON THE OURMENUS SECTION: 
![img_9.png](img_9.png)   YOU CAN ADD ANOTHER ITEM THAT IS NOT ON THE MENU BY CLICKING THE "ADD OURMENU+" BUTTON AT THE TOP RIGHT SIDE, ABOVE THE SECTION WRITTEN FILTER

![img_10.png](img_10.png)    THIS IS WHAT WILL BE DISPLAYED WHEN YOU WANT TO ADD AN ITEM TO THE MENU.  YOU CAN ALSO DELETE AN ITEM USING THE DELETE BUTTON


### Still on the Specialties page, a customer can place an order by clicking on the order now button of the item they want to order and the following form will be displayed:

![img_11.png](img_11.png)

### after placing the order, an email will be sent to the email on the order containing the details of the order: 

![img_12.png](img_12.png)
![img_13.png](img_13.png)

## The orders page is where all the orders are displayed.

##This is the reservations page where one can reserve a table

![img_14.png](img_14.png)

![img_15.png](img_15.png)

# It is a real-time table reservation system


## RESERVATION ON THE ADMIN SIDE

# On the admin side, one can edit the number of tables available for reservation by doing the following

1. Go to the admin side, on the section written Tables 
2. ![img_16.png](img_16.png)
3. You can add or edit a table. You can also delete a table.
4. ![img_17.png](img_17.png)   
5. Make sure to save the edited changes.
6. ![img_18.png](img_18.png)
7. You can also go to the Reservations section on the admin side and see the number of people who have reserved tables or even edit them or delete them.
8. The Booked page on the Customer side displays the number of people who have made table reservations at the Restaurant as shown by the screenshots below:
9. ![img_19.png](img_19.png)
10. ![img_20.png](img_20.png)
11. Upon making a Reservation, an email is sent to the person who reserved the table together with the details of the resevation.


## REPORT SECTION
1. The reports are only available on the frontend side, and can only be accessed by an account that has super user priviledges/ an admin account. Normal customers won't be abe to see these reports
2. ![img_23.png](img_23.png)
3. ![img_22.png](img_22.png)
4. ![img_24.png](img_24.png)

5. To let a normal account access the reports, or to upgrage a customer account to have admin priviledges, let the customer register first,then go to the admin side on the section written Users and click on it, The number of people who have registered on the website will be displayed.

6. ![img_25.png](img_25.png)

7. Select the user whose status you want to upgrade.

8. ![img_26.png](img_26.png)

9. On the Permissions section, tick Staff Status and Super User status.


# Other screenshots
1. ![img_27.png](img_27.png)     THIS IS THE REGISTRATION PAGE

2. ![img_28.png](img_28.png)  ![img_29.png](img_29.png)   THE BLOG PAGE

3. ![img_30.png](img_30.png)  ![img_31.png](img_31.png)   THE CONTACT PAGE

4. ![img_32.png](img_32.png) THIS IS HOW THE FOOTER LOOKS LIKE, YOU CAN EDIT IT'S CONTENTS ON THE ADMIN SIDE ON THE SECTION "FOOTERS"   ![img_33.png](img_33.png)

5. NB: THIS PROJECT IS FULLY DYNAMIC WHICH MEANS THAT YOU CAN EDIT OR CHANGE MOST OF THE THINGS ON THE WEBSITE FROM THE ADMIN SIDE WITHOUT HAVING TO GO BACK TO THE CODE, HENCE IT IS USER FRIENDLY.






