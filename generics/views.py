from django.template.loader import render_to_string
from django.views.generic.base import TemplateView


class TableView(TemplateView):
    table_template_name = 'generics/table.html'
    template_name = ''
    table_classes = []
    model = None
    exclude = []
    css_classes = {}

    @property
    def columns(self):
        columns = [column.name for column in self.model._meta.fields]
        return filter(lambda c: c not in self.exclude, columns)


    @property
    def rows(self):
        rows = self.model.objects.all()
        return rows

    def get_context_data(self, **kwargs):
        css_classes_formatted = {}
        for k, v in self.css_classes.iteritems():
            css_classes_formatted[k] = ' '.join(v)
        table = render_to_string(self.table_template_name,
                                 {
                                     'table_classes': ' '.join(self.table_classes),
                                     'rows': self.rows.values_list(*self.columns),
                                     'columns': self.columns,
                                     'css_classes': css_classes_formatted
                                 })
        kwargs['table'] = table
        return super(TableView, self).get_context_data(**kwargs)