import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('name', ['Название книги, состоящей из 41 символа  ', ''])
    def test_add_new_book_negative_not_add(self, name):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        #добавляем книги с невалидными названиями - 0 символов и 41 символ
        collector.add_new_book(name)

        # проверяем, что книги не добавилась
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 0
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_set_genre_true(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # устанавливаем добавленной книге жанр из списка genre
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')

        # проверяем,что жанр установлен добавленной книге
        assert collector.get_book_genre('Что делать, если ваш кот хочет вас убить') == 'Комедии'

    def test_set_book_genre_set_genre_not_from_books_genre_false(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Ведьмак')

        # устанавливаем добавленной книге жанр не из списка genre
        collector.set_book_genre('Ведьмак', 'Фэнтези')

        # проверяем,что жанр не установлен добавленной книге
        assert not collector.get_book_genre('Ведьмак') == 'Фэнтези'

    def test_get_books_with_specific_genre_get_list_true(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книги
        collector.add_new_book('Десять негритят')
        collector.add_new_book('Молчание ягнят')

        # устаналиваем книгам жанры из списка genre
        collector.set_book_genre('Десять негритят', 'Детективы')
        collector.set_book_genre('Молчание ягнят', 'Детективы')

        # проверяем, что книги с жанром 'Детективы' попали в список детективов
        assert collector.get_books_with_specific_genre('Детективы') == ['Десять негритят', 'Молчание ягнят']

    def test_get_books_for_children_set_genre_not_age_rating_get_list_true(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книги
        collector.add_new_book('Черепашки ниндзя')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # устаналиваем книгам жанры из списка genre
        collector.set_book_genre('Черепашки ниндзя', 'Мультфильмы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')

        # проверяем, что книги с жанром без ограничений попали в список для детей
        assert collector.get_books_for_children() == ['Черепашки ниндзя', 'Что делать, если ваш кот хочет вас убить']

    def test_get_books_for_children_set_genre_age_rating_get_list_empty(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книги
        collector.add_new_book('Десять негритят')
        collector.add_new_book('Гордость и предубеждение и зомби')

        # устаналиваем книгам жанр с возрастным ограничением
        collector.set_book_genre('Десять негритят', 'Детективы')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        # проверяем, что книги с жанром с возрастным ограничением не попали в список для детей
        # список для детей пустой
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_add_to_favorites(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # добавляем книгу с избранное
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        # проверяем, что книга добавлена в избранное
        # список favorites имеет длину 1
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_book_already_in_favorites_false(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # добавляем книгу с избранное
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        # добавляем книгу с избранное еще раз
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        # проверяем, что книга из избранного не добавлена повторно в избранное
        # список favorites не имеет длину 2
        assert not len(collector.get_list_of_favorites_books()) == 2

    def test_add_book_in_favorites_add_book_not_from_books_genre_false(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # добавляем в избранное книгу, которая отсутствует в словаре книг
        collector.add_book_in_favorites('Черепашки ниндзя')

        # проверяем, что книга не добавлена в избранное
        # список favorites не имеет длину 1
        assert not len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_book_deleted_from_favorites(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # добавляем книгу с избранное
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        # удаляем книгу из избранного
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')

        # проверяем, что книга удалена из избранного
        # список избранных книг имеет длину 0
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_book_not_from_favorites_not_deleted(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # добавляем книгу в избранное
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        # удаляем из избранного книгу, которой нет в избранном
        collector.delete_book_from_favorites('Черепашки ниндзя')

        # проверяем, что из списка избранных книг ничего не удалено
        # список избранных книг имеет длину 1
        assert len(collector.get_list_of_favorites_books()) == 1