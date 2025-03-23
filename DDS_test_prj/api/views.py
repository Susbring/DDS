from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import FinancialMove, DDSCategory, DDSStatus, DDSSubcategory, DDSType
from .forms import DDSForm


def dds_list(request):
    """Отображение списка записей с фильтрацией и пагинацией"""
    all_dds = FinancialMove.objects.all().order_by('-date')

    date_form = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    status_id = request.GET.get('status')
    type_id = request.GET.get('type')
    category_id = request.GET.get('category')
    subcategory_id = request.GET.get('subcategory')

    if date_form:
        all_dds = all_dds.filter(date__gte=date_form)
    if date_to:
        all_dds = all_dds.filter(date__lte=date_to)

    if status_id:
        all_dds = all_dds.filter(status_id=status_id)
    if type_id:
        all_dds = all_dds.filter(type_id=type_id)
    if category_id:
        all_dds = all_dds.filter(category_id=category_id)
    if subcategory_id:
        all_dds = all_dds.filter(subcategory_id=subcategory_id)

    paginator = Paginator(all_dds, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    statuses = DDSStatus.objects.all()
    types = DDSType.objects.all()
    categories = DDSCategory.objects.all()
    subcategories = DDSSubcategory.objects.all()

    active_filters = {
        'date_from': date_form,
        'date_to': date_to,
        'status': status_id,
        'type': type_id,
        'category': category_id,
        'subcategory': subcategory_id,
    }

    context = {
        'page_obj': page_obj,
        'statuses': statuses,
        'types': types,
        'categories': categories,
        'subcategories': subcategories,
        'date_from': date_form or '',
        'date_to': date_to or '',
        'selected_status': status_id or '',
        'selected_type': type_id or '',
        'selected_category': category_id or '',
        'selected_subcategory': subcategory_id or '',
        'active_filters': active_filters,
    }
    return render(request, 'dds_app/dds_list.html', context)


def dds_form(request, pk=None):
    """Создает или редактирует запись ДДС"""
    if pk:
        dds = get_object_or_404(FinancialMove, pk=pk)
    else:
        dds = None

    if request.method == 'POST':
        form = DDSForm(request.POST, instance=dds)
        if form.is_valid():
            form.save()
            return redirect('dds_list')
    else:
        form = DDSForm(instance=dds)

    context = {
        'form': form,
        'dds': dds,
    }
    return render(request, 'dds_app/dds_form.html', context)


def delete_dds(request, pk):
    """Удаляет запись ДДС."""
    dds = get_object_or_404(FinancialMove, pk=pk)
    if request.method == 'POST':
        dds.delete()
        return redirect('dds_list')
    return render(request, 'dds_app/dds_delete_confirm.html', {'dds': dds})


class StatusListView(ListView):
    model = DDSStatus
    template_name = 'dds_app/status_list.html'
    context_object_name = 'statuses'


class StatusCreateView(CreateView):
    model = DDSStatus
    template_name = 'dds_app/status_form.html'
    fields = ['name']
    success_url = reverse_lazy('status_list')


class StatusUpdateView(UpdateView):
    model = DDSStatus
    template_name = 'dds_app/status_form.html'
    fields = ['name']
    success_url = reverse_lazy('status_list')


class StatusDeleteView(DeleteView):
    model = DDSStatus
    template_name = 'dds_app/status_confirm_delete.html'
    success_url = reverse_lazy('status_list')


class TypeListView(ListView):
    model = DDSType
    template_name = 'dds_app/type_list.html'
    context_object_name = 'types'


class TypeCreateView(CreateView):
    model = DDSType
    template_name = 'dds_app/type_form.html'
    fields = ['name']
    success_url = reverse_lazy('type_list')


class TypeUpdateView(UpdateView):
    model = DDSType
    template_name = 'dds_app/type_form.html'
    fields = ['name']
    success_url = reverse_lazy('type_list')


class TypeDeleteView(DeleteView):
    model = DDSType
    template_name = 'dds_app/type_confirm_delete.html'
    success_url = reverse_lazy('type_list')


class CategoryListView(ListView):
    model = DDSCategory
    template_name = 'dds_app/category_list.html'
    context_object_name = 'categories'


class CategoryCreateView(CreateView):
    model = DDSCategory
    template_name = 'dds_app/category_form.html'
    fields = ['type', 'name']
    success_url = reverse_lazy('category_list')


class CategoryUpdateView(UpdateView):
    model = DDSCategory
    template_name = 'dds_app/category_form.html'
    fields = ['type', 'name']
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(DeleteView):
    model = DDSCategory
    template_name = 'dds_app/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')


class SubcategoryListView(ListView):
    model = DDSSubcategory
    template_name = 'dds_app/subcategory_list.html'
    context_object_name = 'subcategories'


class SubcategoryCreateView(CreateView):
    model = DDSSubcategory
    template_name = 'dds_app/subcategory_form.html'
    fields = ['category', 'name']
    success_url = reverse_lazy('subcategory_list')


class SubcategoryUpdateView(UpdateView):
    model = DDSSubcategory
    template_name = 'dds_app/subcategory_form.html'
    fields = ['category', 'name']
    success_url = reverse_lazy('subcategory_list')


class SubcategoryDeleteView(DeleteView):
    model = DDSSubcategory
    template_name = 'dds_app/subcategory_confirm_delete.html'
    success_url = reverse_lazy('subcategory_list')


def reference_dds(request):
    """Общее представление для страницы справочников."""
    return render(request, 'dds_app/dds_reference.html')
