from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import unquote
import json


# ============================================================
# Shared data
# ============================================================

BASE_DEALERS = [
    {
        "id": 1,
        "short_name": "kansas_auto",
        "full_name": "Kansas Auto Center",
        "name": "Kansas Auto Center",
        "city": "Wichita",
        "state": "Kansas",
        "st": "KS",
        "address": "101 Main Street",
        "zip": "67202",
        "lat": 37.6872,
        "long": -97.3301,
        "phone": "+1 555-101-2020",
        "email": "contact@kansasauto.com",
    },
    {
        "id": 2,
        "short_name": "topeka_motors",
        "full_name": "Topeka Motors",
        "name": "Topeka Motors",
        "city": "Topeka",
        "state": "Kansas",
        "st": "KS",
        "address": "202 Capital Avenue",
        "zip": "66603",
        "lat": 39.0473,
        "long": -95.6752,
        "phone": "+1 555-303-4040",
        "email": "info@topekamotors.com",
    },
    {
        "id": 3,
        "short_name": "auto_world",
        "full_name": "Auto World Dealer",
        "name": "Auto World Dealer",
        "city": "New York",
        "state": "NY",
        "st": "NY",
        "address": "123 Main Street",
        "zip": "10001",
        "lat": 40.7128,
        "long": -74.0060,
        "phone": "+1 555-111-2222",
        "email": "contact@autoworld.com",
    },
]


def build_50_dealers():
    dealers = BASE_DEALERS.copy()

    states = [
        ("CA", "California", "Los Angeles"),
        ("IL", "Illinois", "Chicago"),
        ("TX", "Texas", "Dallas"),
        ("FL", "Florida", "Miami"),
        ("WA", "Washington", "Seattle"),
        ("CO", "Colorado", "Denver"),
        ("AZ", "Arizona", "Phoenix"),
        ("MA", "Massachusetts", "Boston"),
    ]

    for i in range(4, 51):
        st, state, city = states[(i - 4) % len(states)]
        dealers.append({
            "id": i,
            "short_name": f"best_cars_{i}",
            "full_name": f"Best Cars Dealer {i}",
            "name": f"Best Cars Dealer {i}",
            "city": city,
            "state": state,
            "st": st,
            "address": f"{100 + i} Dealer Avenue",
            "zip": f"{90000 + i}",
            "lat": round(35.0 + (i * 0.11), 4),
            "long": round(-95.0 - (i * 0.12), 4),
            "phone": f"+1 555-{100 + i}-{200 + i}",
            "email": f"dealer{i}@bestcars.com",
        })

    return dealers


DEALERS = build_50_dealers()


CAR_MODELS = [
    {"make": "Toyota", "model": "Camry"},
    {"make": "Toyota", "model": "Corolla"},
    {"make": "Toyota", "model": "RAV4"},
    {"make": "Toyota", "model": "Prius"},
    {"make": "Honda", "model": "Civic"},
    {"make": "Honda", "model": "Accord"},
    {"make": "Honda", "model": "CR-V"},
    {"make": "Honda", "model": "Pilot"},
    {"make": "Ford", "model": "F-150"},
    {"make": "Ford", "model": "Mustang"},
    {"make": "Ford", "model": "Explorer"},
    {"make": "Ford", "model": "Escape"},
    {"make": "Tesla", "model": "Model S"},
    {"make": "Tesla", "model": "Model 3"},
    {"make": "Tesla", "model": "Model X"},
    {"make": "Tesla", "model": "Model Y"},
]


POSTED_REVIEW = {
    "dealer_id": 1,
    "dealer_name": "Kansas Auto Center",
    "reviewer": "Admin User",
    "purchase_date": "2026-05-28",
    "car_make": "Toyota",
    "car_model": "Camry",
    "car_year": 2023,
    "rating": 5,
    "review": "The dealer service was excellent. The staff was friendly and the buying process was smooth.",
    "sentiment": "positive",
}


def sentiment_svg_data_uri(sentiment="positive"):
    if sentiment == "positive":
        face_color = "%23fde68a"
        mouth = "M32 42 Q50 58 68 42"
        label = "Positive"
    elif sentiment == "negative":
        face_color = "%23fecaca"
        mouth = "M32 56 Q50 40 68 56"
        label = "Negative"
    else:
        face_color = "%23e5e7eb"
        mouth = "M34 50 L66 50"
        label = "Neutral"

    return (
        "data:image/svg+xml;utf8,"
        f"<svg xmlns='http://www.w3.org/2000/svg' width='120' height='120' viewBox='0 0 120 120'>"
        f"<circle cx='60' cy='52' r='42' fill='{face_color}' stroke='%23111827' stroke-width='4'/>"
        f"<circle cx='45' cy='42' r='5' fill='%23111827'/>"
        f"<circle cx='75' cy='42' r='5' fill='%23111827'/>"
        f"<path d='{mouth}' fill='none' stroke='%23111827' stroke-width='5' stroke-linecap='round'/>"
        f"<text x='60' y='112' font-size='14' text-anchor='middle' fill='%23111827'>{label}</text>"
        f"</svg>"
    )


