import discord
from discord.ext import commands

"""
Дискорд бот для удаления не цензурных выражений

"""

def reed_file(name_file):
    """

    :param naim_file: имя документа
    :return: файл с текстом
    """
    with open(f'{name_file}', 'r', encoding='utf-8') as file:
        file_reed = file.read()
        #print(1)
        return file_reed
    # f = open('bad words.txt', 'r', encoding="utf-8")
    # print(f.read(1))
    # f.close()

# def list_creation():
#     list_bad_words = []
#     return list_bad_words
def on_red_file_in_list(name_file):
    """
    :param naim_file: имя документа
    :return: список слов
    """
    list_bad_words = [] #list_bad_words = list_creation
    n = reed_file(name_file)
    for i in n.split():
        list_bad_words.append(i)
    #print(list_bad_words[0])
    return list_bad_words

def save_list_in_file(name_file_save):
    """
    функция не дописана
    :param name_file_save:
    :return:
    """
    with open(f'{name_file_save}', 'w', encoding='utf-8') as file:
        for i in on_red_file_in_list(enter_file_open):
            file.write(i)
            print(i)



client = discord.Client()

@client.event
async def on_ready():
    print('Conjunction {0.user} ... True'.format(client))

# удаляет слова из списка
@client.event
async def on_message(message): #message.content сообщение в чате тип str
    if message.author == client.user:
        return

    if message.content in list_bad_words:
        await message.channel.purge(limit=1)


if __name__ == '__main__':
    enter_file_open = "bad words.txt"
    #enter_file_save = 'list bad words.txt'
    #reed_file(enter_file)
    list_bad_words = on_red_file_in_list(enter_file_open)

    #save_list_in_file(enter_file_save)


    client.run('OTI4NzIyODUxMzAzOTMxOTE0.Ydc6jg.88Jl-_l-uy8leBlHL-BXqPMZinA')