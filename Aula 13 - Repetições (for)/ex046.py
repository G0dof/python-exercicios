import emoji
from time import sleep
for c in range(10, 0, -1):
    sleep(1)
    print(c)
print(emoji.emojize('BUM!:boom::anger: UM!:anger::boom: POOW!:boom::anger:', use_aliases=True))
