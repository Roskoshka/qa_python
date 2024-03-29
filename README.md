# qa_python
Pozitive tests:
test_add_new_book_add_two_books - добавляем две книги
test_set_book_genre_set_genre_true - устанавливаем жанр книге
test_get_books_with_specific_genre_get_list_true - выводим список книг с определённым жанром
test_get_books_for_children_set_genre_not_age_rating_get_list_true - книги с жанром без ограничений попали в список для детей
test_add_book_in_favorites_add_to_favorites - книга добавлена в избранное
test_delete_book_from_favorites_book_deleted_from_favorites - книга удалена из избранного


Negative tests:
test_add_new_book_negative_not_add - книги с пустым названием и названием свыше 40 символов не добавлены
test_set_book_genre_set_genre_not_from_books_genre_false - жанр не из списка жанров не установлен
test_get_books_for_children_set_genre_age_rating_get_list_empty - книги с жанром с ограничениями не попали в список для детей
test_add_book_in_favorites_book_already_in_favorites_false - книга, которая присутствует в избранном, не добавлена повторно в избранное
test_add_book_in_favorites_add_book_not_from_books_genre_false - книга, которая отсутствует в словаре книг, не добавлена в избранное
test_delete_book_from_favorites_book_not_from_favorites_not_deleted - при удалении книги, которой нет в избранном, из избранного ничего не удалено
