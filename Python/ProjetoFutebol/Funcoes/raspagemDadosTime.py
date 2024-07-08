import requests

def raspagemDados(time):
    print("Adiquirindo dados por favor aguarde!");
    url = "https://webws.365scores.com/web/games/results"

    idTime = int(time)
    querystring = {"appTypeId":"5","langId":"31","timezoneName":"America/Sao_Paulo","userCountryId":"21","competitors":idTime,"showOdds":"true","":""}

    payload = ""
    headers = {"Content-Type": "multipart/form-data; boundary=---011000010111000001101001"}

    print(url)

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    return response