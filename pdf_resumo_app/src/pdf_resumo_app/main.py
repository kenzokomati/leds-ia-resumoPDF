import os
from pdf_resumo_app.crew import ResumidorPdfs

def pdf_path_searcher(folder_path):
    # Function to retrieve all .pdf files from a given directory
    inputs = []
    folder_path = os.path.abspath(folder_path)  

    for filename in os.listdir(folder_path):
        # If the file has a .pdf extension, add to inputs list
        if filename.lower().endswith(".pdf"): 
            file_path = os.path.abspath(os.path.join(folder_path, filename))  
            inputs.append(file_path)
    
    return inputs

def run():
    relative_path_to_pdfs = "../data/pdfs"
    os.makedirs(relative_path_to_pdfs, exist_ok=True)  # Ensure directory exists
    
    pdf_files_path = pdf_path_searcher(relative_path_to_pdfs)
    # output_dir = os.path.abspath("C:\Users\Erick (DEX)\Documents\GitHub\leds-ia-resumoPDF\data\outputs")  # Absolute path to outputs
    # os.makedirs(output_dir, exist_ok=True)  # Ensure directory exists
    
    try:
        for pdf_file_path in pdf_files_path:
            print(f"\n📄 Processing: {pdf_file_path}")

            # Start the workflow
            try:
                
                # Extract file name without extension
                file_name = os.path.splitext(os.path.basename(pdf_file_path))[0]

                print(f"🚀 DEBUG - Tipo de pdf_file: {type(pdf_file_path)}, Valor: {pdf_file_path} \n File name: {file_name}")

                inputs = {"pdf_path": pdf_file_path, "file_name": file_name}
                
                print(f"📄 Inputs: {inputs}")

                result = ResumidorPdfs().crew().kickoff(inputs=inputs)

            except Exception as e:
                print(f"❌ Error processing {pdf_file_path}: {e}")
                continue

    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")