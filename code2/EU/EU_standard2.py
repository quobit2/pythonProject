import EU_surcharge
import math

# 定义包裹类型判断逻辑  这里的逻辑有点疑惑
def determine_package_category(length, width, height, weight):
    # 判断包裹的类型和尺寸
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
    elif length <= 45 and width <= 34 and height <= 26:
        return "Standard parcel"
    elif length <= 61 and width <= 46 and height <= 46:
        return "Small oversize1"
    elif length <= 120 and width <= 60 and height <= 60:
        return "Standard oversize1"
    elif length > 120 and width > 60 and height > 60:
        return "Large oversize1"
    elif length > 175:
        return "Special oversize1"
    else:
        return None

# 计算费用（根据不同的国家）
def calculate_shipping_fee(category, weight, country):
    if country == "UK":
        return calculate_uk_fee(category, weight)
    if country == "FR":
        return calculate_fr_fee(category, weight)
    if country == "IT":
        return calculate_it_fee(category, weight)
    if country == "DE":
        return calculate_de_fee(category, weight)
    if country == "ES":
        return calculate_es_fee(category, weight)
    if country == "NL":
        return calculate_nl_fee(category, weight)
    if country == "SE":
        return calculate_se_fee(category, weight)
    if country == "PL":
        return calculate_pl_fee(category, weight)
    if country == "BE4":
        return calculate_be4_fee(category, weight)
    # 可以继续为不同国家添加对应的费用规则函数...
    else:
        return "No matching country"
# 英国
def calculate_uk_fee(category, weight):
    size_rates = {
        "Small envelope": {80: 1.71},
        "Standard envelope": {60: 1.89, 210: 2.07, 460: 2.2},
        "Large envelope": {960: 2.73},
        "Extra-large envelope": {960: 2.95},
        "Small parcel": {150: 2.99, 400: 3.01, 900: 3.05, 1400: 3.23, 1900: 3.58, 3900: 5.62},
        "Standard parcel": {150: 3.0, 400: 3.16, 900: 3.37, 1400: 3.6, 1900: 3.9, 2900: 5.65, 3900: 5.96, 5900: 6.13,
                            8900: 6.99, 11900: 7.39},
        "Small oversize1": {760: 5.32, 1260: 6.17, 1760: 6.36, ">1760": lambda w: round(6.36 + 0.01 * math.ceil((w - 1760) / 1000), 2)},
        "Standard oversize1": {760: 6.32, 1760: 6.67, 2760: 6.82, 3760: 6.86, 4760: 6.89, 9760: 8.24, 14760: 8.82,
                               19760: 9.24, 24760: 10.24, 29760: 10.25,
                               ">29760": lambda w: round(10.25 + 0.01 * math.ceil((w - 29760) / 1000), 2)},
        "Large oversize1": {4760: 11.45, 9760: 12.52, 14760: 13.22, 19760: 13.86, 24760: 15.08, 31500: 15.12,
                            ">31500": lambda w: round(15.12 + 0.01 * math.ceil((w - 31500) / 1000), 2)},
        "Special oversize1": {20000: 15.43, 30000: 18.48, 40000: 19.16, 50000: 42.98, 60000: 44.25,
                              ">60000": lambda w: round(44.25 + 0.39 * math.ceil((w - 60000) / 1000), 2)}
    }

    if category not in size_rates:
        return "No matching category"

    # Handle numeric weight limits first
    numeric_limits = {k: v for k, v in size_rates[category].items() if isinstance(k, int)}
    for weight_limit, fee in sorted(numeric_limits.items()):
        if weight <= weight_limit:
            return fee

    # Handle string-based weight limits (e.g., ">1760")
    string_limits = {k: v for k, v in size_rates[category].items() if isinstance(k, str)}
    for weight_limit in string_limits:
        limit_value = int(weight_limit[1:])  # Extract number from string like ">1760"
        if weight > limit_value:
            return string_limits[weight_limit](weight)

    return "No matching weight"
