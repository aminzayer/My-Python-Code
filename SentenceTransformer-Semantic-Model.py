import torch,nltk
from hazm import *
from sentence_transformers import SentenceTransformer,util
import warnings
warnings.filterwarnings('ignore')

class Semantic:

    def __init__(self):
        # Load Model in Sentence Transformer
        # More Model available in https://huggingface.co/models
        self.model= SentenceTransformer('distiluse-base-multilingual-cased-v1')

    def CorpusEmbedding(self, corpus):
        # Encode Corpus in Vector Space (Transformers)
        if torch.cuda.is_available():
            embeddings = self.model.encode(corpus, device='cuda')  # CPU = cpu & GPU = cuda
        else:
            embeddings = self.model.encode(corpus, device='cpu')  # CPU = cpu & GPU = cuda
        return embeddings

    def SentenceEmbedding(self, sentences):
        # Encode Sentences in Vector Space (Transformers)
        if torch.cuda.is_available():
            embeddings = self.model.encode(sentences, device='cuda')  # CPU = cpu & GPU = cuda
        else:
            embeddings = self.model.encode(sentences, device='cpu')  # CPU = cpu & GPU = cuda
        return embeddings

    def English_Text_Convert_To_Sentences(self, text):
        # Download nltk dictionary punkt English Language
        nltk.download('punkt', quiet=True)  # Download nltk dictionary punkt English Language for first time
        nltk.download('averaged_perceptron_tagger', quiet=True)  # Download nltk dictionary averaged_perceptron_tagger for first time
        # Convert Text to Sentences
        sentences = nltk.text.sent_tokenize(text)
        return sentences

    def Farsi_Text_Convert_To_Sentences(self, text):
        # Normalize Persian Corpus
        normalizer = Normalizer()
        text = normalizer.normalize(text)
        return sent_tokenize(text)

    def Calculate_Semantic_Two_Sentences(self,sentence1,sentence2):
        # Embeddings Sentences
        SentEmbed1= self.SentenceEmbedding(sentences=sentence1)
        SentEmbed2= self.SentenceEmbedding(sentences=sentence2)
        return util.cos_sim(SentEmbed1, SentEmbed2).numpy()[0][0]

    def Calculate_Semantic_Two_Corpus(self,corpus1,corpus2):
        # Embeddings Corpus
        CorpusEmbed1 = self.CorpusEmbedding(corpus=corpus1)
        CorpusEmbed2 = self.CorpusEmbedding(corpus=corpus2)
        return util.cos_sim(CorpusEmbed1, CorpusEmbed2).numpy()[0][0]

    def Calculate_Semantic_List_Sentences(self,list_sentences):
        # Embeddings List of Sentences
        list_sentences_Embed = self.SentenceEmbedding(sentences=list_sentences)
        # Calculate Cosine Similarity of Sentences Embeddings
        cos_similarity = util.cos_sim(list_sentences_Embed, list_sentences_Embed)
        all_sentence_combinations = []
        # Separation of scores into two-by-two sentences
        for i in range(len(cos_similarity) - 1):
            for j in range(i + 1, len(cos_similarity)):
                all_sentence_combinations.append([
                    list_sentences[i],
                    list_sentences[j],
                    float(cos_similarity[i][j].numpy()),
                ])
        # Sort by highest score to lowest
        all_sentence_combinations = sorted(all_sentence_combinations, key=lambda x: x[0], reverse=True)
        return all_sentence_combinations

    def Calculate_Semantic_List_corpus(self,list_corpus):
        # Embeddings List of Corpus
        list_corpus_Embed = self.CorpusEmbedding(corpus=list_corpus)
        # Calculate Cosine Similarity of Corpus Embeddings
        cos_similarity = util.cos_sim(list_corpus_Embed, list_corpus_Embed)
        all_corpus_combinations = []
        # Separation of scores into two-by-two Corpus
        for i in range(len(cos_similarity) - 1):
            for j in range(i + 1, len(cos_similarity)):
                all_corpus_combinations.append([
                    list_corpus[i],
                    list_corpus[j],
                    float(cos_similarity[i][j].numpy()),
                ])
        # Sort by highest score to lowest
        all_corpus_combinations = sorted(all_corpus_combinations, key=lambda x: x[0], reverse=True)
        return all_corpus_combinations


