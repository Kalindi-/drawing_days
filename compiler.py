# Code to render content to be hosted on google app engine

import os
import webapp2
import jinja2
import daydrawing

from google.appengine.ext import ndb


template_dir = os.path.join(os.path.dirname(__file__), "templates")
JINJA_ENVIRONMENT  = jinja2.Environment(
                loader = jinja2.FileSystemLoader(template_dir),
                autoescape = True)

location = "melbourne"
day = "2017-01-01"

class Page(webapp2.RequestHandler):

    def get(self, reg_input=""):

        location, date = "melbourne", "2017-01-01"
        template_values = {
            "day_percentages": {
                "sunrise" : 24,
                "sunset" : 80
            }
        }

        user_location = self.request.get('location')
        user_date = self.request.get('date')

        if user_location and user_date:
            location, date = user_location, user_date

        page_dictionary = {"": "index.html"}
        html_template = page_dictionary[reg_input]

        sun_data = daydrawing.sun_on_date(location, date)

        if sun_data:
            day_percentages = daydrawing.get_day_percent(sun_data)

            if day_percentages:
                template_values["day_percentages"] = day_percentages
        else:
            template_values["error"] = True

        template_values["date"] = date
        template_values["location"] = location


        template = JINJA_ENVIRONMENT.get_template(html_template)
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([(r'/', Page)
                              # ('/(\w+)', Page),
                              ],
                              debug = True)

# https://cloud.google.com/appengine/docs/python/tools/libraries27#vendoring