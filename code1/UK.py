# 定义费用规则

def calculate_shipping_fee(length, width, height, weight):
    # 判断包裹的类型和尺寸
    if length <= 20 and width <= 15 and height <= 1:
        # Small envelope
        if weight <= 80:
            return 2.3
    elif length <= 33 and width <= 23 and height <= 2.5:
        # Standard envelope
        if weight <= 60:
            return 2.5
        elif weight <= 210:
            return 2.7
        elif weight <= 460:
            return 2.9
    elif length <= 33 and width <= 23 and height <= 4:
        # Large envelope
        if weight <= 960:
            return 3.6
    elif length <= 33 and width <= 23 and height <= 6:
        # Extra-large envelope
        if weight <= 960:
            return 3.9
    elif length <= 35 and width <= 25 and height <= 12:
        # Small parcel
        if weight <= 150:
            return 3.9
        elif weight <= 400:
            return 4.0
        elif weight <= 900:
            return 4.0
        elif weight <= 1.4 * 1000:
            return 4.3
        elif weight <= 1.9 * 1000:
            return 4.7
        elif weight <= 3.9 * 1000:
            return 7.4
    elif length <= 45 and width <= 34 and height <= 26:
        # Standard parcel
        if weight <= 150:
            return 4.0
        elif weight <= 400:
            return 4.2
        elif weight <= 900:
            return 4.4
        elif weight <= 1.4 * 1000:
            return 4.7
        elif weight <= 1.9 * 1000:
            return 5.1
        elif weight <= 2.9 * 1000:
            return 7.5
        elif weight <= 3.9 * 1000:
            return 7.9
        elif weight <= 5.9 * 1000:
            return 8.1
        elif weight <= 8.9 * 1000:
            return 9.2
        elif weight <= 11.9 * 1000:
            return 9.7
    elif length <= 61 and width <= 46 and height <= 46:
        # Small oversize1
        if weight <= 760:
            return 7.0
        elif weight <= 1.26 * 1000:
            return 8.1
        elif weight <= 1.76 * 1000:
            return 8.4
        else:
            return 8.4 + 0.01319 * (weight - 1760) / 1000
    elif length <= 120 and width <= 60 and height <= 60:
        # Standard oversize1
        if weight <= 760:
            return 8.3
        elif weight <= 1.76 * 1000:
            return 8.8
        elif weight <= 2.76 * 1000:
            return 9.0
        elif weight <= 3.76 * 1000:
            return 9.0
        elif weight <= 4.76 * 1000:
            return 9.1
        elif weight <= 9.76 * 1000:
            return 10.9
        elif weight <= 14.76 * 1000:
            return 11.6
        elif weight <= 19.76 * 1000:
            return 12.2
        elif weight <= 24.76 * 1000:
            return 13.5
        elif weight <= 29.76 * 1000:
            return 13.5
        else:
            return 13.5 + 0.01319 * (weight - 1760) / 1000
    elif length > 120 and width <= 60 and height <= 60:
        # Large oversize1
        if weight <= 4.76 * 1000:
            return 15.1
        elif weight <= 9.76 * 1000:
            return 16.5
        elif weight <= 14.76 * 1000:
            return 17.4
        elif weight <= 19.76 * 1000:
            return 18.3
        elif weight <= 24.76 * 1000:
            return 19.9
        elif weight <= 31.5 * 1000:
            return 19.9
        else:
            return 19.9 + 0.01319 * (weight - 1760) / 1000
    elif length > 175:
        # Special oversize1
        if weight < 20 * 1000:
            return 20.4
        elif weight < 30 * 1000:
            return 24.4
        elif weight < 40 * 1000:
            return 25.3
        elif weight < 50 * 1000:
            return 56.7
        elif weight < 60 * 1000:
            return 58.4
        else:
            return 58.4 + 0.51441 * (weight - 60 * 1000)

    return "No matching category"

# 示例使用
length = 60  # cm
width = 45   # cm
height = 45  # cm
weight = 2000  # g

fee = calculate_shipping_fee(length, width, height, weight)
print(f"包裹的物流费用是: {fee} 美元")
