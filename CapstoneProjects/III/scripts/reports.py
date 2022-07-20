#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
# For Pie Chart
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
# For Bar Chart
from reportlab.graphics.charts.barcharts import VerticalBarChart
import pandas



# Methods Start Here

def generate_total_sales_pie_chart(table_data):
  d = Drawing(250,250) # width, height
  pc = Pie()
  pc.x = 150
  pc.y = 15
  pc.width = 150
  pc.height = 150
  pc.data = table_data['total_sales'].tolist()[:15]
  pc.labels = table_data['car.car_make'].tolist()[:15]
  pc.sideLabels = 1
  pc.simpleLabels = 0
  pc.slices.strokeWidth = 0.5
  d.add(pc)
  return d
  
def generate_total_sales_bar_chart(table_data):
  drawing = Drawing(400, 200)
  # Expand the first 10 items from the table_data 
  data = [table_data['total_sales'].tolist()[:10] ]

  # Bar chart configuration
  bc = VerticalBarChart()
  bc.x = 75
  bc.y = 50
  bc.height = 125
  bc.width = 300
  bc.data = data
  bc.strokeColor = colors.black
  bc.bars[(0,)].fillColor = colors.cornflowerblue

  # The range of our y-axis 
  bc.valueAxis.valueMin = table_data['total_sales'][:10].min() - 1000
  bc.valueAxis.valueMax = table_data['total_sales'][:10].max() + 1000
  bc.valueAxis.valueStep = 3000

  # Label Configuration
  bc.categoryAxis.labels.boxAnchor = 'ne'
  bc.categoryAxis.labels.dx = 0
  bc.categoryAxis.labels.dy = -2
  bc.categoryAxis.labels.angle = 45
  bc.categoryAxis.categoryNames = table_data['car.car_make'].tolist()[:10]

  drawing.add(bc)
  return drawing

def generate(filename, title, additional_info, table_data, max_sales_by_car):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])

  
  # Pie Chart Details
  title = 'Car Makers: Total Sales' 
  pie_title_style = styles['h2']
  pie_title_style.alignment = 1
  pie_title = Paragraph(title, pie_title_style)
  pie = generate_total_sales_pie_chart(max_sales_by_car)

  # Bar Chart Details
  #bar = generate_total_sales_bar_chart(max_sales_by_car)
  title = 'Car Makers: Top Ten in Total Sales'
  bar_title_style = styles['h2']
  bar_title_style.alignment = 1
  bar_title = Paragraph(title, bar_title_style )
  bar = generate_total_sales_bar_chart(max_sales_by_car)


  # Table Details
  table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]
  report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

  empty_line = Spacer(1,30)
  report.build([report_title, empty_line, report_info, empty_line, pie_title, pie,empty_line, bar_title ,bar,empty_line, report_table])


