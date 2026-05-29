from django.contrib import admin
from django.urls import path

from .views import (
    home_page,
    login_user,
    logout_user,
    get_dealer_reviews,
    get_all_dealers,
    get_dealer_by_id,
    get_dealers_by_state,
    get_all_car_makes,
    analyze_review,
    dealer_details_page,
    post_review_page,
    added_review_page,
)


urlpatterns = [
    # Home
    path('', home_page),

    # Admin
    path('admin/', admin.site.urls),

    # Login / Logout - old routes
    path('login/', login_user),
    path('logout/', logout_user),

    # Login / Logout - required Coursera routes
    path('djangoapp/login', login_user),
    path('djangoapp/login/', login_user),
    path('djangoapp/logout', logout_user),
    path('djangoapp/logout/', logout_user),

    # Dealer reviews - old route
    path('dealer/<int:dealer_id>/reviews/', get_dealer_reviews),

    # Dealer reviews - required Coursera route
    path('djangoapp/fetchReviews/dealer/<int:dealer_id>', get_dealer_reviews),
    path('djangoapp/fetchReviews/dealer/<int:dealer_id>/', get_dealer_reviews),

    # All dealers - old route
    path('dealers/', get_all_dealers),

    # All dealers - required Coursera route
    path('djangoapp/get_dealers', get_all_dealers),
    path('djangoapp/get_dealers/', get_all_dealers),

    # Dealer by id - old route
    path('dealer/<int:dealer_id>/', get_dealer_by_id),

    # Dealer by id - required Coursera route
    path('djangoapp/fetchDealer/<int:dealer_id>', get_dealer_by_id),
    path('djangoapp/fetchDealer/<int:dealer_id>/', get_dealer_by_id),

    # Dealers by state - old route
    path('dealers/state/<str:state>/', get_dealers_by_state),

    # Dealers by state - required Coursera route
    path('djangoapp/get_dealers/<str:state>', get_dealers_by_state),
    path('djangoapp/get_dealers/<str:state>/', get_dealers_by_state),

    # Cars
    path('cars/', get_all_car_makes),
    path('djangoapp/get_cars', get_all_car_makes),
    path('djangoapp/get_cars/', get_all_car_makes),

    # Analyze review
    path('analyze_review/', analyze_review),
    path('djangoapp/analyze_review', analyze_review),
    path('djangoapp/analyze_review/', analyze_review),

    # Frontend pages
    path('dealer/<int:dealer_id>/details/', dealer_details_page),
    path('review-dealer/', post_review_page),
    path('added-review/', added_review_page),
]