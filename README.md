# AI_PROMPT_OPTIMIZER
A Django application designed to take a user's input prompt, optimize it using Cohere's API for improved results, and save the optimized prompt to a database for future reference.

# Features
Prompt Optimization: Leverages Cohere's API to enhance and refine user prompts.  
Database Storage: Saves optimized prompts for future reference and easy access.  
User-Friendly Interface: Provides a simple interface to input prompts and view optimized results.  
# Prerequisites
Python (3.7 or higher)  
Django  
Access to the Cohere API  
pip (Python package manager)  



# Setup Guide    
1. Clone the Repository    
   git clone https://github.com/yourusername/YOUTUBE_VIDEO_SUMMARIZER.git    
cd YOUTUBE_VIDEO_SUMMARIZER     
  
2. Create and Activate a Virtual Environment    
To avoid package conflicts, set up a virtual environment:  

 # Create virtual environment    
python3 -m venv venv   

# Activate virtual environment    
# On macOS/Linux    
source venv/bin/activate    
# On Windows    
venv\Scripts\activate    



  
3. Install Dependencies  
Install required packages from requirements.txt:    
 pip install -r requirements.txt  

  
4. Set Up API Keys  
You will need both the Cohere API key and the YouTube Data API key. Follow these steps:   

Cohere API:  
Go to Cohere's API documentation.  
Sign up and get your API key. 
  


# Add API in the views.py file of the project  

5. Run the Development Server  
Start the Django development server:  
  python manage.py runserver  
