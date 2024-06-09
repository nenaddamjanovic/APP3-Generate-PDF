from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

datafile = pd.read_csv("topics.csv")

for index, row in datafile.iterrows():
    #  Set the header
    pdf.add_page()  # Kreira naslovnu stranicu
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
    #  pdf.line(10, 21, 200, 21)

    #  set all lines
    for line in range(21, 290, 10):
        pdf.line(10, line, 200, line)

    #  Set the futer
    pdf.ln(260)  # Mesto gde futer počinje
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # Kreira ostale prazne stranice (-1 prva stranica)
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        #  Set the futer
        pdf.ln(272)  # Mesto gde futer počinje
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        #  set all lines
        for line in range(21, 290, 10):
            pdf.line(10, line, 200, line)

pdf.output("output.pdf")
