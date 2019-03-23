from datamuse import datamuse
import json
import requests


api = datamuse.Datamuse()

start_e = api.words(sp='e?*e')


def generateword_list(letter):
  list = api.words(sp = letter+"?*"+letter)
  answer = []

  for i in list:
    word = str(i['word'])

    if(word.__contains__(" ")):
      pass
    else:
      answer.append(word)

  return (answer)


print(generateword_list("o"))