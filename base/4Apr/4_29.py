"""
使用Python实现emoji表情
pip3 install emoji
"""

import emoji

# 默认的表情可以直接通过表情的字符实现
# https://www.unicode.org/emoji/charts/emoji-list.html
# Python is
print(emoji.emojize('Python is :thumbs_up:'))
# 有些特殊的表情需要指定 use_aliases=True 参数才可以实现
# Sleeping is
print(emoji.emojize('你是猪吗？:rolling_on_the_floor_laughing:'))
# 也可以用= unicode 形式
print(emoji.emojize('\U0001F32D'), emoji.emojize('\U0001F354'),
      emoji.emojize('\U0001F35F'), emoji.emojize('\U0001F355'),
      emoji.emojize('\U0001F35F'), emoji.emojize('\U0001F355'))
print(emoji.emojize('\U0001F33A'), emoji.emojize('\U0001F33A'),
      emoji.emojize('\U0001F33A'), emoji.emojize('\U0001F33A'),
      emoji.emojize('\U0001F33A'), emoji.emojize('\U0001F33A'))
print(emoji.emojize('\U0001F497'), emoji.emojize('\U0001F496'),
      emoji.emojize('\U0001F495'), emoji.emojize('\U0001F497'),
      emoji.emojize('\U0001F496'), emoji.emojize('\U0001F495'))
