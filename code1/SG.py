import pandas as pd

# 读取Excel中的SG-result数据
file_path = '/*/AMZ Fulfilment fees-US JP AU SG CA_re7 1.xlsx'
sg_result_data = pd.read_excel(file_path, sheet_name='SG-result')


def calculate_fulfillment_fee(length, width, height, weight, sg_result_data):
    # 确保长宽高按照从大到小排序
    dimensions = sorted([length, width, height], reverse=True)
    max_length, mid_length, min_length = dimensions

    # 第一步：判断包裹的最长边，次长边，最短边，重量是否同时小于或等于length, width, height, weightJudge
    sg_result_data['符合条件'] = (max_length <= sg_result_data['length 上限（cm）']) & \
                                 (mid_length <= sg_result_data['width 上限（cm）']) & \
                                 (min_length <= sg_result_data['height 上限（cm）']) & \
                                 (weight <= sg_result_data['weightJudge'])

    # 筛选出符合条件的行
    filtered_data = sg_result_data[sg_result_data['符合条件']]

    if filtered_data.empty:
        return "没有符合条件的区域"

    # 第二步：判断包裹的重量小于或等于当前区域中的哪一个weight，上限，并选择符合条件的费用
    filtered_data = filtered_data[filtered_data['weight 上限（g）'] >= weight]

    if filtered_data.empty:
        return "没有符合条件的区域"

    # 选择符合条件的费用（从2024年8月1日开始）
    fee = filtered_data.iloc[0][
        'Fulfillment fees ($) effective from August 1, 2024, (per unit, sold on Amazon including Goods and Services Tax (GST))（美元）']

    return fee


# 示例使用
length = 35  # 包裹的最长边
width = 24  # 次长边
height = 11  # 最短边
weight = 1800  # 重量

fee = calculate_fulfillment_fee(length, width, height, weight, sg_result_data)
print(fee)
