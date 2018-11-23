# coding:utf-8
import urllib.parse
import video_parse
import random

"""
現在新しく投稿されている動画IDを取得する(smXXXXXXXX,soXXXXXXXX,nmXXXXXXXX)
@returns {str} - 最新の動画ID
"""
def new_video_search():
    keyword_set = "アニメ OR ゲーム OR 実況プレイ動画 OR 東方 OR アイドルマスター OR ラジオ OR 描いてみた OR TRPG OR\
                エンターテイメント OR 音楽 OR 歌ってみた OR 演奏してみた OR 踊ってみた OR VOCALOID OR ニコニコインディーズ OR ASMR OR MMD OR バーチャル OR\
                動物 OR 料理 OR 自然 OR 旅行 OR スポーツ OR ニコニコ動画講座 OR 車載動画 OR 歴史 OR 鉄道 OR\
                科学 OR ニコニコ技術部 OR ニコニコ手芸部 OR 作ってみた OR\
                政治 OR\
                例のアレ OR その他 OR 日記"
    # カテゴリタグから最新の動画をJSON形式で取得
    new_video_url = 'http://api.search.nicovideo.jp/api/v2/video/contents/search?q=' + urllib.parse.quote(keyword_set) + '&targets=tagsExact&fields=contentId&_sort=' + urllib.parse.quote("-") + 'startTime&_limit=1'
    # JSON形式からreadできる形式に変換
    json_video = video_parse.Json_VideoData(new_video_url)
    json_video_data = json_video.video_parse()
    # parseして動画IDを返す
    return json_video_data['data'][0]['contentId']


"""
最新動画IDからランダムで動画IDを取得する(smXXXXXXXX,soXXXXXXXX,nmXXXXXXXX)
@param {str} videoID 動画ID
@returns {str} ランダムで取得した動画ID
"""
def rand_video_search(videoID):
    # 動画IDの形式(sm,so,nm)を切り取る
    videoID = videoID[2:]

    while True:
        rand_videoID = random.randint(1, int(videoID))
        format_rand_videoID = format_video_search(rand_videoID)
        if format_rand_videoID == "novideo":
            continue
        else:
            return format_rand_videoID + str(rand_videoID)

"""
動画IDから形式を取得する(sm,so,nm)
@param {str} videoID 形式を省いた動画ID
@returns {str} 取得した形式(取得できなかったら消去・非公開にされているため、"novideo"を返す)
"""
def format_video_search(videoID):
    # 形式がsmか判定
    # XML形式からreadできる形式に変換
    xml_video = video_parse.XML_VideoData("http://ext.nicovideo.jp/api/getthumbinfo/sm", str(videoID))
    root = xml_video.video_parse()

    if "sm" in str(root[0][0].text):
        return "sm"
    # 形式がsoか判定
    else:
        # XML形式からreadできる形式に変換
        xml_video = video_parse.XML_VideoData("http://ext.nicovideo.jp/api/getthumbinfo/so", str(videoID))
        root = xml_video.video_parse()

        if "so" in str(root[0][0].text):
            return "so"
        # 形式がnmか判定
        else:
            # XML形式からreadできる形式に変換
            xml_video = video_parse.XML_VideoData("http://ext.nicovideo.jp/api/getthumbinfo/nm", str(videoID))
            root = xml_video.video_parse()

            if "nm" in str(root[0][0].text):
                return "nm"

            else:
                return "novideo"