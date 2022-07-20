#!/usr/bin/env python3

from distutils.command.install_egg_info import to_filename
import json
import locale
from pty import slave_open
import sys
import operator
import reports
import emails
import pandas as pd

def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data

def process_data_frames(df):
  # create a total_revenue column to get max_revenue
  df['price'] = df['price'].str.strip("$")
  df['total_revenue'] = df['price'].astype(float) * df['total_sales'].astype(float)
  df = df.sort_values(by=['total_revenue'], ascending=False)

  # Car with the most total revenue
  max_revenue_index = df['total_revenue'].idxmax()
  max_revenue = df.loc[max_revenue_index]

  # Car with the most total sales
  max_sales_index = df['total_sales'].idxmax()
  max_sales = df.loc[max_sales_index]

  # Year with the most sales
    # Group by year
  sales_by_year = df.groupby(df['car.car_year'])['total_sales'].sum().reset_index()
  max_sales_by_year_index = sales_by_year['total_sales'].idxmax()
  max_sales_by_year = sales_by_year.loc[max_sales_by_year_index]



  summary = [
    "The {} generated the most revenue: ${}".format(format_car_df(max_revenue), max_revenue['total_revenue'] ),
    "The {} had the most sales: {}".format(format_car_df(max_sales), max_sales["total_sales"]),
    "The most popular year was {} with {} sales.".format(max_sales_by_year['car.car_year'], max_sales_by_year['total_sales'])
  ]
  return summary

def get_max_sales_by_car(df):
  # Group by car make
  max_sales =  df.groupby(df['car.car_make'])['total_sales'].sum().reset_index()
  return max_sales.sort_values('total_sales', ascending=False)
def format_car_df(car):
  """Given a car dataframe, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car.car_make"], car["car.car_model"], car["car.car_year"])

def cars_dataframe_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  # Sort by total_sales (additional project task item)
  car_data = car_data.sort_values(by=['total_sales'], ascending=False)
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for index,row in car_data.iterrows():
    table_data.append([index, format_car_df(row), row["price"], row["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data into a Pandas DataFrame and generate a full report out of it."""
  # Get the data
  data = load_data("data/car_sales.json")

  # Set up the dataframe (collapse nested objects)
  df = pd.json_normalize(data)
  df = df.set_index('id')

  # Get summary (top performers)
  summary_df = process_data_frames(df)
  print(summary_df)

  # Generate PDF 
  # Year with the most sales (Optional Task)
  max_sales_by_car = get_max_sales_by_car(df)

  cars_list = cars_dataframe_to_table(df)
  body = "<br/>".join(summary_df)
  reports.generate('/tmp/cars.pdf','Sales summary for last month', body , cars_list, max_sales_by_car)

  # Send the PDF report as an email attachment
  sender = 'automation@example.com'
  recipient = 'student-01-f3ca5d8d5514'
  subject = 'Sales summary for last month'
  body = '\n'.join(summary_df)
  attachment_path = '/tmp/cars.pdf'

  email = emails.generate(sender,recipient, subject, body, attachment_path)
  #print(email)
  #emails.send(email)

if __name__ == "__main__":
  main(sys.argv)