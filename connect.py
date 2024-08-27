import json
import google.generativeai as genai
import os

api_key = 'AIzaSyBCcg0skdWwwG-hBucIvDCLHY9FFtzw9-0'
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

def con(input_data):
    item_counts = {
        "本書": 0,
        "個水壺": 0,  # 初始值
        "張椅子": 0,
        "張桌子": 0,   # 初始值
        "台筆電": 0,
        "枝筆": 0
    }
    # 確保 input_data 是可迭代的
    for item in input_data:
        if isinstance(item, dict):
            if item["name"] == "Book" and item["confidence"] > 0.6:
                item_counts["本書"] += 1
            elif item["name"] == "Bottle" and item["confidence"] > 0.6:
                item_counts["個水壺"] += 1
            elif item["name"] == "Chair" and item["confidence"] > 0.6:
                item_counts["張椅子"] += 1
            elif item["name"] == "Desk" and item["confidence"] > 0.6:
                item_counts["張桌子"] += 1
            elif item["name"] == "Laptop" and item["confidence"] > 0.6:
                item_counts["台筆電"] += 1
            elif item["name"] == "Pen" and item["confidence"] > 0.6:
                item_counts["枝筆"] += 1
    # 只保留數量大於 0 的項目
    fitem = {item: count for item, count in item_counts.items() if count > 0}
    
    # 構建結果字符串，包含物品名稱和數量
    result = "、".join(f"{count}{item}" for item, count in fitem.items())
    ans="畫面中有"+result
    return ans

# 測試資料
a = [
    {"name": "Pen", "class": 5, "confidence": 0.88762, "box": {"x1": 228.48288, "y1": 236.46939, "x2": 402.25836, "y2": 362.51645}},
    {"name": "Chair", "class": 5, "confidence": 0.88762, "box": {"x1": 228.48288, "y1": 236.46939, "x2": 402.25836, "y2": 362.51645}},
    {"name": "Chair", "class": 5, "confidence": 0.88762, "box": {"x1": 228.48288, "y1": 236.46939, "x2": 402.25836, "y2": 362.51645}},
    {"name": "Chair", "class": 5, "confidence": 0.88762, "box": {"x1": 228.48288, "y1": 236.46939, "x2": 402.25836, "y2": 362.51645}},
    {"name": "Chair", "class": 5, "confidence": 0.88762, "box": {"x1": 228.48288, "y1": 236.46939, "x2": 402.25836, "y2": 362.51645}},
    {"name": "Chair", "class": 5, "confidence": 0.88762, "box": {"x1": 228.48288, "y1": 236.46939, "x2": 402.25836, "y2": 362.51645}},
    {"name": "Pen", "class": 5, "confidence": 0.5721, "box": {"x1": 322.14481, "y1": 270.21649, "x2": 441.98309, "y2": 342.27811}},
    {"name": "Book", "class": 5, "confidence": 0.8721, "box": {"x1": 322.14481, "y1": 270.21649, "x2": 441.98309, "y2": 342.27811}},
    {"name": "Pen", "class": 5, "confidence": 0.76254, "box": {"x1": 237.65097, "y1": 324.98867, "x2": 391.23650, "y2": 411.85339}}
]

print(con(a))

