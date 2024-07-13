from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Books
from .serializers import BookSerializer
from .forms import *
from django.contrib import messages
from django.db.models import Q

def get_book(request):
    if request.user.is_authenticated:
        if request.method=="GET":
            try:
                books=Books.objects.all()
                serializer=BookSerializer(books,many=True)
                return render(request,"get_book.html",{"books":serializer.data})
            except:
                return HttpResponse("Something went wrong")
    else:
        return redirect("/login/")

def Add_book(request):
    if request.user.is_authenticated:
        form=AddForm()
        if request.method=="POST":
            form=AddForm(request.POST)
            if form.is_valid():
                Author=form.cleaned_data["Author"]
                Title=form.cleaned_data["Title"]
                ISBN=form.cleaned_data["ISBN"]
                data={"Title":Title,"Author":Author,"ISBN":ISBN}
                serializer=BookSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    messages.success(request,"Added Successfully")
                    return redirect("/add_book/")
                else:
                    messages.success(request,"Wrong input") 
                    print(serializer.errors)
                    return redirect("/add_book/")   
            else:
                print("asdas")
                messages.error(request,"Wrong input")
        return render(request,"add_book.html",{"form":form})
    else:
        return redirect("/login/")

def edit_book(request,book_id):
    if request.user.is_authenticated:
        obj=Books.objects.get(id=book_id)
        initial_data={
            "id":obj.id,
            "Title":obj.Title,
            "Author":obj.Author,
            "ISBN":obj.ISBN
        }
        form=EditForm(initial=initial_data)
        if request.method=="POST":
            form=EditForm(request.POST)
            if form.is_valid():
                id=form.cleaned_data["id"]
                Author=form.cleaned_data["Author"]
                Title=form.cleaned_data["Title"]
                ISBN=form.cleaned_data["ISBN"]
                data={"id":id,"Title":Title,"Author":Author,"ISBN":ISBN}
                serializer=BookSerializer(obj,data=data)
                if serializer.is_valid():
                    serializer.save()
                    messages.success(request,"Added Successfully")
                    return redirect(f"/edit_book/{id}")
                else:
                    messages.success(request,"Wrong input") 
                    print(serializer.errors)
                    return redirect("/edit_book/")
    
            else:
                messages.error(request,"Wrong input")
        return render(request,"edit_book.html",{"form":form,"Book":obj})
    else:
        return redirect("/login/")
         
def delete_book(request,book_id):
    if request.user.is_authenticated:
        obj=Books.objects.get(id=book_id)
        obj.delete()
        messages.success(request,"Deleted Successfully")
        return redirect("/get_book/")
    else:
        return redirect("/login/")
         
def look_for_book(request,book_id):
    if request.user.is_authenticated:
        try:
            obj=Books.objects.filter(id=book_id)
            if len(obj)!=0:
                return render(request,"get_book.html",{"books":obj})
            else:
                messages.error(request,"Invalid Id")
                return render(request,"get_book.html")
        except Exception as e:
            print(e)
            messages.error(request,"Invalid Id")
            return redirect("/get_book/")
    else:
        return redirect("/login/")
    
def search(request):
    if request.method=="POST" and "search" in request.POST:
        search=request.POST["search"]
        objs=Books.objects.filter(Q(Title__startswith=search) |Q(Author__startswith=search)|Q(id=search))
        return render(request,"get_book.html",{"books":objs})