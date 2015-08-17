# -*- coding: utf-8 -*-
from bottle import MakoTemplate, Bottle, request
from model.foo import Foo

foo_app = Bottle()

@foo_app.get('/')
def home():
    return MakoTemplate(name='foo', lookup=['./view/']).render()

@foo_app.post('/save')
def save():
    name = request.forms.get('name')
    params = {}
    params['name'] = name
    foo = Foo();
    result =  foo.save_and_find_all(params);
    render = {}
    render['result'] = result
    return MakoTemplate(name='result', lookup=['./view/']).render(render)