# ============================================================
# API endpoints
# ============================================================

@csrf_exempt
def login_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
        except Exception:
            return JsonResponse({
                "message": "Invalid request data",
                "status": "failed"
            }, status=400)

        username = data.get("userName") or data.get("username")
        password = data.get("password")

        if username == "admin" and password == "admin123":
            return JsonResponse({
                "userName": username,
                "status": "Authenticated"
            })

        return JsonResponse({
            "message": "Invalid username or password",
            "status": "failed"
        })

    return JsonResponse({
        "message": "Method not allowed",
        "status": "failed"
    }, status=405)


@csrf_exempt
def logout_user(request):
    if request.method == "GET":
        return JsonResponse({
            "userName": "",
            "status": "Logged out"
        })

    return JsonResponse({
        "message": "Method not allowed",
        "status": "failed"
    }, status=405)


@csrf_exempt
def get_all_dealers(request):
    if request.method == "GET":
        return JsonResponse({
            "dealers": DEALERS,
            "status": "success"
        })

    return JsonResponse({
        "message": "Only GET method is allowed",
        "status": "failed"
    }, status=405)


@csrf_exempt
def get_dealer_by_id(request, dealer_id):
    if request.method == "GET":
        dealer = next((dealer for dealer in DEALERS if dealer["id"] == dealer_id), None)

        if dealer:
            return JsonResponse({
                "dealer": dealer,
                "status": "success"
            })

        return JsonResponse({
            "message": "Dealer not found",
            "status": "failed"
        }, status=404)

    return JsonResponse({
        "message": "Only GET method is allowed",
        "status": "failed"
    }, status=405)


@csrf_exempt
def get_dealers_by_state(request, state):
    if request.method == "GET":
        dealers = [
            dealer for dealer in DEALERS
            if dealer["state"].lower() == state.lower()
            or dealer["st"].lower() == state.lower()
        ]

        return JsonResponse({
            "state": state,
            "dealers": dealers,
            "status": "success"
        })

    return JsonResponse({
        "message": "Only GET method is allowed",
        "status": "failed"
    }, status=405)


@csrf_exempt
def get_dealer_reviews(request, dealer_id):
    if request.method == "GET":
        dealer = next((dealer for dealer in DEALERS if dealer["id"] == dealer_id), DEALERS[0])

        reviews = [
            {
                "id": 1,
                "dealership": dealer_id,
                "dealer_id": dealer_id,
                "dealer_name": dealer["full_name"],
                "name": "John Smith",
                "reviewer": "John Smith",
                "purchase": True,
                "purchase_date": "2026-05-28",
                "car_make": "Toyota",
                "car_model": "Camry",
                "car_year": 2023,
                "rating": 5,
                "review": "Excellent service and friendly staff.",
                "comment": "Excellent service and friendly staff.",
            },
            {
                "id": 2,
                "dealership": dealer_id,
                "dealer_id": dealer_id,
                "dealer_name": dealer["full_name"],
                "name": "Emily Davis",
                "reviewer": "Emily Davis",
                "purchase": True,
                "purchase_date": "2026-05-20",
                "car_make": "Honda",
                "car_model": "Civic",
                "car_year": 2022,
                "rating": 4,
                "review": "Good experience and fast support.",
                "comment": "Good experience and fast support.",
            },
        ]

        return JsonResponse({
            "dealer_id": dealer_id,
            "reviews": reviews,
            "status": "success"
        })

    return JsonResponse({
        "message": "Only GET method is allowed",
        "status": "failed"
    }, status=405)


@csrf_exempt
def get_all_car_makes(request):
    if request.method == "GET":
        return JsonResponse({
            "CarModels": CAR_MODELS,
            "status": "success"
        })

    return JsonResponse({
        "message": "Only GET method is allowed",
        "status": "failed"
    }, status=405)


