from django.shortcuts import render, redirect
import cohere
from .models import PromptRating
import re


cohere_client = cohere.Client('your_COHERE_API_KEY')


def home(request):
    if request.method == 'POST':
        original_prompt = request.POST.get('prompt')
        optimized_prompts = generate_optimized_prompts(original_prompt)

        
        optimized_prompts_list = [
            f"{i + 1}. {prompt.strip()}" 
            for i, prompt in enumerate(optimized_prompts) 
            if prompt.strip() 
        ]
        
        return render(request, 'optimize.html', {
            'original_prompt': original_prompt,
            'optimized_prompts': optimized_prompts_list 
        })
    
    return render(request, 'home.html')


def generate_optimized_prompts(original_prompt):
    prompt = (f'''You are a prompt optimizer designed to help users get the best results. Your task is to analyze the prompt and make improvements for clarity, specificity, and effectiveness. Consider the intent of the user and enhance the prompt by adding necessary details, eliminating ambiguity, and ensuring it is concise and well-structured. Generate only three optimized prompts and nothing else for '{original_prompt}'.''')
    
    response = cohere_client.generate(
        model='command-xlarge',
        prompt=prompt,
        max_tokens=10000,
        temperature=0.9
    )

    if hasattr(response, 'generations') and len(response.generations) > 0:
        raw_text = response.generations[0].text.strip()
        
       
        optimized_prompts = re.findall(r'\d+\.\s*(.+?)(?=\n\d+\.\s*|$)', raw_text, re.DOTALL)

       
        if optimized_prompts:
           
            optimized_prompts = optimized_prompts[:3]

        return [prompt.strip() for prompt in optimized_prompts if prompt.strip()] 
    else:
        return [] 


def get_answer(request):
    if request.method == 'POST':
        original_prompt = request.POST.get('original_prompt')
        new_prompt = request.POST.get('optimized_prompt')

        
        if not original_prompt or not new_prompt:
            return render(request, 'result.html', {
                'error': 'Both the original and the new prompt must be filled out.'
            })

       
        original_answer = get_prompt_answer(original_prompt)
        new_answer = get_prompt_answer(new_prompt) 

        
        return render(request, 'result.html', {
            'original_prompt': original_prompt,
            'original_answer': original_answer,
            'new_prompt': new_prompt,
            'new_answer': new_answer
        })

    return redirect('home')


def get_prompt_answer(prompt):
    response = cohere_client.generate(
        model='command-xlarge',
        prompt=prompt,
        max_tokens=10000,
        temperature=0.9
    )
    return response.generations[0].text.strip()

    
def save_ratings(request):
    if request.method == 'POST':
        original_prompt = request.POST.get('original_prompt')
        new_prompt = request.POST.get('new_prompt')

        try:
            original_rating = int(request.POST.get('rating_original'))
            new_rating = int(request.POST.get('rating_new'))

            original_feedback = 'True' if original_rating > 3 else 'False'
            new_feedback = 'True' if new_rating > 3 else 'False'

            rating_entry = PromptRating(
                original_prompt=original_prompt,
                new_prompt=new_prompt,
                original_rating=original_rating,
                new_rating=new_rating,
                original_feedback=original_feedback,
                new_feedback=new_feedback
            )
            rating_entry.save()

           
            return redirect('home') 

        except (ValueError, TypeError):
            return render(request, 'result.html', {
                'error': 'Invalid ratings provided. Please enter valid numbers.'
            })

    return redirect('home')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
