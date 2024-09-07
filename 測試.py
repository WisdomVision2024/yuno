def face(input_data):
    item_counts = {
        "Huang": 0,
        "Irene": 0,
        "Paney": 0,
    }
    
    # 確保 input_data 是可迭代的
    for item in input_data:
        if isinstance(item, dict):
            if item["name"] == "Huang" and item["confidence"] > 0.5:
                item_counts["Huang"] += 1
            elif item["name"] == "Irene" and item["confidence"] > 0.5:
                item_counts["Irene"] += 1
            elif item["name"] == "Paney" and item["confidence"] > 0.5:
                item_counts["Paney"] += 1
    
    # 只保留數量大於 0 的項目
    fitem = {item: count for item, count in item_counts.items() if count > 0}
    
    # 構建結果字符串，僅包含物品名稱
    result = "、".join(f"{item}" for item in fitem.keys())
    ans = "畫面中有" + result
    return ans

# 測試資料
a = [
    {"name": "Paney", "confidence": 0.6877386840481583},
    {"name": "Irene", "confidence": 0.6877386840481583},
    {"name": "Huang", "confidence": 0.6877386840481583}
]
b = [
    {"name": "Paney", "confidence": 0.6877386840481583},
    {"name": "Huang", "confidence": 0.6877386840481583}
]
c = [
    {"name": "Paney", "confidence": 0.6877386840481583},
    {"name": "Huang", "confidence": 0.6877386840481583}
]
d = [
    {"name": "Paney", "confidence": 0.6877386840481583},
    {"name": "Huang", "confidence": 0.6877386840481583}
]
e = [
    {"name": "Paney", "confidence": 0.6877386840481583},
    {"name": "Irene", "confidence": 0.6877386840481583},
]

print(face(a))
print(face(b))
print(face(c))
print(face(d))
print(face(e))



