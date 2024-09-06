import EU_surcharge

# 定义包裹类型判断逻辑
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
    elif length > 120 and width <= 60 and height <= 60:
        return "Large oversize1"
    elif length > 175:
        return "Special oversize1"
    else:
        return None


# 计算费用（根据不同的国家）
def calculate_shipping_fee(category, weight, country):
    if country == "UK":
        return calculate_uk_fee(category, weight)
    elif country == "FR":
        return calculate_fr_fee(category, weight)
    elif country == "IT":
        return calculate_it_fee(category, weight)
    elif country == "ES":
        return calculate_es_fee(category, weight)
    elif country == "DE":
        return calculate_de_only2_fee(category, weight)
    elif country == "NL":
        return calculate_nl_fee(category, weight)
    elif country == "PL":
        return calculate_pl_fee(category, weight)
    elif country == "BE4":
        return calculate_be4_fee(category, weight)
    # 可以继续为不同国家添加对应的费用规则函数...
    else:
        return "No matching country"

# 英国的费用规则
def calculate_uk_fee(category, weight):
    size_rates = {
        "Small envelope": {80: 2.3},
        "Standard envelope": {60: 2.5, 210: 2.7, 460: 2.9},
        "Large envelope": {960: 3.6},
        "Extra-large envelope": {960: 3.9},
        "Small parcel": {150: 3.9, 400: 4.0, 900: 4.0, 1400: 4.3, 1900: 4.7, 3900: 7.4},
        "Standard parcel": {150: 4.0, 400: 4.2, 900: 4.4, 1400: 4.7, 1900: 5.1, 2900: 7.5, 3900: 7.9, 5900: 8.1,
                            8900: 9.2, 11900: 9.7},
        "Small oversize1": {760: 7.0, 1260: 8.1, 1760: 8.4, ">1760": lambda w: 8.4 + 0.01319 * (w - 1760) / 1000},
        "Standard oversize1": {760: 8.3, 1760: 8.8, 2760: 9.0, 3760: 9.0, 4760: 9.1, 9760: 10.9, 14760: 11.6,
                               19760: 12.2, 24760: 13.5, 29760: 13.5,
                               ">29760": lambda w: 13.5 + 0.01319 * (w - 29760) / 1000},
        "Large oversize1": {4760: 15.1, 9760: 16.5, 14760: 17.4, 19760: 18.3, 24760: 19.9, 31500: 19.9,
                            ">31500": lambda w: 19.9 + 0.01319 * (w - 31500) / 1000},
        "Special oversize1": {20000: 20.4, 30000: 24.4, 40000: 25.3, 50000: 56.7, 60000: 58.4,
                              ">60000": lambda w: 58.4 + 0.51441 * (w - 60000)}
    }

    if category not in size_rates:
        return "No matching category"

    # 排序整数类型的重量限制，并逐个检查
    for weight_limit, fee in sorted((k, v) for k, v in size_rates[category].items() if isinstance(k, int)):
        if weight <= weight_limit:
            return fee

    # 如果没有匹配的整数类型的重量限制，检查是否有超重的lambda函数
    if ">1760" in size_rates[category] and weight > 1760:
        return size_rates[category][">1760"](weight)
    if ">29760" in size_rates[category] and weight > 29760:
        return size_rates[category][">29760"](weight)
    if ">31500" in size_rates[category] and weight > 31500:
        return size_rates[category][">31500"](weight)
    if ">60000" in size_rates[category] and weight > 60000:
        return size_rates[category][">60000"](weight)

    return "No matching weight"
