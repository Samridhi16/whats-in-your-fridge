import sqlite3
import pandas as pd
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class RecommendationEngine:
    """
        Recommendation Engine to recommend recipies
    """
    __slots__ = 'input_dataset','recipes_with_ratings_frequency','current_fridge_items'

    def __init__(self,input_dataset):
        """
                Initializes the dataset to be used for recommendation
                :param input_dataset:   Original dataset of recipies Id,Recipe Name and Ingredients
                :param recipes_with_ratings_frequency: Original dataset with ratings and frequency features added to it
                :param current_fridge_items: Current items in your fridge
        """
        self.input_dataset = input_dataset
        self.recipes_with_ratings_frequency = []
        self.current_fridge_items = []

    def recommend_recipes(self):
        """
                Create dataset with all the ingridients present in the fridge
        """
        self.recipes_with_ratings_frequency = pd.DataFrame(columns=['Name', 'Category', 'Ingredients', 'Rating', 'frequency'])

        data = pd.read_csv(self.input_dataset)

        self.recipes_with_ratings_frequency['Name'] = data['Recipe Name']
        self.recipes_with_ratings_frequency['Ingredients'] = data['Ingredients']


        #generate random ratings and frequencies and create list of ingridients
        for i in range(len(self.recipes_with_ratings_frequency)):
            self.recipes_with_ratings_frequency.loc[i, "Rating"] = random.randint(1, 5)
            self.recipes_with_ratings_frequency.loc[i, "frequency"] = random.randint(0, 10)
            ingrd = self.recipes_with_ratings_frequency.loc[i, "Ingredients"].split(",")
            self.recipes_with_ratings_frequency.loc[i, "Ingredients"] = ingrd

        #dummy fridge items
        # import numpy as np
        # self.current_fridge_items = set(np.concatenate((self.recipes_with_ratings_frequency.loc[5, "Ingredients"], self.recipes_with_ratings_frequency.loc[81, "Ingredients"],
        #                                         self.recipes_with_ratings_frequency.loc[369, "Ingredients"],self.recipes_with_ratings_frequency.loc[9245, "Ingredients"],
        #                                         self.recipes_with_ratings_frequency.loc[10438, "Ingredients"])))

        self.fetchItems()

        possible_recipes = pd.DataFrame(columns=['Name', 'Category', 'Ingredients', 'Rating', 'frequency'])
        for i in range(len(self.recipes_with_ratings_frequency)):
            if set(self.recipes_with_ratings_frequency.loc[i, "Ingredients"]).issubset(self.current_fridge_items):
                possible_recipes.loc[len(possible_recipes.index)] = self.recipes_with_ratings_frequency.loc[i]

        possible_recipes = possible_recipes.sort_values(["frequency", "Rating"], ascending=(False, False))

        recommended_recipes = self.get_recommendations('Lollipop Sugar Cookies Recipe')
        return recommended_recipes

    #fetch
    def fetchItems(self):
        """
            Fetch newly added fridge items from the user and store it into the database
        """
        db = sqlite3.connect('db.sqlite3')
        sql = "SELECT * from mainapp_addmodel"
        cur = db.cursor()
        cur.execute(sql)
        record = cur.fetchall()
        self.current_fridge_items = set()
        for item in record:
            self.current_fridge_items.add(item[1])
        print(self.current_fridge_items)
        db.close()

    def get_recommendations(self,name):
        """
            Create Vectors of inrgedients and compare recipes based on cosine similarities
        """
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(self.recipes_with_ratings_frequency['Ingredients'])
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

        idx = self.recipes_with_ratings_frequency.index[self.recipes_with_ratings_frequency['Name'].str.strip() == name][0]
        sim_scores = list(enumerate(cosine_sim[idx]))

        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        sim_scores = sim_scores[1:11]

        food_indices = [i[0] for i in sim_scores]
        return self.recipes_with_ratings_frequency['Name'].iloc[food_indices]

