# Custom validation error
class CSVValidationError(Exception):
    pass

# The CSV should have...
class ValidateCSV(object):

    def __init__(self, parsed_data):
        self.columns(parsed_data)
        self.lines(parsed_data)
        self.content(parsed_data)

    # Only two columns (one for the SF key and one for the college name)
    def columns(self, parsed_data):
        for line in parsed_data:
            if len(line) != 2:
                raise CSVValidationError("Incorrect CSV: Number of columns should be 2, atleast one line had {}.".format(len(line)))

    # All lines NOT empty.
    def lines(self, parsed_data):
        for line in parsed_data:
            if not line:
                raise CSVValidationError("Incorrect CSV: File contained empty lines.")

    # Sanity check, should have some data.
    def content(self, parsed_data):
        if not parsed_data:
            raise CSVValidationError("Incorrect CSV: File is empty.")
