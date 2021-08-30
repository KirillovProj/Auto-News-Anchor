import news_scrapping
import news_tts

def main():
    news_type = input('Какие вы бы хотели услышать новости: самые популярные за день (П) или самые важные к этому часу (В)?\n').lower()
    if news_type == 'п':
        news_tts.voice(news_scrapping.get_popular())
    elif news_type == 'в':
        news_tts.voice(news_scrapping.get_important())
    else:
        raise Exception('Вы ввели неверное значение. Попробуйте еще раз.')

if __name__ == '__main__':
    main()