# 法国
def calculate_fr_fee(category, weight):
    size_rates = {
        "Small envelope": {80: 2.7},
        "Standard envelope": {60: 2.8, 210: 3.34, 460: 3.82},
        "Large envelope": {960: 4.45},
        "Extra-large envelope": {960: 4.79},
        "Small parcel": {150: 4.79, 400: 5.18, 900: 5.92, 1400: 6.16, 1900: 6.24, 3900: 9.55},
        "Standard parcel": {150: 4.84, 400: 5.5, 900: 6.4, 1400: 6.77, 1900: 6.97, 2900: 9.55, 3900: 9.74, 5900: 10.22, 8900: 11.12, 11900: 11.65},
        "Small oversize1": {760: 9.36, 1260: 9.75, 1760: 10.39, ">1760": lambda w: round(10.39 + 0.01 * math.ceil((w - 1760) / 1000), 2)},
        "Standard oversize1": {760: 9.37, 1760: 10.57, 2760: 11.1, 3760: 11.56, 4760: 11.64, 9760: 12.54, 14760: 13.46, 19760: 14.14, 24760: 15.75, 29760: 15.75,
                               ">29760": lambda w: round(15.75 + 0.01 * math.ceil((w - 29760) / 1000), 2)},
        "Large oversize1": {4760: 16.91, 9760: 20.6, 14760: 21.69, 19760: 22.76, 24760: 24.88, 31500: 25.45,
                            ">31500": lambda w: round(25.45 + 0.01 * math.ceil((w - 31500) / 1000), 2)},
        "Special oversize1": {20000: 23.95, 30000: 30.88, 40000: 31.76, 50000: 54.04, 60000: 55.63,
                              ">60000": lambda w: round(55.63 + 0.42 * math.ceil((w - 60000) / 1000), 2)}
    }

    if category not in size_rates:
        return "No matching category"

    # Handle numeric weight limits first
    numeric_limits = {k: v for k, v in size_rates[category].items() if isinstance(k, int)}
    for weight_limit, fee in sorted(numeric_limits.items()):
        if weight <= weight_limit:
            return fee

    # Handle string-based weight limits (e.g., ">1760")
    string_limits = {k: v for k, v in size_rates[category].items() if isinstance(k, str)}
    for weight_limit in string_limits:
        limit_value = int(weight_limit[1:])  # Extract number from string like ">1760"
        if weight > limit_value:
            return string_limits[weight_limit](weight)

    return "No matching weight"
