import os

def start(path):
    """
    处理path的文件路径，并排序好为合并文件正确顺序作准备
    path: 视频所在的目录
    """
    # 视频所在的目录
    path = path
    # 获取当前目录下的文件，返回为list
    lists = os.listdir(path)
    print(lists)
    for e_file in lists:
        # 组合地址
        new = path + "/" + e_file
        # print(new)
        if os.path.isdir(new):
            # 新地址
            file = os.listdir(new)
            # print(file)
            filename_list = []
            data = []
            for each in file:
                # 取出.ts前的数字
                j = each.split(".")[0]
                data.append(j)
            # 排序从小到大
            data.sort()
            # print(data)
            # 使data的每个元素的长度一样，并重新增加到另一个list（filename_list）
            for i in data:
                if len(str(i)) < 2:
                    s = new + "/" + str(i).rjust(3, "0") + ".ts"
                    filename_list.append(s)
                elif len(str(i)) < 3:
                    s = new + "/" + str(i).rjust(3, "0") + ".ts"
                    filename_list.append(s)
                else:
                    s = new + "/" + str(i) + ".ts"
                    filename_list.append(s)
            # print(filename_list)
            # 调用函数
            write(filename_list, new)
            # return filename_list,new

def write(filename_list,name):
    """
    合并文件
    filename_list:指定文件对应的目录的列表
    name :  写入新文件的名字
    """
    # 循环list下对应的文件，写入到指定文件
    for filename in filename_list:
        # print(filename)
        try:
            with open(filename,"rb") as f:
                new = f.read()
        except Exception as e:
            print(e)
        with open("%s.mp4" % name, "ab+")as g:
            g.write(new)
        # print("%s合并完成"%name)
    delete_dir(name)
    
def delete_dir(dirName):
    # 如何是文件直接删除
    if os.path.isfile(dirName):
        try:
            os.remove(dirName)
        except:
            pass
    elif os.path.isdir(dirName):
        # 如果是文件夹，则首先删除文件夹下文件和子文件夹，再删除文件夹
        for item in os.listdir(dirName):
            tf = os.path.join(dirName, item)
            # 递归调用
            delete_dir(tf)
            try:
                os.rmdir(dirName)
            except:
                pass
    print("%s文件夹下所有文件已删除"%dirName)

if __name__ == '__main__':
    start("J:/VIDEO")
    # print(filename_list)
    # print(new)
    # write(filename_list,new)


