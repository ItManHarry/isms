'''
Form handling with class-based views
Form processing generally has 3 paths:
    1. Initial GET (blank or prepopulated form)
    2. POST with invalid data (typically redisplay form with errors)
    3. POST with valid data (process the data and typically redirect)
Implementing this yourself often results in a lot of repeated boilerplate code
(see Using a form in a view). To help avoid this, Django provides a collection
of generic class-based views for form processing.
'''