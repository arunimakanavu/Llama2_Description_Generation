import csv
import ollama
import time

def generate_description(l2,l3):
    """Generate a concise, engaging, and informative description within two lines."""
    prompt = f"""Generate a professional, industry-specific description for the subcategory: {l3}, refering to the maincategory {l2}. 
    The description should be **concise (2 lines max, under 200 characters)** and easy to understand."""
    
    try:
        response = ollama.chat(model='llama2', messages=[{"role": "user", "content": prompt}])
        return response['message']['content']
    except Exception as e:
        print(f"Error generating description for {l3}: {e}")
        return "Error generating description"

def process_csv(input_file, output_file):
    """Reads L3 categories from a CSV file and generates descriptions using Llama2 model."""
    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames + ['Description']
        
        rows = []
        for row in reader:
            l2 = row['L2']
            l3 = row['L3']
            print(f"Generating description for: {l2,l3}")
            row['Description'] = generate_description(l2,l3)
            rows.append(row)
            time.sleep(1)  # To avoid rate limits
        
    with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Descriptions saved to {output_file}")

if __name__ == "__main__":
    input_csv = "categories.csv"  # Input CSV file with 'L3' column
    output_csv = "l3_descriptions_batch-6.csv"  # Output CSV with descriptionsde
    process_csv(input_csv, output_csv)
