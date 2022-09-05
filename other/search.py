from django.views.generic import TemplateView
from django.http import HttpResponse
import json

from vacancy.models import Vacancy

class Search(TemplateView):
    template_name: "search.html"
    
    def get(self, request, *args, **kwargs):
        k = request.GET.get('k')
        query = 'SELECT * FROM TB_VACANCY WHERE doc_id LIKE %s OR employer_name LIKE %s OR date_posted LIKE %s OR employment_type LIKE %s OR location LIKE %s OR title LIKE %s OR description LIKE %s'
        res = []
        
        for v in Vacancy.objects.raw(query, ['%%' + k + '%%'] * 7):
            v_json = {
                'doc_id': v.doc_id,
                'employer_name': v.employer_name,
                'date_posted': v.date_posted,
                'employment_type': v.employment_type,
                'location': v.location,
                'title': v.title,
                'description': v.description,
            }
            res.append(v_json)
        
        return HttpResponse(json.dumps(res))