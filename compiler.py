# Code to render content to be hosted on google app engine

import os
import webapp2
import jinja2

from google.appengine.ext import ndb

# import day_image_class

template_dir = os.path.join(os.path.dirname(__file__), "templates")
JINJA_ENVIRONMENT  = jinja2.Environment(
                loader = jinja2.FileSystemLoader(template_dir),
                autoescape = True)


class Page(webapp2.RequestHandler):

    def get(self, reg_input=""):

        day = ["20", "80"]
        #day2 = ["30", "70"]

        page_dictionary = {
            "" : "index.html"
            #"x" : "x"
        }

        html_template = page_dictionary[reg_input]
        template_values = {
            "day": day
            #"day2": day2
        }

        template = JINJA_ENVIRONMENT.get_template(html_template)
        self.response.write(template.render(template_values))


app = webapp2.WSGIApplication([(r'/', Page),
                              # ('/(\w+)', Page),
                              ],
                              debug = True)

# https://cloud.google.com/appengine/docs/python/tools/libraries27#vendoring