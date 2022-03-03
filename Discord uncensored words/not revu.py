
def test():
    list_text = ['поле', 'тревога', 'y', 'y', 'cekb']
    words = ' п,ол*е цветов cek b цветов неполесадник п,л*е cek,b'

    test_counter = 0
    for i in list_text: # перебираем list_text
        position_in_i = 0
        intersection_counter_list_text_in_words = 0
        #if words == i or words.replace(' ', '') in i or i in words:
        if i[0] in words and i[position_in_i - 1] in words: # в words есть такая буква
            s = 0
            print('s = 0')
            for _ in range(words.count(i[0])): #цыкл количество раз совподений первого элемента i
                #s = 0
                #section_words = words[words.index(i[0]) + s:]
                for _ in range(len(i)) : # цыкл количество раз длинны аргумента


                    if len(i) > position_in_i: # длинна аргуиента больше позиции аргумента
                        #print(i[position_in_i])
                        position_in_i += 1
                        n = words.index(i[0], words.index(i[0]) + s)
                        if i[position_in_i - 1] in words[n:]: # в words есть такая буква


                                if i[position_in_i - 1] == words[(words.index(i[position_in_i - 1], n))]: #позиция в i таже что и в words
                                    if i[position_in_i - 1] == i[0]:
                                        intersection_counter_list_text_in_words += 1
                                        print(i[position_in_i - 1])
                                    else:
                                        allowed_number_of_characters = words.index(i[position_in_i - 1], n) - words.index(i[position_in_i - 2], n)

                                        if words.index(i[position_in_i - 1], n) > words.index(i[position_in_i - 2], n)\
                                                and allowed_number_of_characters <= 2:
                                            intersection_counter_list_text_in_words += 1



                                        print(i[position_in_i - 1])
                                        if intersection_counter_list_text_in_words == len(i):
                                            print('здесь прописать код при обнаружении совпадения')
                                            #s += 1
                                            test_counter += 1
                                            intersection_counter_list_text_in_words = 0
                        else:
                            print('no')
                            break
                    if len(i) == position_in_i:
                        s += 1
                        position_in_i = 0
                        intersection_counter_list_text_in_words = 0
                        print('s += 1')
        else:
            pass
    print('количество совпадений list_text in words',test_counter)
    #print('на какой позиции п', words.index("п",1))
    print('количество п', words.count("п"))
if __name__ == '__main__':
    test()