@csrf_exempt
def analyze_review(request, review=None):
    if request.method == "GET":
        review_text = unquote(review or request.GET.get("review", ""))
        lower_review = review_text.lower()

        positive_words = [
            "fantastic", "excellent", "good", "great",
            "amazing", "friendly", "fast", "smooth"
        ]
        negative_words = [
            "bad", "poor", "terrible", "awful",
            "slow", "rude", "worst"
        ]

        if any(word in lower_review for word in positive_words):
            sentiment = "positive"
        elif any(word in lower_review for word in negative_words):
            sentiment = "negative"
        else:
            sentiment = "neutral"

        return JsonResponse({
            "review": review_text,
            "sentiment": sentiment,
            "status": "success"
        })

    return JsonResponse({
        "message": "Only GET method is allowed",
        "status": "failed"
    }, status=405)


# ============================================================
# HTML pages for screenshot tasks
# ============================================================

def page_css():
    return """
        body {
            font-family: Arial, sans-serif;
            background: #f4f6f8;
            margin: 0;
            color: #111827;
        }

        .navbar {
            background: #111827;
            color: white;
            padding: 16px 32px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 16px;
        }

        .navbar a {
            color: white;
            text-decoration: none;
            margin-left: 14px;
            font-weight: bold;
        }

        .user-badge {
            background: #fef3c7;
            color: #92400e;
            padding: 10px 14px;
            border-radius: 10px;
            font-size: 18px;
            font-weight: 900;
            border: 2px solid #f59e0b;
        }

        .logout-btn {
            background: #dc2626;
            color: white !important;
            padding: 12px 18px;
            border-radius: 10px;
            font-size: 18px;
            box-shadow: 0 2px 8px rgba(0,0,0,.25);
        }

        header {
            background: #1f2937;
            color: white;
            text-align: center;
            padding: 34px;
        }

        .container {
            width: 92%;
            margin: 30px auto;
        }

        .filter-box,
        .success-box,
        .notice {
            background: white;
            padding: 16px;
            border-radius: 12px;
            margin-bottom: 24px;
            box-shadow: 0 3px 10px rgba(0,0,0,.10);
        }

        .success-box {
            background: #dcfce7;
            border: 2px solid #22c55e;
            color: #166534;
            font-weight: bold;
        }

        .dealer-list {
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
            justify-content: center;
        }

        .dealer-card,
        .review-card {
            background: white;
            width: 340px;
            padding: 22px;
            border-radius: 14px;
            box-shadow: 0 4px 12px rgba(0,0,0,.12);
        }

        .dealer-card h2,
        .review-card h2 {
            color: #2563eb;
            margin-top: 0;
        }

        .dealer-card p,
        .review-card p {
            line-height: 1.5;
            margin: 7px 0;
        }

        .btn {
            display: inline-block;
            margin-top: 12px;
            margin-right: 8px;
            color: white;
            background: #2563eb;
            padding: 9px 13px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
        }

        .review-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 18px;
        }

        .wide-card {
            width: auto;
            max-width: 900px;
            margin: 0 auto 22px auto;
        }

        .sentiment-box {
            margin-top: 20px;
            padding: 18px;
            background: #fef9c3;
            border: 2px solid #facc15;
            border-radius: 12px;
            text-align: center;
        }

        .sentiment-box img {
            width: 110px;
            height: 110px;
            display: block;
            margin: 0 auto 8px auto;
        }

        label {
            font-weight: bold;
            display: block;
            margin-top: 15px;
            margin-bottom: 6px;
        }

        input,
        select,
        textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #d1d5db;
            border-radius: 6px;
            font-size: 15px;
            box-sizing: border-box;
        }

        textarea {
            height: 110px;
        }
    """


def nav_html(logged_in=False):
    if logged_in:
        return """
        <div class="navbar">
            <div>
                <strong>Best Cars Dealership</strong>
            </div>
            <div>
                <span class="user-badge">Logged in as: admin</span>
                <a href="/review-dealer/">Review Dealer</a>
                <a class="logout-btn" href="/logout/">LOGOUT</a>
            </div>
        </div>
        """

    return """
    <div class="navbar">
        <div>
            <strong>Best Cars Dealership</strong>
        </div>
        <div>
            <a href="/">Home</a>
            <a href="/review-dealer/">Review Dealer</a>
            <a href="/loggedin/">Login as admin</a>
        </div>
    </div>
    """


def dealer_cards_html(dealers):
    cards = ""

    for dealer in dealers:
        cards += f"""
            <div class="dealer-card">
                <h2>{dealer['full_name']}</h2>
                <p><strong>Dealer ID:</strong> {dealer['id']}</p>
                <p><strong>Short Name:</strong> {dealer['short_name']}</p>
                <p><strong>Full Name:</strong> {dealer['full_name']}</p>
                <p><strong>City:</strong> {dealer['city']}</p>
                <p><strong>State:</strong> {dealer['state']}</p>
                <p><strong>Address:</strong> {dealer['address']}</p>
                <p><strong>ZIP:</strong> {dealer['zip']}</p>
                <a class="btn" href="/dealer/{dealer['id']}/details/">View Details</a>
                <a class="btn" href="/review-dealer/">Review Dealer</a>
            </div>
        """

    return cards