# 意大利
def calculate_it_fee(category, weight):
    size_rates = {
        'Small envelope': {
            80: 3.11
        },
        'Standard envelope': {
            60: 3.24,
            210: 3.37,
            460: 3.60
        },
        'Large envelope': {
            960: 3.90
        },
        'Extra-large envelope': {
            960: 4.13
        },
        'Small parcel': {
            150: 4.13,
            400: 4.44,
            900: 4.97,
            1400: 5.59,
            1900: 5.84,
            3900: 7.70
        },
        'Standard parcel': {
            150: 4.50,
            400: 5.08,
            900: 5.78,
            1400: 6.52,
            1900: 6.78,
            2900: 7.72,
            3900: 8.01,
            5900: 9.14,
            8900: 10.13,
            11900: 10.87
        },
        'Small oversize1': {
            760: 9.24,
            1260: 9.72,
            1760: 9.86,
            ">1760": lambda w: round(9.86 + 0.01 * math.ceil((w - 1760) / 1000), 2)
        },
        'Standard oversize1': {
            760: 9.79,
            1760: 9.94,
            2760: 9.96,
            3760: 10.64,
            4760: 10.68,
            9760: 12.11,
            14760: 13.45,
            19760: 13.87,
            24760: 14.76,
            29760: 15.50,
            ">29760": lambda w: round(15.50 + 0.01 * math.ceil((w - 29760) / 1000), 2)
        },
        'Large oversize1': {
            4760: 10.84,
            9760: 12.33,
            14760: 13.57,
            19760: 14.01,
            24760: 15.71,
            31500: 15.80,
            ">31500": lambda w: round(15.80 + 0.01 * math.ceil((w - 31500) / 1000), 2)
        },
        'Special oversize1': {
            20000: 17.41,
            30000: 20.16,
            40000: 20.91,
            50000: 27.93,
            60000: 28.48,
            ">60000": lambda w: round(28.48 + 0.60 * math.ceil((w - 60000) / 1000), 2)
        }
    }

    if category not in size_rates:
        return "No matching category"

    # Iterate through the weight limits and find the applicable fee
    for weight_limit, fee in sorted((k, v) for k, v in size_rates[category].items() if isinstance(k, int)):
        if weight <= weight_limit:
            return fee

    # Check if there's a lambda function for the exceeding portion
    if ">1760" in size_rates[category] and weight > 1760:
        return size_rates[category][">1760"](weight)
    if ">29760" in size_rates[category] and weight > 29760:
        return size_rates[category][">29760"](weight)
    if ">31500" in size_rates[category] and weight > 31500:
        return size_rates[category][">31500"](weight)
    if ">60000" in size_rates[category] and weight > 60000:
        return size_rates[category][">60000"](weight)

    return "No matching weight"
# 德国only
def calculate_de_fee(category, weight):
    size_rates = {
        'Small envelope': {
            80: 2.16
        },
        'Standard envelope': {
            60: 2.35,
            210: 2.49,
            460: 2.65
        },
        'Large envelope': {
            960: 3.00
        },
        'Extra-large envelope': {
            960: 3.38
        },
        'Small parcel': {
            150: 3.38,
            400: 3.58,
            900: 3.96,
            1400: 4.63,
            1900: 5.02,
            3900: 6.23
        },
        'Standard parcel': {
            150: 3.48,
            400: 3.89,
            900: 4.37,
            1400: 5.10,
            1900: 5.58,
            2900: 6.24,
            3900: 6.81,
            5900: 7.15,
            8900: 7.70,
            11900: 7.99
        },
        'Small oversize1': {
            760: 6.65,
            1260: 6.67,
            1760: 6.69,
            ">1760": lambda w: round(6.69 + 0.01 * math.ceil((w - 1760) / 1000), 2)
        },
        'Standard oversize1': {
            760: 6.72,
            1760: 7.03,
            2760: 7.85,
            3760: 7.91,
            4760: 7.94,
            9760: 8.33,
            14760: 9.05,
            19760: 9.60,
            24760: 10.84,
            29760: 10.85,
            ">29760": lambda w: round(10.85 + 0.01 * math.ceil((w - 29760) / 1000), 2)
        },
        'Large oversize1': {
            4760: 9.52,
            9760: 10.92,
            14760: 11.26,
            19760: 11.89,
            24760: 13.12,
            31500: 13.16,
            ">31500": lambda w: round(13.16 + 0.01 * math.ceil((w - 31500) / 1000), 2)
        },
        'Special oversize1': {
            20000: 19.98,
            30000: 27.16,
            40000: 28.46,
            50000: 59.97,
            60000: 61.17,
            ">60000": lambda w: round(61.17 + 0.38 * math.ceil((w - 60000) / 1000), 2)
        }
    }

    if category not in size_rates:
        return "No matching category"

    # Sort the integer weight limits and check if weight falls within them
    for weight_limit, fee in sorted((k, v) for k, v in size_rates[category].items() if isinstance(k, int)):
        if weight <= weight_limit:
            return fee

    # Check for the lambda functions for the categories with excess weight
    if '>1760' in size_rates[category] and weight > 1760:
        return size_rates[category]['>1760'](weight)
    if '>29760' in size_rates[category] and weight > 29760:
        return size_rates[category]['>29760'](weight)
    if '>31500' in size_rates[category] and weight > 31500:
        return size_rates[category]['>31500'](weight)
    if '>60000' in size_rates[category] and weight > 60000:
        return size_rates[category]['>60000'](weight)

    return "No matching weight"
