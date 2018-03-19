'''
Created on Mar 16, 2018

@author: 10643275
'''

import Movie
from xlrd import open_workbook
from xlrd.xldate import xldate_as_tuple, xldate_from_date_tuple,\
    xldate_from_datetime_tuple, xldate_as_datetime
from datetime import datetime
from builtins import str
 
# Convert the .csv file to .xlsx, since xlrd only supports .xls and .xlsx files
# FUTURE SCOPE. For now, convert the below files explicitly and use...

movies_list = []
# Read the .xlsx files and populate movies_list list
wb = open_workbook('Movie-Data.xlsx')
for sheet in wb.sheets():
    number_of_rows = sheet.nrows
    number_of_cols = sheet.ncols
    # print("No. of rows and cols: " + str(number_of_rows) + "," + str(number_of_cols))
    
    for row in range(1, number_of_rows):
        values = []
        for col in range(0, number_of_cols):
            value = sheet.cell(row, col).value
            if col == 4:
                value = xldate_as_datetime(value, wb.datemode)
                value = str(value.date()).replace('-','/')
            elif col == 0 or col == 1 or col == 2 or col == 3 or col == 5:
                value = str(value)
            values.append(value)
        movies_list.append(Movie.Movie.create_movie_from_datafile(values))
    # print(len(movies_list))    # 608

wb = open_workbook('Movie-Ratings.xlsx')
for sheet in wb.sheets():
    number_of_rows = sheet.nrows
    number_of_cols = sheet.ncols
    # print("No. of rows and cols: " + str(number_of_rows) + "," + str(number_of_cols))
    
    for row in range(1, number_of_rows):
        values = []
        for col in range(0, number_of_cols):
            value = sheet.cell(row, col).value
            if col == 0 or col == 1 or col == 5:
                value = str(value)
            values.append(value)
        movies_list.append(Movie.Movie.create_movie_from_ratingsfile(values))

print(len(movies_list))    # 1167

# Find duplicates in the movies_list and merge them
count = 0
for x in movies_list:
    for y in movies_list:
        print("Checking:" + x.movie_title + " vs." + y.movie_title)
        if x is y:
            print("continued")
            continue
        if x.equals_movie(y):
            print("equal")
            x.fill_details_from_movie(y)
            movies_list.remove(y)
            count += 1
        print('Unequal\n')
print("Duplicate count = " + str(count))
print("Movies List len = " + str(len(movies_list)))