from .models import *
import django_filters
from django import forms



class ListTextWidget(forms.TextInput):
    def __init__(self, data_list, name, *args, **kwargs):
        super(ListTextWidget, self).__init__(*args, **kwargs)
        self._name = name
        self._list = data_list
        self.attrs.update({'list':'list__%s' % self._name})

    def render(self, name, value, attrs=None, renderer=None):
        text_html = super(ListTextWidget, self).render(name, value, attrs=attrs)
        data_list = '<datalist id="list__%s">' % self._name
        for item in self._list:
            data_list += '<option value="%s">' % item
        data_list += '</datalist>'

        return (text_html + data_list)

class SessionFilter(django_filters.FilterSet):
    #room = django_filters.ChoiceFilter(label=("room name"), choices=Room.objects.all()., widget=ListTextWidget(data_list=Room.objects.all(), name='room'))
    class Meta:
        model = Session
        fields = ['speaker', 'room', 'time_slot' ]
        ordering = ('name',)