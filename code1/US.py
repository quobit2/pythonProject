import math


def calculate_shipping_fee(length, width, height, weight):
    # 定义各个类别的尺寸和重量上限
    small_standard_size = {"Length": 457.2, "Width": 365.8, "Height": 22.9, "Weight_Max": 453.6}
    large_standard_size = {"Length": 548.6, "Width": 426.7, "Height": 243.8, "Weight_Max": 9071.8}
    large_bulky = {"Length": 1798.3, "Width": 1005.8, "Height": 1005.8, "Weight_Max": 22679.6}

    # 检查包裹属于哪种尺寸类别
    if length <= small_standard_size["Length"] and width <= small_standard_size["Width"] and height <= \
            small_standard_size["Height"]:
        # Small standard-size
        if weight <= 56.7:
            return 3.1
        elif weight <= 113.4:
            return 3.2
        elif weight <= 170.1:
            return 3.2
        elif weight <= 226.8:
            return 3.3
        elif weight <= 283.5:
            return 3.4
        elif weight <= 340.2:
            return 3.5
        elif weight <= 396.9:
            return 3.6
        elif weight <= 453.6:
            return 3.7

    elif length <= large_standard_size["Length"] and width <= large_standard_size["Width"] and height <= \
            large_standard_size["Height"]:
        # Large standard-size
        if weight <= 113.4:
            return 3.7
        elif weight <= 226.8:
            return 3.9
        elif weight <= 340.2:
            return 4.2
        elif weight <= 453.6:
            return 4.6
        elif weight <= 567:
            return 5.0
        elif weight <= 680.4:
            return 5.4
        elif weight <= 793.8:
            return 5.5
        elif weight <= 907.2:
            return 5.8
        elif weight <= 1020.6:
            return 5.9
        elif weight <= 1134:
            return 6.1
        elif weight <= 1247.4:
            return 6.2
        elif weight <= 1360.8:
            return 6.6
        elif weight <= 9071.8:
            return 6.92 + 0.08 * ((weight - 3 * 453.5924) / 113.398)

    elif length <= large_bulky["Length"] and width <= large_bulky["Width"] and height <= large_bulky["Height"]:
        # Large bulky
        return 9.61 + ((weight - 453.5924) / 453.5924) * 0.38

    else:
        # Extra-large
        if weight <= 22679.6:
            return 26.33 + ((weight - 453.5924) / 453.5924) * 0.38
        elif weight <= 31751.4:
            return 40.12 + ((weight - 51 * 453.5924) / 453.5924) * 0.75
        elif weight <= 68038.8:
            return 54.81 + ((weight - 71 * 453.5924) / 453.5924) * 0.75
        else:
            return 194.95 + ((weight - 151 * 453.5924) / 453.5924) * 0.19


# 示例使用
length, width, height, weight = 1800, 1100, 1100, 22000  # 可替换为其他包裹数据
fee = calculate_shipping_fee(length, width, height, weight)
print(f"包裹的物流费用是: {fee} 美元")
