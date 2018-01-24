import re
from django.shortcuts import render
from django.http import HttpRequest


def remove_csrf(dom):
    regex_csrf = "<input type=\'hidden\' name=\'csrfmiddlewaretoken\' value=\'[a-zA-Z0-9]+\' />"
    return re.sub(regex_csrf, '', dom)


def get_csrf_tag():
    request = HttpRequest()
    return render(request, 'generate_csrf.html')._container[0].decode("utf-8")
