def speak(str):
    from win32com.client import Dispattch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == "__main__":
    import requests
    import json

    query_params = {
        "sours": "bbc-news",
        "sortBy": "top",
        "apiKey": "4bbc14007ab436fb66416009dfb9a8"
    }
    main_url = "https://newsapi.org/v1/articles"
    res = request.get(main_url, params=query_params)
    load = json.loads(res.text)
    speak("Here you listen BBC news from SoftUni Team.")
    speak("first news")

    for i in range(5):
        print(load["articles"][i]["title"])
        print(load["articles"][i]["title"])
        if i < 3:
            speak("next news")
        else:
            speak("This was top 4 BBC news")
