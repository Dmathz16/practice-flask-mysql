from flask import abort, Blueprint, render_template, send_file, current_app
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import portrait, landscape, A4
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

import io, os

generate_pdf = Blueprint('generate_pdf', __name__)

title   = 'Generate PDF'
view    = 'generate-pdf'

@generate_pdf.route('/generate-pdf/')
def index():
    data = { "title": title, "view": view }
    return render_template('generate_pdf/index.html', data=data)

@generate_pdf.route('/generate-pdf/print/')
def print():
    pdf_data = io.BytesIO()
    
    c = canvas.Canvas(pdf_data, pagesize=portrait(A4))
    canvas_width, _ = portrait(A4)
    
    side_margin = 50
    c.setTitle('Some Title')
    
    c.drawString(side_margin, 750, "Hello World!")
    
    # Create table data
    data = [
        ['Column 1', 'Column 2', 'Column 3', 'Column 4'],
        ['Data 1', 'Data 2', 'Data 3', 'Data 4'],
        ['Data 5', 'Data 6', 'Data 7', 'Data 8']
    ]
    
    # ============================ TABLE ============================
    # Create table
    table_columns = 4
    table = Table(data, colWidths=((canvas_width-(side_margin*2))/table_columns)) 

    # Add style to table
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (-1, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ]))

    # Draw table on the canvas
    table.wrapOn(c, 0, 0)  # Width and height of the table
    table.drawOn(c, side_margin, 650)  # Position of the table
    # ============================ TABLE ============================
    
    # ============================ IMAGE ============================
    image_path = os.path.join(current_app.root_path, 'static', 'img', 'logo.jpg')
    if os.path.isfile(image_path):
        c.drawImage(image_path, 150, 750, width=50, height=50)
    # ============================ IMAGE ============================
    
    c.showPage()
    c.save()
    
    pdf_data.seek(0)
    return send_file(pdf_data, mimetype='application/pdf', download_name='sample.pdf')

