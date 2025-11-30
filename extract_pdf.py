import pypdf

reader = pypdf.PdfReader("Probability SM301 Project 2026.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

print(text)
