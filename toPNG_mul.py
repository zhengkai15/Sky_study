# @Author: ZhengKai
# @Date:   2020-12-20 11:22:00
# @Last Modified by:   ZhengKai
# @Last Modified time: 2021-04-07 14:15:35
import PyPDF4
import pikepdf
import fitz
import os
#对pdf文件进行简单的解密 
def jiemi(pdfpath):
 
    new_pdfpath = pdfpath[:-4] + '_new' + pdfpath[-4:]
 
    fp = open(pdfpath, "rb+")
    pdfFile = PyPDF4.pdf.PdfFileReader(fp)
 
    # pdf 解密
    if pdfFile.isEncrypted:
        pdf = pikepdf.open(pdfpath, password='')
        pdf.save(new_pdfpath)
    return new_pdfpath 
 
 #将每一页转化为图片并保存
def pdf_image(pdf_name):
    img_paths = []
    pdf = fitz.Document(pdf_name)
    for i,pg in enumerate(range(0, pdf.pageCount)):
        page = pdf[pg]  # 获得每一页的对象
        trans = fitz.Matrix(8.0, 8.0).preRotate(0)
        pm = page.getPixmap(matrix=trans, alpha=False)  # 获得每一页的流对象
        # pm.writePNG(dir_name + os.sep + base_name[:-4] + '_' + '{:0>3d}.png'.format(pg + 1))  # 保存图片
        os.makedirs(pdf_name[:-4],exist_ok=True)
        img_path = pdf_name[:-4] + '_' + str(pg+1) + '.jpg'
        pm.writePNG(pdf_name[:-4]+'/'+img_path)  # 保存图片
        img_paths.append(img_path)
    pdf.close()
    return img_paths
pdf_image("拼图.pdf")

# import fitz
# import sys
# import glob
# pdffile=glob.glob("*.pdf")
# pngfile = []
# for f in pdffile:
#     pngfile.append(f.rstrip("pdf"))
# for i in range(len(pdffile)):
#     pdf_image(pdffile[i])

# ————————————————
# 版权声明：本文为CSDN博主「stay_foolish12」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/stay_foolish12/article/details/113653224