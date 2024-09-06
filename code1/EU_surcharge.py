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
            'Small oversize1': {760: 1.6, 1260: 1.6, 1760: 1.6, 'extra': 1.9},
            'Standard oversize1': {760: 1.6, 1760: 1.7, 2760: 2.1, 3760: 2.1, 4760: 2.1, 9760: 2.2, 14760: 3.5, 19760: 4.5, 24760: 4.6, 29760: 4.6, 'extra': 8.8},
            'Large oversize1': {4760: 2.2, 9760: 2.2, 14760: 3.5, 19760: 4.5, 24760: 4.6, 31500: 4.6, 'extra': 9.1}
        },
        'FR': {
            'Small oversize1': {760: 1.8, 1260: 2.0, 1760: 2.2, 'extra': 2.2},
            'Standard oversize1': {760: 1.8, 1760: 3.2, 2760: 3.2, 3760: 3.2, 4760: 3.2, 9760: 3.3, 14760: 4.4, 19760: 4.4, 24760: 6.6, 29760: 6.7, 'extra': 7.9},
            'Large oversize1': {4760: 3.2, 9760: 3.3, 14760: 4.3, 19760: 4.4, 24760: 4.4, 31500: 6.7, 'extra': 6.7}
        },
        'IT': {
            'Small oversize1': {760: 0.9, 1260: 1.2, 1760: 1.2, 'extra': 1.3},
            'Standard oversize1': {760: 1.4, 1760: 1.6, 2760: 1.6, 3760: 1.7, 4760: 1.7, 9760: 3.8, 14760: 5.5, 19760: 7.8, 24760: 7.8, 29760: 7.9, 'extra': 7.9},
            'Large oversize1': {4760: 3.3, 9760: 6.5, 14760: 6.9, 19760: 7.8, 24760: 7.8, 31500: 7.9, 'extra': 7.9}
        },
        'ES': {
            'Small oversize1': {760: 1.5, 1260: 1.9, 1760: 1.9, 'extra': 2.4},
            'Standard oversize1': {760: 2.9, 1760: 3.4, 2760: 3.4, 3760: 3.4, 4760: 3.8, 9760: 5.4, 14760: 6.8, 19760: 7.8, 24760: 7.8, 29760: 7.9, 'extra': 7.9},
            'Large oversize1': {4760: 3.3, 9760: 6.5, 14760: 6.9, 19760: 7.8, 24760: 7.8, 31500: 7.9, 'extra': 7.9}
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
