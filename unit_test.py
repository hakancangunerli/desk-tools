import unittest
from unittest.mock import patch
from io import StringIO
from main import main

class TestMain(unittest.TestCase):
    
    @patch('news.news')
    def test_news_command(self, mock_news):
        with patch('builtins.input', return_value='news'):
            main()
        mock_news.assert_called_once()

    @patch('ticker_finder.get_ticker', return_value='AAPL')
    def test_ticker_finder_command(self, mock_ticker_finder):
        with patch('builtins.input', side_effect=['tf', 'Apple']):
            main()
        mock_ticker_finder.assert_called_once_with('Apple')


    @patch('builtins.input', side_effect=['help', 'line'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_help_command_for_line(self, mock_stdout, mock_input):
        main()
        self.assertEqual(mock_stdout.getvalue(), 'line  <start_date> <end_date> <ticker>\n')

    @patch('plots.line')
    def test_line_command(self, mock_line):
        with patch('builtins.input', side_effect=['line', '2022-01-01', '2022-03-01', 'AAPL']):
            main()
        mock_line.assert_called_once_with('2022-01-01', '2022-03-01', 'AAPL')

    @patch('builtins.input', side_effect=['help', 'candlestick'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_help_command_for_candlestick(self, mock_stdout, mock_input):
        main()
        self.assertEqual(mock_stdout.getvalue(), 'candlestick  <start_date> <end_date> <ticker>\n')

    @patch('plots.candlestick')
    def test_candlestick_command(self, mock_candlestick):
        with patch('builtins.input', side_effect=['candlestick', '2022-01-01', '2022-03-01', 'AAPL']):
            main()
        mock_candlestick.assert_called_once_with('2022-01-01', '2022-03-01', 'AAPL')
