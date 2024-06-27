from flask import Blueprint, request, render_template

main_views = Blueprint('main', __name__)


total_survey = [
    {   'id': 1,
        'survey_name': 'Policy One',
        'video_src': '127.0.0.1:9000/static/videos/sample1.mp4',
        'survey_content' : [
            {'id': 1, 'question': 'What did you see there?', 'type': 'radio', 'options': ['Pen', 'Pencil', 'eraser']},
            {'id': 2, 'question': 'Are you sure about it?', 'type': 'radio', 'options': ['Yes', 'No', 'Maybe']},
        ]
    },
    {   'id' : 2,
        'survey_name': 'Policy Two',
        'video_src': '127.0.0.1:9000/static/videos/sample2.mp4',
        'survey_content' : [
            {'id': 1, 'question': 'What did you see there?', 'type': 'radio', 'options': ['Pen', 'Pencil', 'eraser']},
            {'id': 2, 'question': 'Are you sure about it?', 'type': 'radio', 'options': ['Yes', 'No', 'Maybe']},
        ]
    },

]

# Create routes on this blueprint instance
@main_views.get("/", strict_slashes=False)
def index():
    # Define application logic for homepage
    return render_template('home.html', surveys = total_survey)


@main_views.get("/profile/<string:username>", strict_slashes=False)
def profile(username):
    # Define application logic for profile page
    return f"<h1>Welcome {username}! This is your profile</h1>"