#--------------------------------------------------------------------------------------
#---------------------------- Examples ------------------------------------------------
#--------------------------------------------------------------------------------------

sentence1 = 'من خوردن پیتزا را دوست دارم'
sentence2 = 'من دیشب در شام زیاد روی کردم'
corpus1 = 'همیشه در هنگام رفتن به محل کار تاکسی میگرفتم.\r\nولی امروز ترجیح دادم که با اتوبوس بروم به همین علت دیر رسیدم.'
corpus2 = 'امروز تمامی همکارانم در محل کار با تاخیر حاضر شدند.\r\nچون خیابان ها بسیار شلوغ و ترافیک بود.'
corpus3 = 'This framework generates embeddings for each input sentence.\r\nSentences are passed as a list of string.\r\nThe quick brown fox jumps over the lazy dog.'
Semantic_Model = Semantic()
score = Semantic_Model.Calculate_Semantic_Two_Sentences(sentence1=sentence1, sentence2=sentence2)
print(score)
score = Semantic_Model.Calculate_Semantic_Two_Corpus(corpus1=corpus1, corpus2=corpus2)
print(score)
ListSentences=Semantic_Model.English_Text_Convert_To_Sentences(text=corpus3)
print(ListSentences)
ListSentences = Semantic_Model.Farsi_Text_Convert_To_Sentences(text=corpus2)
print(ListSentences)
Sentences = ["مردی در حال خوردن غذا است.",
           "مردی در حال خوردن یک لقمه نان است.",
           "دختر در حال حمل نوزاد است.",
           "مردی سوار بر اسب است.",
           "زنی در حال نواختن ویولن است.",
           "دو مرد گاری ها را از میان جنگل هل دادند.",
           "مردی سوار بر اسب سفید بر روی زمینی محصور شده است.",
           "یک میمون در حال نواختن طبل است.",
           "کسی در لباس گوریل در حال نواختن مجموعه ای از طبل است."
           ]
