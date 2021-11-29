import os
import sys
sys.path.append(os.path.abspath('../../'))

from Recipe_Recommender.Data.csv_reader import restaurant_data, location_data, diet_type_data 

def test_restaurant_data_punjabi():
    assert "Punjabi Dhaba" in restaurant_data("Punjabi", "North Indian", "Punjabi Dhaba", "")
    
def test_restaurant_data_indian():
    assert "Indian" in restaurant_data("Indian", "Gujarati", "Indian", "")
    
def test_location_data():
    assert "Raleigh" in location_data("Punjabi", "North Indian", "Raleigh", "")

def test_diet_type_data_Non_Veg():
	assert "Non-Vegetarian" in diet_type_data("chicken")

def test_diet_type_data_Veg():
	assert "Vegetarian" in diet_type_data("milk")

def test_diet_type_data_Vegan():
	assert "Vegan" in diet_type_data("oats")
