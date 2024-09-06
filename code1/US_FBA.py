import math

# 定义 low-price 和 non-apparel 的物流费用规则
low_price_rules = {
    "Small standard-size": {
        "dimensions": {"length": 457.2, "width": 365.8, "height": 22.9},
        "weights": [56.7, 113.4, 170.1, 226.8, 283.5, 340.2, 396.9, 453.6],
        "prices": [2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.8, 2.9]
    },
    "Large standard-size": {
        "dimensions": {"length": 548.6, "width": 426.7, "height": 243.8},
        "weights": [113.4, 226.8, 340.2, 453.6, 567, 680.4, 793.8, 907.2, 1020.6, 1134, 1247.4, 1360.8, 9071.8],
        "prices": [2.9, 3.1, 3.4, 3.8, 4.2, 4.6, 4.8, 5.0, 5.1, 5.3, 5.4, 5.9,
                   '6.15 + 0.08 * ((X - 3*453.5924) / 113.398)']
    },
    "Large bulky": {
        "dimensions": {"length": 1798.3, "width": 1005.8, "height": 1005.8},
        "weight_limit": 22679.6,
        "formula": '8.84 + ((X - 1*453.5924) / 453.5924) * 0.38'
    },
    "Extra-large": {
        "dimensions": {"length": float('inf'), "width": float('inf'), "height": float('inf')},
        "weights": [22679.6, 31751.4, 68038.8, ">68038.8"],
        "formulas": [
            '25.56 + ((X - 1*453.5924) / 453.5924) * 0.38',
            '39.35 + ((X - 51*453.5924) / 453.5924) * 0.75',
            '54.04 + ((X - 71*453.5924) / 453.5924) * 0.75',
            '194.18 + ((X - 151*453.5924) / 453.5924) * 0.19'
        ]
    }
}

non_apparel_rules = {
    "Small standard-size": {
        "dimensions": {"length": 457.2, "width": 365.8, "height": 22.9},
        "weights": [56.7, 113.4, 170.1, 226.8, 283.5, 340.2, 396.9, 453.6],
        "prices": [3.1, 3.2, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7]
    },
    "Large standard-size": {
        "dimensions": {"length": 548.6, "width": 426.7, "height": 243.8},
        "weights": [113.4, 226.8, 340.2, 453.6, 567, 680.4, 793.8, 907.2, 1020.6, 1134, 1247.4, 1360.8, 9071.8],
        "prices": [3.7, 3.9, 4.2, 4.6, 5.0, 5.4, 5.5, 5.8, 5.9, 6.1, 6.2, 6.6,
                   '6.92 + 0.08 * ((X - 3*453.5924) / 113.398)']
    },
    "Large bulky": {
        "dimensions": {"length": 1798.3, "width": 1005.8, "height": 1005.8},
        "weight_limit": 22679.6,
        "formula": '9.61 + ((X - 453.5924) / 453.5924) * 0.38'
    },
    "Extra-large": {
        "dimensions": {"length": float('inf'), "width": float('inf'), "height": float('inf')},
        "weights": [22679.6, 31751.4, 68038.8, ">68038.8"],
        "formulas": [
            '26.33 + ((X - 453.5924) / 453.5924) * 0.38',
            '40.12 + ((X - 51*453.5924) / 453.5924) * 0.75',
            '54.81 + ((X - 71*453.5924) / 453.5924) * 0.75',
            '194.95 + ((X - 151*453.5924) / 453.5924) * 0.19'
        ]
    }
}


# 定义计算物流费用的函数
def calculate_shipping_fee(length, width, height, weight, price):
    # 判断是 low-price 还是 non-apparel
    if price <= 1000:
        rules = low_price_rules
    else:
        rules = non_apparel_rules

    # 检查包裹属于哪个尺寸类别
    if length <= rules["Small standard-size"]["dimensions"]["length"] and \
            width <= rules["Small standard-size"]["dimensions"]["width"] and \
            height <= rules["Small standard-size"]["dimensions"]["height"]:
        # Small standard-size
        for i, w in enumerate(rules["Small standard-size"]["weights"]):
            if weight <= w:
                return rules["Small standard-size"]["prices"][i]

    elif length <= rules["Large standard-size"]["dimensions"]["length"] and \
            width <= rules["Large standard-size"]["dimensions"]["width"] and \
            height <= rules["Large standard-size"]["dimensions"]["height"]:
        # Large standard-size
        for i, w in enumerate(rules["Large standard-size"]["weights"]):
            if weight <= w:
                price_formula = rules["Large standard-size"]["prices"][i]
                if isinstance(price_formula, str):  # 如果是公式，则计算
                    return eval(price_formula.replace('X', str(weight)))
                else:
                    return price_formula

    elif length <= rules["Large bulky"]["dimensions"]["length"] and \
            width <= rules["Large bulky"]["dimensions"]["width"] and \
            height <= rules["Large bulky"]["dimensions"]["height"]:
        # Large bulky
        return eval(rules["Large bulky"]["formula"].replace('X', str(weight)))

    else:
        # Extra-large
        for i, w in enumerate(rules["Extra-large"]["weights"]):
            if isinstance(w, str) or weight <= w:
                return eval(rules["Extra-large"]["formulas"][i].replace('X', str(weight)))

    return "No matching category found"


# 示例使用
length, width, height, weight, price = 1800, 1100, 1100, 22000, 1100  # 可替换为其他包裹数据
fee = calculate_shipping_fee(length, width, height, weight, price)
print(f"包裹的物流费用是: {fee} 美元")
