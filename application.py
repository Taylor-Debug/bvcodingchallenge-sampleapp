from flask import Flask
from flask import render_template
from datetime import datetime
from helpers.stats_helper import StatsHelper

app = Flask(__name__)
stats_helper = StatsHelper()

@app.route('/')
def homepage():
    # HINT: Pass variables through to the HTML using Flask - https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
    return render_template('index.html', avg_r = get_average_overall_rating(), top_five = [get_top_five()], best_style = get_best_appearance(), avg_t = get_avg_taste(), avg_p = get_avg_palate())

# HINT: This could be your first statistic!
def get_average_overall_rating():
    return stats_helper.caculate_ave_overall_rating()

def get_top_five():
    return stats_helper.top_five_beers()


def get_best_appearance():
    return stats_helper.calculate_best_style()

def get_avg_taste():
    return stats_helper.calc_avg_taste()

def get_avg_palate():
    return stats_helper.calc_avg_palate()