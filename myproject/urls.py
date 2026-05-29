from django.contrib import admin
from django.urls import path

from .views import (
    home_page,
    loggedin_page,
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
    path('', home_page),
    path('loggedin/', loggedin_page),

    path('admin/', admin.site.urls),

    path('login/', login_user),
    path('logout/', logout_user),

    path('djangoapp/login', login_user),
    path('djangoapp/login/', login_user),

    path('djangoapp/logout', logout_user),
    path('djangoapp/logout/', logout_user),

    path('dealers/', get_all_dealers),
    path('djangoapp/get_dealers', get_all_dealers),
    path('djangoapp/get_dealers/', get_all_dealers),

    path('dealer/<int:dealer_id>/', get_dealer_by_id),
    path('djangoapp/fetchDealer/<int:dealer_id>', get_dealer_by_id),
    path('djangoapp/fetchDealer/<int:dealer_id>/', get_dealer_by_id),

    path('dealers/state/<str:state>/', get_dealers_by_state),
    path('djangoapp/fetchDealers/<str:state>', get_dealers_by_state),
    path('djangoapp/fetchDealers/<str:state>/', get_dealers_by_state),
    path('djangoapp/get_dealers/<str:state>', get_dealers_by_state),
    path('djangoapp/get_dealers/<str:state>/', get_dealers_by_state),

    path('dealer/<int:dealer_id>/reviews/', get_dealer_reviews),
    path('djangoapp/fetchReviews/dealer/<int:dealer_id>', get_dealer_reviews),
    path('djangoapp/fetchReviews/dealer/<int:dealer_id>/', get_dealer_reviews),

    path('cars/', get_all_car_makes),
    path('djangoapp/get_cars', get_all_car_makes),
    path('djangoapp/get_cars/', get_all_car_makes),

    path('analyze_review/', analyze_review),
    path('djangoapp/analyze_review', analyze_review),
    path('djangoapp/analyze_review/', analyze_review),
    path('djangoapp/analyze/<str:review>', analyze_review),
    path('djangoapp/analyze/<str:review>/', analyze_review),

    path('dealer/<int:dealer_id>/details/', dealer_details_page),
    path('review-dealer/', post_review_page),
    path('added-review/', added_review_page),
]