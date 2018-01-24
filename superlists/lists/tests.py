import re

from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.urls.base import resolve

from lists.models import Item
from lists.views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html', request=request)
        # Remove the csrf token in both pages:
        re_csrf = "<input type=\'hidden\' name=\'csrfmiddlewaretoken\' value=\'[a-zA-Z0-9]+\' />"
        response_without_csrf = re.sub(re_csrf, '', response.content.decode())
        expected_html_without_csrf = re.sub(re_csrf, '', expected_html)

        self.assertEqual(response_without_csrf, expected_html_without_csrf)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'
        response = home_page(request)
        self.assertIn('A new list item', response.content.decode())

        expected_html = render_to_string(
            'home.html',
            {'new_item_text': 'A new list item'},
            request=request
        )

        # Remove the csrf token in both pages:
        re_csrf = "<input type=\'hidden\' name=\'csrfmiddlewaretoken\' value=\'[a-zA-Z0-9]+\' />"
        response_without_csrf = re.sub(re_csrf, '', response.content.decode())
        expected_html_without_csrf = re.sub(re_csrf, '', expected_html)

        self.assertEqual(response_without_csrf, expected_html_without_csrf)


class ItemModelsTest(TestCase):
    def test_saveing_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The firest (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_items = saved_items[0]
        second_saved_items = saved_items[1]
        self.assertEqual(first_saved_items.text, 'The firest (ever) list item')
        self.assertEqual(second_saved_items.text, 'Item the second')
