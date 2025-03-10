import os
from pdf_resumo_app.crew import ResumidorPdfs

def pdf_path_searcher(folder_path):
    inputs = []
    folder_path = os.path.abspath(folder_path)  

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"): 
            file_path = os.path.abspath(os.path.join(folder_path, filename))  
            inputs.append(file_path)
    
    return inputs

def run():
    # script_dir = os.path.dirname(os.path.abspath(__file__))
    relative_path_to_pdfs = "../data/pdfs"

    # Ensure output directory exists
    # os.makedirs(output_dir, exist_ok=True)

    pdf_files_path = pdf_path_searcher(relative_path_to_pdfs)
    
    try:
        for pdf_file_path in pdf_files_path:
            print(f"\n📄 Processing: {pdf_file_path}")

            # Start the workflow
            try:
                # Todo: Usar caminho Relativo
                # Extract file name without extension
                file_name = os.path.splitext(os.path.basename(pdf_file_path))[0]

                print(type(file_name))

                print(f"🚀 DEBUG - Tipo de pdf_file: {type(pdf_file_path)}, Valor: {pdf_file_path} \n File name: {file_name}")

                inputs = {"pdf_path": pdf_file_path, "file_name": file_name}
                
                print(f"📄 Inputs: {inputs}")

                result = ResumidorPdfs().crew().kickoff(inputs=inputs)

            except Exception as e:
                print(f"❌ Error processing {pdf_file_path}: {e}")
                continue

    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")