# 西班牙
def calculate_es_fee(category, weight):
    size_rates = {
        'Small envelope': {
            80: 2.53
        },
        'Standard envelope': {
            60: 2.84,
            210: 3.18,
            460: 3.42
        },
        'Large envelope': {
            960: 3.57
        },
        'Extra-large envelope': {
            960: 3.80
        },
        'Small parcel': {
            150: 3.80,
            400: 4.03,
            900: 4.26,
            1400: 4.75,
            1900: 4.82,
            3900: 6.27
        },
        'Standard parcel': {
            150: 3.82,
            400: 4.39,
            900: 4.73,
            1400: 5.44,
            1900: 5.54,
            2900: 6.29,
            3900: 7.70,
            5900: 7.95,
            8900: 7.97,
            11900: 7.98
        },
        'Small oversize1': {
            760: 7.32,
            1260: 8.03,
            1760: 8.13,
            ">1760": lambda w: round(8.13 + 0.01 * math.ceil((w - 1760) / 1000), 2)
        },
        'Standard oversize1': {
            760: 7.37,
            1760: 8.16,
            2760: 8.95,
            3760: 9.02,
            4760: 9.31,
            9760: 13.62,
            14760: 14.71,
            19760: 15.95,
            24760: 15.96,
            29760: 17.72,
            ">29760": lambda w: round(17.72 + 0.01 * math.ceil((w - 29760) / 1000), 2)
        },
        'Large oversize1': {
            4760: 11.19,
            9760: 15.01,
            14760: 16.21,
            19760: 17.36,
            24760: 18.82,
            31500: 21.57,
            ">31500": lambda w: round(21.57 + 0.01 * math.ceil((w - 31500) / 1000), 2)
        },
        'Special oversize1': {
            20000: 17.75,
            30000: 24.33,
            40000: 25.23,
            50000: 39.32,
            60000: 40.08,
            ">60000": lambda w: round(40.08 + 0.51 * math.ceil((w - 60000) / 1000), 2)
        }
    }

    if category not in size_rates:
        return "No matching category"

    # Sort the integer weight limits and check if weight falls within them
    for weight_limit, fee in sorted((k, v) for k, v in size_rates[category].items() if isinstance(k, int)):
        if weight <= weight_limit:
            return fee

    # Check for the lambda functions for the categories with excess weight
    if '>1760' in size_rates[category] and weight > 1760:
        return size_rates[category]['>1760'](weight)
    if '>29760' in size_rates[category] and weight > 29760:
        return size_rates[category]['>29760'](weight)
    if '>31500' in size_rates[category] and weight > 31500:
        return size_rates[category]['>31500'](weight)
    if '>60000' in size_rates[category] and weight > 60000:
        return size_rates[category]['>60000'](weight)

    return "No matching weight"