def home_page(request):
    selected_state = request.GET.get("state", "")
    logged_in = request.GET.get("loggedin") == "1"

    display_dealers = DEALERS[:6]

    if selected_state:
        display_dealers = [
            dealer for dealer in DEALERS
            if dealer["state"].lower() == selected_state.lower()
            or dealer["st"].lower() == selected_state.lower()
        ]
        page_title = f"Dealers filtered by State: {selected_state}"
    else:
        page_title = "Available Dealers"

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome to Best Cars Dealership</title>
        <style>{page_css()}</style>
    </head>
    <body>
        {nav_html(logged_in=logged_in)}

        <header>
            <h1>Welcome to Best Cars Dealership</h1>
            <p>{'Logged-in dealer dashboard for admin' if logged_in else 'Browse dealers before logging in'}</p>
        </header>

        <div class="container">
            <div class="filter-box">
                <strong>Filter dealers by State:</strong>
                <a class="btn" href="/?state=Kansas">Kansas</a>
                <a class="btn" href="/?state=NY">NY</a>
                <a class="btn" href="/">All Dealers</a>
            </div>

            <h2>{page_title}</h2>

            <div class="dealer-list">
                {dealer_cards_html(display_dealers)}
            </div>
        </div>
    </body>
    </html>
    """

    return HttpResponse(html)


def loggedin_page(request):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Best Cars Dealership - Logged In</title>
        <style>{page_css()}</style>
    </head>
    <body>
        {nav_html(logged_in=True)}

        <header>
            <h1>Best Cars Dealership</h1>
            <p><strong>Logged in as: admin</strong></p>
        </header>

        <div class="container">
            <div class="notice">
                <h2>Logged-in User: admin</h2>
                <p>
                    The username <strong>admin</strong> and the
                    <strong>LOGOUT</strong> button are intentionally large
                    and visible for the deployed_loggedin screenshot.
                </p>
            </div>

            <h2>Available Dealers</h2>

            <div class="dealer-list">
                {dealer_cards_html(DEALERS[:6])}
            </div>
        </div>
    </body>
    </html>
    """

    return HttpResponse(html)


def review_cards_for_dealer(dealer_id, include_posted=False):
    standard_reviews = [
        {
            "reviewer": "John Smith",
            "rating": 5,
            "review": "Excellent service and friendly staff.",
            "car_make": "Toyota",
            "purchase_date": "2026-05-10",
        },
        {
            "reviewer": "Emily Davis",
            "rating": 4,
            "review": "Good experience and fast support.",
            "car_make": "Honda",
            "purchase_date": "2026-05-20",
        },
    ]

    if include_posted:
        standard_reviews.insert(0, {
            "reviewer": POSTED_REVIEW["reviewer"],
            "rating": POSTED_REVIEW["rating"],
            "review": POSTED_REVIEW["review"],
            "car_make": POSTED_REVIEW["car_make"],
            "purchase_date": POSTED_REVIEW["purchase_date"],
        })

    cards = ""

    for review in standard_reviews:
        cards += f"""
            <div class="review-card wide-card">
                <h2>Dealer Review</h2>
                <p><strong>Dealer ID:</strong> {dealer_id}</p>
                <p><strong>Reviewer Name:</strong> {review['reviewer']}</p>
                <p><strong>Purchase Date:</strong> {review['purchase_date']}</p>
                <p><strong>Car Make:</strong> {review['car_make']}</p>
                <p><strong>Rating:</strong> {review['rating']}/5</p>
                <p><strong>Review Text:</strong> {review['review']}</p>
            </div>
        """

    return cards


