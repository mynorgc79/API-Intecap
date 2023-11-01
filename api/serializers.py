from usuario.models import Usuario
from api.models import Estudiante,Favorito, Inscripcion, Notificacion

from api.models import CategoriaCurso, Curso, Notificacion_Curso
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=Usuario.objects.all())],
        error_messages={
            'unique': 'El usuario ya existe .'
        }
    )

    class Meta:
        model = Usuario
        fields = '__all__'

        
class CategoriaCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaCurso
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__' 

class FavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = '__all__'

class InscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscripcion
        fields = '__all__'

class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = '__all__'

class NotificacionCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion_Curso
        fields = '__all__'