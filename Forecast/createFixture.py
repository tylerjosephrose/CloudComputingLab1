import json

fixture = []
with open('dailyweather.csv') as dw:
    i = 0
    for line in dw:
        if i == 0:
            i += 1
            continue
        token = line.split(',')
        entry = {"model": "Forecast.Weather", "pk": "{}-{}-{}".format(token[0][:4], token[0][4:6], token[0][6:]),
                 'fields': {"TMAX": float(token[1]),
                            "TMIN": float(token[2])}}
        fixture.append(entry)
        i += 1

with open('fixtures.json', 'w+') as f:
    f.write(json.dumps(fixture))
