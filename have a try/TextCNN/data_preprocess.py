"""
    数据预处理
"""
import zipfile

import nltk
import bs4

from nltk.stem import WordNetLemmatizer
from gensim.models import word2vec

# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

def tokenize(text):
    """
        对原始文本数据进行清洗，获取单词列表
    """
    tokens = nltk.word_tokenize(text)
    tokens = [t.lower() for t in tokens]
    tokens = map(lemmatizer.lemmatize, tokens)
    # 去停用词
    stop_words = set(nltk.corpus.stopwords.words('english'))
    tokens = [t for t in tokens if t not in stop_words]
    # 去数字
    tokens = [t for t in tokens if not t.isnumeric()]
    # 去字符
    tokens = [t for t in tokens if
              not any(c in "`,.?!:;" for c in t) and
              not all(c in "-'" for c in t)]
    # 去单字符
    tokens = [t for t in tokens if len(t) > 1]
    return tokens

def save_tokens(tokens,filename):
    """
        保存单词表
    """
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(' '.join(tokens) + '\n')

def get_data_from_zip(file_path,maxsize = 100):
    """
        从zip文件中获取数据
    """
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        sum = 0
        for p in [p for p in zip_ref.namelist() if p.endswith('.txt')]:
            with zip_ref.open(p,'r') as f:
                text = f.read().decode('utf-8')
                # 去掉html标签
                soup = bs4.BeautifulSoup(text, 'html.parser')
                text = soup.get_text()
                tokens = tokenize(text)
                save_tokens(tokens,file_path.replace('.zip','.csv'))
                sum += 1
                if sum >= maxsize:
                    break

def train_word2vec(file):
    """
        训练word2vec模型
    """
    sentences = word2vec.Text8Corpus(file) # 加载数据

    model = word2vec.Word2Vec(sentences, sg=1 , window=5, min_count=10, workers=4,vector_size=300) # 训练模型
    model.save('word2vec.model') # 保存模型以便之后使用

def main():
    """
        主函数
    """
    size = 2000000
    with open('IMDB_train.csv', 'w', encoding='utf-8') as f:
        f.write('')

    with open('test_neg.csv', 'w', encoding='utf-8') as f:
        f.write('')

    with open('test_pos.csv', 'w', encoding='utf-8') as f:
        f.write('')

    with open('train_pos.csv', 'w', encoding='utf-8') as f:
        f.write('')

    with open('train_neg.csv', 'w', encoding='utf-8') as f:
        f.write('')


    get_data_from_zip('IMDB.zip',size)
    train_word2vec('IMDB.csv')
    # 处理测试集
    get_data_from_zip('test_neg.zip',size)
    get_data_from_zip('test_pos.zip',size)
    get_data_from_zip('train_pos.zip',size)
    get_data_from_zip('train_neg.zip',size)

if __name__ == '__main__':
    main()
