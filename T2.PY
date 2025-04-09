from fpdf import FPDF
import pandas as pd

# Built-in dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Department": ["HR", "IT", "Finance", "Marketing", "IT"],
    "Score": [88, 90, 79, 85, 92],
    "Completion Date": ["2025-03-20", "2025-03-21", "2025-03-22", "2025-03-23", "2025-03-24"]
}

# Convert data to a pandas DataFrame
df = pd.DataFrame(data)

# Analyze data
average_score = df["Score"].mean()

# Initialize FPDF class
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, "Automated Internship Report", ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 10)
        self.cell(0, 10, f"Page {self.page_no()}", align='C')

# Generate PDF
pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', '', 12)

# Add Report Title
pdf.cell(0, 10, "Completion Certificate Report", ln=True, align='C')
pdf.ln(10)

# Add Analysis Summary
pdf.cell(0, 10, f"Average Score: {average_score:.2f}", ln=True)
pdf.ln(10)

# Add Detailed Data
pdf.cell(0, 10, "Participant Details:", ln=True)
pdf.ln(5)

for index, row in df.iterrows():
    pdf.cell(0, 10, f"Name: {row['Name']}, Department: {row['Department']}, "
                    f"Score: {row['Score']}, Completion Date: {row['Completion Date']}", ln=True)

# Save the PDF
output_filename = "internship_report.pdf"
pdf.output(output_filename)

print(f"Report generated and saved as '{output_filename}'")
