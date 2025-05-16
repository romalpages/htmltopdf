from flask import Flask, render_template, send_file
import datetime
import pdfkit
import os
import io  

app = Flask(__name__)

config = pdfkit.configuration()

options = {
    'enable-local-file-access': '',
    'page-size': 'A4',
    'encoding': 'UTF-8',
}
timestamp = datetime.datetime.now().strftime("%Y%m%D_%H%M%S")
employee_list = [
    {"companyname": "OM SAI SAFEGUARD SERVICES PVT LTD", "companyaddress": "Office No 3238, 2nd Floor, Above SBI Bank,,Konark Indrayu Mall, Kondhwa Khurd,Pune,Maharashtra,411048", "companyphone": " 7070020202","companymobile":" 918904330374","companymail":"support@omsaisafeguardservi","BillingAdress":"M/S ICAR- Directorate of Onion and Garlic Research"}
    
]
@app.route('/')
def index():
    return render_template('temp.html',employees=employee_list)

@app.route('/generate-pdf')
def generate_pdf():
    rendered = render_template('temp.html',employees=employee_list)
    pdf = pdfkit.from_string(rendered, False, configuration=config, options=options)
    return send_file(
        io.BytesIO(pdf),
        download_name= f"output_{timestamp}.pdf",
        as_attachment=True
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
