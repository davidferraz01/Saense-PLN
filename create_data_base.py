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
        stopWords = set(stopwords.words("portuguese"))
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
                tf_idf_table[word1] = float(value1 * value2)

            tf_idf_matrix[sent1] = tf_idf_table

        self.tf_idf_matrix = tf_idf_matrix

    def _score_sentences(self) -> dict:
        sentenceValue = {}

        for sent, f_table in self.tf_idf_matrix.items():
            total_score_per_sentence = 0

            count_words_in_sentence = len(f_table)
            for word, score in f_table.items():
                total_score_per_sentence += score

            sentenceValue[sent] = total_score_per_sentence / count_words_in_sentence

        self.sentenceValue = sentenceValue

    def _find_average_score(self) -> int:
        sumValues = 0
        for entry in self.sentenceValue:
            sumValues += self.sentenceValue[entry]

        average = (sumValues / len(self.sentenceValue))

        self.average = average

    def _generate_summary(self):
        sentence_limit = 1
        sentence_count = 0
        summary = ''

        for sentence in self.sentences:
            if sentence_count != sentence_limit and sentence[:15] in self.sentenceValue and self.sentenceValue[sentence[:15]] >= (self.average):
                summary += " " + sentence
                sentence_count += 1

        self.summary = summary
    

    def save_summary(self):
        # Salvar resumos #
        nomearquivo = "Summary_" + self.arq_path[-1]
        nomecompleto = os.path.join("data_base/", nomearquivo)
        f = open(nomecompleto, "w")
        f.write(self.summary)
        f.close()
        
        # Removendo Sentenca do Texto original #
        with open("artigos/" + self.arq_path[-1], "r+") as txt:
            conteudo = txt.read()
            nomearquivo = self.arq_path[-1]
            nomecompleto = os.path.join("data_base", nomearquivo)
            f = open(nomecompleto, "w")
            conteudo = conteudo.replace(self.summary, "")
            f.write(conteudo)

            f.close()
            txt.close()


def main():
    try:
        if sys.argv[1] == "--help" or sys.argv[1] == "-h":
            print("""
            Create Data Base ( https://github.com/0xdferraz/Saense-PLN )
            Gera uma base de dados que pode ser utilizada para realizar ajuste fino de Algoritmos Abstrativos.

            Uso: python create_data_base.py <Opcional: Tamanho do resumo ( padrao = 1100 caracteres )>
            """)
            exit()
    
    except SystemExit:
        sys.exit()
    
    except:
        pass

    nltk.download('punkt')
    nltk.download('stopwords')

    for file in glob.glob("artigos/*.txt"):
        if file != "artigos/__controle.txt":

            summary = Summary_TF_IDF()

            summary.arq_path = file.split('/')

            with open(file, "r", encoding="utf-8") as f:
                text = " ".join(f.readlines())

            summary.sentences = sent_tokenize(text)
            summary.total_documents = len(summary.sentences)

            summary._create_frequency_matrix()

            summary._create_tf_matrix()

            summary._create_documents_per_words()

            summary._create_idf_matrix()

            summary._create_tf_idf_matrix()

            summary._score_sentences()

            summary._find_average_score()

            summary._generate_summary()
            summary.save_summary()
    

if __name__ == "__main__":
    main()