from django import forms

from .models import Evangelista

class EvangelistaForm(forms.ModelForm):
	class Meta:
		model = Evangelista
		fields = [
			"igreja",
			"projeto",
			"funcao",
			"nome",
			"data_nascimento",
			"data_entrada_evg",
			"foto_perfil",
			"data_batismo_no_espirito_santo",
			"foto_perfil",
			"obreiro",
			"inativo"
		]