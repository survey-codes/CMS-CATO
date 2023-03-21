import unittest

from domain.main.exceptions.empty_pk_exception import BadPkException
from domain.main.exceptions.empty_value_exception import EmptyValueException
from domain.tests.contents.model.databuilder.PageDataBuilder import PageDataBuilder


class TestPage(unittest.TestCase):

    def test_given_the_creation_of_page_when_is_bad_pk_then_return_bad_pk_exception(self):
        bad_pk = -1
        data_builder = PageDataBuilder().with_pk(bad_pk)
        try:
            data_builder.build()
            self.fail(f"Expected {BadPkException.__name__}")
        except Exception as error:
            self.assertIsInstance(error, BadPkException)

    def test_given_the_creation_of_page_when_is_empty_title_then_return_empty_value_exception(self):
        empty_title = ""
        data_builder = PageDataBuilder().with_title(empty_title)
        try:
            data_builder.build()
            self.fail(f"Expected {EmptyValueException.__name__}")
        except Exception as error:
            self.assertIsInstance(error, EmptyValueException)

    def test_given_the_creation_of_page_when_is_empty_slug_then_return_empty_value_exception(self):
        empty_slug = ""
        data_builder = PageDataBuilder().with_slug(empty_slug)
        try:
            data_builder.build()
            self.fail(f"Expected {EmptyValueException.__name__}")
        except Exception as error:
            self.assertIsInstance(error, EmptyValueException)

    def test_given_the_creation_of_page_when_is_all_correct_field_then_return_correct_object(self):
        pk = 2
        title = "Example 2"
        description = "Example 2"
        slug = "example-2"
        page = PageDataBuilder().with_pk(pk).with_title(title).with_description(description).with_slug(slug).build()
        self.assertEqual(page.pk, pk)
        self.assertEqual(page.title, title)
        self.assertEqual(page.description, description)
        self.assertEqual(page.slug, slug)
