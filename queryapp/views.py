# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.views.decorators.csrf import csrf_exempt
# from .utils import query_model 
# from rest_framework.permissions import IsAuthenticated
# from django.shortcuts import render

# def email_intent_view(request):
#     return render(request, "email_intent.html")


# class EmailIntentView(APIView):
#     # permission_classes = [IsAuthenticated]
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

#     @csrf_exempt
#     def post(self, request, *args, **kwargs):
#         context = request.data.get('context')
#         query = request.data.get('query')
#         if not context or not query:
#             return Response({"error": "Invalid input"}, status=400)

#         try:
#             response = query_model(context, query)  # Use the query_model function
#             return Response({"response": response})
#         except Exception as e:
#             return Response({"error": str(e)}, status=500)


from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .utils import query_model 
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

def email_intent_view(request):
    # Render an empty form or a template
    return render(request, "email_intent.html")

class EmailIntentView(APIView):
    # permission_classes = [IsAuthenticated]  # Uncomment if authentication is needed

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        context = request.data.get('context')  # Only get context now
        if not context:
            return Response({"error": "Context is required"}, status=400)

        try:
            responses = query_model(context)  # Call query_model with just context
            return Response({"responses": responses})  # Return responses for predefined queries
        except Exception as e:
            return Response({"error": str(e)}, status=500)
