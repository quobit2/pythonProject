# 定义各个国家的low-price费用规则
low_price_rates = {
    "CEP (DE/PL/CZ)/IT/ES": {
        "Small envelope": {80: 5.4},
        "Standard envelope": {60: 5.6, 210: 6.0, 460: 6.0},
        "Large envelope": {960: 6.6},
        "Extra-large envelope": {960: 7.3},
        "Small parcel": {150: 7.3, 400: 7.8},
    },
    "DE only2": {
        "Small envelope": {80: 5.7},
        "Standard envelope": {60: 5.9, 210: 6.3, 460: 6.3},
        "Large envelope": {960: 6.9},
        "Extra-large envelope": {960: 7.6},
        "Small parcel": {150: 7.6, 400: 8.1},
    },
    "FR": {
        "Small envelope": {80: 5.6},
        "Standard envelope": {60: 5.8, 210: 6.2, 460: 6.2},
        "Large envelope": {960: 6.8},
        "Extra-large envelope": {960: 7.6},
        "Small parcel": {150: 7.6, 400: 8.1},
    },
    "NL": {
        "Small envelope": {80: 5.2},
        "Standard envelope": {60: 5.4, 210: 5.8, 460: 5.8},
        "Large envelope": {960: 6.2},
        "Extra-large envelope": {960: 6.9},
        "Small parcel": {150: 6.9, 400: 7.5},
    },
    "SE": {
        "Small envelope": {80: 52.2},
        "Standard envelope": {60: 55.0, 210: 58.7, 460: 59.0},
        "Large envelope": {960: 63.6},
        "Extra-large envelope": {960: 68.9},
        "Small parcel": {150: 69.1, 400: 75.4},
    },
    "PL": {
        "Small envelope": {80: 22.5},
        "Standard envelope": {60: 23.4, 210: 25.1, 460: 25.5},
        "Large envelope": {960: 27.2},
        "Extra-large envelope": {960: 32.9},
        "Small parcel": {150: 32.9, 400: 35.9},
    },
    "BE4": {
        "Small envelope": {80: 5.2},
        "Standard envelope": {60: 5.4, 210: 5.8, 460: 5.8},
        "Large envelope": {960: 6.2},
        "Extra-large envelope": {960: 6.9},
        "Small parcel": {150: 6.9, 400: 7.5},
    }
}


# 定义low-price计算函数
def calculate_low_price_shipping_fee(length, width, height, weight, country):
    # 判断包裹的类型和尺寸
    category = None
    if length <= 20 and width <= 15 and height <= 1:
        category = "Small envelope"
    elif length <= 33 and width <= 23 and height <= 2.5:
        category = "Standard envelope"
    elif length <= 33 and width <= 23 and height <= 4:
        category = "Large envelope"
    elif length <= 33 and width <= 23 and height <= 6:
        category = "Extra-large envelope"
    elif length <= 35 and width <= 25 and height <= 12:
        category = "Small parcel"

    if category is None:
        return "No matching category for size"

    # 获取国家的费用规则
    if country not in low_price_rates:
        return "Country not supported"

    country_rates = low_price_rates[country]

    # 根据重量选择对应的费用
    if category in country_rates:
        size_rates = country_rates[category]
        for weight_limit, fee in sorted(size_rates.items()):
            if weight <= weight_limit:
                return fee

    return "No matching category for weight"


# 示例使用
length = 33  # cm
width = 23  # cm
height = 2.5  # cm
weight = 210  # g
country = "SE"

fee = calculate_low_price_shipping_fee(length, width, height, weight, country)
print(f"包裹的物流费用是: {fee} 美元")
