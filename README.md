# whats-in-your-fridge
# Inspiration
Student time management when it comes to deciding on what to cook with items they have. Eating out on a daily basis is not healthy.

# What it does
Recommends recipes based on ingredients in the kitchen and user behavior that is what the person likes to eat and has liked in the past so that the ingredients are used before they expire!

# How we built it
Created recommendation engine that makes use of content based filtering using python and frontend was developed using django, html, js and css.

# What's next for What's In Your Fridge
Integrate it with smart devices /smart fridge /and with grocery apps like wegmans and walmart to recommend ingredients that you might buy to make a specific recipe.

# Application Flow
* Choose whether you wanna add items to the fridge or cook today!

![home_web](https://user-images.githubusercontent.com/26019260/164943774-aff08f4b-cd19-42dc-900a-55d6ec88c86f.PNG)

* If you decided to add, feed your fridge list with the new items you got from the grocery store!

![add_web](https://user-images.githubusercontent.com/26019260/164943810-ff37ab24-139d-46a3-8191-3c458bc44148.PNG)

* If you chose to cook today, get all the dishes you can make using those ingredients!!

![cook_web](https://user-images.githubusercontent.com/26019260/164943854-55718a9d-ad42-4c78-8a55-12449f0f58df.PNG)

* Wanna try a recipe similar to those you've already tried! You can get those by clicking any of the recipes from the previous list! 

![recom_web](https://user-images.githubusercontent.com/26019260/164943902-4f76bc2c-d5ec-423b-89ee-77970fe294a8.PNG)

# Running Instructions
## Requirements
Python3 with django and requests module.

## Running instructions
To run clone repository using git clone <repository link>
Run using below command in base directory python3 manage.py runserver
