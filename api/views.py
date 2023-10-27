from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from api.serializers import UserSerializer,CategoriaCursoSerializer, CursoSerializer, EstudianteSerializer,FavoritoSerializer, InscripcionSerializer, NotificacionSerializer
from rest_framework.decorators import api_view

from usuario.models import Usuario
from api.models import Estudiante, Favorito, Inscripcion,Notificacion
from django.contrib.auth import get_user_model
from api.models import Estudiante,CategoriaCurso, Curso
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet


# Create your views here.

# Extender el schema nos permite manipular OPEN API con lo que trabaja spectacular
# Nos permite hacer cambios.
@extend_schema_view(
    list=extend_schema(description='permite obtener lista usuarios.'),
    retrieve=extend_schema(description='permite obtener un usuario.'),
    create=extend_schema(description='permite crear un usuario.'),
    update=extend_schema(description='permite actualizar un usuario.'),
    destroy=extend_schema(description='permite eliminar un usuario.'),
)
# Definimos nuestra clase, viewset nos permite trabajar con modelos, hace los dif.metodos
# GET, POST, PUT, DELETE = List, retrieve, update, destroy
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Usuario.objects.all()
    
    #lookup_field = 'id' #esto es para que cuando se haga una peticion se pueda buscar por id
    #lookup_url_kwarg = 'id' #esto es para que cuando se haga una peticion se pueda buscar por id


User = get_user_model()


class UserRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Verificar si el correo electrónico ya está en uso
            email = serializer.validated_data.get('email')
            if Usuario.objects.filter(email=email).exists():
                return Response({'detail': 'El usuario ya existe con este correo electrónico.'}, status=status.HTTP_400_BAD_REQUEST)
            
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            return Response({'detail': 'Usuario registrado con éxito'}, status=status.HTTP_201_CREATED)
        return Response({'detail': 'El usuario ya existe .'}, status=status.HTTP_400_BAD_REQUEST)
        #return Response({'detail': 'Ocurrió un error en el registro', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)  # Obtener el token de acceso

        if response.status_code == 200:
            token = response.data['access']  # Obtener el token de acceso del JSON de respuesta
            user = Usuario.objects.get(email=request.data['email'])  # Obtener el usuario por su email

            # Obtener los campos del usuario que deseas incluir
            user_data = {
                'id_usuario': user.id_usuario,
                'email': user.email,
                'nombre': user.nombre,
                'apellido': user.apellido,
                'dpi': user.dpi,
                'genero': user.genero,
                'escolaridad': user.escolaridad,
                'telefono': user.telefono,
                'direccion': user.direccion,
                'etnia': user.etnia,
                'fecha_nacimiento': user.fecha_nacimiento,
                'edad': user.edad,
                'created_at': user.created_at,
                'update_at': user.update_at,
            }
            response.data['user'] = user_data  # Agregar datos del usuario al JSON de respuesta

        return response



class IsSuperUserOrCustomPermission(BasePermission):
    message = "No está autorizado para realizar esta acción."

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if request.user.is_superuser:
                return True  # Los superusuarios tienen acceso completo
            # Agrega lógica personalizada para otros permisos aquí
            # Por ejemplo, verifica si el usuario tiene un permiso específico
        return False  # Usuario no autorizado

# En tus vistas, usa el decorador personalizado o anula `has_permission` como sigue:

from rest_framework.views import APIView

class CustomView(APIView):
    permission_classes = [IsAuthenticated, IsSuperUserOrCustomPermission]

    def get(self, request):
        # Aquí colocas tu lógica de vista personalizada
        return Response({"message": "Puedes ver esta vista porque eres superusuario o tienes un permiso especial."}, status=status.HTTP_200_OK)


#–--------------PARA REGISTRO -----------------
class CategoriaCursoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaCurso.objects.all()
    serializer_class = CategoriaCursoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer

class InscripcionViewSet(viewsets.ModelViewSet):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer

class NotificacionViewSet(viewsets.ModelViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer




