# 定义附加费计算函数
def determine_package_category(length, width, height):
    """根据包裹的三边，判断包裹的类型"""
    if length <= 61 and width <= 46 and height <= 46:
        return "Small oversize1"
    elif length <= 120 and width <= 60 and height <= 60:
        return "Standard oversize1"
    elif length > 120 and width <= 60 and height <= 60:
        return "Large oversize1"
    else:
        return None  # 不符合 oversize 分类


def calculate_surcharge(length, width, height, weight, country):
    """根据包裹的尺寸、重量和国家计算附加费"""
    surcharge_rates = {
        'DE': {
            'Small oversize1': {760: 1.42, 1260: 1.43, 1760: 1.44, 'extra': 1.67},
            'Standard oversize1': {760: 1.67, 1760: 1.47, 2760: 1.50, 3760: 1.89, 4760: 1.91, 9760: 1.93, 14760: 1.97,
                                   19760: 3.14, 24760: 4.06, 29760: 4.11, 'extra': 7.90},
            'Large oversize1': {4760: 1.95, 9760: 1.99, 14760: 3.16, 19760: 4.08, 24760: 4.13, 31500: 4.18,
                                'extra': 8.18}
        },
        'FR': {
            'Small oversize1': {760: 1.63, 1260: 1.76, 1760: 2.01, 'extra': 2.02},
            'Standard oversize1': {760: 2.02, 1760: 1.65, 2760: 2.86, 3760: 2.88, 4760: 2.89, 9760: 2.91, 14760: 2.96,
                                   19760: 3.93, 24760: 3.98, 29760: 5.98, 'extra': 7.15},
            'Large oversize1': {4760: 2.93, 9760: 2.98, 14760: 3.90, 19760: 3.95, 24760: 4.00, 31500: 6.00,
                                'extra': 6.04}
        },
        'IT': {
            'Small oversize1': {760: 0.77, 1260: 1.07, 1760: 1.12, 'extra': 1.13},
            'Standard oversize1': {760: 1.13, 1760: 1.27, 2760: 1.45, 3760: 1.47, 4760: 1.49, 9760: 1.51, 14760: 3.40,
                                   19760: 4.99, 24760: 7.01, 29760: 7.05, 'extra': 7.15},
            'Large oversize1': {4760: 2.96, 9760: 5.90, 14760: 6.25, 19760: 7.02, 24760: 7.07, 31500: 7.15,
                                'extra': 7.16}
        },
        'ES': {
            'Small oversize1': {760: 1.34, 1260: 1.67, 1760: 1.68, 'extra': 2.16},
            'Standard oversize1': {760: 2.16, 1760: 2.64, 2760: 3.04, 3760: 3.06, 4760: 3.09, 9760: 3.41, 14760: 4.89,
                                   19760: 6.15, 24760: 7.01, 29760: 7.05, 'extra': 7.15},
            'Large oversize1': {4760: 2.96, 9760: 5.90, 14760: 6.25, 19760: 7.02, 24760: 7.07, 31500: 7.15,
                                'extra': 7.16}
        }
    }

    # 获取包裹类别
    category = determine_package_category(length, width, height)

    # 如果没有匹配的 oversize 类别，返回0（没有附加费）
    if not category or country not in surcharge_rates:
        return 0

    # 获取附加费率
    rates = surcharge_rates[country].get(category, {})

    # 匹配重量区间
    for weight_limit, fee in sorted((k, v) for k, v in rates.items() if isinstance(k, int)):
        if weight <= weight_limit:
            return fee

    # 超重的附加费计算
    if 'extra' in rates:
        return rates['extra']

    # 默认无附加费
    return 0


# 示例使用
if __name__ == "__main__":
    length = 61  # cm
    width = 46  # cm
    height = 46  # cm
    weight = 2000  # g
    country = "DE"  # 国家代码

    surcharge = calculate_surcharge(length, width, height, weight, country)
    print(f"附加费是: {surcharge} 美元")