# 法国的费用规则
def calculate_fr_fee(category, weight):
    size_rates = {
        'Small envelope': {
            80: 3.0
        },
        'Standard envelope': {
            60: 3.1,
            210: 3.7,
            460: 4.2
        },
        'Large envelope': {
            960: 4.9
        },
        'Extra-large envelope': {
            960: 5.3
        },
        'Small parcel': {
            150: 5.3,
            400: 5.7,
            900: 6.6,
            1400: 6.8,
            1900: 6.9,
            3900: 10.6
        },
        'Standard parcel': {
            150: 5.4,
            400: 6.1,
            900: 7.1,
            1400: 7.5,
            1900: 7.7,
            2900: 10.6,
            3900: 10.8,
            5900: 11.3,
            8900: 12.3,
            11900: 12.9
        },
        'Small oversize1': {
            760: 10.4,
            1260: 10.8,
            1760: 11.5
        },
        'Standard oversize1': {
            760: 10.4,
            1760: 11.5,
            2760: 12.3,
            3760: 12.8,
            4760: 12.9,
            9760: 13.9,
            14760: 14.9,
            19760: 15.7,
            24760: 15.7,
            29760: 17.5
        },
        'Large oversize1': {
            4760: 18.8,
            9760: 22.8,
            14760: 24.1,
            19760: 25.2,
            24760: 27.6,
            31500: 28.2
        },
        'Special oversize1': {
            20000: 26.6,
            30000: 34.2,
            40000: 35.2,
            50000: 59.9,
            60000: 61.7
        }
    }

    # 找到相应的重量区间并计算费用
    if category in size_rates:
        for weight_limit, fee in sorted(size_rates[category].items()):
            if weight <= weight_limit:
                return fee
        # 如果超过了最高重量区间，返回超重费用计算
        if category == 'Small oversize1' and weight > 1760:
            return 11.5 + 0.0109 * (weight - 1760) / 1000
        elif category == 'Standard oversize1' and weight > 29760:
            return 17.5 + 0.0109 * (weight - 1760) / 1000
        elif category == 'Large oversize1' and weight > 31500:
            return 28.2 + 0.0109 * (weight - 1760) / 1000
        elif category == 'Special oversize1' and weight > 60000:
            return 61.7 + 0.46578 * (weight - 60000) / 1000

    return "No matching category"
# 定义意大利的费用规则
def calculate_it_fee(category, weight):
    size_rates = {
        'Small envelope': {
            80: 3.4
        },
        'Standard envelope': {
            60: 3.6,
            210: 3.7,
            460: 4.0
        },
        'Large envelope': {
            960: 4.9
        },
        'Extra-large envelope': {
            960: 4.6
        },
        'Small parcel': {
            150: 4.6,
            400: 4.9,
            900: 5.5,
            1400: 6.2,
            1900: 6.5,
            3900: 8.5
        },
        'Standard parcel': {
            150: 5.0,
            400: 5.6,
            900: 6.4,
            1400: 7.2,
            1900: 7.5,
            2900: 8.6,
            3900: 8.9,
            5900: 10.1,
            8900: 11.2,
            11900: 12.1
        },
        'Small oversize1': {
            760: 10.2,
            1260: 10.8,
            1760: 10.9
        },
        'Standard oversize1': {
            760: 10.9,
            1760: 11.0,
            2760: 11.0,
            3760: 11.8,
            4760: 11.8,
            9760: 13.4,
            14760: 14.9,
            19760: 15.4,
            24760: 16.4,
            29760: 17.2
        },
        'Large oversize1': {
            4760: 12.0,
            9760: 13.7,
            14760: 15.0,
            19760: 15.5,
            24760: 17.4,
            31500: 17.5
        },
        'Special oversize1': {
            20000: 19.3,
            30000: 22.4,
            40000: 23.2,
            50000: 31.0,
            60000: 31.6
        }
    }

    # 找到相应的重量区间并计算费用
    if category in size_rates:
        for weight_limit, fee in sorted(size_rates[category].items()):
            if weight <= weight_limit:
                return fee
        # 如果超过了最高重量区间，返回超重费用计算
        if category == 'Small oversize1' and weight > 1760:
            return 10.9 + 0.0109 * (weight - 1760) / 1000
        elif category == 'Standard oversize1' and weight > 29760:
            return 17.2 + 0.0109 * (weight - 1760) / 1000
        elif category == 'Large oversize1' and weight > 31500:
            return 17.5 + 0.0109 * (weight - 1760) / 1000
        elif category == 'Special oversize1' and weight > 60000:
            return 31.6 + 0.6654 * (weight - 60000) / 1000

    return "No matching category"