# 荷兰
def calculate_nl_fee(category, weight):
    size_rates = {
        'Small envelope': {
            80: 1.91
        },
        'Standard envelope': {
            60: 2.08,
            210: 2.28,
            460: 2.42
        },
        'Large envelope': {
            960: 2.88
        },
        'Extra-large envelope': {
            960: 3.21
        },
        'Small parcel': {
            150: 3.22,
            400: 3.26,
            900: 3.83,
            1400: 4.50,
            1900: 4.82,
            3900: 6.25
        },
        'Standard parcel': {
            150: 3.28,
            400: 3.60,
            900: 4.13,
            1400: 4.93,
            1900: 5.40,
            2900: 6.26,
            3900: 6.29,
            5900: 6.53,
            8900: 6.89,
            11900: 7.34
        },
        'Small oversize1': {
            760: 7.22,
            1260: 7.23,
            1760: 7.23,
            ">1760": lambda w: round(7.23 + 0.01 * math.ceil((w - 1760) / 1000), 2)
        },
        'Standard oversize1': {
            760: 7.22,
            1760: 7.53,
            2760: 8.38,
            3760: 8.45,
            4760: 8.49,
            9760: 8.75,
            14760: 9.57,
            19760: 10.22,
            24760: 10.69,
            29760: 10.71,
            ">29760": lambda w: round(10.71 + 0.01 * math.ceil((w - 29760) / 1000), 2)
        },
        'Large oversize1': {
            4760: 9.96,
            9760: 11.38,
            14760: 11.82,
            19760: 12.49,
            24760: 13.83,
            31500: 13.86,
            ">31500": lambda w: round(13.86 + 0.01 * math.ceil((w - 31500) / 1000), 2)
        }
    }

    if category not in size_rates:
        return "No matching category"

    # Sort the integer weight limits and check if weight falls within them
    for weight_limit, fee in sorted((k, v) for k, v in size_rates[category].items() if isinstance(k, int)):
        if weight <= weight_limit:
            return fee

    # Check for the lambda functions for the categories with excess weight
    if '>1760' in size_rates[category] and weight > 1760:
        return size_rates[category]['>1760'](weight)
    if '>29760' in size_rates[category] and weight > 29760:
        return size_rates[category]['>29760'](weight)
    if '>31500' in size_rates[category] and weight > 31500:
        return size_rates[category]['>31500'](weight)

    return "No matching weight"
# 瑞典
def calculate_se_fee(category, weight):
    size_rates = {
        'Small envelope': {
            80: 30.04
        },
        'Standard envelope': {
            60: 30.86,
            210: 32.20,
            460: 37.09
        },
        'Large envelope': {
            960: 38.55
        },
        'Extra-large envelope': {
            960: 42.24
        },
        'Small parcel': {
            150: 43.67,
            400: 45.75,
            900: 46.38,
            1400: 47.77,
            1900: 49.37,
            3900: 58.79
        },
        'Standard parcel': {
            150: 47.09,
            400: 49.95,
            900: 50.07,
            1400: 52.34,
            1900: 55.24,
            2900: 58.94,
            3900: 59.11,
            5900: 63.44,
            8900: 65.18,
            11900: 85.31
        },
        'Small oversize1': {
            760: 82.32,
            1260: 84.40,
            1760: 85.26,
            ">1760": lambda w: round(85.26 + 0.1 * math.ceil((w - 1760) / 1000), 2)
        },
        'Standard oversize1': {
            760: 83.09,
            1760: 86.73,
            2760: 101.26,
            3760: 102.09,
            4760: 102.09,
            9760: 106.71,
            14760: 117.29,
            19760: 124.72,
            24760: 139.86,
            29760: 139.92,
            ">29760": lambda w: round(139.92 + 0.1 * math.ceil((w - 29760) / 1000), 2)
        },
        'Large oversize1': {
            4760: 118.02,
            9760: 136.14,
            14760: 145.63,
            19760: 153.90,
            24760: 170.43,
            31500: 170.79,
            ">31500": lambda w: round(170.79 + 0.1 * math.ceil((w - 31500) / 1000), 2)
        }
    }

    if category not in size_rates:
        return "No matching category"

    # Sort the integer weight limits and check if weight falls within them
    for weight_limit, fee in sorted((k, v) for k, v in size_rates[category].items() if isinstance(k, int)):
        if weight <= weight_limit:
            return fee

    # Check for the lambda functions for the categories with excess weight
    if '>1760' in size_rates[category] and weight > 1760:
        return size_rates[category]['>1760'](weight)
    if '>29760' in size_rates[category] and weight > 29760:
        return size_rates[category]['>29760'](weight)
    if '>31500' in size_rates[category] and weight > 31500:
        return size_rates[category]['>31500'](weight)

    return "No matching weight"
