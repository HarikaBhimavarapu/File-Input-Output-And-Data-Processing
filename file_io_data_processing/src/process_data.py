import csv

def read_csv(file_path):
    """Reads data from a CSV file and returns a list of dictionaries."""
    data = []
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def calculate_statistics(data):
    """Calculates statistics from the data."""
    total_age = 0
    total_salary = 0
    num_records = len(data)
    
    for record in data:
        total_age += int(record['Age'])
        total_salary += int(record['Salary'])
    
    average_age = total_age / num_records if num_records > 0 else 0
    average_salary = total_salary / num_records if num_records > 0 else 0
    
    return {
        'average_age': average_age,
        'average_salary': average_salary
    }

def write_csv(file_path, data):
    """Writes the processed data to a new CSV file."""
    headers = ['Statistic', 'Value']
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for key, value in data.items():
            writer.writerow([key, value])

def main():
    # File paths
    input_file = 'data/users.csv'
    output_file = 'results/processed_data.csv'
    
    # Read data
    data = read_csv(input_file)
    
    # Process data
    stats = calculate_statistics(data)
    
    # Write results
    write_csv(output_file, stats)

if __name__ == "__main__":
    main()