# 定义西班牙的费用规则
def calculate_es_fee(category, weight):
    size_rates = {
        'Small envelope': {
            80: 2.8
        },
        'Standard envelope': {
            60: 3.1,
            210: 3.7,
            460: 4.0
        },
        'Large envelope': {
            960: 4.3
        },
        'Extra-large envelope': {
            960: 4.6
        },
        'Small parcel': {
            150: 4.2,
            400: 4.5,
            900: 4.7,
            1400: 5.3,
            1900: 5.3,
            3900: 7.0
        },
        'Standard parcel': {
            150: 4.2,
            400: 5.0,
            900: 5.6,
            1400: 6.0,
            1900: 6.1,
            2900: 7.0,
            3900: 8.5,
            5900: 8.8,
            8900: 8.8,
            11900: 8.8
        },
        'Small oversize1': {
            760: 8.1,
            1260: 8.9,
            1760: 9.0
        },
        'Standard oversize1': {
            760: 8.2,
            1760: 9.0,
            2760: 9.9,
            3760: 10.0,
            4760: 10.3,
            9760: 15.1,
            14760: 16.3,
            19760: 17.7,
            24760: 19.3,
            29760: 19.7
        },
        'Large oversize1': {
            4760: 12.4,
            9760: 16.6,
            14760: 18.0,
            19760: 19.3,
            24760: 20.9,
            31500: 23.9
        },
        'Special oversize1': {
            20000: 19.7,
            30000: 27.0,
            40000: 28.0,
            50000: 43.6,
            60000: 44.4
        }
    }

    # 找到相应的重量区间并计算费用
    if category in size_rates:
        for weight_limit, fee in sorted(size_rates[category].items()):
            if weight <= weight_limit:
                return fee
        # 如果超过了最高重量区间，返回超重费用计算
        if category == 'Small oversize1' and weight > 1760:
            return 9.0 + 0.0109 * (weight - 1760) / 1000
        elif category == 'Standard oversize1' and weight > 29760:
            return 19.7 + 0.0109 * (weight - 1760) / 1000
        elif category == 'Large oversize1' and weight > 31500:
            return 23.9 + 0.0109 * (weight - 1760) / 1000
        elif category == 'Special oversize1' and weight > 60000:
            return 44.4 + 0.6654 * (weight - 60000) / 1000

    return "No matching category"
# 定义德国专用 (DE only2) 的费用规则
def calculate_de_only2_fee(category, weight):
    size_rates = {
        'Small envelope': {
            80: 2.4
        },
        'Standard envelope': {
            60: 2.6,
            210: 2.8,
            460: 2.9
        },
        'Large envelope': {
            960: 3.3
        },
        'Extra-large envelope': {
            960: 3.7
        },
        'Small parcel': {
            150: 3.7,
            400: 4.0,
            900: 4.4,
            1400: 5.1,
            1900: 5.6,
            3900: 6.9
        },
        'Standard parcel': {
            150: 3.9,
            400: 4.3,
            900: 4.8,
            1400: 5.7,
            1900: 6.2,
            2900: 6.9,
            3900: 7.6,
            5900: 7.9,
            8900: 8.5,
            11900: 8.9
        },
        'Small oversize1': {
            760: 7.4,
            1260: 7.4,
            1760: 7.4
        },
        'Standard oversize1': {
            760: 7.5,
            1760: 7.8,
            2760: 8.7,
            3760: 8.8,
            4760: 8.8,
            9760: 9.2,
            14760: 10.0,
            19760: 10.6,
            24760: 12.0,
            29760: 12.0
        },
        'Large oversize1': {
            4760: 10.6,
            9760: 12.1,
            14760: 12.5,
            19760: 13.2,
            24760: 14.6,
            31500: 14.6
        },
        'Special oversize1': {
            20000: 22.2,
            30000: 30.1,
            40000: 31.6,
            50000: 66.5,
            60000: 67.8
        }
    }

    # 找到相应的重量区间并计算费用
    if category in size_rates:
        for weight_limit, fee in sorted(size_rates[category].items()):
            if weight <= weight_limit:
                return fee
        # 如果超过了最高重量区间，返回超重费用计算
        if category == 'Small oversize1' and weight > 1760:
            return 7.4 + 0.0109 * (weight - 1760) / 1000
        elif category == 'Standard oversize1' and weight > 29760:
            return 12.0 + 0.0109 * (weight - 1760) / 1000
        elif category == 'Large oversize1' and weight > 31500:
            return 14.6 + 0.0109 * (weight - 1760) / 1000
        elif category == 'Special oversize1' and weight > 60000:
            return 67.8 + 0.42142 * (weight - 60000) / 1000

    return "No matching category"
