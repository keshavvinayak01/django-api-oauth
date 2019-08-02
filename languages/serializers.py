from rest_framework import serializers as sz
from .models import *

class LanguageSerializer(sz.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('id','url','name','paradigm')

class ParadigmSerializer(sz.HyperlinkedModelSerializer):
    class Meta:
        model = Paradigm
        fields = ('id','url','name')


class ProgrammerSerializer(sz.HyperlinkedModelSerializer):
    class Meta:
        model = Programmer
        fields = ('id','url','name','languages')
