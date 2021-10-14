from django.test import SimpleTestCase

from domain.entity.general_language import GeneralLanguage
from domain.exceptions.general.empty_metadata_exception import EmptyMetadataException


class GeneralLanguageTestCase(SimpleTestCase):
    def test_metadata_arrive_empty_then_empty_metadata_exception_is_return(self):
        footer = "Algo"
        metadata = ""
        menssage = "Debes ingresar metadata correctamente, por favor llena todos los campos!"
        try:
            GeneralLanguage(footer, metadata)
            self.fail("Se espera que metadata sea vacio")
        except EmptyMetadataException as error:
            self.assertEqual(menssage, str(error))