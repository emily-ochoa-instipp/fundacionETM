from django import forms
from .models import DocumentoTransparencia

class DocumentoTransparenciaForm(forms.ModelForm):
    class Meta:
        model = DocumentoTransparencia
        fields = ['nombre', 'archivo', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del documento'}),
            'archivo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'custom-control-input','id': 'RepeatSwitch'}),
        }