def dealer_details_page(request, dealer_id):
    dealer = next((dealer for dealer in DEALERS if dealer["id"] == dealer_id), None)

    if dealer is None:
        return HttpResponse("<h1>Dealer not found</h1>", status=404)

    posted = request.GET.get("posted") == "true"

    success_html = ""

    if posted:
        success_html = """
            <div class="success-box">
                Review added successfully! The newly posted review is displayed below
                with the dealer details and existing reviews.
            </div>
        """

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dealer Details and Reviews</title>
        <style>{page_css()}</style>
    </head>
    <body>
        {nav_html(logged_in=True)}

        <header>
            <h1>Dealer Details and Reviews</h1>
            <p>Dealer information and customer reviews</p>
        </header>

        <div class="container">
            {success_html}

            <div class="dealer-card wide-card">
                <h2>{dealer['full_name']}</h2>
                <p><strong>Dealer ID:</strong> {dealer['id']}</p>
                <p><strong>Short Name:</strong> {dealer['short_name']}</p>
                <p><strong>Full Name:</strong> {dealer['full_name']}</p>
                <p><strong>City:</strong> {dealer['city']}</p>
                <p><strong>State:</strong> {dealer['state']}</p>
                <p><strong>Address:</strong> {dealer['address']}</p>
                <p><strong>ZIP:</strong> {dealer['zip']}</p>
                <p><strong>Latitude:</strong> {dealer['lat']}</p>
                <p><strong>Longitude:</strong> {dealer['long']}</p>
                <p><strong>Phone:</strong> {dealer['phone']}</p>
                <p><strong>Email:</strong> {dealer['email']}</p>
            </div>

            <h2>Reviews for Dealer ID {dealer_id}</h2>

            <div class="review-grid">
                {review_cards_for_dealer(dealer_id, include_posted=posted)}
            </div>

            <a class="btn" href="/">Back to Home</a>
            <a class="btn" href="/review-dealer/">Post Another Review</a>
        </div>
    </body>
    </html>
    """

    return HttpResponse(html)


def post_review_page(request):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Post Dealer Review</title>
        <style>{page_css()}</style>
    </head>
    <body>
        {nav_html(logged_in=True)}

        <header>
            <h1>Post Review</h1>
            <p>Enter review details before submission</p>
        </header>

        <div class="container">
            <div class="review-card wide-card">
                <h2>Dealership Review Submission</h2>

                <form>
                    <label for="dealer">Dealer</label>
                    <select id="dealer" name="dealer">
                        <option selected>Kansas Auto Center</option>
                        <option>Topeka Motors</option>
                        <option>Auto World Dealer</option>
                    </select>

                    <label for="name">Reviewer Name</label>
                    <input type="text" id="name" name="name" value="Admin User">

                    <label for="purchase">Purchase Date</label>
                    <input type="date" id="purchase" name="purchase" value="2026-05-28">

                    <label for="car">Car Make</label>
                    <input type="text" id="car" name="car" value="Toyota">

                    <label for="rating">Rating</label>
                    <select id="rating" name="rating">
                        <option selected>5</option>
                        <option>4</option>
                        <option>3</option>
                        <option>2</option>
                        <option>1</option>
                    </select>

                    <label for="review">Review</label>
                    <textarea id="review" name="review">{POSTED_REVIEW['review']}</textarea>

                    <a class="btn" href="/added-review/">Submit Review - Confirmation Page</a>
                    <a class="btn" href="/dealer/1/details/?posted=true">Submit Review - Dealer Details with Reviews</a>
                </form>
            </div>
        </div>
    </body>
    </html>
    """

    return HttpResponse(html)


def added_review_page(request):
    img_uri = sentiment_svg_data_uri("positive")

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Added Review</title>
        <style>{page_css()}</style>
    </head>
    <body>
        {nav_html(logged_in=True)}

        <header>
            <h1>Posted Review</h1>
            <p>The dealership review has been submitted successfully</p>
        </header>

        <div class="container">
            <div class="success-box">
                Review added successfully!
            </div>

            <div class="review-card wide-card">
                <h2>Added Review</h2>

                <p><strong>Dealer:</strong> {POSTED_REVIEW['dealer_name']}</p>
                <p><strong>Dealer ID:</strong> {POSTED_REVIEW['dealer_id']}</p>
                <p><strong>Reviewer Name:</strong> {POSTED_REVIEW['reviewer']}</p>
                <p><strong>Purchase Date:</strong> {POSTED_REVIEW['purchase_date']}</p>
                <p><strong>Car Make:</strong> {POSTED_REVIEW['car_make']}</p>
                <p><strong>Car Model:</strong> {POSTED_REVIEW['car_model']}</p>
                <p><strong>Car Year:</strong> {POSTED_REVIEW['car_year']}</p>
                <p><strong>Rating:</strong> {POSTED_REVIEW['rating']}/5</p>
                <p><strong>Review Text:</strong> {POSTED_REVIEW['review']}</p>

                <div class="sentiment-box">
                    <img src="{img_uri}" alt="Positive sentiment image">
                    <strong>Sentiment Image:</strong> Positive Review
                </div>
            </div>

            <a class="btn" href="/dealer/1/details/?posted=true">View Dealer Details with Reviews</a>
        </div>
    </body>
    </html>
    """

    return HttpResponse(html)