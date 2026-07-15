def notEmptyStr(s):
    return len(s) > 0

def getHoursMinutesSeconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    result = []
    if(hours >0):
        result.append(f"{hours}h")
    if(minutes >0):
        result.append(f"{minutes}m")
    if(seconds >0 or len(result) == 0):
        result.append(f"{seconds}s")
        
    return " ".join(result)


def main():
    assert getHoursMinutesSeconds(30) == '30s'
    assert getHoursMinutesSeconds(60) == '1m'
    assert getHoursMinutesSeconds(90) == '1m 30s'
    assert getHoursMinutesSeconds(3600) == '1h'
    assert getHoursMinutesSeconds(3601) == '1h 1s'
    assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
    assert getHoursMinutesSeconds(90042) == '25h 42s'
    assert getHoursMinutesSeconds(0) == '0s'

if __name__ == "__main__":
    main()