# 定义CEP (DE/PL/CZ)/IT/ES 的费用规则
def calculate_cep_it_es_fee(category, weight):
    size_rates = {
        'Small envelope': {
            80: 2.1
        },
        'Standard envelope': {
            60: 2.3,
            210: 2.5,
            460: 2.7
        },
        'Large envelope': {
            960: 3.0
        },
        'Extra-large envelope': {
            960: 3.5
        },
        'Small parcel': {
            150: 3.5,
            400: 3.7,
            900: 4.1,
            1400: 4.8,
            1900: 5.3,
            3900: 6.6
        },
        'Standard parcel': {
            150: 3.6,
            400: 4.0,
            900: 4.6,
            1400: 5.4,
            1900: 5.9,
            2900: 6.6,
            3900: 7.3,
            5900: 7.6,
            8900: 8.3,
            11900: 8.6
        },
        'Small oversize1': {
            760: 7.1,
            1260: 7.1,
            1760: 7.1
        },
        'Standard oversize1': {
            760: 7.2,
            1760: 7.5,
            2760: 8.4,
            3760: 8.5,
            4760: 8.5,
            9760: 8.9,
            14760: 9.7,
            19760: 10.4,
            24760: 11.7,
            29760: 11.7
        },
        'Large oversize1': {
            4760: 10.3,
            9760: 11.8,
            14760: 12.2,
            19760: 12.9,
            24760: 14.3,
            31500: 14.3
        }
    }

    # 找到相应的重量区间并计算费用
    if category in size_rates:
        for weight_limit, fee in sorted(size_rates[category].items()):
            if weight <= weight_limit:
                return fee
        # 如果超过了最高重量区间，返回超重费用计算
        if category == 'Small oversize1' and weight > 1760:
            return 7.1 + 0.0109 * (weight - 1760) / 1000
        elif category == 'Standard oversize1' and weight > 29760:
            return 11.7 + 0.0109 * (weight - 1760) / 1000
        elif category == 'Large oversize1' and weight > 31500:
            return 14.3 + 0.0109 * (weight - 1760) / 1000

    return "No matching category"