b = [
    {"name": "Pen", "class": 5, "confidence": 0.88762, "box": {"x1": 228.48288, "y1": 236.46939, "x2": 402.25836, "y2": 362.51645}},
     {"name": "Desk", "class": 5, "confidence": 0.8721, "box": {"x1": 322.14481, "y1": 270.21649, "x2": 441.98309, "y2": 342.27811}},
         {"name": "Chair", "class": 5, "confidence": 0.88762, "box": {"x1": 228.48288, "y1": 236.46939, "x2": 402.25836, "y2": 362.51645}},
    {"name": "Chair", "class": 5, "confidence": 0.88762, "box": {"x1": 228.48288, "y1": 236.46939, "x2": 402.25836, "y2": 362.51645}},
    {"name": "Chair", "class": 5, "confidence": 0.88762, "box": {"x1": 228.48288, "y1": 236.46939, "x2": 402.25836, "y2": 362.51645}},
    {"name": "Chair", "class": 5, "confidence": 0.88762, "box": {"x1": 228.48288, "y1": 236.46939, "x2": 402.25836, "y2": 362.51645}},
    {"name": "Chair", "class": 5, "confidence": 0.88762, "box": {"x1": 228.48288, "y1": 236.46939, "x2": 402.25836, "y2": 362.51645}},
    {"name": "Chair", "class": 5, "confidence": 0.88762, "box": {"x1": 228.48288, "y1": 236.46939, "x2": 402.25836, "y2": 362.51645}},
    {"name": "Book", "class": 5, "confidence": 0.8721, "box": {"x1": 322.14481, "y1": 270.21649, "x2": 441.98309, "y2": 342.27811}}
    
]
print(con(b))
c = [
    {"name": "Pen", "class": 5, "confidence": 0.88762, "box": {"x1": 228.48288, "y1": 236.46939, "x2": 402.25836, "y2": 362.51645}},
    {"name": "Book", "class": 5, "confidence": 0.8721, "box": {"x1": 322.14481, "y1": 270.21649, "x2": 441.98309, "y2": 342.27811}},
        {"name": "Chair", "class": 5, "confidence": 0.88762, "box": {"x1": 228.48288, "y1": 236.46939, "x2": 402.25836, "y2": 362.51645}},
    {"name": "Chair", "class": 5, "confidence": 0.88762, "box": {"x1": 228.48288, "y1": 236.46939, "x2": 402.25836, "y2": 362.51645}},
    {"name": "Chair", "class": 5, "confidence": 0.88762, "box": {"x1": 228.48288, "y1": 236.46939, "x2": 402.25836, "y2": 362.51645}},
    {"name": "Chair", "class": 5, "confidence": 0.88762, "box": {"x1": 228.48288, "y1": 236.46939, "x2": 402.25836, "y2": 362.51645}},
    {"name": "Chair", "class": 5, "confidence": 0.88762, "box": {"x1": 228.48288, "y1": 236.46939, "x2": 402.25836, "y2": 362.51645}},
    {"name": "Chair", "class": 5, "confidence": 0.88762, "box": {"x1": 228.48288, "y1": 236.46939, "x2": 402.25836, "y2": 362.51645}},
    {"name": "Desk", "class": 5, "confidence": 0.8721, "box": {"x1": 322.14481, "y1": 270.21649, "x2": 441.98309, "y2": 342.27811}},
    {"name": "Desk", "class": 5, "confidence": 0.8721, "box": {"x1": 322.14481, "y1": 270.21649, "x2": 441.98309, "y2": 342.27811}},
    {"name": "Pen", "class": 5, "confidence": 0.5721, "box": {"x1": 322.14481, "y1": 270.21649, "x2": 441.98309, "y2": 342.27811}},
    {"name": "Pen", "class": 5, "confidence": 0.76254, "box": {"x1": 237.65097, "y1": 324.98867, "x2": 391.23650, "y2": 411.85339}}
]
d = [
    {"name": "Pen", "class": 5, "confidence": 0.88762, "box": {"x1": 228.48288, "y1": 236.46939, "x2": 402.25836, "y2": 362.51645}},
    {"name": "Pen", "class": 5, "confidence": 0.5721, "box": {"x1": 322.14481, "y1": 270.21649, "x2": 441.98309, "y2": 342.27811}},
    {"name": "Desk", "class": 5, "confidence": 0.8721, "box": {"x1": 322.14481, "y1": 270.21649, "x2": 441.98309, "y2": 342.27811}},
    {"name": "Desk", "class": 5, "confidence": 0.8721, "box": {"x1": 322.14481, "y1": 270.21649, "x2": 441.98309, "y2": 342.27811}},
    {"name": "Pen", "class": 5, "confidence": 0.76254, "box": {"x1": 237.65097, "y1": 324.98867, "x2": 391.23650, "y2": 411.85339}}
]
e = [
    {"name": "Pen", "class": 5, "confidence": 0.88762, "box": {"x1": 228.48288, "y1": 236.46939, "x2": 402.25836, "y2": 362.51645}},
    {"name": "Pen", "class": 5, "confidence": 0.5721, "box": {"x1": 322.14481, "y1": 270.21649, "x2": 441.98309, "y2": 342.27811}},
    {"name": "Desk", "class": 5, "confidence": 0.8721, "box": {"x1": 322.14481, "y1": 270.21649, "x2": 441.98309, "y2": 342.27811}},
    {"name": "Desk", "class": 5, "confidence": 0.8721, "box": {"x1": 322.14481, "y1": 270.21649, "x2": 441.98309, "y2": 342.27811}},
    {"name": "Desk", "class": 5, "confidence": 0.8721, "box": {"x1": 322.14481, "y1": 270.21649, "x2": 441.98309, "y2": 342.27811}},
    {"name": "Pen", "class": 5, "confidence": 0.76254, "box": {"x1": 237.65097, "y1": 324.98867, "x2": 391.23650, "y2": 411.85339}}
]
x=("結果一:"+con(a)+"\n，結果二:"+con(b)+ "\n，結果三:"+con(c)+"\n，結果四:"+con(d)+"\n，結果五:"+con(e))
print(x)
response = model.generate_content("現在一共有六種物品，分別是書、水壺、椅子、桌子、筆電、筆，接下來會有五個結果敘述出畫面中六種物品的數量，畫面中沒有提到即代表數量為0，同一種物品在不同結果中可能會有不同數量，請綜合所有結果，以多數為真的邏輯，整合出最終答案，以下中括號中的文字為例題:[結果一:畫面中有1本書、3個水壺、7張椅子、39張桌子、2枝筆，結果二:畫面中有1本書、3個水壺、7張椅子、40張桌子、1枝筆，結果三:畫面中有1本書、3個水壺、7張椅子、40張桌子、1台筆電、2枝筆，結果四:畫面中有2本書、3個水壺、7張椅子、40張桌子、2枝筆，結果五:畫面中有3個水壺、7張椅子、40張桌子、2枝筆]以下中括號部分為思考過程，接下來請完全參考此過程作答[判斷書:三個結果中書數量為1，一個結果中書數量為2，一個結果中書數量為0，因為最多結果顯示書的數量為1，所以最終書的數量為1；判斷水壺:五個結果中水壺數量為3，因為最多結果顯示水壺的數量為3，所以最終水壺的數量為3；判斷椅子:五個結果中椅子數量為7，因為最多結果顯示椅子的數量為3，所以最終椅子的數量為7；判斷桌子:四個結果中桌子數量為40，一個結果中桌子數量為39，因為最多結果顯示桌子的數量為40，所以最終桌子的數量為40；判斷筆電:4個結果中沒有提到筆電，即代表數量為0，一個結果中筆電數量為，因為最多結果顯示筆電的數量為0，所以最終筆電的數量為0，由於數量為0，最後答案不必顯示；判斷筆:四個結果中筆的數量為2，一個結果中筆的數量為1，因為最多結果顯示筆的數量為2，所以最終筆的數量為2；判斷完所有物品即可整合出答案:畫面中有1本書、3個水壺、7張椅子、40張桌子、2枝筆；以下是你之前回答正確的紀錄，這正是我想要的回答:結果一:畫面中有1本書、2枝筆，結果二:畫面中有1本書、1張桌子、1枝筆，結果三:畫面中有1本書、2張桌子、2枝筆，結果四:畫面中有2張桌子、2枝筆，結果五:畫面中有3張桌子、2枝筆**思考流程：****判斷書：*** 三個結果中書數量為1，兩個結果中書數量為0。* 最多結果顯示書的數量為1，故最終書的數量為1。**判斷筆：*** 五個結果中筆的數量為2，故最終筆的數量為2。**判斷桌子：*** 三個結果中桌子數量為2，兩個結果中桌子數量為1，一個結果中桌子數量為3。* 最多結果顯示桌子的數量為2，故最終桌子的數量為2。]。以下為題目，請參考剛剛的思考流程整合結果，再次強調，我需要的是重複次數最多的答案，請幫我隱藏過程，只留下最終答案:"+x)
print(response.text)
q=input("輸入問題:")
response = model.generate_content("現在"+response.text+"，此為使用者前方的畫面，請根據此回答問題，請回答完整句子，如果畫面中沒有該物品，就請回答沒有。接下來為問題:"+q)
print(response.text)





#{global history
#history=1
#def comp(a):
#    print(history+a)
#    history+=1
#comp()
#comp()}

