

def create_youtube_video(title, descripton):
	youtube_videos={"title":title,"descripton":descripton,"like":0,"dislike":0,"comments":{}}
	return youtube_videos

def like (youtube_videos):
	if "like" in youtube_videos:
		youtube_videos["like"] += 1
	return youtube_videos
def dislike (youtube_videos):
    if "dislike" in youtube_videos:
    	youtube_videos["dislike"] += 1
    return youtube_videos
def add_comment (youtube_videos,comment,username):
	youtube_videos["comments"][username]=comment
	return youtube_videos



hi=create_youtube_video("hello","hello world")
h2=add_comment(hi,"hs","uh")