# 波兰
def calculate_pl_fee(category, weight):
    size_rates = {
        'Small envelope': {
            80: 4.75
        },
        'Standard envelope': {
            60: 4.80,
            210: 4.94,
            460: 5.20
        },
        'Large envelope': {
            960: 5.64
        },
        'Extra-large envelope': {
            960: 5.70
        },
        'Small parcel': {
            150: 5.70,
            400: 5.77,
            900: 6.55,
            1400: 6.81,
            1900: 6.82,
            3900: 6.86
        },
        'Standard parcel': {
            150: 5.79,
            400: 5.83,
            900: 6.61,
            1400: 6.88,
            1900: 6.89,
            2900: 6.95,
            3900: 7.00,
            5900: 7.08,
            8900: 7.46,
            11900: 9.21
        },
        'Small oversize1': {
            760: 8.05,
            1260: 8.29,
            1760: 8.40,
            ">1760": lambda w: round(8.40 + 0.05 * math.ceil((w - 1760) / 1000), 2)
        },
        'Standard oversize1': {
            760: 8.05,
            1760: 8.40,
            2760: 9.81,
            3760: 9.89,
            4760: 9.89,
            9760: 10.48,
            14760: 11.36,
            19760: 12.08,
            24760: 13.68,
            29760: 13.68,
            ">29760": lambda w: round(13.68 + 0.05 * math.ceil((w - 29760) / 1000), 2)
        },
        'Large oversize1': {
            4760: 10.74,
            9760: 12.39,
            14760: 13.25,
            19760: 14.00,
            24760: 15.51,
            31500: 15.54,
            ">31500": lambda w: round(15.54 + 0.05 * math.ceil((w - 31500) / 1000), 2)
        }
    }

    if category not in size_rates:
        return "No matching category"

    # Sort the integer weight limits and check if weight falls within them
    for weight_limit, fee in sorted((k, v) for k, v in size_rates[category].items() if isinstance(k, int)):
        if weight <= weight_limit:
            return fee

    # Check for the lambda functions for the categories with excess weight
    if '>1760' in size_rates[category] and weight > 1760:
        return size_rates[category]['>1760'](weight)
    if '>29760' in size_rates[category] and weight > 29760:
        return size_rates[category]['>29760'](weight)
    if '>31500' in size_rates[category] and weight > 31500:
        return size_rates[category]['>31500'](weight)

    return "No matching weight"
# 比利时
def calculate_be4_fee(category, weight):
    size_rates = {
        'Small envelope': {
            80: 1.90
        },
        'Standard envelope': {
            60: 2.07,
            210: 2.27,
            460: 2.41
        },
        'Large envelope': {
            960: 2.91
        },
        'Extra-large envelope': {
            960: 3.19
        },
        'Small parcel': {
            150: 2.98,
            400: 3.30,
            900: 3.84,
            1400: 4.51,
            1900: 4.83,
            3900: 6.26
        },
        'Standard parcel': {
            150: 3.21,
            400: 3.60,
            900: 4.14,
            1400: 4.94,
            1900: 5.41,
            2900: 6.27,
            3900: 6.30,
            5900: 6.54,
            8900: 6.90,
            11900: 7.36
        },
        'Small oversize1': {
            760: 6.63,
            1260: 6.78,
            1760: 6.80,
            ">1760": lambda w: round(6.80 + 0.01 * math.ceil((w - 1760) / 1000), 2)
        },
        'Standard oversize1': {
            760: 6.69,
            1760: 6.98,
            2760: 8.03,
            3760: 8.10,
            4760: 8.12,
            9760: 8.54,
            14760: 9.30,
            19760: 9.56,
            24760: 9.64,
            29760: 9.66,
            ">29760": lambda w: round(9.66 + 0.01 * math.ceil((w - 29760) / 1000), 2)
        },
        'Large oversize1': {
            4760: 9.50,
            9760: 10.96,
            14760: 11.64,
            19760: 12.30,
            24760: 13.61,
            31500: 13.64,
            ">31500": lambda w: round(13.64 + 0.01 * math.ceil((w - 31500) / 1000), 2)
        }
    }

    if category not in size_rates:
        return "No matching category"

    # 排序整数类型的重量限制，并逐个检查
    for weight_limit, fee in sorted((k, v) for k, v in size_rates[category].items() if isinstance(k, int)):
        if weight <= weight_limit:
            return fee

    # 检查是否有超重的lambda函数
    if '>1760' in size_rates[category] and weight > 1760:
        return size_rates[category]['>1760'](weight)
    if '>29760' in size_rates[category] and weight > 29760:
        return size_rates[category]['>29760'](weight)
    if '>31500' in size_rates[category] and weight > 31500:
        return size_rates[category]['>31500'](weight)

    return "No matching weight"
