from django.shortcuts import render
from django import forms
import random

img = "https://www.currenwatches.com/cdn/shop/products/Currensmartwatch218_650x.jpg?v=1655203460"
img1 = "https://brunswickbowling.com/uploads/bowler_products/Products/Shoes/Mens/_600x600_crop_center-center_none/Brunswick_Avalanche_Grey_Navy_Side_Right_Outer_catalog_1600x1600.png"
img2 = "https://brunswickbowling.com/imgr/bowlerproducts/Products/Bags/Tournament-Totes/459512/Brunswick_Edge_Double_wo_Pouch_left_1600x1600_17f4986ac7f4990eb3b95b1b30d5f652.png"
img3 = "https://m.media-amazon.com/images/I/81mDltcnpBL.jpg"
img4 = "https://cdn.shopify.com/s/files/1/0578/6245/5485/files/marques-velo-haut-de-gamme-pinarello-occasion_1024x1024.jpg?v=1702375799"
img5 = "https://cdn.shopify.com/s/files/1/0278/9723/3501/files/49-Richard-Mille-Brands.jpg?v=1651007465"
img6 = "https://pyxis.nymag.com/v1/imgs/57d/fa1/340c4b953167c902b1dea3b905057dbf9a-perfume-7.jpg"
img7 = "https://i0.wp.com/almostvintagestyle.com/wp-content/uploads/2018/09/845b34d6574e1fa_front500.jpg?resize=500%2C500&ssl=1"

img_list = [img,img1,img2,img3,img4,img5,img6,img7]


class NewForm(forms.Form):
    name = forms.CharField(label="Enter your name")

# Create your views here.


def index(request):
    if not "user" in request.session:
        request.session["user"] = []
    return render(request, 'ratingapp/index.html',{})

def ask_name(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            request.session["user"]+= [name]
    return render(request, 'ratingapp/askname.html',{
        "form":NewForm(),
    })

def first_page(request):
    return render(request, 'ratingapp/fpage.html', {
        "image":img_list[0],
    })

def second_page(request):
    return render(request, 'ratingapp/spage.html', {
        "image":img_list[1]
    })


def third_page(request):
    return render(request, 'ratingapp/tpage.html', {
        "image":img_list[2]
    })


def end_page(request):
    name = request.session["user"]
    return render(request, 'ratingapp/epage.html', {
        "name":request.session["user"]
    })
