## テキストからコーパスを作成する簡単な方法
## 本来は正規表現等で汎用的に記述することが望ましいが
## 練習用作成した関数
def preprocess(text):
	text = text.lower()
	text = text.replace('.', ' .')
	words = text.split(' ')

	word_to_id = {}
	id_to_word = {}
	for word in words:
		if word not in word_to_id:
			new_id = len(word_to_id)
			word_to_id[word] = new_id
			id_to_word[new_id] = word

	corpus = np.array([word_to_id[w] for w in words])


