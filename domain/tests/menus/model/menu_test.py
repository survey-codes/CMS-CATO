import unittest

from domain.main.exceptions.empty_pk_exception import BadPkException
from domain.main.exceptions.empty_value_exception import EmptyValueException
from domain.tests.menus.model.databuilder.MenuDataBuilder import MenuDataBuilder


class MenuTest(unittest.TestCase):
    def test_given_the_creation_of_menu_when_is_bad_pk_then_return_bad_pk_exception(self):
        bad_pk: property = -1
        data_builder = MenuDataBuilder().with_pk(bad_pk)
        try:
            data_builder.build()
            self.fail(f"Expected {BadPkException.__name__}")
        except Exception as error:
            self.assertIsInstance(error, BadPkException)

    def test_given_the_creation_of_menu_when_is_empty_name_then_return_empty_value_exception(self):
        empty_name = ""
        data_builder = MenuDataBuilder().with_name(empty_name)
        try:
            data_builder.build()
            self.fail(f"Expected {EmptyValueException.__name__}")
        except Exception as error:
            self.assertIsInstance(error, EmptyValueException)

    def test_given_the_creation_of_menu_when_is_correct_fields_then_return_correct_object(self):
        pk = 2
        name = "About us"
        menu = MenuDataBuilder().with_pk(pk).with_name(name).build()
        self.assertEqual(menu.pk, pk)
        self.assertEqual(menu.name, name)
