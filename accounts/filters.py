import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class JobFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date_created", lookup_expr='gte')
	end_date = DateFilter(field_name="date_created", lookup_expr='lte')
	note = CharFilter(field_name='note', lookup_expr='icontains')


	class Meta:
		model = Job
		fields = '__all__'
		exclude = ['customer', 'date_created']

# class JobFilter(django_filters.FilterSet):
# 	start_date = DateFilter(field_name="date_created", lookup_expr='gte')
# 	end_date = DateFilter(field_name="date_created", lookup_expr='lte')
# 	description = CharFilter(field_name='note', lookup_expr='icontains')


# 	class Meta:
# 		model = Order
# 		fields = '__all__'
# 		exclude = ['employer', 'date_created']