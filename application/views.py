from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import fileForm
from .analyzer import analyze_code
import os
from django.core.files.uploadedfile import InMemoryUploadedFile
import tempfile

def analyze_code_view(request):
    if request.method == 'POST':
        python_file = request.FILES.get('python_file')

        # Check if a file was uploaded
        if python_file:
            # Read the content of the uploaded file
            file_content = python_file.read().decode('utf-8')

            # Save the content to a temporary file
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
                temp_file.write(file_content)
                temp_file_path = temp_file.name

            total_loops, nested_loops, if_else_statements = analyze_code(temp_file_path)
            
            results = {
                "total_loops": total_loops,
                "nested_loops": nested_loops,
                "if_else_statements": len(if_else_statements),
            }
            
            request.session['analysis_results'] = results
            return redirect('result')
        else:
            return HttpResponse("No Python file uploaded.")
    else:
        context = {'form': fileForm()}
        return render(request, 'index.html', context=context)



    
# def fileuplaoding(request):
#     if request.method == 'POST':
#         form = fileForm(request.POST, request.FILES)
#         if form.is_valid():
#             uploadedfile = form.save()
#             filecontent = uploadedfile.file.read().decode()
#             analyzer = CodeAnalyzer()
#             tree = ast.parse(filecontent)
#             analyzer.visit(tree)
#             analyzer.handle_nested_loops(tree.body)
#             results = {
#                 "total_loops": analyzer.loop_count,
#                 "nested_loops": analyzer.nested_loop_count,
#                 "if_else_statements": analyzer.if_else_count,
#             }
#             # Save the results in the session so that you can access them in the 'result' view
#             request.session['analysis_results'] = results
#             return redirect('result')  # Redirect to the 'result' view
#         else:
#             context = {'form': form}
#             return render(request, 'index.html', context=context)
    
#     context = {'form': fileForm()}
#     return render(request, 'index.html', context=context)


def result(request):
    # Retrieve the analysis results from the session
    results = request.session.get('analysis_results', None)

    if results is not None:
        # If results are found in the session, render the 'result.html' template with the results
        return render(request, 'result.html', context={"results": results})
    else:
        # If results are not found in the session, you can handle this case as per your requirements
        # For example, you can display an error message or redirect to the home page.
        return HttpResponse("Analysis results not found. Please upload a file first.")
