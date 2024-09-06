# 包裹类型判断
def determine_package_category(length, width, height):
    if length <= 20 and width <= 15 and height <= 1:
        return "Small envelope"
    elif length <= 33 and width <= 23 and height <= 2.5:
        return "Standard envelope"
    elif length <= 33 and width <= 23 and height <= 4:
        return "Large envelope"
    elif length <= 33 and width <= 23 and height <= 6:
        return "Extra-large envelope"
    elif length <= 35 and width <= 25 and height <= 12:
        return "Small parcel"
    else:
        return None

# 根据国家和类型计算费用
def calculate_shipping_fee(category, weight, country):
    # 各国的费用表
    size_rates = {
        "Small envelope": {
            "CEP": {80: 4.91}, "DE": {80: 5.17}, "FR": {80: 5.06}, "NL": {80: 4.73},
            "SE": {80: 47.08}, "PL": {80: 20.25}, "BE4": {80: 4.73}
        },
        "Standard envelope": {
            "CEP": {60: 5.06, 210: 5.41, 460: 5.44}, "DE": {60: 5.32, 210: 5.67, 460: 5.7},
            "FR": {60: 5.22, 210: 5.57, 460: 5.61}, "NL": {60: 4.88, 210: 5.21, 460: 5.25},
            "SE": {60: 49.59, 210: 52.91, 460: 53.22}, "PL": {60: 21.12, 210: 22.61, 460: 22.95},
            "BE4": {60: 4.88, 210: 5.21, 460: 5.25}
        },
        "Large envelope": {
            "CEP": {960: 5.99}, "DE": {960: 6.25}, "FR": {960: 6.17}, "NL": {960: 5.6},
            "SE": {960: 57.38}, "PL": {960: 24.57}, "BE4": {960: 5.6}
        },
        "Extra-large envelope": {
            "CEP": {960: 6.61}, "DE": {960: 6.87}, "FR": {960: 6.81}, "NL": {960: 6.18},
            "SE": {960: 62.1}, "PL": {960: 29.68}, "BE4": {960: 6.18}
        },
        "Small parcel": {
            "CEP": {150: 6.61, 400: 7.05}, "DE": {150: 6.87, 400: 7.31},
            "FR": {150: 6.81, 400: 7.26}, "NL": {150: 6.18, 400: 6.76},
            "SE": {150: 62.34, 400: 67.95}, "PL": {150: 29.68, 400: 32.33}, "BE4": {150: 6.18, 400: 6.76}
        }
    }

    # 确认包裹类型是否在费用表中
    if category not in size_rates:
        return "No matching category"

    # 匹配国家的费用表
    if country not in size_rates[category]:
        return "No matching country"

    # 根据重量匹配对应的费用
    for weight_limit, fee in sorted(size_rates[category][country].items()):
        if weight <= weight_limit:
            return fee

    return "No matching weight"

# 综合计算费用
def calculate_total_fee(length, width, height, weight, country):
    category = determine_package_category(length, width, height)
    if not category:
        return "No matching category for dimensions"

    return calculate_shipping_fee(category, weight, country)

# 示例使用
length = 33  # cm
width = 23  # cm
height = 6  # cm
weight = 500  # g
country = "FR"  # 法国

fee = calculate_total_fee(length, width, height, weight, country)
print(f"包裹的物流费用是: {fee} ")
