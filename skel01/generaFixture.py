#!/usr/bin/python
# -*- coding: utf-8 -*-

import json



import sys

reload(sys)
sys.setdefaultencoding("utf-8")


fixture=[]

def dataToJson (app, model, fixture, data, pk):
	for x in data:
		fixture.append ( {'pk': pk, 'model': app + "." + model, 'fields': x})
		pk +=1
polls = [
 	{'question': u'Cómo esta el día?'},
 	{'question': u'Cuál es el mejor beatle?'},
 	{'question': u'Qué pasa?'}
]

choices = [
      {'poll':'1', 'choice_text': 'bueno'},
      {'poll':'1', 'choice_text': 'feo'},
      {'poll':'1', 'choice_text': 'malo'},
      {'poll':'2', 'choice_text': 'ringo'},
      {'poll':'2', 'choice_text': 'john'},
      {'poll':'2', 'choice_text': 'paul'},
      {'poll':'3', 'choice_text': 'nada'},
      {'poll':'3', 'choice_text': 'algo'},
      {'poll':'3', 'choice_text': 'de todo'},
]


def main():
  app='polls'

  data = polls
  model='poll'
  dataToJson(app, model, fixture, data, 4)

  data = choices
  model='choice'
  dataToJson(app, model, fixture, data, 4)


  #print (fixture)
  #print json.dumps(fixture, ensure_ascii=False)
  print json.dumps(fixture)


if __name__ == "__main__":
    main()


