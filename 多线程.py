import os
import threading

allfile = []


def find_file(path):
    files = os.listdir(path)

    for file in files:
        filepath = os.path.join(path, file)
        if os.path.isdir(filepath):
            find_file(filepath)
        elif file.endswith(".txt"):
            allfile.append(filepath)
    return allfile


class MyThread(threading.Thread):
    def __init__(self, path):
        threading.Thread.__init__(self)
        self.path = path

    def run(self):
        with open(self.path, 'r', encoding="utf-8") as f:
            content = f.read()
            print(content)


if __name__ == '__main__':
    p = r"E:\myproj\mianshiti"
    filelist = find_file(p)
    print(filelist)
    threadlist = []
    for file in filelist:
        mythd = MyThread(file)
        mythd.start()
        threadlist.append(mythd)
    for mythd in threadlist:
        mythd.join()
