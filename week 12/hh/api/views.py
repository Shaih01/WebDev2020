from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from api.models import Company, Vacancy


def get_company(request, company_id):
    try:
        company = Company.objects.get(id=company_id).to_json()
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(company.to_json())


def get_companies(request):
    companies = Company.objects.all()
    company_json = [companies.to_json() for company in companies]
    return JsonResponse(company_json, safe=False)


def get_company_vacancies(request, need_company_id):
    vacancies = Vacancy.objects.all()
    out = []

    for i in vacancies:
        if i.company.id == need_company_id:
            out.append(i.to_json())
        else:
            return JsonResponse({'error'})

    return JsonResponse(out, safe=False)


def get_vacancies(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancies.to_json() for vac in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def get_vacancy(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id).to_json()
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(vacancy.to_json())


def vacancy_top(request):
    vacancies = Vacancy.objects.filter().order_by("-salary")[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)