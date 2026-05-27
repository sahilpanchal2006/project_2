from django import forms
from .models import Quote


TAILWIND_INPUT_CLASSES = (
    'form-input w-full px-4 py-3 rounded-xl border-2 border-gray-200 '
    'bg-gray-50/50 text-ink-charcoal placeholder-gray-300 '
    'focus:border-squeegee-cyan focus:ring-0 transition-all duration-300'
)

TAILWIND_SELECT_CLASSES = (
    'form-input w-full px-4 py-3 rounded-xl border-2 border-gray-200 '
    'bg-gray-50/50 text-ink-charcoal '
    'focus:border-squeegee-cyan focus:ring-0 transition-all duration-300'
)

TAILWIND_TEXTAREA_CLASSES = (
    'form-input w-full px-4 py-3 rounded-xl border-2 border-gray-200 '
    'bg-gray-50/50 text-ink-charcoal placeholder-gray-300 '
    'focus:border-squeegee-cyan focus:ring-0 transition-all duration-300 resize-none'
)

TAILWIND_FILE_CLASSES = (
    'w-full px-4 py-2 border border-gray-300 rounded-lg '
    'file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 '
    'file:bg-squeegee-cyan file:text-ink-charcoal file:font-bold file:cursor-pointer '
    'hover:file:bg-white hover:file:text-squeegee-cyan transition duration-200 ease-in-out'
)


class QuoteForm(forms.ModelForm):
    """Form for submitting a quote request with Tailwind-styled widgets."""

    class Meta:
        model = Quote
        fields = [
            'client_name',
            'company_email',
            'phone',
            'material_choice',
            'finish_type',
            'design_file',
            'message',
        ]
        widgets = {
            'client_name': forms.TextInput(attrs={
                'class': TAILWIND_INPUT_CLASSES,
                'placeholder': 'Enter your full name',
            }),
            'company_email': forms.EmailInput(attrs={
                'class': TAILWIND_INPUT_CLASSES,
                'placeholder': 'your.email@company.com',
            }),
            'phone': forms.TextInput(attrs={
                'class': TAILWIND_INPUT_CLASSES,
                'placeholder': '+91 XXXXX XXXXX',
            }),
            'material_choice': forms.Select(attrs={
                'class': TAILWIND_SELECT_CLASSES,
            }),
            'finish_type': forms.Select(attrs={
                'class': TAILWIND_SELECT_CLASSES,
            }),
            'design_file': forms.ClearableFileInput(attrs={
                'class': TAILWIND_FILE_CLASSES,
                'accept': '.pdf,.ai,.psd,.png,.jpg,.jpeg',
            }),
            'message': forms.Textarea(attrs={
                'class': TAILWIND_TEXTAREA_CLASSES,
                'placeholder': 'Describe your printing requirements, quantities, sizes, etc.',
                'rows': 5,
            }),
        }