scores = Semantic_Model.Calculate_Semantic_List_Sentences(list_sentences=Sentences)
print(scores)
corpus = [
    "پیاده روی بهترین و ساده ترین ورزش برای تمامی سنین است که تاثیر زیادی در بهبود روند زندگی و داشتن تناسب اندام افراد دارد. این ورزش که به صورت تک نفره و گروهی قابل انجام است روند درمان بسیاری از بیماری ها را تسریع می بخشد.",
    "آیا از درد مفاصل، مشکلات قلبی، استرس، افسردگی و یا چاقی رنج می برید ؟ سپس سعی کنید تمام مشکلات سلامتی خود را با پیاده روی شکست دهید. چون پیاده روی به کاهش خطر همه بیماری های مزمن کمک می کند اما این تنها خواص و فواید پیاده رویاین ورزش ارزان و ساده نیست پس این بخش از سلامت نمناک را بخوانید تا در مورد فواید روزانه پیاده روی بدانید.",
    "پیاده روی به بهبود سلامت قلب کمک می کند. دانشمندان ایرلندی گزارش داده اند که راه رفتن بهترین ورزش برای افراد بی تحرک به خصوص بزرگسالان، برای کاهش خطر بیماری های قلبی و عروقی است. مردان و زنان 65 ساله یا مسن تر که حداقل 4 ساعت در هفته راه می رفتند، کمتر در معرض خطر بیماری های قلبی و عروقی قرار دارند . بنابراین، مطمئن شوید که 4 ساعت در هفته پیاده روی کنید تا از بیماری های قلبی و عروقی در امان باشید.",
    "پیاده روی یک ورزش عالی است و به کاهش وزن کمک می کند . دانشمندان آمریکایی آزمایشی را طراحی کردند که در آن بیماران چاق با هم قدم می زدند پس از 8 هفته، وزن آن ها بررسی شد و بیش از 50 درصد از شرکت کنندگان به طور متوسط 5 پوند وزن از دست دادند. بنابراین ممکن است ایده خوبی باشد که به جای رانندگی با اتومبیل، به مقصد نزدیک پیاده روی کنید.",
    "هم چنین پیاده روی می تواند به کاهش فشار خون کمک کند. آزمایشی روی افراد مبتلا به فشار خون بالا انجام دادند، جایی که 83 شرکت کننده هر روز به مدت 12 هفته 10،000 قدم را پیاده طی می کردند. در پایان 12 هفته، آن ها افت قابل توجهی در فشار خون و افزایش بنیه داشتند حتی اگر قادر به تکمیل کردن 10000 قدم در روز باشید، باید هر روز 60 دقیقه راه بروید تا میزان فشار خون را چک کنید.",
    "سرطان جان بیش از یک میلیون نفر را گرفته است. زندگی بی تحرک یکی از علل سرطان است و این جا است که پیاده روی روزانه می تواند به شما کمک کند. راه رفتن می تواند به کاهش وزن کمک کند در نتیجه خطر ابتلا به سرطان را کاهش می دهد. راه رفتن برای افراد تحت درمان سرطان با کاهش اثرات جانبی شیمی درمانی مفید بوده است . همچنین می تواند خطر سرطان پستان را کاهش دهد.",
    "راه رفتن می تواند هوش را افزایش دهد . راه رفتن به تغذیه مغز با مقادیر مورد نیاز اکسیژن و گلوکز کمک می کند که به عملکرد بهتر آن کمک می کند. هم چنین سطح کلسترول بد را کاهش می دهد ، که شریان ها را مسدود و از این رو خطر سکته را کاهش می دهد . بنابراین پیاده روی می تواند به بهبود گردش خون مغز و عملکردهای سلولی کمک کند.",
    "سبک زندگی بی تحرک به رشد یکی از شایع ترین بیماری ها ، دیابت منجر شده است. دانشمندان 3000 تا 7،500 گام در روز را برای درمان دیابت نوع 2 توصیه می کنند و پیشنهاد می کنند که کم تر بنشینند و فعال تر باشند . هر روز راه رفتن می تواند به کنترل سطح قند خون کمک کند که به پیش گیری از دیابت نوع 2 کمک می کند.",
    "استخوان ها با افزایش سن و سال ضعیف تر می شوند. اما خبر خوب این است که می توانید با راه رفتن به طور مرتب استخوان ها را تقویت کنید. این ورزش ، از دست رفتن تراکم استخوان جلوگیری می کند در نتیجه خطر پوکی استخوان، شکستگی و آسیب را کاهش می دهد .",
    "مانند استخوان می توانید از دست دادن ماهیچه ها را با افزایش سن تجربه کنید . در اینجا پیاده روی می تواند به تقویت و قوی تر کردن ماهیچه ها و به جلوگیری از دست دادن ماهیچه کمک کند. پیاده روی منظم می تواند پا و ماهیچه های کمر را تقویت کند.",
    "هضم نادرست می تواند منجر به ناراحتی معده و روده، نفخ، یبوست، اسهال و حتی سرطان روده شود. بنابراین بسیار مهم است که سیستم گوارشی خود را سالم نگه دارید. علاوه بر حفظ عادات غذایی خوب و آب آشامیدنی، باید برای بهبود هضم پیاده روی کنید. پیاده روی بعد از غذا عالی است. به کاهش وزن کمک می کند و همچنین از سیستم گوارشی حمایت می کند ."
]
scores = Semantic_Model.Calculate_Semantic_List_corpus(list_corpus=corpus)
print(scores)
#--------------------------------------------------------------------------------------