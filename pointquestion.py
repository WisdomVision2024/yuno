import pandas as pd
import json
import google.generativeai as genai
import os

api_key = 'AIzaSyBCcg0skdWwwG-hBucIvDCLHY9FFtzw9-0'
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')


# 讀取 Excel 檔案
df = pd.read_excel(r'C:\Users\USER\OneDrive\Desktop\專題\程式\yuno\environmentimfo.xlsx')

def find_point(question,data):
    # 取出 x 和 y 的值
    x = data[0]['x']
    y = data[0]['y']
    # 選取符合 x 和 y 的行
    result = df[(df['x'] == x) & (df['y'] == y)]
    
    if not result.empty:
        # 提取物件的 name 和 info
        name = result['name'].values[0]
        info = result['資訊'].values[0]
        response = model.generate_content("使用者現在在"+name+"點，"+info+"。請根據以上資訊來回答使用者的問題，問題中的「我」代表使用者，請用您來稱呼使用者，請用完整句子來回答使用者，且回答中別帶有空格及特殊符號，使用者的問題:"+question)
    
        return response.text
    else:
        return "辨識失敗，請再試一次"

# 輸入資料
# dataa = [{"x": 606.5, "y": 400}]

# # 取出 x 和 y 的值
# q=input("輸入問題:")

# output = find_point(q,dataa)

# print(output)
