# 오답 답안.. (나중에 공부하면서 틀린 부분 보완 예정)
# 테스트 케이스 10개(이하) 중 2개 정도 틀림
import spacy

nlp = spacy.load("en_core_web_sm")

def anonymize_text(sentences):
    sentence = nlp(sentences)
    for ent in sentence.ents:
        if 'PERSON' == ent.label_:
            name = ent.text
            return sentences.replace(name, len(name) * 'X')

    return sentences

anonymize_text("John is old")
