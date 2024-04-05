import torch

with open('data/p1ch4/jane-austen/1342-0.txt',encoding='utf-8') as f:
    text = f.read()
lines = text.split('\n')
line = lines[200]

# 用ASCII编码为每个字符进行独热编码（独热编码字符）
letter_t = torch.zeros(len(line),128)
print(letter_t.shape)


#第一种方式，手动编码
for i,letter in enumerate(line.lower().strip()):
    letter_index = ord(letter) if ord(letter) < 128 else 0 # 定向性双引号是无效的ASCII，这里屏蔽掉
    letter_t[i][letter_index] = 1

#第二种方式，利用scatter_函数进行编码
# line_ASCII_l = [(ord(c) if ord(c) <128 else 0) for c in line.lower().strip()]
# line_t = torch.tensor(line_ASCII_l)
# letter_t = torch.zeros(line_t.shape[0],128)
# letter_t.scatter_(1,line_t.unsqueeze(1),1.0)

# 独热编码整个词（对处理词汇来说不实用，编码向量太宽）
def clean_words(input_str:str):
    punctuation = '.,;:!?“”_-'
    word_list = input_str.lower().replace('\n','').split()
    word_list = [word.strip(punctuation) for word in word_list] # 删去多余标点字符
    return word_list

words_in_line = clean_words(line)
print(words_in_line)

word_list = sorted(set(clean_words(text))) # list转set会去除相同元素
word2index_dict = {word: i for (i,word) in enumerate(word_list)} # 为每一个单词分配映射数字

word_t = torch.zeros(len(words_in_line),len(word2index_dict))
for i,word in enumerate(words_in_line):
    word_index = word2index_dict[word]
    word_t[i][word_index] = 1
    print({f'{i:2} {word_index:4} {word}'})

print(word_t.shape)
