from django.urls import path

from api.views import get_vacancies, get_companies, get_company, get_company_vacancies, get_vacancy, vacancy_top

urlpatterns = [
    path('vacancies/', get_vacancies),
    path('vacancies/<int:vacancy_id>/', get_vacancy),
    path('vacancies/top_ten/', vacancy_top),
    path('companies/', get_companies),
    path('companies/<int:company_id>/', get_company),
    path('companies/<int:id>/vacancies/', get_company_vacancies)
]