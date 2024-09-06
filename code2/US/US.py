import math

# 商品价格超过这个值就用non-apparel 不然就是low-price
BillingLimit = 1000


def calculate_shipping_fee(length, width, height, weight, price):
    # 确定尺寸类别
    if length <= 15 and width <= 12 and height <= 0.75 and weight <= 16:
        # Small standard-size
        return calculate_small_standard_size(weight, price)
    elif length <= 18 and width <= 14 and height <= 8 and weight <= 320:
        # Large standard-size
        return calculate_large_standard_size(weight, price)
    elif length <= 59 and width <= 33 and height <= 33:
        # Large bulky (需要检查重量是否小于等于 800oz)
        if weight <= 800:
            return calculate_large_bulky(weight, price)
        else:
            # 重量超过 800oz，则归为 Extra-large
            return calculate_extra_large(weight, price)
    else:
        # Extra-large
        return calculate_extra_large(weight, price)


def calculate_small_standard_size(weight, price):
    # Small standard-size 运费逻辑
    weight_ranges = [2, 4, 6, 8, 10, 12, 14, 16]
    non_apparel_prices = [3.06, 3.15, 3.24, 3.33, 3.43, 3.53, 3.60, 3.65]
    low_price_prices = [2.29, 2.38, 2.47, 2.56, 2.66, 2.76, 2.83, 2.88]

    for i, max_weight in enumerate(weight_ranges):
        if weight <= max_weight:
            if price <= BillingLimit:
                return f"Low-price: {low_price_prices[i]} USD"
            else:
                return f"Non-apparel: {non_apparel_prices[i]} USD"


def calculate_large_standard_size(weight, price):
    # Large standard-size 运费逻辑
    if weight <= 48:
        weight_ranges = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48]
        non_apparel_prices = [3.68, 3.9, 4.15, 4.55, 4.99, 5.37, 5.52, 5.77, 5.87, 6.05, 6.21, 6.62]
        low_price_prices = [2.91, 3.13, 3.38, 3.78, 4.22, 4.6, 4.75, 5.0, 5.1, 5.28, 5.44, 5.85]

        for i, max_weight in enumerate(weight_ranges):
            if weight <= max_weight:
                if price <= BillingLimit:
                    return f"Low-price: {low_price_prices[i]} USD"
                else:
                    return f"Non-apparel: {non_apparel_prices[i]} USD"
    else:
        # 超过48oz，使用公式
        non_apparel_formula = 6.92 + math.ceil((weight - 3 * 16) / 4) * 0.08
        low_price_formula = 6.15 + math.ceil((weight - 3 * 16) / 4) * 0.08
        if price <= BillingLimit:
            return f"Low-price: {low_price_formula:.2f} USD"
        else:
            return f"Non-apparel: {non_apparel_formula:.2f} USD"


def calculate_large_bulky(weight, price):
    # Large bulky 运费逻辑 (重量必须 <= 800oz)
    non_apparel_formula = 9.61 + math.ceil((weight - 1 * 16) / 16) * 0.38
    low_price_formula = 8.84 + math.ceil((weight - 1 * 16) / 16) * 0.38
    if price <= BillingLimit:
        return f"Low-price: {low_price_formula:.2f} USD"
    else:
        return f"Non-apparel: {non_apparel_formula:.2f} USD"


def calculate_extra_large(weight, price):
    # Extra-large 运费逻辑
    if weight <= 800:
        non_apparel_formula = 26.33 + math.ceil((weight - 1 * 16) / 16) * 0.38
        low_price_formula = 25.56 + math.ceil((weight - 1 * 16) / 16) * 0.38
    elif weight <= 1120:
        non_apparel_formula = 40.12 + math.ceil((weight - 51 * 16) / 16) * 0.75
        low_price_formula = 39.35 + math.ceil((weight - 51 * 16) / 16) * 0.75
    elif weight <= 2400:
        non_apparel_formula = 54.81 + math.ceil((weight - 71 * 16) / 16) * 0.75
        low_price_formula = 54.04 + math.ceil((weight - 71 * 16) / 16) * 0.75
    else:
        non_apparel_formula = 194.95 + math.ceil((weight - 151 * 16) / 16) * 0.19
        low_price_formula = 194.18 + math.ceil((weight - 151 * 16) / 16) * 0.19

    if price <= BillingLimit:
        return f"Low-price: {low_price_formula:.2f} USD"
    else:
        return f"Non-apparel: {non_apparel_formula:.2f} USD"


# 测试例子
# L,W,H单位都是英尺   重量单位是盎司   还有商品价格，单位美元
length, width, height, weight, price = 20, 15, 10, 345.32, 1100  # 示例数据

fee1 = calculate_shipping_fee(length, width, height, weight, price)
print("用商品重量算出来的费用:" + fee1)

