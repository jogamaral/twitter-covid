import nltk

tw_dict = {'created_at':[],
               'id':[],
               'id_str':[],
               'full_text':[],
               'entities':[],
               'source':[],
               'user':[],
               'lang':[]}

def Preprocessing(instancia):
    # Remove caracteres indesejados.
    instancia = re.sub(r"#\S+", "", instancia)
    instancia = re.sub(r"@\S+", "", instancia).lower().replace('.','').replace(';','').replace('-','').replace(':','').replace(')','').replace('"','').replace(',','')
    # Removendo palavras e termos frequentes que não tem relevância nos dados.
    stopwords = set(nltk.corpus.stopwords.words('portuguese'))
    palavras = [i for i in instancia.split() if not i in stopwords]
    return (" ".join(palavras))