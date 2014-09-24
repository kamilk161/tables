from example.models import Contact
from generics.views import TableView


class ExampleView(TableView):
    template_name = 'base.html'
    table_classes = ['table', 'table-bordered']
    model = Contact
    exclude = ['id']
    css_classes = {
        'first_name': ['test']
    }
