from PyPDF2 import PdfReader, PdfWriter

# 这个代码是把pdf切割出一个小的pdf

def extract_page(pdf_path, page_number, output_path):
    # 打开PDF文件
    with open(pdf_path, 'rb') as pdf_file:
        reader = PdfReader(pdf_file)

        # 检查页面数
        if page_number >= len(reader.pages):
            raise ValueError("页面编号超出范围")

        # 创建一个PDF写入对象
        writer = PdfWriter()

        # 获取指定页面
        page = reader.pages[page_number]
        writer.add_page(page)

        # 保存为新的PDF文件
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)


# 使用示例
extract_page('C:/Users/高文彬/Desktop/240523-FBA-Rate-Card-UK_2 1.pdf', 4,
             'C:/Users/高文彬/Desktop/low-price EU.pdf')
