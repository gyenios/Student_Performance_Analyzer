from data_loader import Students
from analytics import compute_all_students

data = Students().data

processed = compute_all_students(data)

print(processed)