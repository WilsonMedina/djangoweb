from .models import RrSs

#------------------------------Processor of context for show the RRSS-----------------------------------------------#
def context_rrss(request):
    model = RrSs
    context_name = {}
    names = model.objects.filter(state = True)
    for name in names:
        context_name[name.name] = {'url' : name.url, 'icon' : name.icon}
    return context_name
