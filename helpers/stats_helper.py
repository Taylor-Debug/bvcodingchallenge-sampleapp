from helpers.database_helper import Database


class StatsHelper():

    def __init__(self):
        self.database = Database()
        print("Stats Helping initialising!")

    def caculate_ave_overall_rating(self):
        result = self.database.fetch_one("SELECT AVG(review_overall) FROM reviews")
        return result[0]

    def top_five_beers(self):
        result = self.database.fetch_one("SELECT beer_name, AVG(review_taste) FROM reviews GROUP BY beer_name ORDER BY review_taste DESC LIMIT 5")
        return result[0]    
        
    def worst_five_beers(self):
        result = self.database.fetch_one("SELECT beer_name, AVG(review_overall), AVG(review_taste) FROM reviews GROUP BY beer_name ORDER BY review_overall ASC LIMIT 5")
        return result[0]    

    # HINT: You can define more queries here, along with some python logic to calculate!
    def calculate_another_stat(self):
      # all_rows = self.database.fetch_all("")
      return None

    def myMethod_test(self):
       result = self.database.fetch_one
