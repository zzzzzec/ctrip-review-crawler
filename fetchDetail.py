import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor


def fetchInfo1(hotelId, save_path):
    cookies = {
        'Hm_lvt_a8d6737197d542432f4ff4abc6e06384': '1757074904',
        'HMACCOUNT': '6F86E0C9E2731DC9',
        'UBT_VID': '1757074904851.1d98GRGifqwz',
        '_ga': 'GA1.1.592361527.1757074905',
        'GUID': '09031125113956821417',
        'Session': 'smartlinkcode=U135371&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=',
        'Union': 'AllianceID=4899&SID=135371&OUID=&createtime=1757074906&Expires=1757679705667',
        'MKT_CKID': '1757074905690.srr46.htfv',
        '_RSG': '9dKReSfFTz6tU0Gh1GgkE8',
        '_RDG': '28001d8b42dca823ec13d249b772a7c990',
        '_RGUID': '6f5d3e97-286d-49c9-83ae-a9006b4007b7',
        'MKT_Pagesource': 'PC',
        'manualclose': '1',
        'ibulanguage': 'CN',
        'ibulocale': 'zh_cn',
        'cookiePricesDisplayed': 'CNY',
        'librauuid': '',
        'nfes_isSupportWebP': '1',
        'Hm_lpvt_a8d6737197d542432f4ff4abc6e06384': '1757075254',
        '_ga_5DVRDQD429': 'GS2.1.s1757074904$o1$g1$t1757075262$j52$l0$h0',
        '_ga_B77BES1Z8Z': 'GS2.1.s1757074904$o1$g1$t1757075262$j52$l0$h0',
        '_ga_9BZF483VNQ': 'GS2.1.s1757074904$o1$g1$t1757075262$j52$l0$h0',
        '_ubtstatus': '%7B%22vid%22%3A%221757074904851.1d98GRGifqwz%22%2C%22sid%22%3A1%2C%22pvid%22%3A12%2C%22pid%22%3A600001375%7D',
        '_bfaStatusPVSend': '1',
        '_bfi': 'p1%3D600001375%26p2%3D102001%26v1%3D12%26v2%3D11',
        '_bfaStatus': 'success',
        'intl_ht1': 'h4=30_67690986,2_8063900,30_535673,30_105849420,30_347431',
        '_jzqco': '%7C%7C%7C%7C1757074905860%7C1.1290556627.1757074905688.1757081292854.1757081998459.1757081292854.1757081998459.0.0.0.16.16',
        '_RF1': '82.26.72.152',
        '_bfa': '1.1757074904851.1d98GRGifqwz.1.1757081997983.1757083547323.1.18.102003',
    }

    headers = {
        'accept': 'application/json',
        'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://hotels.ctrip.com',
        'p': '37856503287',
        'priority': 'u=1, i',
        'referer': 'https://hotels.ctrip.com/',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Microsoft Edge";v="139", "Chromium";v="139"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0',
        # 'cookie': 'Hm_lvt_a8d6737197d542432f4ff4abc6e06384=1757074904; HMACCOUNT=6F86E0C9E2731DC9; UBT_VID=1757074904851.1d98GRGifqwz; _ga=GA1.1.592361527.1757074905; GUID=09031125113956821417; Session=smartlinkcode=U135371&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; Union=AllianceID=4899&SID=135371&OUID=&createtime=1757074906&Expires=1757679705667; MKT_CKID=1757074905690.srr46.htfv; _RSG=9dKReSfFTz6tU0Gh1GgkE8; _RDG=28001d8b42dca823ec13d249b772a7c990; _RGUID=6f5d3e97-286d-49c9-83ae-a9006b4007b7; MKT_Pagesource=PC; manualclose=1; ibulanguage=CN; ibulocale=zh_cn; cookiePricesDisplayed=CNY; librauuid=; nfes_isSupportWebP=1; Hm_lpvt_a8d6737197d542432f4ff4abc6e06384=1757075254; _ga_5DVRDQD429=GS2.1.s1757074904$o1$g1$t1757075262$j52$l0$h0; _ga_B77BES1Z8Z=GS2.1.s1757074904$o1$g1$t1757075262$j52$l0$h0; _ga_9BZF483VNQ=GS2.1.s1757074904$o1$g1$t1757075262$j52$l0$h0; _ubtstatus=%7B%22vid%22%3A%221757074904851.1d98GRGifqwz%22%2C%22sid%22%3A1%2C%22pvid%22%3A12%2C%22pid%22%3A600001375%7D; _bfaStatusPVSend=1; _bfi=p1%3D600001375%26p2%3D102001%26v1%3D12%26v2%3D11; _bfaStatus=success; intl_ht1=h4=30_67690986,2_8063900,30_535673,30_105849420,30_347431; _jzqco=%7C%7C%7C%7C1757074905860%7C1.1290556627.1757074905688.1757081292854.1757081998459.1757081292854.1757081998459.0.0.0.16.16; _RF1=82.26.72.152; _bfa=1.1757074904851.1d98GRGifqwz.1.1757081997983.1757083547323.1.18.102003',
    }

    json_data = {
        'masterHotelId': hotelId,
        'isBusiness': False,
        'feature': [],
        'cityCode': 30,
        'checkIn': '2025-09-05',
        'checkOut': '2025-09-06',
        'head': {
            'Locale': 'zh-CN',
            'Currency': 'CNY',
            'Device': 'PC',
            'UserIP': '82.26.72.152',
            'Group': 'ctrip',
            'ReferenceID': '',
            'UserRegion': 'CN',
            'AID': '4899',
            'SID': '135371',
            'Ticket': '',
            'UID': '',
            'IsQuickBooking': '',
            'ClientID': '09031125113956821417',
            'OUID': '',
            'TimeZone': '8',
            'P': '37856503287',
            'PageID': '102003',
            'Version': '',
            'HotelExtension': {
                'WebpSupport': True,
                'group': 'CTRIP',
                'Qid': '411664735611',
                'hasAidInUrl': False,
            },
            'Frontend': {
                'vid': '1757074904851.1d98GRGifqwz',
                'sessionID': '1',
                'pvid': '18',
            },
        },
        'ServerData': '',
    }
    response = requests.post(
        'https://m.ctrip.com/restapi/soa2/21881/json/hotelStaticInfo',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    import json
    data = json.loads(response.text)['Response']
    with open(f"{save_path}/detail_{hotelId}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    # # 酒店名称，星级，具体地址，房间数，开业时间，description
    # name = data['hotelInfo']['basic']['name']
    # kaiye = data['hotelInfo']['basic']['label'][0]
    # kefangshu = data['hotelInfo']['basic']['label'][1]
    # description = data['hotelInfo']['basic']['description']
    # return {
    #     'name': name,
    #     'kaiye': kaiye,
    #     'kefangshu': kefangshu,
    #     'description': description
    # }

def fetchInfo2(hotelId, save_path):
    import requests
    cookies = {
        'Hm_lvt_a8d6737197d542432f4ff4abc6e06384': '1757074904',
        'HMACCOUNT': '6F86E0C9E2731DC9',
        'UBT_VID': '1757074904851.1d98GRGifqwz',
        '_ga': 'GA1.1.592361527.1757074905',
        'GUID': '09031125113956821417',
        'Session': 'smartlinkcode=U135371&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=',
        'Union': 'AllianceID=4899&SID=135371&OUID=&createtime=1757074906&Expires=1757679705667',
        'MKT_CKID': '1757074905690.srr46.htfv',
        '_RSG': '9dKReSfFTz6tU0Gh1GgkE8',
        '_RDG': '28001d8b42dca823ec13d249b772a7c990',
        '_RGUID': '6f5d3e97-286d-49c9-83ae-a9006b4007b7',
        'MKT_Pagesource': 'PC',
        'manualclose': '1',
        'ibulanguage': 'CN',
        'ibulocale': 'zh_cn',
        'cookiePricesDisplayed': 'CNY',
        'IBU_TRANCE_LOG_P': '37856503287',
        'Hm_lvt_4a51227696a44e11b0c61f6105dc4ee4': '1757074933',
        'librauuid': '',
        'nfes_isSupportWebP': '1',
        'Hm_lpvt_a8d6737197d542432f4ff4abc6e06384': '1757075254',
        '_ga_5DVRDQD429': 'GS2.1.s1757074904$o1$g1$t1757075262$j52$l0$h0',
        '_ga_B77BES1Z8Z': 'GS2.1.s1757074904$o1$g1$t1757075262$j52$l0$h0',
        '_ga_9BZF483VNQ': 'GS2.1.s1757074904$o1$g1$t1757075262$j52$l0$h0',
        '_ubtstatus': '%7B%22vid%22%3A%221757074904851.1d98GRGifqwz%22%2C%22sid%22%3A1%2C%22pvid%22%3A12%2C%22pid%22%3A600001375%7D',
        '_bfaStatusPVSend': '1',
        '_bfi': 'p1%3D600001375%26p2%3D102001%26v1%3D12%26v2%3D11',
        '_bfaStatus': 'success',
        'Hm_lpvt_4a51227696a44e11b0c61f6105dc4ee4': '1757081998',
        'intl_ht1': 'h4=30_67690986,2_8063900,30_535673,30_105849420,30_347431',
        '_bfa': '1.1757074904851.1d98GRGifqwz.1.1757081292584.1757081997983.1.17.102003',
        'hotel': '67690986',
        '_jzqco': '%7C%7C%7C%7C1757074905860%7C1.1290556627.1757074905688.1757081292854.1757081998459.1757081292854.1757081998459.0.0.0.16.16',
        '_RF1': '82.26.72.152',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'referer': 'https://hotels.ctrip.com/hotels/list?countryId=1&city=30&provinceId=0&checkin=2025/09/05&checkout=2025/09/06&optionId=30&optionType=City&directSearch=0&display=%E6%B7%B1%E5%9C%B3&crn=1&adult=1&children=0&searchBoxArg=t&travelPurpose=0&ctm_ref=ix_sb_dl&domestic=1&&starlist=&highPrice=-1&barCurr=CNY&sort=1&brandType=BRAND&brandValue=2%7C631&location=213',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Microsoft Edge";v="139", "Chromium";v="139"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0',
        # 'cookie': 'Hm_lvt_a8d6737197d542432f4ff4abc6e06384=1757074904; HMACCOUNT=6F86E0C9E2731DC9; UBT_VID=1757074904851.1d98GRGifqwz; _ga=GA1.1.592361527.1757074905; GUID=09031125113956821417; Session=smartlinkcode=U135371&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; Union=AllianceID=4899&SID=135371&OUID=&createtime=1757074906&Expires=1757679705667; MKT_CKID=1757074905690.srr46.htfv; _RSG=9dKReSfFTz6tU0Gh1GgkE8; _RDG=28001d8b42dca823ec13d249b772a7c990; _RGUID=6f5d3e97-286d-49c9-83ae-a9006b4007b7; MKT_Pagesource=PC; manualclose=1; ibulanguage=CN; ibulocale=zh_cn; cookiePricesDisplayed=CNY; IBU_TRANCE_LOG_P=37856503287; Hm_lvt_4a51227696a44e11b0c61f6105dc4ee4=1757074933; librauuid=; nfes_isSupportWebP=1; Hm_lpvt_a8d6737197d542432f4ff4abc6e06384=1757075254; _ga_5DVRDQD429=GS2.1.s1757074904$o1$g1$t1757075262$j52$l0$h0; _ga_B77BES1Z8Z=GS2.1.s1757074904$o1$g1$t1757075262$j52$l0$h0; _ga_9BZF483VNQ=GS2.1.s1757074904$o1$g1$t1757075262$j52$l0$h0; _ubtstatus=%7B%22vid%22%3A%221757074904851.1d98GRGifqwz%22%2C%22sid%22%3A1%2C%22pvid%22%3A12%2C%22pid%22%3A600001375%7D; _bfaStatusPVSend=1; _bfi=p1%3D600001375%26p2%3D102001%26v1%3D12%26v2%3D11; _bfaStatus=success; Hm_lpvt_4a51227696a44e11b0c61f6105dc4ee4=1757081998; intl_ht1=h4=30_67690986,2_8063900,30_535673,30_105849420,30_347431; _bfa=1.1757074904851.1d98GRGifqwz.1.1757081292584.1757081997983.1.17.102003; hotel=67690986; _jzqco=%7C%7C%7C%7C1757074905860%7C1.1290556627.1757074905688.1757081292854.1757081998459.1757081292854.1757081998459.0.0.0.16.16; _RF1=82.26.72.152',
    }

    params = {
        'cityId': '30',
        'checkIn': '2025-09-05',
        'checkOut': '2025-09-06',
        'hotelId': str(hotelId),
        'adult': '1',
        'crn': '1',
        'children': '0',
        'highprice': '-1',
        'lowprice': '0',
        'listfilter': '1',
    }

    response = requests.get('https://hotels.ctrip.com/hotels/detail/', params=params, cookies=cookies, headers=headers)
    with open(f"{save_path}/page_{hotelId}.html", "w", encoding="utf-8") as f:
        f.write(response.text)

# def fetchDetail(hotelId):
    
#     return {
#         'hotelId': hotelId,
        
#     }  
    


# # just for testing
# if __name__ == "__main__":
#     allComments = fetchHotelComments(3725392, numPages=1)

#     with open("comments.json", "w", encoding="utf-8") as f:
#         json.dump(allComments, f, ensure_ascii=False, indent=4)
        