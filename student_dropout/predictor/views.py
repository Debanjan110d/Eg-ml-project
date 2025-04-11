from django.shortcuts import render
from .django_predictor import DropoutPredictor

predictor = DropoutPredictor()

def predict_view(request):
    if request.method == 'POST':
        try:
            input_data = {
                'jee_main_score': request.POST.get('jee_main_score'),
                'attendance': request.POST.get('attendance'),
                'cgpa': request.POST.get('cgpa')
            }
            prediction = predictor.predict(input_data)
            return render(request, 'predictor/result.html', {
                'prediction': prediction,
                'input_data': input_data
            })
        except Exception as e:
            return render(request, 'predictor/predict.html', {'error': str(e)})
    return render(request, 'predictor/predict.html')
