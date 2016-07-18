import MeCab

def execute(sentence):
    meCab = MeCab.Tagger()
    return meCab.parse(sentence)