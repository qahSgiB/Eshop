from .NavigationBar import NavigationBar
from .NameSyntax import NameSyntaxSimple



class ProductManager:
    def createProduct(name):
        from shop.models import Product, ProductX, ProductXDetailImage

        Product.objects.create(name=name)

    def createProductX(productName, style, price, sizes, imagesCount):
        from django.core.files import File
        from shop.models import Product, ProductX, ProductXDetailImage

        productNameSU = NameSyntaxSimple.su(productName)
        product = Product.objects.get(name=productName)

        styleSU = NameSyntaxSimple.su(style)
        image = File(open('_temporary/images/{name}/{style}/main.jpg'.format(name=productNameSU, style=styleSU), 'rb'))

        productX = ProductX(product=product, style=style, price=price, sizes=sizes)
        productX.image.save('{name}/{style}/main.jpg'.format(name=productNameSU, style=styleSU), image)

        for i in range(imagesCount):
            image = File(open('_temporary/images/{name}/{style}/details/{index}.jpg'.format(name=productNameSU, style=styleSU, index=i), 'rb'))

            productXDetailImage = ProductXDetailImage(productX=productX)
            productXDetailImage.image.save('{name}/{style}/details/{index}.jpg'.format(name=productNameSU, style=styleSU, index=i), image)

class MainInfoManager:
    def createMainInfo(title, text):
        from shop.models import MainInfo

        MainInfo.objects.create(title=title, text=text)



def createContext(**params):
    title = params['title'] if 'title' in list(params.keys()) else None

    context = {
        'title': 'Fiii' + ('' if title == None else ' * '+title),
        'navigationBar': navigationBar.items,
    }

    for paramKey in list(params.keys()):
        if not paramKey in list(context.keys()):
            context[paramKey] = params[paramKey]

    return context



navigationBar = NavigationBar()
navigationBar.addItem('main', 'main')
navigationBar.addItem('catalog', 'catalog')
navigationBar.addItem('about', 'catalog')
navigationBar.addItem('contact', 'catalog')
