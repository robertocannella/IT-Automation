#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(paragraph, title, attachment_path):

    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment_path)
    report_title = Paragraph(title, styles["h1"])
    empty_line = Spacer(1,10)

    # Table Details
    table_style = [ ('FONTNAME', (0,0), (-1,0), 'Helvetica'),
                    ('ALIGN', (0,0), (-1,-1), 'LEFT')]
    report_table = Table(paragraph, style=table_style, hAlign="LEFT", rowHeights=10)

    report.build([report_title,empty_line,report_table])
    print("building report")
    return report
