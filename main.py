# coding:utf-8
import video_search
import video_info
import video_tweet

if __name__ == "__main__":
    # 現在投稿されている動画から、ランダムで動画IDを取得
    videoID = video_search.rand_video_search(video_search.new_video_search())
    # 動画情報の取得
    video_info_list = video_info.video_info(videoID)
    # tweet
    video_tweet.tweet(video_info_list)