import os
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory

# 创建 Tkinter 根窗口
root = Tk()
root.withdraw()

# 提示用户选择 CSV 文件
csv_path = askopenfilename(title="选择 CSV 文件", filetypes=[("CSV Files", "*.csv")])

# 读取 CSV 文件
df = pd.read_csv(csv_path)

# 提示用户选择文件夹
folder_path = askdirectory(title="选择文件夹")

# 创建字典，用于存储国际域名缩写和对应的国家或地区
country_dict = {}
for index, row in df.iterrows():
    abbreviation = row['国际域名缩写']
    country_name = row['国家或地区']
    country_dict[abbreviation] = country_name

# 遍历文件夹中的文件
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    file_name, file_extension = os.path.splitext(filename)
    file_name = file_name.lower()  # 忽略文件名大小写

    # 根据文件名在字典中查找对应的国家或地区
    if file_name in country_dict:
        new_file_name = country_dict[file_name]
        new_file_path = os.path.join(folder_path, new_file_name + file_extension)
        os.rename(file_path, new_file_path)
        print(f"重命名文件：{filename} -> {new_file_name}{file_extension}")

print("重命名完成")