import daydrawing

class DayImageOnDate(object):
    """docstring for DayOnDate"""
    drawing_precision = 4

    def __init__(self, location, date, precision=drawing_precision):
        self.location_lat_lng = daydrawing.valid_location(location)
        self.date = daydrawing.is_valid_date(date)
        self.precision = precision
        self.sunrise, self.sunset = daydrawing.sun_on_date(self.location_lat_lng, self.date)

    def make_drawing(self):
        self.drawing = daydrawing.make_day(self.sunrise, self.sunset, self.drawing_precision)
        return self.drawing



#my = DayImageOnDate("koper", "2000-06-11")
#my.drawing_precision = 5
#print my.make_drawing()


def compare_locations(locations, date, precision=4):
    location_drawings = []
    for loc in locations:
        drawing = DayImageOnDate(loc, date).make_drawing()
        drawing += "    " + loc + "on" + date + "\n"
        location_drawings.append(drawing)

    return "".join(location_drawings)


def compare_dates(location, dates, precision=4):
    date_drawings = []
    for date in dates:
        drawing = DayImageOnDate(location, date).make_drawing()
        drawing += "    " + location + " on " + date + "\n"

        date_drawings.append(drawing)

    return "".join(date_drawings)

locations = ["koper", "warwick", "quito"]
#print compare_locations(locations, "2016-04-22")
dates = ["2015-12-20", "2015-06-21"]
print compare_dates("quito", dates)

