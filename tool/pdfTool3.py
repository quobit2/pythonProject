import pdfplumber
import pandas as pd

# 这个代码是将pdf里面的表格提取出来，转换成excel文件

def extract_tables_from_pdf(pdf_path, excel_path):
    with pdfplumber.open(pdf_path) as pdf:
        all_tables = []
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                df = pd.DataFrame(table[1:], columns=table[0])  # 创建DataFrame
                all_tables.append(df)

        # 将所有表格写入到一个Excel文件中，每个表格放在一个单独的工作表
        with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
            for i, df in enumerate(all_tables):
                df.to_excel(writer, sheet_name=f'Table_{i + 1}', index=False)


# 使用示例
pdf_path = 'C:/Users/高文彬/Desktop/low-price EU.pdf'  # 替换为你的PDF文件路径
excel_path = 'C:/Users/高文彬/Desktop/low-price EU.xlsx'  # 输出Excel文件的路径
extract_tables_from_pdf(pdf_path, excel_path)
