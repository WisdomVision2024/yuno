import pandas as pd

# 讀取 Excel 檔案
file_path = r"C:\Users\cyn91\OneDrive\文件\專題\yuno\environmentimfo.xlsx"  # 確保檔案路徑正確
data = pd.read_excel(file_path)

# 根據輸入的 name 回傳對應的資訊
def get_environment_info(name_input):
    result = data[data['name'] == name_input]['資訊']
    
    if not result.empty:
        return "使用者現在在"+name_input+"點。"+result.values[0]
    else:
        return "辨識失敗，請再試一次。"

# 測試
name_to_search = input("輸入點位:")  # 替換成你要查找的 name
info = get_environment_info(name_to_search)
print(info)