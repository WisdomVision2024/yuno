import json
import google.generativeai as genai
import os

api_key = 'AIzaSyBCcg0skdWwwG-hBucIvDCLHY9FFtzw9-0'
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

z=input("輸入關注對象:")
response = model.generate_content("使用者要求"+z+"請判斷使用者想關注下列六項物品中的哪幾項並回答物品名稱1.書2.水壺3.椅子4.桌子5.筆電6.筆，回答的物品名稱必須何上述一模一樣。例如要求為:請幫我關注書本和筆，則回答書、筆，")
target=response.text
print("正在幫您關注:"+target+"\n")

history="無"
count=0

def con(input_data):
    global history
    global target
    global count
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
    fitem = {item: count for item, count in item_counts.items()}
    
    # 構建結果字符串，包含物品名稱和數量
    result = "、".join(f"{count}{item}" for item, count in fitem.items())
    ans="使用者的視野裡有"+result
    print(ans)
    final=model.generate_content("請幫我篩選出使用者關注目標的資訊，以下兩個情況為參考回答示範。示範1:示範題目:使用者的視野裡有1本書、0個水壺、5張椅子、0張桌子、0台筆電、2枝筆。使用者的關注目標:書本、筆電、筆。在這個情況中需回答:使用者的的視野裡有1本書、0台筆電、2枝筆。示範題目2:使用者的視野裡有1本書、0個水壺、6張椅子、1張桌子、0台筆電、1枝筆。使用者的關注目標:書本、筆電。在這個情況中需回答:使用者的視野裡有1本書、0台筆電。請注意，以上只是範例，一切資訊包括使用者視野裡有甚麼跟關注對象皆以接下來的題目為準，尤其是關注目標，請必定要依照接下來後面題目的關注目標篩選題目資訊，非關注目標的資訊一律都必須過濾掉。只需要給我最終的回答就好，不需要有多餘的過程。題目:"+ans+"。使用者的關注目標:"+target)
    print("過去:"+history+"\n現在:"+final.text)
    koko=model.generate_content("請幫我比對過去跟現在兩筆資料回應給使用者，如果過去資料為無，即回答現在資料，如果過去資料存在，則告訴使用者和過去資料相比，使用者的視野出現了甚麼變化，如果物品數量為0，請回報畫面中沒有該物品。接下來3個情況為回答參考，情況1:過去資料:無 現在資料:使用者的視野裡有0個水壺、5張椅子。因為水壺數量為0，因此最終須回答:[您的視野中有五張椅子，沒有水壺]。情況2:過去資料:使用者的視野裡有0個水壺、5張椅子 現在資料:使用者的視野裡有0個水壺、5張椅子。因為和過去資料相比，現在的資料沒有變化，，因此最終須回答:[您視野中的畫面沒有變化]。情況2:過去資料:使用者的視野裡有0個水壺、5張椅子 現在資料:使用者的視野裡有2個水壺、4張椅子。因為和過去資料相比，使用者的視野多了2個水壺，少了一張椅子，因此須回報給使用者環境的改變，因此最終須回答:[您的視野中多出了兩個水壺，有一張椅子離開了您的視野]，請記住，這三個參考情況為範例，接下來請根據後面輸入的現在資料跟過去資料，依照範例的方式回答使用者。我最後只需要回報給使用者的回答，如果現在資料跟現在資料之間完全沒有變化，回答一定要包含關鍵字:沒有變化，反之，如果有任何一物品出現變化，則不能包含關鍵字:沒有變化。過去資料:"+history+" 現在資料:"+final.text)
    print("b:"+koko.text)
    z=koko.text
    keyword = ["沒有變化"]
    for keyword in keyword:
        if keyword in koko.text:
            if count<=3:
                z=" "
                count+=1
                break
            else:
                count=0
    print("a"+z)

    history=final.text
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
con(b)
con(b)
con(b)
con(c)
con(b)
con(a)
con(b)