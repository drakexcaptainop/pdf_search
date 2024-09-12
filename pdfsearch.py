import pdfplumber as pdf
import regex as r


pages = None
pdff = open(r"", "rb")
reader = pdf.open(pdff)
pages = reader.pages 



def match_text( text ):
    pat = f"{text}"
    for page in pages:
        txt = " ".join(page.extract_text().split("\n"))
        m = [*r.finditer( pat, txt, r.DOTALL )]
        if len(m):
            print(f"page #{page.page_number}")
            print(txt[m[0].start():])
            break
    print("not found!")
        

match_text( input(">> ") ) 

pdff.close()