# 定义荷兰 (NL) 的费用规则
def calculate_nl_fee(category, weight):
    size_rates = {
        'Small envelope': {
            80: 2.1
        },
        'Standard envelope': {
            60: 2.3,
            210: 2.5,
            460: 2.7
        },
        'Large envelope': {
            960: 3.2
        },
        'Extra-large envelope': {
            960: 3.6
        },
        'Small parcel': {
            150: 3.6,
            400: 3.6,
            900: 4.2,
            1400: 5.0,
            1900: 5.3,
            3900: 6.9
        },
        'Standard parcel': {
            150: 3.6,
            400: 4.0,
            900: 4.6,
            1400: 5.5,
            1900: 6.0,
            2900: 6.9,
            3900: 7.0,
            5900: 7.2,
            8900: 7.6,
            11900: 8.1
        },
        'Small oversize1': {
            760: 8.0,
            1260: 8.0,
            1760: 8.0
        },
        'Standard oversize1': {
            760: 8.0,
            1760: 8.4,
            2760: 9.3,
            3760: 9.4,
            4760: 9.4,
            9760: 9.7,
            14760: 10.6,
            19760: 11.3,
            24760: 11.9,
            29760: 11.9
        },
        'Large oversize1': {
            4760: 11.0,
            9760: 12.6,
            14760: 13.1,
            19760: 13.9,
            24760: 15.3,
            31500: 15.4
        }
    }

    # 找到相应的重量区间并计算费用
    if category in size_rates:
        for weight_limit, fee in sorted(size_rates[category].items()):
            if weight <= weight_limit:
                return fee
        # 如果超过了最高重量区间，返回超重费用计算
        if category == 'Small oversize1' and weight > 1760:
            return 8.0 + 0.0109 * (weight - 1760) / 1000
        elif category == 'Standard oversize1' and weight > 29760:
            return 11.9 + 0.0109 * (weight - 1760) / 1000
        elif category == 'Large oversize1' and weight > 31500:
            return 15.4 + 0.0109 * (weight - 1760) / 1000

    return "No matching category"
# 定义瑞典 (SE) 的费用规则
def calculate_se_fee(category, weight):
    size_rates = {
        'Small envelope': {
            80: 2.9
        },
        'Standard envelope': {
            60: 3.0,
            210: 3.2,
            460: 3.6
        },
        'Large envelope': {
            960: 3.8
        },
        'Extra-large envelope': {
            960: 4.1
        },
        'Small parcel': {
            150: 4.3,
            400: 4.5,
            900: 4.5,
            1400: 4.7,
            1900: 4.8,
            3900: 5.8
        },
        'Standard parcel': {
            150: 4.6,
            400: 4.9,
            900: 4.9,
            1400: 5.1,
            1900: 5.4,
            2900: 5.8,
            3900: 5.8,
            5900: 6.2,
            8900: 6.4,
            11900: 8.4
        },
        'Small oversize1': {
            760: 8.1,
            1260: 8.3,
            1760: 8.4
        },
        'Standard oversize1': {
            760: 8.1,
            1760: 8.5,
            2760: 9.9,
            3760: 10.0,
            4760: 10.0,
            9760: 10.5,
            14760: 11.5,
            19760: 12.2,
            24760: 13.7,
            29760: 13.7
        },
        'Large oversize1': {
            4760: 11.6,
            9760: 13.3,
            14760: 14.3,
            19760: 15.1,
            24760: 16.7,
            31500: 16.7
        }
    }

    # 找到相应的重量区间并计算费用
    if category in size_rates:
        for weight_limit, fee in sorted(size_rates[category].items()):
            if weight <= weight_limit:
                return fee
        # 如果超过了最高重量区间，返回超重费用计算
        if category == 'Small oversize1' and weight > 1760:
            return 8.4 + 0.0109 * (weight - 1760) / 1000
        elif category == 'Standard oversize1' and weight > 29760:
            return 13.7 + 0.0109 * (weight - 1760) / 1000
        elif category == 'Large oversize1' and weight > 31500:
            return 16.7 + 0.0109 * (weight - 1760) / 1000

    return "No matching category"
