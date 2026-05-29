from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

@csrf_exempt
def login_user(request):
    if request.method == "POST":
        data = json.loads(request.body)

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
    })

@csrf_exempt
def logout_user(request):
    if request.method == "POST":
        return JsonResponse({
            "message": "Logout successful",
            "status": "success"
        })

    return JsonResponse({
        "message": "Only POST method is allowed"
    }, status=405)

@csrf_exempt
def get_dealer_reviews(request, dealer_id):
    if request.method == "GET":
        reviews = [
            {
                "dealer_id": dealer_id,
                "reviewer": "John Smith",
                "rating": 5,
                "comment": "Excellent service and friendly staff."
            },
            {
                "dealer_id": dealer_id,
                "reviewer": "Emily Davis",
                "rating": 4,
                "comment": "Good experience and fast support."
            }
        ]

        return JsonResponse({
            "dealer_id": dealer_id,
            "reviews": reviews,
            "status": "success"
        })

    return JsonResponse({
        "message": "Only GET method is allowed"
    }, status=405)

@csrf_exempt
def get_all_dealers(request):
    if request.method == "GET":
        dealers = [
            {
                "id": 1,
                "name": "Auto World Dealer",
                "city": "New York",
                "state": "NY",
                "address": "123 Main Street",
                "zip": "10001"
            },
            {
                "id": 2,
                "name": "Best Cars Center",
                "city": "Los Angeles",
                "state": "CA",
                "address": "456 Sunset Boulevard",
                "zip": "90001"
            },
            {
                "id": 3,
                "name": "Premium Motors",
                "city": "Chicago",
                "state": "IL",
                "address": "789 Lake Shore Drive",
                "zip": "60601"
            }
        ]

        return JsonResponse({
            "dealers": dealers,
            "status": "success"
        })

    return JsonResponse({
        "message": "Only GET method is allowed"
    }, status=405)

@csrf_exempt
def get_dealer_by_id(request, dealer_id):
    if request.method == "GET":
        dealers = {
            1: {
                "id": 1,
                "name": "Auto World Dealer",
                "city": "New York",
                "state": "NY",
                "address": "123 Main Street",
                "zip": "10001",
                "phone": "+1 555-111-2222",
                "email": "contact@autoworld.com"
            },
            2: {
                "id": 2,
                "name": "Best Cars Center",
                "city": "Los Angeles",
                "state": "CA",
                "address": "456 Sunset Boulevard",
                "zip": "90001",
                "phone": "+1 555-333-4444",
                "email": "info@bestcars.com"
            },
            3: {
                "id": 3,
                "name": "Premium Motors",
                "city": "Chicago",
                "state": "IL",
                "address": "789 Lake Shore Drive",
                "zip": "60601",
                "phone": "+1 555-555-6666",
                "email": "support@premiummotors.com"
            }
        }

        dealer = dealers.get(dealer_id)

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
        "message": "Only GET method is allowed"
    }, status=405)

@csrf_exempt
def get_dealers_by_state(request, state):
    if request.method == "GET":
        all_dealers = [
            {
                "id": 1,
                "name": "Kansas Auto Center",
                "city": "Wichita",
                "state": "Kansas",
                "address": "101 Main Street",
                "zip": "67202",
                "phone": "+1 555-101-2020"
            },
            {
                "id": 2,
                "name": "Topeka Motors",
                "city": "Topeka",
                "state": "Kansas",
                "address": "202 Capital Avenue",
                "zip": "66603",
                "phone": "+1 555-303-4040"
            },
            {
                "id": 3,
                "name": "Auto World Dealer",
                "city": "New York",
                "state": "NY",
                "address": "123 Main Street",
                "zip": "10001",
                "phone": "+1 555-111-2222"
            }
        ]

        dealers = [
            dealer for dealer in all_dealers
            if dealer["state"].lower() == state.lower()
        ]

        return JsonResponse({
            "state": state,
            "dealers": dealers,
            "status": "success"
        })

    return JsonResponse({
        "message": "Only GET method is allowed"
    }, status=405)

@csrf_exempt
def get_all_car_makes(request):
    if request.method == "GET":
        car_makes = [
            {
                "make": "Toyota",
                "models": ["Camry", "Corolla", "RAV4", "Prius"]
            },
            {
                "make": "Honda",
                "models": ["Civic", "Accord", "CR-V", "Pilot"]
            },
            {
                "make": "Ford",
                "models": ["F-150", "Mustang", "Explorer", "Escape"]
            },
            {
                "make": "Tesla",
                "models": ["Model S", "Model 3", "Model X", "Model Y"]
            }
        ]

        return JsonResponse({
            "car_makes": car_makes,
            "status": "success"
        })

    return JsonResponse({
        "message": "Only GET method is allowed"
    }, status=405)

