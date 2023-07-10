import csv

# Open the input CSV file
with open('school.csv', 'r', encoding='utf-8', errors='replace') as input_file:
    # Create a CSV reader object
    reader = csv.reader(input_file)
    
    # Skip the header row if present
    header = next(reader)  
    
    # Initialize variables
    row_count = 0
    page_count = 1
    output_file = None
    output_writer = None
    
    # Iterate over each row in the input file
    for row in reader:
        # Remove double quotation marks from each value in the row
        row_without_quotes = [value.replace('"', '') for value in row]
        
        # Check if a new page needs to be started
        if row_count % 400 == 0:
            # Close the previous output file if open
            if output_file is not None:
                output_file.close()
            
            # Create a new output CSV file
            output_file = open(f'schoool_{page_count}.csv', 'w', newline='')
            output_writer = csv.writer(output_file)
            
            # Write the header row to the new output file
            output_writer.writerow(header)
            
            # Increment the page count
            page_count += 1
        
        # Write the modified row (without double quotation marks) to the current output file
        output_writer.writerow(row_without_quotes)
        
        # Increment the row count
        row_count += 1
    
    # Close the last output file
    if output_file is not None:
        output_file.close()

print('Separation complete.')
