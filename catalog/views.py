from django.shortcuts import render

def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    if request.method == 'POST':
        # Обработка данных формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Новое сообщение от {name} ({phone}): {message}")
        return render(request, 'catalog/contacts.html', {'success': True})
    return render(request, 'catalog/contacts.html')