# 定义波兰 (PL) 的费用规则
def calculate_pl_fee(category, weight):
    size_rates = {
        'Small envelope': {
            80: 1.2
        },
        'Standard envelope': {
            60: 1.2,
            210: 1.3,
            460: 1.3
        },
        'Large envelope': {
            960: 1.5
        },
        'Extra-large envelope': {
            960: 1.5
        },
        'Small parcel': {
            150: 1.5,
            400: 1.5,
            900: 1.7,
            1400: 1.8,
            1900: 1.8,
            3900: 1.8
        },
        'Standard parcel': {
            150: 1.5,
            400: 1.5,
            900: 1.7,
            1400: 1.8,
            1900: 1.8,
            2900: 1.8,
            3900: 1.8,
            5900: 1.8,
            8900: 1.9,
            11900: 2.4
        },
        'Small oversize1': {
            760: 2.1,
            1260: 2.1,
            1760: 2.2
        },
        'Standard oversize1': {
            760: 2.1,
            1760: 2.2,
            2760: 2.5,
            3760: 2.6,
            4760: 2.6,
            9760: 2.7,
            14760: 2.9,
            19760: 3.1,
            24760: 3.5,
            29760: 3.5
        },
        'Large oversize1': {
            4760: 2.8,
            9760: 3.2,
            14760: 3.4,
            19760: 3.6,
            24760: 4.0,
            31500: 4.0
        }
    }

    if category in size_rates:
        for weight_limit, fee in sorted(size_rates[category].items()):
            if weight <= weight_limit:
                return fee
        # 如果超重，计算额外费用
        if category == 'Small oversize1' and weight > 1760:
            return 2.2 + 0.0109 * (weight - 1760) / 1000
        elif category == 'Standard oversize1' and weight > 29760:
            return 3.5 + 0.0109 * (weight - 1760) / 1000
        elif category == 'Large oversize1' and weight > 31500:
            return 4.0 + 0.0109 * (weight - 1760) / 1000

    return "No matching category"
# 定义比利时 (BE4) 的费用规则
def calculate_be4_fee(category, weight):
    size_rates = {
        'Small envelope': {
            80: 2.1
        },
        'Standard envelope': {
            60: 2.3,
            210: 2.5,
            460: 2.7
        },
        'Large envelope': {
            960: 3.2
        },
        'Extra-large envelope': {
            960: 3.5
        },
        'Small parcel': {
            150: 3.3,
            400: 3.7,
            900: 4.3,
            1400: 5.0,
            1900: 5.4,
            3900: 6.9
        },
        'Standard parcel': {
            150: 3.6,
            400: 4.0,
            900: 4.6,
            1400: 5.5,
            1900: 6.0,
            2900: 7.0,
            3900: 7.0,
            5900: 7.3,
            8900: 7.7,
            11900: 8.2
        },
        'Small oversize1': {
            760: 7.4,
            1260: 7.5,
            1760: 7.5
        },
        'Standard oversize1': {
            760: 7.4,
            1760: 7.7,
            2760: 8.9,
            3760: 9.0,
            4760: 9.0,
            9760: 9.5,
            14760: 10.3,
            19760: 10.6,
            24760: 10.7,
            29760: 10.7
        },
        'Large oversize1': {
            4760: 10.5,
            9760: 12.2,
            14760: 12.9,
            19760: 13.6,
            24760: 15.1,
            31500: 15.1
        }
    }

    if category in size_rates:
        for weight_limit, fee in sorted(size_rates[category].items()):
            if weight <= weight_limit:
                return fee
        # 如果超重，计算额外费用
        if category == 'Small oversize1' and weight > 1760:
            return 7.5 + 0.0109 * (weight - 1760) / 1000
        elif category == 'Standard oversize1' and weight > 29760:
            return 10.7 + 0.0109 * (weight - 1760) / 1000
        elif category == 'Large oversize1' and weight > 31500:
            return 15.1 + 0.0109 * (weight - 1760) / 1000

    return "No matching category"




# 综合计算费用的函数
def calculate_total_fee(length, width, height, weight, country):
    category = determine_package_category(length, width, height, weight)
    if not category:
        return "No matching category for dimensions"

    surcharge = EU_surcharge.calculate_surcharge(length, width, height, weight, country)
    print(f"物流费用: {surcharge}")
    return calculate_shipping_fee(category, weight, country) + surcharge


# 示例使用
length = 60  # cm
width = 45  # cm
height = 45  # cm
weight = 2000  # g
country = "FR"

fee = calculate_total_fee(length, width, height, weight, country)
print(f"包裹的物流费用是: {fee} ")

