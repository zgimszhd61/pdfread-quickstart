# pdfread-quickstart

当然可以！下面是一个完整的 PyPDF2 快速入门指南，涵盖了使用 PyPDF2 打开和读取 PDF 文件、合并 PDF 文件以及从一个 PDF 中拆分页面的完整示例代码。

### 安装 PyPDF2

首先，确保在你的环境中安装了 PyPDF2。可以使用以下命令安装：

```bash
pip install PyPDF2
```

### 示例代码

这个示例代码包含读取 PDF、合并多个 PDF 以及拆分特定页面到新的 PDF 文件。

```python
from PyPDF2 import PdfReader, PdfWriter

# 读取 PDF
def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = []
    for page in reader.pages:
        text.append(page.extract_text())
    return text

# 合并 PDF
def merge_pdfs(paths, output_path):
    pdf_writer = PdfWriter()
    for path in paths:
        pdf_reader = PdfReader(path)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
    with open(output_path, 'wb') as out:
        pdf_writer.write(out)

# 拆分 PDF
def split_pdf(input_path, page_numbers, output_path):
    pdf_reader = PdfReader(input_path)
    pdf_writer = PdfWriter()
    for page in page_numbers:
        pdf_writer.add_page(pdf_reader.pages[page])
    with open(output_path, 'wb') as out:
        pdf_writer.write(out)

# 使用示例
# 更改 'example.pdf'、'output.pdf' 和其他文件路径为你的具体文件路径
input_pdf = "example.pdf"
output_pdf = "output.pdf"
merge_output = "merged.pdf"
split_output = "split.pdf"

# 读取 PDF 文本
pdf_text = read_pdf(input_pdf)
print("PDF Text:", pdf_text)

# 合并 PDF
merge_pdfs([input_pdf, input_pdf], merge_output)
print(f"Merged PDF saved as {merge_output}")

# 拆分 PDF
split_pdf(input_pdf, [0, 1], split_output)  # 例如提取前两页
print(f"Split PDF saved as {split_output}")
```

### 代码解释
- `read_pdf`: 这个函数接收一个文件路径，打开 PDF 文件，并从每一页中提取文本。
- `merge_pdfs`: 这个函数接收一个文件路径列表和一个输出文件路径，将所有提供的 PDF 文档合并成一个文件。
- `split_pdf`: 这个函数接收一个输入文件路径、需要提取的页码列表和输出文件路径，只保存指定的页码到新的 PDF 文件。

确保在运行这些函数之前，你已将 PDF 文件放在正确的路径下，或者更新文件路径以匹配你的实际文件位置。
