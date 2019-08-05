from rest_framework import viewsets,permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from global_config import get_global_config
from .models import Language,Paradigm,Programmer
import pandas as pd
import psycopg2 as pg
from json import dumps
from .serializers import LanguageSerializer,ProgrammerSerializer,ParadigmSerializer 
# Create your views here.
active_config = get_global_config()

class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer 

class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer

class ProgrammerAndLanguages(APIView):
    def get(self,request,format=None):
        conn = pg.connect(active_config['local_db']['apiurl'])
        data = pd.read_sql_query("""
            select t1.name as programmer_name, string_agg(t3.name,',') as language_name 
            from languages_programmer t1 
            join languages_programmer_languages t2 
            on t1.id = t2.programmer_id 
            join languages_language t3 on
            t2.language_id = t3.id 
            group by 1 
        """,con=conn)
        
        return Response({
            "result" : "success",
            "data" : dumps(data.to_dict('records'))
        })