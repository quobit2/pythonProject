def determine_size_category(length, width, height, weight):
    # 判断尺寸类别
    if length <= 15 and width <= 12 and height <= 0.75 and weight <= 16:
        return "Small standard size"
    elif length <= 18 and width <= 14 and height <= 8 and weight <= 320:
        return "Large standard size"
    elif length <= 59 and width <= 33 and height <= 33 and weight <= 800:
        return "Large bulky"
    elif weight <= 2400:
        return "Extra-large (0 to 150 lb)"
    else:
        return "Extra-large (150+ lb)"

def calculate_shipping_weight(length, width, height, actual_weight):
    # 计算体积重量 (磅)
    dimensional_weight_lbs = (length * width * height) / 139
    # 将体积重量转换为盎司
    dimensional_weight_oz = dimensional_weight_lbs * 16

    # 根据尺寸和重量确定尺寸类别
    size_category = determine_size_category(length, width, height, actual_weight)

    # 根据不同的尺寸类别来判断发货重量
    if size_category == "Small standard size":
        shipping_weight = actual_weight  # 使用商品重量
    elif size_category in ["Large standard size", "Large bulky", "Extra-large (0 to 150 lb)"]:
        # 取商品重量或体积重量中的较大值
        shipping_weight = max(actual_weight, dimensional_weight_oz)
    elif size_category == "Extra-large (150+ lb)":
        shipping_weight = actual_weight  # 只使用商品重量
    else:
        raise ValueError("Unknown size category")

    return shipping_weight, size_category

# 示例输入
length = 20  # 英寸
width = 15   # 英寸
height = 10  # 英寸
actual_weight = 300  # 盎司

# 计算发货重量
shipping_weight, size_category = calculate_shipping_weight(length, width, height, actual_weight)
print(f"Shipping weight: {shipping_weight:.2f} oz")
print(f"Size category: {size_category}")
