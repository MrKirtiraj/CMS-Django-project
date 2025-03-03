from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ComplaintForm
from .models import Complaint
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404
from .models import Complaint, Comment

'''
@login_required
def complaint_details(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    comments = Comment.objects.filter(complaint=complaint)
    return render(request, 'complaints/complaint_details.html', {'complaint': complaint, 'comments': comments})

'''
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ComplaintForm
from .models import Complaint
from django.template.loader import get_template

# @login_required
# def file_complaint(request):
#     if request.method == 'POST':
#         form = ComplaintForm(request.POST)
#         if form.is_valid():
#             complaint = form.save(commit=False)
#             complaint.created_by = request.user
#             complaint.save()
#             return redirect('dashboard')
#     else:
#         form = ComplaintForm()

#     # Debug: Check if the template exists
#     try:
#         template = get_template('complaints/file_complaint.html')
#         print("Template found:", template.origin.name)
#     except Exception as e:
#         print("Template not found:", e)

#     return render(request, 'complaints/file_complaint.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ComplaintForm
from .models import Complaint


from django.shortcuts import render, get_object_or_404
from .models import Complaint, Comment

# @login_required
# def complaint_details(request, complaint_id):
#     """
#     View for displaying the details of a specific complaint.
#     """
#     # Fetch the complaint or return a 404 error if not found
#     complaint = get_object_or_404(Complaint, id=complaint_id)
#     # Fetch all comments related to the complaint
#     comments = Comment.objects.filter(complaint=complaint)
#     return render(request, 'complaints/complaint_details.html', {'complaint': complaint, 'comments': comments})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ComplaintForm
from .models import Complaint
from users.models import UserProfile

"""
@login_required
def file_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.created_by = request.user

            # Automatically assign the complaint to a staff member
            # For example, assign it to the first available staff member
            staff_member = UserProfile.objects.filter(role='staff')
            if staff_member:
                complaint.assigned_to = staff_member

            complaint.save()
            return redirect('dashboard')
    else:
        form = ComplaintForm()
    return render(request, 'complaints/file_complaint.html', {'form': form})
"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ComplaintForm
from .models import Complaint
from users.models import UserProfile
from django.contrib import messages

@login_required
def file_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.created_by = request.user

            # Automatically assign the complaint to a staff member
            staff_member = UserProfile.objects.filter(role='staff').first()
            if staff_member:
                complaint.assigned_to = staff_member  # Assign a single UserProfile instance
            else:
                # Handle the case where no staff member is available
                messages.error(request, 'No staff member available to assign the complaint.')
                return redirect('file_complaint')

            complaint.save()
            return redirect('dashboard')
    else:
        form = ComplaintForm()
    return render(request, 'complaints/file_complaint.html', {'form': form})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Complaint, Comment
from .forms import CommentForm

'''
@login_required
def complaint_details(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    comments = Comment.objects.filter(complaint=complaint)

    if request.method == 'POST':
        if request.user.role == 'admin':
            # Update status
            new_status = request.POST.get('status')
            if new_status:
                complaint.status = new_status
                complaint.save()

            # Add comment
            comment_text = request.POST.get('comment')
            if comment_text:
                Comment.objects.create(
                    complaint=complaint,
                    comment=comment_text,
                    commented_by=request.user
                )

            return redirect('complaint_details', complaint_id=complaint.id)
    else:
        form = CommentForm()

    context = {
        'complaint': complaint,
        'comments': comments,
        'form': form,
    }
    return render(request, 'complaints/complaint_details.html', context)
'''


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Complaint, Comment
from .forms import CommentForm
"""
@login_required
def complaint_details(request, complaint_id):
    # Fetch the complaint or return a 404 error if not found
    complaint = get_object_or_404(Complaint, id=complaint_id)
    # Fetch all comments related to the complaint
    comments = Comment.objects.filter(complaint=complaint)

    if request.method == 'POST':
        if request.user.role == 'admin':
            # Update status
            new_status = request.POST.get('status')
            if new_status:
                complaint.status = new_status
                complaint.save()

            # Add comment
            comment_text = request.POST.get('comment')
            if comment_text:
                Comment.objects.create(
                    complaint=complaint,
                    comment=comment_text,
                    commented_by=request.user
                )

            return redirect('complaint_details', complaint_id=complaint.id)
    else:
        form = CommentForm()

    context = {
        'complaint': complaint,
        'comments': comments,
        'form': form,
    }
    return render(request, 'complaints/complaint_details.html', context)
"""
    
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Complaint, Comment
from .forms import CommentForm

@login_required
def complaint_details(request, complaint_id):
    # Fetch the complaint or return a 404 error if not found
    complaint = get_object_or_404(Complaint, id=complaint_id)
    # Fetch all comments related to the complaint
    comments = Comment.objects.filter(complaint=complaint)

    if request.method == 'POST':
        if request.user.role in ['staff','admin']:
            # Update status
            new_status = request.POST.get('status')
            if new_status:
                complaint.status = new_status
                complaint.save()

            # Add comment
            comment_text = request.POST.get('comment')
            if comment_text:
                Comment.objects.create(
                    complaint=complaint,
                    comment=comment_text,
                    commented_by=request.user
                )

            return redirect('complaint_details', complaint_id=complaint.id)
    else:
        form = CommentForm()

    context = {
        'complaint': complaint,
        'comments': comments,
        'form': form,
    }
    return render(request, 'complaints/complaint_details.html', context)