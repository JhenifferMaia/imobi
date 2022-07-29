from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
# auth é o modo de autenticacao do django
from django.contrib.messages import constants


def cadastro(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')

        return render(request, 'cadastro.html')
    elif request .method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        # caso o tamanho da senha/email/user for igual a 0 , o usuário será redirecinado ao cadsatro denovo. mesmo se o usuário der vários espaços, eles será redirecionado
        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0:
            messages.add_message(request, constants.ERROR,
                                 'Preencha todos os campos')
            return redirect('/auth/cadastro')

        user = User.objects.filter(username=username)
        print(user)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Usuário já existe')
            return redirect('/auth/cadastro')

        try:
            user = User.objects.create_user(
                username=username, email=email, password=senha)

            user.save()
            messages.add_message(request, constants.SUCCESS,
                                 'Usuário cadastrado com sucesso')
            return redirect('/auth/logar')

        except:
            messages.add_message(request, constants.ERROR,
                                 'Erro interno do sistema')
            return redirect('/auth/logar')


def logar(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')

        return render(request, 'logar.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        usuario = auth.authenticate(username=username, password=senha)
    if not usuario:
        messages.add_message(request, constants.ERROR,
                             'Username ou senha inválidos')
        return redirect('/auth/logar')
    else:
        auth.login(request, usuario)
        return redirect('/')


def sair(request):
    auth.logout(request)
    return redirect('/auth/logar')


# pra o q eu está no arquivo html aparecer, o arquivo tem renderizar. com a função render
# todo app criado deverá ser cadastrado em settings, em 'installed_apps'
# python manage.py createsuperuser
# python menage.py migrate
