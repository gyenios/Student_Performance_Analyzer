import csv

class csvFile:
    def __init__(self):
        self.data = {}

    def _get_int(self, row, *keys):
        for key in keys:
            value = row.get(key)
            if value is not None:
                return int(value or 0)
        return 0
        
    def load_data(self, fileName):
        try:
            with open(fileName, mode = 'r') as file:
                fileContent = csv.DictReader(file)
                for row in fileContent:
                    if row['Student_ID']:
                        student_ID = row['Student_ID'] 
                    else:
                        continue
                    
                    Name =  row['Name'] or 'Unknown' # Name is set to Unknown if it is blank
                    
                    Scores = {
                     'Programming': self._get_int(row, 'Programming'), # or 0 fills in for missing values
                     'Hardware': self._get_int(row, 'Hardware', 'Hardware Assembly'),
                     'Calculus': self._get_int(row, 'Calculus'),
                     'Electronics': self._get_int(row, 'Electronics'),
                     'Semiconductor Devices': self._get_int(row, 'Semiconductor Devices')
                     }
                    
                    if student_ID in self.data:
                        print(f'Student with ID: {student_ID} already exists')
                        continue
                    
                    self.data[student_ID] = {'name': Name, 'Scores': Scores}
                return self.data # returns dictionary with student details
        except FileNotFoundError:
            print('File not found')
            return None
        except Exception as e:
            print('An unexpected error occured: ', e)
            return None
            
class Students:
    def __init__(self, filename = 'students_dataset.csv'):
        self.data = csvFile().load_data(filename) or {} # if load_data returns None self.data will be {}
        
