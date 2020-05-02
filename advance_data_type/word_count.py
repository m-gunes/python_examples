def word_count(text):
    text_dict = dict()
    for i in text:
        if i in text_dict:
            text_dict[i] += 1
        else:
            text_dict[i] = 1
    print(text_dict)



text = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"


word_count(text)