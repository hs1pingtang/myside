import os

# 获取所有文件名
file_list = os.listdir()
# 筛选出jpg png后缀的文件
# 更新文件名为数字序列
for i in range(len(file_list)):
    if file_list[i][-3:] == "jpg" or file_list[i][-3:] == "png":
        os.rename(file_list[i], str(i) + ".jpg")
    else:
        continue