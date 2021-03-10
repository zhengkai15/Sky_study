import fitz
import sys
import glob
pdffile=glob.glob("*.pdf")
pngfile = []
for f in pdffile:
    pngfile.append(f.rstrip("pdf"))
for i in range(len(pdffile)):
    doc = fitz.open(pdffile[i])
    page = doc[0]
    zoom = int(1000)
    rotate = int(0)
    trans = fitz.Matrix(zoom / 100.0, zoom / 100.0).preRotate(rotate)
    pm = page.getPixmap(matrix=trans, alpha=False)
    pm.writePNG(pngfile[i] + "png")
