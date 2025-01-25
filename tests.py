from main import BooksCollector
import pytest

class TestBooksCollector:


    def test_add_new_book_add_two_books_books_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2


    def test_set_book_genre_adding_a_genre_genre_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'


    def test_set_book_genre_genre_not_added_book_has_no_genre(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        assert collector.get_book_genre(name) is None


    def test_get_book_genre_we_get_the_genre_of_the_book_genre_received(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Фантастика')
        assert collector.get_book_genre(name) == 'Фантастика'


    def test_get_books_with_specific_genre_adding_books_with_genres_list_contains_a_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        horror_books = collector.get_books_with_specific_genre('Ужасы')
        assert horror_books == ['Что делать, если ваш кот хочет вас убить']


    @pytest.mark.parametrize("name, genre", [
        ('Гордость и предубеждение и зомби', 'Фантастика'),
        ('Что делать, если ваш кот хочет вас убить', 'Ужасы'),
    ])
    def test_get_books_with_specific_genre_add_two_books_result_contains_the_title_of_the_book(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        result = collector.get_books_with_specific_genre(genre)
        assert name in result


    def test_get_books_genre_adding_an_empty_dictionary_dictionary_is_empty(self):
        collector = BooksCollector()
        assert (collector.get_books_genre(), {})


    def test_get_books_for_children_adding_various_books_we_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.add_new_book('Вий')
        collector.set_book_genre('Вий', 'Ужасы')
        children_books = collector.get_books_for_children()
        assert children_books == ['Гордость и предубеждение и зомби']


    def test_add_book_in_favorites_adding_a_book_to_favorites_book_added_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.get_list_of_favorites_books()


    def test_delete_book_from_favorites_deleting_a_book_from_favorites_book_deleted(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' not in collector.get_list_of_favorites_books()
