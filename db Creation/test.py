import pdfplumber


enWord = ''

with pdfplumber.open("eng-rus-susch.pdf") as pdf:
    bold_text_page_7_8 = []
    for page_num in range(6, 8):  # Индексы страниц начинаются с 0
        page = pdf.pages[page_num]
        for element in page.chars:
            if "bold" in element["fontname"].lower():
                enWord += element["text"]


    print(enWord.replace(' ', '\n'))
