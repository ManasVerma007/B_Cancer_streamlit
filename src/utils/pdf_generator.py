from fpdf import FPDF

def create_pdf(result, form_data):
    class PDF(FPDF):
        def header(self):
            # Add logo if needed
            self.set_font('Arial', 'B', 20)
            self.cell(0, 10, 'Breast Cancer Prediction Report', 0, 1, 'C')
            self.ln(10)
            
        def footer(self):
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', 0, 0, 'C')

    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    
    # Add Diagnosis Result
    pdf.set_font('Arial', 'B', 16)
    pdf.set_fill_color(255, 160, 122) if result == "Malignant" else pdf.set_fill_color(144, 238, 144)
    pdf.cell(0, 10, f'Diagnosis Result: {result}', 1, 1, 'L', True)
    pdf.ln(10)
    
    # Add Input Features
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Input Features:', 0, 1, 'L')
    pdf.ln(5)
    
    # Organize features by category
    mean_features = {k:v for k,v in form_data.items() if 'mean' in k}
    se_features = {k:v for k,v in form_data.items() if 'se' in k}
    worst_features = {k:v for k,v in form_data.items() if 'worst' in k}
    
    # Function to add feature section
    def add_feature_section(title, features):
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, title, 0, 1, 'L')
        pdf.set_font('Arial', '', 11)
        for key, value in features.items():
            formatted_key = key.replace('_', ' ').title()
            pdf.cell(0, 8, f'{formatted_key}: {value:.2f}', 0, 1, 'L')
        pdf.ln(5)
    
    # Add each feature section
    add_feature_section('Mean Values:', mean_features)
    add_feature_section('Standard Error Values:', se_features)
    add_feature_section('Worst Values:', worst_features)
    
    # Add timestamp
    from datetime import datetime
    pdf.set_font('Arial', 'I', 10)
    pdf.cell(0, 10, f'Report generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', 0, 1, 'R')
    
    return pdf.output(dest='S').encode('latin-1')
