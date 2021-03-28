
########
queryset
########

.. py:function:: get_queryset(self, request)

Esta función sobreescribe el queryset del padre el cual es un objeto de tipo Page_

.. code-block::

 def get_queryset(self, request):
        queryset = super(__class__, self).get_queryset(request)
        #Page.objects.annotate(section_count=Count('section'))
        return queryset.annotate(section_count=Count('section'))

..


Y desde aquí accedemos a :ref:`Section`

.. py:class:: PageLanguage(LanguageAbstract)

Esta clase contiene los campos traducibles del modelo Page_

    :LaguageAbstract: Hereda de esta clase la cual contiene una foránea a Language

