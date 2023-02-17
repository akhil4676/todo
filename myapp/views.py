from ast import Return
from urllib import request
from django.shortcuts import render,redirect

# Create your views here.
from myapp.forms import LoginForm, TodoForm,TodoModelForm,RegistrationForm

from django.views.generic import ListView,View,DetailView,CreateView,UpdateView

from myapp.models import Todos, todos

from django.contrib import messages



from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator


def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"u must login first")
            return redirect("signin")
        else:
            return fn(request,*args,*kwargs)
    return wrapper

@method_decorator(signin_required,name="dispatch")
class TodoCreateView(CreateView):

    model=Todos
    form_class=TodoModelForm
    template_name:str="add_todo.html"
    success_url=reverse_lazy("todo-list")

    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"todo create")
        return super().form_valid(form)

    # def get(self,request,*args,**kwargs):
    #     form=TodoModelForm()
    #     return render(request,"add_todo.html",{"form":form})
    # def post(self,request,*args,**kwargs):
    #     form=TodoModelForm(request.POST) 
    #     if form.is_valid():
    #         form.instance.user=request.user
    #         form.save()
    #         messages.success(request,"todo has been created")
    #         # t_name=form.cleaned_data.get('task_name')
    #         # usr=form.cleaned_data.get("user")
    #         # Todos.objects.create(task_name=t_name,user=usr)
    #         return redirect("todo-list")
    #     else:
    #         messages.error(request,"cant create")
    #         return render(request, "add_todo.html",{"form":form})
@method_decorator(signin_required,name="dispatch")
class TodoListView(ListView):
    model=Todos
    context_object_name="todos"
    template_name="todo-list.html"

    def get_queryset(self):
        return Todos.objects.filter(user=self.request.user)
    


    
    # def get(self,request,*args,**kwargs):
    #     qs=Todos.objects.filter(user=request.user)
    #     return render(request,"todo-list.html",{"todos":qs})



@method_decorator(signin_required,name="dispatch")
class TodoDetailView(DetailView):

    model=Todos
    template_name:str="todo-detail.html"
    context_object_name: str="todo"
    pk_url_kwarg: str="id"


    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("id")
    #     todo=Todos.objects.filter(id=id)[0]
    #     return render(request,"todo-detail.html",{"todo":todo})
@method_decorator(signin_required,name="dispatch")       
class TodoDeleteView(View):
     def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        todo=Todos.objects.filter(id=id).delete()
        messages.success(request,"deleted successfully")
        return redirect("todo-list")

@method_decorator(signin_required,name="dispatch")
class TodoUpdateView(UpdateView):
    model=Todos
    form_class=TodoModelForm
    template_name: str="update-todo.html"
    pk_url_kwarg: str="id"
    success_url=reverse_lazy("todo-list")

    def form_valid(self, form):
        messages.success(self.request,"todo change")
        return super().form_valid(form)



    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("id")
    #     # todo=[todo for todo in todos if todo.get("id")==id].pop()
    #     todo=Todos.objects.get(id=id)
    #     form=TodoModelForm(instance=todo)
    #     return render(request, "update-todo.html",{"form":form})
    # def post(self,request,*args,**kwargs):
    #     id=kwargs.get("id")

    #     todo=Todos.objects.get(id=id)

    #     form=TodoModelForm(request.POST,instance=todo)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request,"todo update")
    #         # data=form.cleaned_data
    #         # todo=[todo for todo in todos if todo.get("id")==id].pop()
    #         # todo.update(data)
    #         # Todos.objects.filter(id=id).update(**form.cleaned_data)
    #         return redirect("todo-list")
    #     else:
    #         messages.error(request,"not updated")
    #         return render(request, "update-todo.html",{"form":form})

class RegistrationView(View):

    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"registration.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            
            User.objects.create_user(**form.cleaned_data )



            messages.success(request,"registration completed successfully")
            return redirect("signin")
        else:
            messages.success(request,"resgistration failed")
            return render(request,"registration.html",{"form":form})


class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
        
            if user:
                login(request,user)


                return redirect("todo-list")
            else:
                messages.error(request,"invalid credentials")
                return render(request,"login.html",{"form":form})

@signin_required
def signout(request,*args,**kwargs):
    logout(request)
    return redirect("signin")

        

            
        