import math
import nltk
import sys
import os
import glob
from nltk import sent_tokenize, word_tokenize, PorterStemmer
from nltk.corpus import stopwords    

class Summary_TF_IDF():
    def __init__(self):
        self.setences = None
        self.total_documents = None
        self.arq_path = None 
        self.average = None
        self.freq_matrix = None
        self.tf_matrix = None
        self.word_per_doc_table = None
        self.idf_matrix = None
        self.tf_idf_matrix = None
        self.sentenceValue = None
        self.summary = None

    def _create_frequency_matrix(self): 
        freq_matrix = {}
        stopWords = set(stopwords.words("portuguese")) # Analisar qual Stopwords gera melhor resultado "english" ou "portuguese"
        ps = PorterStemmer()

        for sent in self.sentences:
            freq_table = {}
            words = word_tokenize(sent)
            for word in words:
                word = word.lower()
                word = ps.stem(word)
                if word in stopWords:
                    continue

                if word in freq_table:
                    freq_table[word] += 1
                else:
                    freq_table[word] = 1

            freq_matrix[sent[:15]] = freq_table

        self.freq_matrix = freq_matrix

    def _create_tf_matrix(self):
        tf_matrix = {}

        for sent, f_table in self.freq_matrix.items():
            tf_table = {}

            count_words_in_sentence = len(f_table)
            for word, count in f_table.items():
                tf_table[word] = count / count_words_in_sentence

            tf_matrix[sent] = tf_table

        self.tf_matrix = tf_matrix

    def _create_documents_per_words(self):
        word_per_doc_table = {}

        for sent, f_table in self.freq_matrix.items():
            for word, count in f_table.items():
                if word in word_per_doc_table:
                    word_per_doc_table[word] += 1
                else:
                    word_per_doc_table[word] = 1

        self.word_per_doc_table = word_per_doc_table

    def _create_idf_matrix(self):
        idf_matrix = {}

        for sent, f_table in self.freq_matrix.items():
            idf_table = {}

            for word in f_table.keys():
                idf_table[word] = math.log10(self.total_documents / float(self.word_per_doc_table[word]))

            idf_matrix[sent] = idf_table

        self.idf_matrix = idf_matrix

    def _create_tf_idf_matrix(self):
        tf_idf_matrix = {}

        for (sent1, f_table1), (sent2, f_table2) in zip(self.tf_matrix.items(), self.idf_matrix.items()):

            tf_idf_table = {}

            for (word1, value1), (word2, value2) in zip(f_table1.items(),f_table2.items()):  
                # here, keys are the same in both the table
                tf_idf_table[word1] = float(value1 * value2)

            tf_idf_matrix[sent1] = tf_idf_table

        self.tf_idf_matrix = tf_idf_matrix

    def _score_sentences(self) -> dict:
        """
        score a sentence by its word's TF
        Basic algorithm: adding the TF frequency of every non-stop word in a sentence divided by total no of words in a sentence.
        :rtype: dict
        """

        sentenceValue = {}

        for sent, f_table in self.tf_idf_matrix.items():
            total_score_per_sentence = 0

            count_words_in_sentence = len(f_table)
            for word, score in f_table.items():
                total_score_per_sentence += score

            sentenceValue[sent] = total_score_per_sentence / count_words_in_sentence

        self.sentenceValue = sentenceValue

    def _find_average_score(self) -> int:
        """
        Find the average score from the sentence value dictionary
        :rtype: int
        """
        sumValues = 0
        for entry in self.sentenceValue:
            sumValues += self.sentenceValue[entry]

        # Average value of a sentence from original summary_text
        average = (sumValues / len(self.sentenceValue))

        self.average = average

    def _generate_summary(self):
        sentence_count = 0
        summary = ''

        for sentence in self.sentences:
            if sentence[:15] in self.sentenceValue and self.sentenceValue[sentence[:15]] >= (self.average):
                summary += " " + sentence
                sentence_count += 1

        self.summary = summary
    
    """
    for i in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]:
        summary = _generate_summary(sentences, sentence_scores, i * threshold)
        if len(summary) <= art_len_limit:
            print("\nTamanho final do texto:", len(summary), "caracteres\n")

            # Save summary #
            #  CRIAR UMA PASTA DE RESUMOS #
            nomearquivo = "Summary_" + path[1]
            nomecompleto = os.path.join("./resumos_tf-idf", nomearquivo)
            f = open(nomecompleto, "w")
            f.write(summary)
            f.close()
            break
    """

    def save_summary(self, art_len_limit):
        average = self.average
        for i in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]:
            self.average = i * average
            self._generate_summary()
            if len(self.summary) <= art_len_limit:
                print("\nTamanho final do texto:", len(self.summary), "caracteres\n")

                # Salvar resumos #
                nomearquivo = "Summary_" + self.arq_path[-1]
                nomecompleto = os.path.join("./resumos_tf-idf", nomearquivo)
                f = open(nomecompleto, "w")
                f.write(self.summary)
                f.close()
                break


def main():
    try:
        if sys.argv[1] == "--help" or sys.argv[1] == "-h":
            print("""
            Summary TF-IDF ( https://github.com/0xdferraz/Saense-PLN )
            Resume textos utilizando a tecnica TF-IDF

            Uso: python summary_tf-idf.py <Opcional: Tamanho do resumo ( padrao = 1100 caracteres )>
            """)
            exit()

        else:
            art_len_limit = int(sys.argv[1])
    except:
        art_len_limit = 1100

    nltk.download('punkt')
    nltk.download('stopwords')

    for file in glob.glob("artigos/*.txt"):
        if file != "artigos/__controle.txt":

            summary = Summary_TF_IDF()

            summary.arq_path = file.split('/')

            with open(file, "r", encoding="utf-8") as f:
                text = " ".join(f.readlines())

            # 1 Sentence Tokenize
            summary.sentences = sent_tokenize(text)
            summary.total_documents = len(summary.sentences)
            
            # 2 Create the Frequency matrix of the words in each sentence.
            summary._create_frequency_matrix()
            
            '''
            #Term frequency (TF) is how often a word appears in a document, divided by how many words are there in a document.
            '''
            # 3 Calculate TermFrequency and generate a matrix
            summary._create_tf_matrix()
            
            # 4 creating table for documents per words
            summary._create_documents_per_words()

            '''
            #Inverse document frequency (IDF) is how unique or rare a word is.
            '''
            # 5 Calculate IDF and generate a matrix
            summary._create_idf_matrix()

            # 6 Calculate TF-IDF and generate a matrix
            summary._create_tf_idf_matrix()
            
            # 7 Important Algorithm: score the sentences
            summary._score_sentences()

            # 8 Find the threshold
            summary._find_average_score()
            
            # 9 Generate the summary
            summary._generate_summary()
            summary.save_summary(art_len_limit)
        

if __name__ == "__main__":
    main()