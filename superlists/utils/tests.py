from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.template import engines, Template, RequestContext, Context
from django.test import TestCase

from utils.utils import remove_csrf, get_csrf_tag


class RemoveCSRFTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_there_is_no_csrf(self):
        dom_no_csrf_with_csrf = "<html></html>"
        dom_no_csrf_without_csrf = "<html></html>"
        self.assertEqual(dom_no_csrf_without_csrf,
                         remove_csrf(dom_no_csrf_with_csrf))

    def test_there_is_one_csrf(self):
        # template = Template("<html><body><form>{% csrf_token %}<input name=\"first_name\"/></form></body></html>")
        # context = Context({})
        # template.render(context)
        # request = HttpRequest()
        # dom_one_csrf_with_csrf = render(request, "<html><body><form>{% csrf_token %}<input name=\"first_name\"/></form></body></html>")

        # dom_one_csrf_with_csrf = HttpResponse("<html><body><form>{% csrf_token %}<input name=\"first_name\"/></form></body></html>")
        # django_engine = engines['django']
        # template = django_engine.from_string("Hello {{ name }}!")
        # dom_one_csrf_with_csrf = HttpResponse("<html><body><form>{% csrf_token %}<input name=\"first_name\"/></form></body></html>")
        # test = Template("{% csrf_token %}")
        # request = HttpRequest("{% csrf_token %}")
        # test2 = RequestContext(request, {
        #     'foo': 'bar',
        # })
        request = HttpRequest()
        csrf_tag = render(request, 'generate_csrf.html')._container[0]
        # import pdb
        # pdb.set_trace()
        dom_one_csrf_without_csrf = HttpResponse("<html><body><form><input name=\"first_name\"/></form></body></html>")
        self.assertEqual(dom_one_csrf_without_csrf,
                         remove_csrf(dom_one_csrf_with_csrf))

    def test_there_is_two_csrf(self):
        pass


class GetCsrfTag(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_csrf_tag_is_right_regex(self):
        regex_csrf_tag = r"<input type='hidden' name='csrfmiddlewaretoken' value='[a-zA-z0-9]{64}' />\n"
        self.assertRegex(get_csrf_tag(), regex_csrf_tag)
