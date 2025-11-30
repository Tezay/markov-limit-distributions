import pypdf

reader = pypdf.PdfReader("Probability SM301 Project 2026.pdf")
text = ""
for i in range(min(10, len(reader.pages))):
    text += reader.pages[i].extract_text() + "\n"

print(text)
