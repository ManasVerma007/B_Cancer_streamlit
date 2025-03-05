from fpdf import FPDF
from datetime import datetime

def create_pdf(result, form_data):
    class PDF(FPDF):
        def header(self):
            self.set_font('Arial', 'B', 20)
            self.set_text_color(44, 62, 80)  
            self.cell(0, 10, 'Breast Cancer Prediction Report', 0, 1, 'C')
            
            self.line(10, 25, 200, 25)
            self.ln(15)
            
        def footer(self):
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.set_text_color(128, 128, 128)  
            self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', 0, 0, 'C')
            self.cell(0, 10, f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M")}', 0, 0, 'R')

    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    
    pdf.set_font('Arial', 'B', 16)
    
    if result == "Malignant":
        pdf.set_fill_color(255, 160, 122)  
        pdf.set_text_color(139, 0, 0)      
    else:
        pdf.set_fill_color(144, 238, 144)  
        pdf.set_text_color(0, 100, 0)      
        
    pdf.cell(0, 10, f'Diagnosis Result: {result}', 1, 1, 'L', True)
    pdf.ln(5)
    
    pdf.set_font('Arial', 'I', 10)
    pdf.set_text_color(80, 80, 80)  
    if result == "Malignant":
        pdf.multi_cell(0, 5, "This prediction suggests the tumor shows characteristics consistent with malignancy. "
                           "The medical professional should consider further diagnostic procedures and additional testing.")
    else:
        pdf.multi_cell(0, 5, "This prediction suggests the tumor shows characteristics consistent with benign tissue. "
                           "Regular monitoring and follow-up may still be advisable as per medical protocols.")
    pdf.ln(10)
    
    pdf.set_font('Arial', 'B', 14)
    pdf.set_text_color(44, 62, 80)  
    pdf.cell(0, 10, 'Input Features', 0, 1, 'L')
    
    mean_features = {k:v for k,v in form_data.items() if 'mean' in k}
    se_features = {k:v for k,v in form_data.items() if 'se' in k}
    worst_features = {k:v for k,v in form_data.items() if 'worst' in k}
    
    def add_feature_section(title, features, fill_color):
        pdf.set_font('Arial', 'B', 12)
        pdf.set_fill_color(fill_color, fill_color, fill_color) 
        pdf.cell(0, 8, title, 0, 1, 'L', True)
        pdf.ln(2)
        
        pdf.set_font('Arial', '', 10)
        pdf.set_fill_color(245, 245, 245) 
        
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(80, 8, "Feature", 1, 0, 'C', True)
        pdf.cell(40, 8, "Value", 1, 1, 'C', True)
        pdf.set_font('Arial', '', 10)
        
        row = 0
        for key, value in features.items():
            formatted_key = key.replace('_', ' ').title()
            fill = row % 2 == 0
            pdf.cell(80, 8, formatted_key, 1, 0, 'L', fill)
            pdf.cell(40, 8, f"{value:.3f}", 1, 1, 'R', fill)
            row += 1
        
        pdf.ln(5)
    
    add_feature_section('Mean Values:', mean_features, 240)
    add_feature_section('Standard Error Values:', se_features, 230)
    add_feature_section('Worst Values:', worst_features, 220)
    
    pdf.ln(5)
    pdf.set_font('Arial', 'I', 8)
    pdf.set_text_color(100, 100, 100) 
    pdf.multi_cell(0, 4, "Disclaimer: This report is generated using a machine learning model and is intended for "
                        "informational purposes only. It should not replace professional medical diagnosis. "
                        "Always consult with a qualified healthcare provider for proper diagnosis and treatment.")
    
    return pdf.output(dest='S').encode('latin-1')