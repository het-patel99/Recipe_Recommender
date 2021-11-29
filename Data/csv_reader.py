import pandas as pd
import random

def restaurant_data(r1_cuisine, r2_cuisine, r2_restaurant, r):
        if r2_cuisine == r1_cuisine:
            r = r + str(r2_restaurant) + "% "
        elif r2_cuisine in r1_cuisine:
            r = r + str(r2_restaurant) + "% "
        elif r1_cuisine == 'Punjabi' and r2_cuisine == 'North Indian':
            r = r + str(r2_restaurant) + "% "
        elif r1_cuisine == 'Indian' and r2_cuisine in ['South Indian', 'Gujarati', 'North Indian']:
            r = r + str(r2_restaurant) + "% "
        elif r2_cuisine == 'South Indian':
            r = r + str(r2_restaurant) + "% "
        return r
        
def diet_type_data(r1_cleaned_ingredients):
        if 'chicken' in r1_cleaned_ingredients or 'fish' in r1_cleaned_ingredients:
            return "Non-Vegetarian"
        elif 'milk' in r1_cleaned_ingredients or 'paneer' in r1_cleaned_ingredients or 'curd' in r1_cleaned_ingredients or 'butter' in r1_cleaned_ingredients or 'ghee' in r1_cleaned_ingredients or (r1_cleaned_ingredients.count('egg') != r1_cleaned_ingredients.count('eggsplant')) or (r1_cleaned_ingredients.count('egg') != r1_cleaned_ingredients.count('eggplant')):
            return "Vegetarian"
        else:
            return "Vegan"

def location_data(r1_cuisine, r2_cuisine, r2_location, l):
        if r2_cuisine == r1_cuisine:
            l = l + str(r2_location) + "% "
        elif r2_cuisine in r1_cuisine:
            l = l + str(r2_location) + "% "
        elif r1_cuisine == 'Punjabi' and r2_cuisine == 'North Indian':
            l = l+ str(r2_location) + "% "
        elif r1_cuisine == 'Indian' and r2_cuisine in ['South Indian', 'Gujarati', 'North Indian']:
            l = l+ str(r2_location) + "% "  
        elif r2_cuisine == 'South Indian':
            l = l+ str(r2_location) + "% "
        return l

def csv_read():
    df1 = pd.read_csv('Cleaned_Indian_Food_Dataset.csv')
    df2 = pd.read_csv('Cuisine.csv')

    cnt = 0

    df1 = df1.fillna('')

    for ind1, row1 in df1.iterrows():

        cnt+=1
        row1['Cleaned-Ingredients'] = row1['Cleaned-Ingredients'].lower()
        df1.at[ind1, 'Recipe-rating'] = str(random.randrange(1, 5))
        restaurant = ""
        location = ""
        
        for ind2, row2 in df2.iterrows():
            restaurant = restaurant_data(row1['Cuisine'], row2['Cuisine'], row2['Restaurant'], restaurant)
            location = location_data(row1['Cuisine'], row2['Cuisine'], row2['Location'], location)
        restaurant = restaurant[:len(restaurant)-2]
        location = location[:len(location)-2]
        df1.at[ind1, 'Restaurant'] = restaurant
        df1.at[ind1, 'Restaurant-Location'] = location.strip('\n')
        df1.at[ind1, 'Diet-type'] = diet_type_data(row1['Cleaned-Ingredients'])

    df1.to_csv('final_recipe_recommender.csv', index=False)
    
#csv_read()
