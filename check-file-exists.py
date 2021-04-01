import os

# 要檢查的檔案路徑
filepath = "files/index.html"
folderpath = "files/css"

# 檢查檔案是否存在
# if os.path.isfile(filepath):
#     print("檔案存在")
# else:
#     print("檔案不存在")

# 檢查檔案是否存在
if os.path.isdir(folderpath):
    print("目錄存在")
else:
    print("目錄不存在")
