import utils


def get_private_check_text(status, video_id=None):
    # import getjson
    # with getjson.build_req(video_id) as res:
    #     html = res.read().decode()
    # info = getjson.get_youtube_video_info(video_id, html)
    # # Do some if-else using info object

    # Change the Text in return "" to customize the Messages in Discord/Push. 
    # For pinging Discord roles right click the group mention, Copy ID and then add them like this: <@&ROLEIDHERE>
    if status is utils.PlayabilityStatus.PRIVATED:
        return "[{video_id}](https://youtu.be/{video_id}) が非公開になりました。 [{channel_name}](https://www.youtube.com/channel/{channel_id})."
    elif status is utils.PlayabilityStatus.REMOVED:
        return "[{video_id}](https://youtu.be/{video_id}) が削除されました。 [{channel_name}](https://www.youtube.com/channel/{channel_id})."
    elif status is utils.PlayabilityStatus.COPYRIGHTED:
        return "[{video_id}](https://youtu.be/{video_id}) は著作権侵害により非公開になりました。 [{channel_name}](https://www.youtube.com/channel/{channel_id})."
    elif status is utils.PlayabilityStatus.UNKNOWN:
        return "[{video_id}](https://youtu.be/{video_id}) something weird occurred on [{channel_name}](https://www.youtube.com/channel/{channel_id})."
    elif status is utils.PlayabilityStatus.MEMBERS_ONLY:
        return "[{video_id}](https://youtu.be/{video_id}) は会員限定です。 [{channel_name}](https://www.youtube.com/channel/{channel_id})."
    elif status is utils.PlayabilityStatus.LOGIN_REQUIRED:
        return "[{video_id}](https://youtu.be/{video_id}) はログインが必要です。 [{channel_name}](https://www.youtube.com/channel/{channel_id})."
    elif status is utils.PlayabilityStatus.OFFLINE: # Should not be here though. But I do dumb things.
        return "[{video_id}](https://youtu.be/{video_id}) はオフラインです。 [{channel_name}](https://www.youtube.com/channel/{channel_id})."
    elif status is utils.PlayabilityStatus.UNLISTED:
        return "[{video_id}](https://youtu.be/{video_id}) is unlisted on [{channel_name}](https://www.youtube.com/channel/{channel_id})."
    else:
        return "[{video_id}](https://youtu.be/{video_id}) something very weird occurred on [{channel_name}](https://www.youtube.com/channel/{channel_id})."


def get_onlive_message(live_status, video_id=None):
    if live_status is utils.PlayabilityStatus.ON_LIVE:
        return "[{video_id}](https://youtu.be/{video_id}) がライブ配信を開始しました。 [{channel_name}](https://www.youtube.com/channel/{channel_id})!"
    elif live_status is utils.PlayabilityStatus.MEMBERS_ONLY:
        return "[{video_id}](https://youtu.be/{video_id}) が限定配信を開始しました。 [{channel_name}](https://www.youtube.com/channel/{channel_id})!"
    elif live_status is utils.PlayabilityStatus.LOGIN_REQUIRED:
        return "[{video_id}](https://youtu.be/{video_id}) がライブ配信を開始しました。 [{channel_name}](https://www.youtube.com/channel/{channel_id})!"
    else:
        return "[{video_id}](https://youtu.be/{video_id}) がライブ配信を開始しました。 [{channel_name}](https://www.youtube.com/channel/{channel_id})!"


# If you leave this empty it will not posts the multiple manifest messages
MULTI_MANIFEST_MESSAGE = "[{video_id}](https://youtu.be/{video_id}) has multiple manifest on [{channel_name}](https://www.youtube.com/channel/{channel_id})!"

PUSHALERT_TITLE = "🔴 Hololive Live Alert"
PUSHALERT_MESSAGE = "{channelName} is Live now!"

FCM_TITLE = "🔴 {channelName}"
FCM_MESSAGE = "{title}"
