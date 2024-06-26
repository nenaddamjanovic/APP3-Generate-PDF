from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Calibri', 'B', 12)
        self.cell(0, 10, 'Integram: Radno Okruženje', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Calibri', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'C')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Calibri', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

pdf = PDF()

# Add UTF-8 supporting font before adding a page
pdf.add_font('Calibri', '', 'calibri.ttf', uni=True)
pdf.add_font('Calibri', 'B', 'calibri.ttf', uni=True)

pdf.add_page()

# Creating the description table
description_data = [
    ["Odeljenja:", "IT", "Marketing", "Finansije", "Ljudski resursi", "Prodaja"],
    ["Zaposleni:", "Ana", "Boris", "Dina", "Milan", "Petra"],
    ["Zadaci:", "Prezentacija", "Izveštaj", "Sastanak", "Analiza", "Trening"],
    ["Dani:", "Ponedeljak", "Utorak", "Sreda", "Četvrtak", "Petak"]
]

def create_description_table(pdf, data):
    pdf.set_font('Calibri', 'B', 11)
    pdf.cell(0, 10, 'Opis', 0, 1, 'C')
    pdf.set_font('Calibri', '', 11)
    for row in data:
        for cell in row:
            pdf.cell(26, 8, cell, border=1)
        pdf.ln()

create_description_table(pdf, description_data)

# Add the "Pravila" section
rules = """
Pravila:
1. Zaposleni iz IT odeljenja nije radio u sredu niti je pravio izveštaj.
2. Boris nije iz finansija i nije radio prezentaciju.
3. Dina je imala sastanak dan pre nego što je Milan imao prezentaciju.
4. Ana je radila trening u petak.
5. Petra nije iz marketinga niti je radila analizu.
6. Zaposleni iz ljudskih resursa je imao sastanak u sredu.
7. Zaposleni iz prodaje nije radio u ponedeljak.
"""

pdf.chapter_body(rules)

# Add a new page for other tables
pdf.add_page()

# Creating other tables
def create_table(pdf, title, data):
    pdf.set_font('Calibri', 'B', 11)
    pdf.cell(0, 10, title, 0, 1, 'C')
    pdf.set_font('Calibri', '', 11)
    for row in data:
        for cell in row:
            pdf.cell(26, 8, cell, border=1)
        pdf.ln()

departments = [
    ["", "IT", "Marketing", "Finansije", "Ljudski resursi", "Prodaja"],
    ["Ana", "", "", "", "", ""],
    ["Boris", "", "", "", "", ""],
    ["Dina", "", "", "", "", ""],
    ["Milan", "", "", "", "", ""],
    ["Petra", "", "", "", "", ""]
]

tasks = [
    ["", "Prezentacija", "Izveštaj", "Sastanak", "Analiza", "Trening"],
    ["Ana", "", "", "", "", ""],
    ["Boris", "", "", "", "", ""],
    ["Dina", "", "", "", "", ""],
    ["Milan", "", "", "", "", ""],
    ["Petra", "", "", "", "", ""]
]

days = [
    ["", "Ponedeljak", "Utorak", "Sreda", "Četvrtak", "Petak"],
    ["Ana", "", "", "", "", ""],
    ["Boris", "", "", "", "", ""],
    ["Dina", "", "", "", "", ""],
    ["Milan", "", "", "", "", ""],
    ["Petra", "", "", "", "", ""]
]

create_table(pdf, "Tabela Odeljenja", departments)
create_table(pdf, "Tabela Zadataka", tasks)
create_table(pdf, "Tabela Dana", days)

# Save PDF
pdf_output = "integram_radno_okruzenje.pdf"
pdf.output(pdf_output)

pdf_output
