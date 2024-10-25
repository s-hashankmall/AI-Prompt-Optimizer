from django.db import models

class PromptRating(models.Model):
    original_prompt = models.TextField()
    new_prompt = models.TextField() 
    original_rating = models.IntegerField(null=True, blank=True)
    new_rating = models.IntegerField(null=True, blank=True)
    original_feedback = models.CharField(max_length=10, null=True, blank=True)
    new_feedback = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Original Prompt: {self.original_prompt[:50]}... | New Prompt: {self.new_prompt[:50]}..."