@csrf_exempt
def analyze_review(request):
    if request.method == "POST":
        import json

        try:
            data = json.loads(request.body)
            review_text = data.get("review", "")

            positive_words = ["fantastic", "excellent", "good", "great", "amazing", "friendly", "fast"]

            if any(word in review_text.lower() for word in positive_words):
                sentiment = "positive"
            else:
                sentiment = "neutral"

            return JsonResponse({
                "review": review_text,
                "sentiment": sentiment,
                "status": "success"
            })

        except Exception as e:
            return JsonResponse({
                "message": "Invalid request data",
                "status": "failed"
            }, status=400)

    return JsonResponse({
        "message": "Only POST method is allowed"
    }, status=405)

def home_page(request):
    username = "admin"
    selected_state = request.GET.get("state", "")

    all_dealers = [
        {
            "name": "Kansas Auto Center",
            "city": "Wichita",
            "state": "Kansas",
            "address": "101 Main Street",
            "phone": "+1 555-101-2020"
        },
        {
            "name": "Topeka Motors",
            "city": "Topeka",
            "state": "Kansas",
            "address": "202 Capital Avenue",
            "phone": "+1 555-303-4040"
        },
        {
            "name": "Auto World Dealer",
            "city": "New York",
            "state": "NY",
            "address": "123 Main Street",
            "phone": "+1 555-111-2222"
        }
    ]

    if selected_state:
        dealers = [
            dealer for dealer in all_dealers
            if dealer["state"].lower() == selected_state.lower()
        ]
        page_title = f"Dealers filtered by State: {selected_state}"
    else:
        dealers = all_dealers
        page_title = "Available Dealers"

    dealer_cards = ""
    for dealer in dealers:
        dealer_cards += f"""
            <div class="dealer-card">
                <h2>{dealer["name"]}</h2>
                <p><strong>City:</strong> {dealer["city"]}</p>
                <p><strong>State:</strong> {dealer["state"]}</p>
                <p><strong>Address:</strong> {dealer["address"]}</p>
                <p><strong>Phone:</strong> {dealer["phone"]}</p>
                <a href="/review-dealer/">Review Dealer</a>
            </div>
        """

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dealers by State</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f6f8;
                margin: 0;
                padding: 0;
            }}

            .navbar {{
                background-color: #111827;
                color: white;
                padding: 15px 30px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }}

            .navbar a {{
                color: white;
                text-decoration: none;
                margin-left: 20px;
                font-weight: bold;
            }}

            .review-btn {{
                background-color: #2563eb;
                padding: 8px 14px;
                border-radius: 6px;
            }}

            header {{
                background-color: #1f2937;
                color: white;
                text-align: center;
                padding: 30px;
            }}

            .container {{
                width: 90%;
                margin: 30px auto;
            }}

            .filter-box {{
                background: white;
                padding: 15px;
                border-radius: 10px;
                margin-bottom: 25px;
                box-shadow: 0 3px 10px rgba(0,0,0,0.1);
            }}

            .filter-box a {{
                display: inline-block;
                margin-right: 10px;
                padding: 8px 12px;
                background-color: #2563eb;
                color: white;
                border-radius: 6px;
                text-decoration: none;
                font-weight: bold;
            }}

            .dealer-list {{
                display: flex;
                gap: 20px;
                flex-wrap: wrap;
                justify-content: center;
            }}

            .dealer-card {{
                background-color: white;
                width: 300px;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.12);
            }}

            .dealer-card h2 {{
                color: #2563eb;
                margin-top: 0;
            }}

            .dealer-card p {{
                color: #374151;
                line-height: 1.5;
            }}

            .dealer-card a {{
                display: inline-block;
                margin-top: 10px;
                color: white;
                background-color: #2563eb;
                padding: 8px 12px;
                border-radius: 6px;
                text-decoration: none;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="navbar">
            <div>
                <strong>Best Cars Dealership</strong>
            </div>
            <div>
                <span>Logged in as: <strong>{username}</strong></span>
                <a href="/review-dealer/" class="review-btn">Review Dealer</a>
                <a href="/logout/">Logout</a>
            </div>
        </div>

        <header>
            <h1>Welcome to Best Cars Dealership</h1>
            <p>Dealers filtered by State on the home page</p>
        </header>

        <div class="container">
            <div class="filter-box">
                <strong>Filter dealers by State:</strong>
                <a href="/?state=Kansas">Kansas</a>
                <a href="/?state=NY">NY</a>
                <a href="/">All Dealers</a>
            </div>

            <h2>{page_title}</h2>

            <div class="dealer-list">
                {dealer_cards}
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)

def dealer_details_page(request, dealer_id):
    dealers = {
        1: {
            "id": 1,
            "name": "Kansas Auto Center",
            "city": "Wichita",
            "state": "Kansas",
            "address": "101 Main Street",
            "zip": "67202",
            "phone": "+1 555-101-2020",
            "email": "contact@kansasauto.com"
        },
        2: {
            "id": 2,
            "name": "Topeka Motors",
            "city": "Topeka",
            "state": "Kansas",
            "address": "202 Capital Avenue",
            "zip": "66603",
            "phone": "+1 555-303-4040",
            "email": "info@topekamotors.com"
        },
        3: {
            "id": 3,
            "name": "Auto World Dealer",
            "city": "New York",
            "state": "NY",
            "address": "123 Main Street",
            "zip": "10001",
            "phone": "+1 555-111-2222",
            "email": "contact@autoworld.com"
        }
    }

    reviews = [
        {
            "reviewer": "John Smith",
            "rating": 5,
            "comment": "Excellent service and friendly staff."
        },
        {
            "reviewer": "Emily Davis",
            "rating": 4,
            "comment": "Good experience and fast support."
        },
        {
            "reviewer": "Michael Brown",
            "rating": 5,
            "comment": "The dealer was helpful and the buying process was smooth."
        }
    ]

    dealer = dealers.get(dealer_id)

    if dealer is None:
        return HttpResponse("<h1>Dealer not found</h1>", status=404)

    review_cards = ""
    for review in reviews:
        review_cards += f"""
            <div class="review-card">
                <h3>{review["reviewer"]}</h3>
                <p><strong>Rating:</strong> {review["rating"]}/5</p>
                <p>{review["comment"]}</p>
            </div>
        """

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dealer Details and Reviews</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f6f8;
                margin: 0;
                padding: 0;
            }}

            .navbar {{
                background-color: #111827;
                color: white;
                padding: 15px 30px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }}

            .navbar a {{
                color: white;
                text-decoration: none;
                margin-left: 20px;
                font-weight: bold;
            }}

            header {{
                background-color: #1f2937;
                color: white;
                text-align: center;
                padding: 30px;
            }}

            .container {{
                width: 85%;
                margin: 30px auto;
            }}

            .dealer-card, .review-card {{
                background-color: white;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.12);
                margin-bottom: 20px;
            }}

            .dealer-card h2 {{
                color: #2563eb;
                margin-top: 0;
            }}

            .review-card h3 {{
                color: #111827;
                margin-top: 0;
            }}

            .back-link {{
                display: inline-block;
                margin-top: 10px;
                background-color: #2563eb;
                color: white;
                padding: 8px 12px;
                border-radius: 6px;
                text-decoration: none;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="navbar">
            <div>
                <strong>Best Cars Dealership</strong>
            </div>
            <div>
                <span>Logged in as: <strong>admin</strong></span>
                <a href="/">Home</a>
                <a href="/review-dealer/">Review Dealer</a>
            </div>
        </div>

        <header>
            <h1>Selected Dealer Details</h1>
            <p>Dealer information and customer reviews</p>
        </header>

        <div class="container">
            <div class="dealer-card">
                <h2>{dealer["name"]}</h2>
                <p><strong>Dealer ID:</strong> {dealer["id"]}</p>
                <p><strong>City:</strong> {dealer["city"]}</p>
                <p><strong>State:</strong> {dealer["state"]}</p>
                <p><strong>Address:</strong> {dealer["address"]}</p>
                <p><strong>Zip:</strong> {dealer["zip"]}</p>
                <p><strong>Phone:</strong> {dealer["phone"]}</p>
                <p><strong>Email:</strong> {dealer["email"]}</p>
            </div>

            <h2>Reviews for Dealer ID {dealer_id}</h2>

            {review_cards}

            <a class="back-link" href="/">Back to Home</a>
        </div>
    </body>
    </html>
    """

    return HttpResponse(html)

def post_review_page(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Post Dealer Review</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f6f8;
                margin: 0;
                padding: 0;
            }

            .navbar {
                background-color: #111827;
                color: white;
                padding: 15px 30px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }

            .navbar a {
                color: white;
                text-decoration: none;
                margin-left: 20px;
                font-weight: bold;
            }

            header {
                background-color: #1f2937;
                color: white;
                text-align: center;
                padding: 30px;
            }

            .container {
                width: 60%;
                margin: 30px auto;
                background-color: white;
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.12);
            }

            label {
                font-weight: bold;
                display: block;
                margin-top: 15px;
                margin-bottom: 6px;
            }

            input, select, textarea {
                width: 100%;
                padding: 10px;
                border: 1px solid #d1d5db;
                border-radius: 6px;
                font-size: 15px;
            }

            textarea {
                height: 110px;
            }

            button {
                margin-top: 20px;
                background-color: #2563eb;
                color: white;
                padding: 10px 16px;
                border: none;
                border-radius: 6px;
                font-weight: bold;
                cursor: pointer;
            }

            .note {
                color: #374151;
                margin-bottom: 20px;
            }
        </style>
    </head>
    <body>
        <div class="navbar">
            <div>
                <strong>Best Cars Dealership</strong>
            </div>
            <div>
                <span>Logged in as: <strong>admin</strong></span>
                <a href="/">Home</a>
                <a href="/dealer/1/details/">Dealer Details</a>
            </div>
        </div>

        <header>
            <h1>Post Review</h1>
            <p>Enter review details before submission</p>
        </header>

        <div class="container">
            <h2>Dealership Review Submission</h2>
            <p class="note">The review details have been entered, but the form has not been submitted yet.</p>

            <form action="/review-dealer/" method="post">
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
                <textarea id="review" name="review">The dealer service was excellent. The staff was friendly and the buying process was smooth.</textarea>

                <a href="/added-review/" style="display:inline-block; margin-top:20px; background-color:#2563eb; color:white; padding:10px 16px; border-radius:6px; text-decoration:none; font-weight:bold;">Submit Review</a>
            </form>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)

def added_review_page(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Added Review</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f6f8;
                margin: 0;
                padding: 0;
            }

            .navbar {
                background-color: #111827;
                color: white;
                padding: 15px 30px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }

            .navbar a {
                color: white;
                text-decoration: none;
                margin-left: 20px;
                font-weight: bold;
            }

            header {
                background-color: #1f2937;
                color: white;
                text-align: center;
                padding: 30px;
            }

            .container {
                width: 70%;
                margin: 30px auto;
            }

            .success-box {
                background-color: #dcfce7;
                border: 1px solid #22c55e;
                color: #166534;
                padding: 15px;
                border-radius: 10px;
                margin-bottom: 25px;
                font-weight: bold;
            }

            .review-card {
                background-color: white;
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.12);
            }

            .review-card h2 {
                color: #2563eb;
                margin-top: 0;
            }

            .review-card p {
                line-height: 1.6;
                color: #374151;
            }

            .back-link {
                display: inline-block;
                margin-top: 20px;
                background-color: #2563eb;
                color: white;
                padding: 9px 14px;
                border-radius: 6px;
                text-decoration: none;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="navbar">
            <div>
                <strong>Best Cars Dealership</strong>
            </div>
            <div>
                <span>Logged in as: <strong>admin</strong></span>
                <a href="/">Home</a>
                <a href="/dealer/1/details/">Dealer Details</a>
                <a href="/review-dealer/">Post Review</a>
            </div>
        </div>

        <header>
            <h1>Posted Review</h1>
            <p>The dealership review has been submitted successfully</p>
        </header>

        <div class="container">
            <div class="success-box">
                Review added successfully!
            </div>

            <div class="review-card">
                <h2>Added Review</h2>

                <p><strong>Dealer:</strong> Kansas Auto Center</p>
                <p><strong>Dealer ID:</strong> 1</p>
                <p><strong>Reviewer Name:</strong> Admin User</p>
                <p><strong>Purchase Date:</strong> 2026-05-28</p>
                <p><strong>Car Make:</strong> Toyota</p>
                <p><strong>Rating:</strong> 5/5</p>
                <p><strong>Review:</strong> The dealer service was excellent. The staff was friendly and the buying process was smooth.</p>
            </div>

            <a class="back-link" href="/dealer/1/details/">Back to Dealer Details</a>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)