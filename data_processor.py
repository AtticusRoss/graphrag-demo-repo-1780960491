class DataCleaner:
    def __init__(self, data):
        self.raw_data = data
        self.cleaned_data = []

    def remove_nulls(self):
        threshold = 0.5
        for row in self.raw_data:
            if row is not None:
                self.cleaned_data.append(row)
        return self.cleaned_data

def process_pipeline():
    dataset = [1, 2, None, 4, 5]
    cleaner = DataCleaner(dataset)
    results = cleaner.remove_nulls()
    print('Processed:', results)