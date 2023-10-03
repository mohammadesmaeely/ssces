from rangefilter2.filter import DateRangeFilter


class CustomDateRangeFilter(DateRangeFilter):
    def __init__(self, field, request, params, model, model_admin, field_path):
        setattr(request, 'LANGUAGE_CODE', 'fa')
        super().__init__(field, request, params, model, model_admin, field_path)
