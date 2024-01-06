import logging
import os
import re

movie_suffix = {'mp4', 'mkv'}
caption_suffix = {'ass'}
movie_suffix_current = 'unselected'
caption_suffix_current = 'unselected'
movie_dict = {}
caption_dict = {}
pattern = re.compile(r'\d+')  # 匹配 [1] [23] [456]

print('当前路径: ' + os.getcwd())

files = os.listdir('.')

for f in files:
    # 排除无后缀的文件(夹)
    index = f.rfind('.')
    if index <= 0:  # index=-1:未找到'.'  index=0:隐藏文件夹
        continue

    # 检测剧集编号
    # 不可含有其他杂乱文件
    series_number = pattern.search(f)
    if series_number is None:
        continue

    # 仅可包含一种视频/字幕后缀
    suffix = f[index+1:]
    if suffix in movie_suffix:
        movie_dict[series_number.group()] = f
        movie_suffix_current = suffix
    if suffix in caption_suffix:
        caption_dict[series_number.group()] = f
        caption_suffix_current = suffix

print('读取到 ' + str(len(movie_dict)) + ' 个 ' + movie_suffix_current + ' 文件')
print('读取到 ' + str(len(caption_dict)) + ' 个 ' + caption_suffix_current + ' 文件')

anime_name = input('请输入目标名称:\n')

task_dict = {}
for number, file in movie_dict.items():
    task_dict[file] = anime_name + '-' + number + '.' + movie_suffix_current
for number, file in caption_dict.items():
    task_dict[file] = anime_name + '-' + number + '.' + caption_suffix_current

print('重命名任务:')
for original, target in task_dict.items():
    print(original)
    print(' -> ' + target)

confirm = input('输入 y 进行确认, 输入其他字符取消:')
if confirm != 'y':
    exit(0)

logging.basicConfig(filename='action.log', level=logging.INFO)
for original, target in task_dict.items():
    logging.info(original + ' -> ' + target)
    os.rename(original, target)

input('已完成, 按回车键结束.')
