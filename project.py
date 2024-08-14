
import openpyxl

# 加载 Excel 工作簿
workbook = openpyxl.load_workbook(r'C:\Users\cyn91\Downloads\test1.xlsx')

# 选择工作表
sheet = workbook['工作表1']  # 将 'Sheet1' 替换为你的工作表名称

# 定义一个函数来获取工作表的所有值
def get_values(sheet):
    arr = []  # 第一层列表
    for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row, min_col=1, max_col=37):
        a=" "
        if(row[4].value):a=row[4].value
        obj = f"{row[0].value}的座標為({row[1].value},{row[2].value})，他是{row[3].value}的{a}"
        arr.append(obj)
    return arr
# 获取并打印工作表的所有值
data="現在有一間長9單位、寬5單位的教室，現在我在教室的最西南角(0,0)，面朝北方，教室的西北角座標為(0,5)，教室的東南角座標為(9,0)，教室的東北角座標為(9,5)"
values = get_values(sheet)
for value in values:
    data+=","+value
#print(data) 
#串接GEMINI
import google.generativeai as genai
import os

question=input("輸入問題:")

api_key = 'AIzaSyBCcg0skdWwwG-hBucIvDCLHY9FFtzw9-0'
genai.configure(api_key = api_key)

model = genai.GenerativeModel('gemini-pro')
a='1.環境類問題Ex:(1)廁所在哪裡？(2)最近的出口在哪裡？Ans:廁所在你的右前方，距離你5公尺2.設備類問題Ex:(1)最近椅子在哪裡？(2)這裡有飲水機嗎？Ans:飲水機在你的右前方，距離你5公尺3.導航和方向類問題Ex:(1)方向指引：如何從這裡到某個特定地點？Ans: 往右前方，往前5五公尺即可到達廁所。如果中途有障礙物的話請補充:請注意往前走2公尺會遇到一張椅子，需要繞開他(2)路線偏差：我是否偏離了路線？Ans:請再稍微往左轉4.安全類問題Ex:(1)障礙物：前方是否有障礙物？Ans: 前方2公尺有一張椅子，可以越過，3公尺會碰到桌子，無法越過(2)路面狀況：地面是否平坦？有無坡度或台階？Ans: 前方4公尺有路面有突起，請小心(3)突發變化：是否有突發的環境變化，如施工或家具移動？Ans: 原本在你右前方的桌子被移動到了你的左前方5.互動類問題Ex:(1)人員位置：附近有我認識的人嗎？Ans: 有，小明在你的右前方(2)社交互動：周圍是否有其他人？Ans: 前方有三個人，都是陌生人'

response = model.generate_content("環境資料:"+data+"環境資料到此結束。問題:「"+question+"」問題結束。請根據問題分類:「"+a+"」判斷問題屬於五種問題的哪一種，先回答問題屬於五種問題的哪一種(回答限定:1.環境類問題,2.設備類問題,3.導航和方向類問題,4.安全類問題,5.互動類問題)，再參考示範回答Ans的形式，根據環境資料回答問題，計算距離請用((x座標差)*(x座標差)+(y座標差)*(y座標差))^0.5的方式計算，請省略過程直接給我簡潔的答案ex:廁所在你的右前方，距離你5公尺")
print(response.text)

#判斷
keyworda = ["1.環境類問題"]
keywordb = ["2.設備類問題"]
keywordc = ["3.導航和方向類問題"]
keywordd = ["4.安全類問題"]
keyworde = ["5.互動類問題"]

b= response.text
c=0

for keyword in keyworda:
    if keyword in b:
        print(f"1")
        # 執行某件事
        break
for keyword in keywordb:
    if keyword in b:
        print(f"2")
        # 執行某件事
        break
for keyword in keywordc:
    if keyword in b:
        print(f"3")
        # 執行某件事
        break
for keyword in keywordd:
    if keyword in b:
        print(f"4")
        # 執行某件事
        break
for keyword in keyworde:
    if keyword in b:
        print(f"5")
        # 執行某件事
        break