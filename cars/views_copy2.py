from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm, BrandModelForm
from django.views import View


class CarsView(View):

    def get(self, request):
        cars = Car.objects.all().order_by('model')
        search = request.GET.get('search')

        if search:
            cars = cars.filter(model__icontains=search)

        context = {
            'cars': cars
        }

        return render(request, 'cars.html', context)


class NewCarView(View):

    def get(self, request):
        new_car_form = CarModelForm()
        return render(request, 'new_car.html', {'new_car_form': new_car_form})

    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        return render(request, 'new_car.html', {'new_car_form': new_car_form})


class NewBrandView(View):

    def get(self, request):
        new_brand_form = BrandModelForm()
        return render(request, 'new_brand.html', {'new_brand_form': new_brand_form})

    def post(self, request):
        new_brand_form = BrandModelForm(request.POST)
        if new_brand_form.is_valid():
            new_brand_form.save()
            return redirect('cars_list')
        return render(request, 'new_brand.html', {'new_brand_form': new_brand_form})