from django.urls import path
from .views import AuthorList, AuthorDetail, PostList, PostDetail,PostFind  # импортируем наше представление

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    path('authors/', AuthorList.as_view()),
    # т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('authors/<int:pk>', AuthorDetail.as_view()),
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    path('news/', PostList.as_view()),

    # т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('news/<int:pk>', PostDetail.as_view()),

    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    # path('', PostList.as_view()),
    # # т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    # path('<int:pk>', PostDetail.as_view()),
    # # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    path('news/search', PostFind.as_view()),


]
