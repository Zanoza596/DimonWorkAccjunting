from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name="main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'KINGKOSHA - Главная'
        context["content"] = 'Магазин тренажёров KINGKOSHA'
        return context
    
class AboutView(TemplateView):
    template_name="main/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'KINGKOSHA - О нас'
        context["content"] = 'О нас'
        context["text_on_page"] = 'KINGKOSHA - эго круто !!!'
        return context
    
# def index(request):
#     context: dict[str,str] = {
#         'title':'KINGKOSHA - Главная',
#         'content':'Магазин тренажёров KINGKOSHA',
#     }               
#     return render(request,'main/index.html',context)

# def about(request):
#     context: dict[str,str] = {
#         'title':'KINGKOSHA - О нас',
#         'content':'О нас',
#         'text_on_page': "KINGKOSHA - эго круто !!!",
#     }               
#     return render(request,'main/about.html',context)
