


from product.models import Category, Brand, Style, Collection, Variant

class BaseMixin:
  def get_mainmenu_context(self, **kwargs):
    context = kwargs
    categorylist = Category.objects.all()
    brandlist = Brand.objects.all()
    stylelist = Style.objects.all()
    collectionlist = Collection.objects.all()
    context['catlist'] = categorylist
    context['styles'] = stylelist
    context['brands'] = brandlist
    context['collections'] = collectionlist
    return context


