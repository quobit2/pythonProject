import openpyxl
import pandas as pd
import random

# 随机生成数

# 生成所有五位数
all_five_digit_numbers = list(range(10000, 100000))

# 随机抽取 10,000 个不重复的五位数
unique_five_digit_numbers = random.sample(all_five_digit_numbers, 10000)

# 创建 DataFrame
df = pd.DataFrame(unique_five_digit_numbers, columns=['Five Digit Numbers'])

# 保存到 Excel 文件
df.to_excel('unique_five_digit_numbers.xlsx', index=False)
