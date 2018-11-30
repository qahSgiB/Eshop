from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import Context, Template

from .other.a import navigationBar, createContext
from .other.NameSyntax import NameSyntaxSimple
from .other.UserInputType import basicUserInputTypes

from .models import Product, MainInfo



def index(request):
    return HttpResponseRedirect(reverse('shop:main'))

def main(request, debug='Debug'):
    mainInfos = []
    for mainInfo in MainInfo.objects.all():
        title = Template(mainInfo.title).render(Context({'debug': debug}))
        text = Template(mainInfo.text).render(Context({'debug': debug}))
        mainInfos.append({'title': title, 'text': text})

    context = createContext(debug=debug, mainInfos=mainInfos)
    return render(request, 'shop/main.html', context)

def catalog(request):
    products = []
    for product in Product.objects.all():
        productXs = product.productx_set.all()

        name = product.name

        for productX in productXs:
            products.append({
                'name': name,
                'style': productX.style,
                'price': productX.price,
                'imageUrl': productX.image.url,
                'url': {
                    'name': NameSyntaxSimple.su(name),
                    'style': NameSyntaxSimple.su(productX.style),
                }
            })

    context = createContext(title='catalog', products=products)
    return render(request, 'shop/catalog.html', context)

def product(request, name, style=None):
    name = NameSyntaxSimple.us(name)

    if style == None:
        style = Product.objects.get(name=name).productx_set.all()[0].style
        params = {
            'name': NameSyntaxSimple.su(name),
            'style': NameSyntaxSimple.su(style),
        }
        return HttpResponseRedirect(reverse('shop:product', kwargs=params))

    style = NameSyntaxSimple.us(style)

    product = Product.objects.get(name=name)
    productX = product.productx_set.get(style=style)
    price = productX.price

    imagesUrl = []
    for producXImage in productX.productxdetailimage_set.all():
        imagesUrl.append(producXImage.image.url)

    otherStyles = [{'name': productX.style, 'url': {'name': NameSyntaxSimple.su(name), 'style': NameSyntaxSimple.su(productX.style)}} for productX in product.productx_set.all()]

    imageText = ' '.join(['{name} {style}'.format(name=name, style=style) for i in range(10)])

    context = createContext(
        title=name,
        name=name,
        style=style,
        imagesUrl=imagesUrl,
        price=price,
        otherStyles=otherStyles,
        imageText=imageText,
        url={
            'name': NameSyntaxSimple.su(name),
            'style': NameSyntaxSimple.su(style),
        }
    )
    return render(request, 'shop/product.html', context)

def buy(request, name, style):
    name = NameSyntaxSimple.us(name)
    style = NameSyntaxSimple.us(style)

    productX = Product.objects.get(name=name).productx_set.get(style=style)
    imageUrl = productX.image.url
    price = productX.price
    buyerDatas = [
        basicUserInputTypes['name'],
        basicUserInputTypes['email'],
        basicUserInputTypes['addressSK'],
        basicUserInputTypes['zipSK'],
    ]

    context = createContext(
        title='Buy',
        name=name,
        style=style,
        imageUrl=imageUrl,
        price=price,
        buyerDatas=buyerDatas,
        url={
            'name': NameSyntaxSimple.su(name),
            'style': NameSyntaxSimple.su(style),
        }
    )
    return render(request, 'shop/buy.html', context)
