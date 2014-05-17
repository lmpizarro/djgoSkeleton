import json

'''
# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
'''


fixture=[]

def dataToJson (app, model, fixture, data, pk):
	for x in data:
		fixture.append ( {'pk': pk, 'model': app + "." + model, 'fields': x})
		pk +=1
polls = [
 	{'question': 'Como esta el dia?'},
 	{'question': 'Cual es el mejor beatle?'}
]

choices = [
      {'poll':'2', 'choice_text': 'bueno'},
      {'poll':'2', 'choice_text': 'feo'},
      {'poll':'2', 'choice_text': 'malo'},
      {'poll':'3', 'choice_text': 'ringo'},
      {'poll':'3', 'choice_text': 'john'},
      {'poll':'3', 'choice_text': 'paul'}
]


def main():
  app='polls'
  model='choice'
  dataToJson(app, model, fixture, choices, 4)
  print json.dumps(fixture)


if __name__ == "__main__":
    main()