# 泛欧计划
def calculate_pan_europe_fee(category, weight):
    size_rates = {
        'Small envelope': {
            80: 1.90
        },
        'Standard envelope': {
            60: 2.09,
            210: 2.23,
            460: 2.39
        },
        'Large envelope': {
            960: 2.74
        },
        'Extra-large envelope': {
            960: 3.12
        },
        'Small parcel': {
            150: 3.12,
            400: 3.32,
            900: 3.70,
            1400: 4.37,
            1900: 4.76,
            3900: 5.97
        },
        'Standard parcel': {
            150: 3.22,
            400: 3.63,
            900: 4.11,
            1400: 4.84,
            1900: 5.32,
            2900: 5.98,
            3900: 6.55,
            5900: 6.89,
            8900: 7.44,
            11900: 7.73
        },
        'Small oversize1': {
            760: 6.39,
            1260: 6.41,
            1760: 6.43,
            ">1760": lambda w: round(6.43 + 0.01 * math.ceil((w - 1760) / 1000), 2)
        },
        'Standard oversize1': {
            760: 6.46,
            1760: 6.77,
            2760: 7.59,
            3760: 7.65,
            4760: 7.68,
            9760: 8.07,
            14760: 8.79,
            19760: 9.34,
            24760: 10.58,
            29760: 10.59,
            ">29760": lambda w: round(10.59 + 0.01 * math.ceil((w - 29760) / 1000), 2)
        },
        'Large oversize1': {
            4760: 9.26,
            9760: 10.66,
            14760: 11.00,
            19760: 11.63,
            24760: 12.86,
            31500: 12.90,
            ">31500": lambda w: round(12.90 + 0.01 * math.ceil((w - 31500) / 1000), 2)
        }
    }

    if category not in size_rates:
        return "No matching category"

    # 排序整数类型的重量限制，并逐个检查
    for weight_limit, fee in sorted((k, v) for k, v in size_rates[category].items() if isinstance(k, int)):
        if weight <= weight_limit:
            return fee

    # 检查是否有超重的lambda函数
    if '>1760' in size_rates[category] and weight > 1760:
        return size_rates[category]['>1760'](weight)
    if '>29760' in size_rates[category] and weight > 29760:
        return size_rates[category]['>29760'](weight)
    if '>31500' in size_rates[category] and weight > 31500:
        return size_rates[category]['>31500'](weight)

    return "No matching weight"


# 综合计算费用的函数
def calculate_total_fee(length, width, height, weight, country):
    category = determine_package_category(length, width, height, weight)
    if not category:
        return "No matching category for dimensions"
    return calculate_shipping_fee(category, weight, country)

# 示例使用
length = 125  # cm
width = 65  # cm
height = 65  # cm
weight = 4700  # g
country = "UK"

fee = calculate_total_fee(length, width, height, weight, country)
print(f"包裹的物流费用是: {fee} ")

