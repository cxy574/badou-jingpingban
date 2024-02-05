import copy
# 词典；每个词后方存储的是其词频，词频仅为示例，不会用到，也可自行修改
Dict = {"经常": 0.1,
        "经": 0.05,
        "有": 0.1,
        "常": 0.001,
        "有意见": 0.1,
        "歧": 0.001,
        "意见": 0.2,
        "分歧": 0.2,
        "见": 0.05,
        "意": 0.05,
        "见分歧": 0.05,
        "分": 0.1}

# 待切分文本
sentence = "经常有意见分歧"

res = []
tmp = []
n = len(sentence)
# 实现全切分函数，输出根据字典能够切分出的所有的切分方式
def all_cut(sentence, Dict):
    # TODO
    backTrace(sentence, Dict, 0)
    return res

def backTrace(senten, Dict, idx):
    if (idx == n):
        res.append(tmp[:])
        return
    for i in range(idx, n+1):
        if senten[idx:i] in Dict:
            tmp.append(senten[idx:i])
            backTrace(senten, Dict, i)
            tmp.pop()

res = all_cut(sentence, Dict)
print(len(res))
print(res)
