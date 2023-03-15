from django.test import SimpleTestCase

from domain.main.exceptions.language.empty_abbreviation_exception import EmptyAbbreviationException
from domain.main.exceptions.language.empty_name_exception import EmptyNameException
from domain.main.exceptions.language.it_is_not_capitalized_exception import ItIsNotCapitalizedException
from domain.main.tools.entity.language import Language


class LanguageTestCase(SimpleTestCase):
    def test_name_arrives_empty_then_custom_exception_is_return(self):
        name = ""
        abbreviation = "ES"
        message = "Debes ingresar un nombre correctamente, por favor llena todos los campos!"
        try:
            Language(name, abbreviation)
            self.fail("Espera que el nombre sea un valor vacio!")
        except EmptyNameException as exception:
            self.assertEqual(message, str(exception))

    def test_abbreviation_arrives_empty_then_custom_exception_is_return(self):
        name = "Español"
        abbreviation = ""
        message = "Debes ingresar una abreviación correcta, por favor llena todos los campos!"
        try:
            Language(name, abbreviation)
            self.fail("Espera que la abreviación sea un valor vacio!")
        except EmptyAbbreviationException as exception:
            self.assertEqual(message, str(exception))

    def test_abbreviation_is_not_uppercase_then_it_is_not_capitalized_exception_is_return(self):
        name = "Español"
        abbreviation = "es"
        message = "Este valor debe estar en mayuscula!"
        try:
            Language(name, abbreviation)
            self.fail("Espera que la abreviación no este en mayuscula!")
        except ItIsNotCapitalizedException as exception:
            self.assertEqual(message, str(exception))

    def test_name_and_abbreviation_is_correct_values_then_end_process(self):
        name = "Español"
        abbreviation = "ES"
        language = Language(name, abbreviation)
        self.assertIsNotNone(language)
