# AnimeRenamer
用于重命名 动漫/字幕 文件

## 例子
下面是你的某个文件夹：
```
FamilyGuy01.mp4
FamilyGuy02.mp4
FamilyGuy03.mp4
[牛马工作室][出生之家][01].ass
[牛马工作室][出生之家][02].ass
[牛马工作室][出生之家][03].ass
无关文件夹
无关文件.jpg
Renamer.py（此脚本）
```
在该目录下运行本脚本即可。

结果：
```
出生之家-01.mp4
出生之家-02.mp4
出生之家-03.mp4
出生之家-01.ass
出生之家-02.ass
出生之家-03.ass
无关文件夹
无关文件.jpg
Renamer.py（此脚本）
action.log（新增的日志记录文件）
```

## 格式
视频/字幕 的格式使用白名单模式。

更多格式请自行添加到movie_suffix与caption_suffix中。

## 误操作
在确认操作前会有重命名预览。

如果发生误操作，可根据生成的action.log进行手动恢复。
