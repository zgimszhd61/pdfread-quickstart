!pip install PyPDF2
from PyPDF2 import PdfReader
import requests
def main(url):
  response = requests.get(url)
  with open('temp.pdf', 'wb') as f:
      f.write(response.content)
  pdf_path = 'temp.pdf'
  reader = PdfReader(pdf_path)

  number_of_pages = len(reader.pages)
  print(number_of_pages)  # 打印页数

  # 提取第一页的文字
  page = reader.pages[0]
  text = page.extract_text()
  print(text)  # 提取出第一页的文字
main("https://arxiv.org/pdf/2311.17227.pdf")
