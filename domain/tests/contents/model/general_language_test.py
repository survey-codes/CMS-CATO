from django.test import SimpleTestCase

from domain.main.contents.model.general_language import GeneralDataLanguage
from domain.main.exceptions.general.empty_metadata_exception import EmptyMetadataException


class GeneralLanguageTestCase(SimpleTestCase):
    def test_metadata_arrive_empty_then_empty_metadata_exception_is_return(self):
        footer = "Algo"
        metadata = ""
        menssage = "Debes ingresar metadata correctamente, por favor llena todos los campos!"
        try:
            GeneralDataLanguage(footer, metadata)
            self.fail("Se espera que metadata sea vacio")
        except EmptyMetadataException as error:
            self.assertEqual(menssage, str(error))
