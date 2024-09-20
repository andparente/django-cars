from django import forms
from cars.models import Brand, Car


class CarModelForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if not photo:
            self.add_error(
                'photo',
                'É necessário enviar pelo menos uma foto do veículo.'
            )
        return photo

    def clean_plate_number(self):
        plate_number = self.cleaned_data.get('plate_number')
        print(plate_number)
        if len(str(plate_number)) > 1:
            self.add_error(
                'plate_number',
                'Por favor, insira apenas o úlimo digito da placa do veículo.'
            )
        return plate_number


class BrandModelForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        brand_filter = Brand.objects.filter(name__icontains=name)
        if brand_filter:
            self.add_error('name', 'Marca já cadastrada.')
        return name
