from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from textblob import TextBlob
from .models import Mood


# -----------------------------------------
# AI Journal Sentiment Analysis
# -----------------------------------------

def analyze_journal(text):
    analysis = TextBlob(text)

    polarity = analysis.sentiment.polarity

    if polarity > 0.2:
        sentiment = "Positive"
        stress = "Low"

    elif polarity < -0.2:
        sentiment = "Negative"
        stress = "High"

    else:
        sentiment = "Neutral"
        stress = "Medium"

    return sentiment, stress


# -----------------------------------------
# Home / Mood Selection
# -----------------------------------------

def home(request):

    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':

        mood = request.POST.get('mood')

        return render(
            request,
            'core/journal.html',
            {
                'mood': mood
            }
        )

    return render(
        request,
        'core/home.html'
    )


# -----------------------------------------
# Journal
# -----------------------------------------

def journal(request):

    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':

        mood = request.POST.get('mood')
        journal_text = request.POST.get('journal')

        # AI sentiment analysis
        sentiment, stress = analyze_journal(journal_text)

        # Save mood + journal + AI results
        Mood.objects.create(
            user=request.user,
            mood=mood,
            journal=journal_text,
            sentiment=sentiment,
            stress_level=stress
        )

        return render(
            request,
            'core/saved.html',
            {
                'mood': mood,
                'sentiment': sentiment,
                'stress': stress
            }
        )

    mood = request.GET.get('mood')

    return render(
        request,
        'core/journal.html',
        {
            'mood': mood
        }
    )


# -----------------------------------------
# User Registration
# -----------------------------------------

def register_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():

            return render(
                request,
                'core/register.html',
                {
                    'error': 'Username already exists'
                }
            )

        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)

        return redirect('home')

    return render(
        request,
        'core/register.html'
    )


# -----------------------------------------
# User Login
# -----------------------------------------

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('home')

        return render(
            request,
            'core/login.html',
            {
                'error': 'Invalid username or password'
            }
        )

    return render(
        request,
        'core/login.html'
    )


# -----------------------------------------
# Logout
# -----------------------------------------

def logout_view(request):

    logout(request)

    return redirect('login')


# -----------------------------------------
# Profile
# -----------------------------------------

def profile(request):

    if not request.user.is_authenticated:
        return redirect('login')

    return render(
        request,
        'core/profile.html'
    )


# -----------------------------------------
# Dashboard
# -----------------------------------------

def dashboard(request):

    if not request.user.is_authenticated:
        return redirect('login')

    moods = Mood.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'core/dashboard.html',
        {
            'moods': moods
        }
    )


# -----------------------------------------
# Mood History
# -----------------------------------------

def mood_history(request):

    if not request.user.is_authenticated:
        return redirect('login')

    moods = Mood.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'core/mood_history.html',
        {
            'moods': moods
        }
    )


# -----------------------------------------
# AI Wellness Analysis
# -----------------------------------------

def wellness_analysis(request):

    if not request.user.is_authenticated:
        return redirect('login')

    moods = Mood.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'core/wellness_analysis.html',
        {
            'moods': moods
        }
    )


# -----------------------------------------
# Wellness Activities
# -----------------------------------------

def wellness_activities(request):

    if not request.user.is_authenticated:
        return redirect('login')

    activities = [
        "🧘 Deep Breathing Exercise",
        "🚶 Take a Short Walk",
        "🎵 Listen to Your Favorite Music",
        "💧 Drink Enough Water",
        "📝 Write in Your Journal",
        "😴 Take Some Time to Relax",
    ]

    return render(
        request,
        'core/wellness_activities.html',
        {
            'activities': activities
        }
    )