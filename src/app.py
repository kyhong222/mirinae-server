from flask import Flask, render_template, request
import requests

app = Flask('__name__')


def modelInit():
    # TODO : init model
    return 1


def sentenceResolution(sourceText, options):
    # post data to URL(mirinae)
    URL = 'http://alpha.mirinae.io/nlp/extractverbphrase'
    data = {'sourceText': sourceText, 'options': options}
    res = requests.post(URL, data=data)

    # res example
    # res = {
    #   'response': [{
    #       'conjugation': 'future, polite informal',
    #       'formPattern': ';타:VV;ㄹ 수 있:VMOD;*;',
    #       'morphemeString': ';타:VV;ㄹ 수 있:VMOD;을 것이:TNS;에요:SEF;',
    #       'sentence': '나는 자전거를 탈 수 있을 거예요.',
    #       'verbPhrase': '~ 탈 수 있을 거예요.'
    #   }],
    #   'success': True
    # }

    # returns resolution data
    json = res.json()
    response = json['response'][0]

    # response = {
    #   'conjugation': 'future, polite informal',
    #   'formPattern': ';타:VV;ㄹ 수 있:VMOD;*;',
    #   'morphemeString': ';타:VV;ㄹ 수 있:VMOD;을 것이:TNS;에요:SEF;',
    #   'sentence': '나는 자전거를 탈 수 있을 거예요.',
    #   'verbPhrase': '~ 탈 수 있을 거예요.'
    # }

    return response


def translateSentence(data, tense):

    # data example

    # data = {
    #   'conjugation': 'future, polite informal',
    #   'formPattern': ';타:VV;ㄹ 수 있:VMOD;*;',
    #   'morphemeString': ';타:VV;ㄹ 수 있:VMOD;을 것이:TNS;에요:SEF;',
    #   'sentence': '나는 자전거를 탈 수 있을 거예요.',
    #   'verbPhrase': '~ 탈 수 있을 거예요.'
    # }

    # TODO : translate sentence with tense
    conjugation = data['conjugation']
    formPattern = data['formPattern']
    morphemeString = data['morphemeString']
    sentence = data['sentence']
    verbPhrase = data['verbPhrase']

    print('conjugation', conjugation)
    print('formPattern', formPattern)
    print('morphemeString', morphemeString)
    print('sentence', sentence)
    print('verbPhrase', verbPhrase)

    return "test sentense"


@app.route('/')
def index():
    return render_template('index.html')

# json loading fail exception handler


def on_json_loading_failed_return_dict(e):
    return {}


@app.route('/translate', methods=['POST'])
def translate():
    request.on_json_loading_failed = on_json_loading_failed_return_dict
    # print(request.get_json())
    json = request.get_json()

    sourceText = json['sourceText']     # text to change
    options = json['options']           # options (use to call mirinae API)
    tense = json['tense']               # tense to change

    # resolution with mirinae API
    data = sentenceResolution(sourceText, options)

    # returns translated sentence with out model
    return translateSentence(data, tense)


app.run(debug=True)
modelInit()
